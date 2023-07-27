import json
import networkx as nx

from src.tools.index import Tool


class PlannerTOT:
    def __init__(self, llm, config, memory):
        self.llm = llm
        self.config = config
        self.memory = memory
        self.tree_graph = nx.DiGraph()

    def plan(self):
        initial_state = {
            "id": 1,
            "description": "",
        }

        self.tree_graph.add_node(initial_state["id"], **initial_state)

        current_states = [initial_state]

        while True:
            if current_states:
                current_state = current_states.pop(0)

                print("-------------------------")
                print(current_state)
                print("-------------------------")

                new_states = []
                for _ in range(3):
                    new_state = self._generate_new_state(current_state, new_states)

                    print("@@@@@@@@@@@@@@@@@@@@@")
                    print(new_state)
                    print("@@@@@@@@@@@@@@@@@@@@@")

                    new_states.append(new_state)

                    new_state = self._add_evaluation_to_new_state(
                        new_state, current_state
                    )

                    print("@@@@@@@@@@@@@@@@@@@@@")
                    print(new_state)
                    print("@@@@@@@@@@@@@@@@@@@@@")

                    self._save_new_state_to_tree_graph(current_state, new_state)

                    print("@@@@@@@@@@@@@@@@@@@@@")
                    print(self.tree_graph)
                    print("@@@@@@@@@@@@@@@@@@@@@")

                    if float(new_state["score"]) >= self.config.threshold:
                        current_states.append(new_state)
            else:
                break

    def _generate_new_state(self, current_state, new_states):
        past_states = list(nx.ancestors(self.tree_graph, current_state["id"]))

        serialized_past_states = self._serialize_past_states(past_states)

        serialized_new_states = self._serialize_new_states(new_states)

        response_format = {
            "title": "You should return a short title for the current step",
            "description": "You should return a long detailed description about the current step and justify it",
            "action": {"name": "tool name", "args": {"arg name": "value"}},
            "files": "You must always list all files created by the action. This can never be empty. Required",
        }

        prompt_string = (
            f"Create a new and different next step for developing this app: "
            f"{self.config.app_description}\n"
            f"You should continue from past steps:\n"
            f"{serialized_past_states}\n\n"
            f"The step should replace this steps:\n"
            f"{serialized_new_states}\n\n"
            f"Think step by step, break the objective in intermediate small and simple steps and justify your step.\n"
            f"Start from the begging.\n\n"
            f"You must always write the correct file path in actions.\n\n"
            f"DO NOT INCLUDE THE FOLLOWING ACTIONS:\n"
            f"- Creation of virtual enviroment\n"
            f"- Deploy\n"
            f"- Run server\n\n"
            f"Each step must be a action using one of this tools:\n"
            f"{json.dumps(Tool.list_tools(), indent=4)}\n\n"
            f"You should only respond in JSON format as described below:\n"
            f"Response Format:\n"
            f"{json.dumps(response_format, indent=4)}\n"
            f"Ensure the response can be parsed by Python json.loads. Only return the json!\n"
        )

        new_states = self.llm.generate(prompt_string)

        return new_states

    def _add_evaluation_to_new_state(self, new_state, current_state):
        past_states = list(nx.ancestors(self.tree_graph, current_state["id"]))

        serialized_past_states = self._serialize_past_states(past_states)

        response_format = {
            "observation": (
                "Check whether the current state is advancing the development of the app."
                "Assess the efficiency of the current state in achieving progress."
                "Evaluate the appropriateness, completeness, and quality of the actions being taken."
                "Determine if the current state has occurred in previous states."
                "Assess whether the current state is complex or simple."
            ),
            "score": (
                "Provide a decimal score for the Current State, ranging from 0 to 1. A score of 1 represents the best state, while 0 represents the worst state."
                "To determine the score, consider the following guidelines:"
                "If the Current State has already occurred, assign a significantly low score."
                "If the Current State is highly complex, assign a low score."
                "If the Current State is simple, assign a high score."
                "If the Action is incomplete, assign a low score."
                "If the Action lacks quality or is incorrect, assign a low score."
            ),
        }

        prompt_string = (
            f"Evaluate the Current State to verify if it makes clear and direct progress to achive the goal of developing the following app: "
            f"{self.config.app_description}"
            f"Current State:\n"
            f"Title: {new_state['title']}\n"
            f"Description: {new_state['description']}\n"
            f"Action: {new_state['action']}\n\n"
            f"You should consider the Past States:"
            f"{serialized_past_states}"
            f"You should only respond in JSON format as described below:\n"
            f"Response Format: \n"
            f"{json.dumps(response_format, indent=4)}\n"
            f"Ensure the response can be parsed by Python json.loads. Only return the json!"
        )

        evaluation = self.llm.generate(prompt_string)

        new_state.update(evaluation)

        return new_state

    def _save_new_state_to_tree_graph(self, current_state, new_state):
        new_state["id"] = self.tree_graph.number_of_nodes() + 1

        self.tree_graph.add_node(new_state["id"], **new_state)
        self.tree_graph.add_edge(current_state["id"], new_state["id"])

    def _serialize_past_states(self, past_states):
        serialized_past_states = ""

        for index, state in enumerate(past_states):
            state_attrs = self.tree_graph.nodes[state["id"]]
            serialized_past_state = (
                f"<Past Step {index+1}>\n"
                f"Title: {state_attrs['title']}\n"
                f"Description: {state_attrs['description']}\n"
                f"Action: {state_attrs['action']}\n"
                f"Observation: {state_attrs['observation']}\n"
                f"<\Past Step {index+1}>\n\n"
            )
            serialized_past_states += serialized_past_state

        return serialized_past_states

    def _serialize_new_states(self, new_states):
        serialized_new_states = ""

        for index, state in enumerate(new_states):
            state_attrs = self.tree_graph.nodes[state["id"]]
            serialized_new_state = (
                f"<Replace Step {index+1}>\n"
                f"Title: {state_attrs['title']}\n"
                f"Description: {state_attrs['description']}\n"
                f"Action: {state_attrs['action']}\n"
                f"Observation: {state_attrs['observation']}\n"
                f"<\Replace Step {index+1}>\n\n"
            )
            serialized_new_states += serialized_new_state

        return serialized_new_states
