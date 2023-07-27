import json

from src.utils.list_file_structure import list_file_structure


class Evaluator:
    @classmethod
    def evaluate(
        self, llm, config, executor_response, tool_response, current_objective
    ):
        response_format = {
            "observation": (
                "Analyze the result of the current tool response and verify if it accomplish its goal or if it fail."
                "Write in step by step your thoughts about the result of the tool and provide feedback for what worked and what can be improved."
                "If it fails provide sugestions for what can be done to overcome the failed."
                "If this error happend '[Errno 2] No such file or directory:' return the correct path."
            ),
            "is_valid": (
                "Return true as a boolean if the response of the tool accomplish the goal of the current strategy. "
                "And if the strategy directyle concretely is making fast progress in achiving the goal of developing the app. "
                "Return false as a boolean if the response of the tool fail to accomplish the goal of the current strategy "
                "or if the current strategy fail to make progress to achieving the goal of developing the app. "
                "If success is equal true and content is empty then return a boolean true."
            ),
            "finish_observation": (
                f"Explain step by step in details your thoughts about the objective is completed or not {current_objective['title']}, {current_objective['description']}."
            ),
            "is_finish": (
                f"Return a boolean true if this objective is completed: {current_objective['title']}, {current_objective['description']}. "
                "Return a boolean false if the objective is incomplete. "
                "If is_valid is false, then is_finish is false too."
            ),
        }

        prompt = (
            f"Evaluate the Current State and Current Tool Response to verify if they are align with the objective:"
            f"Title: {current_objective['title']}.\n"
            f"Description: {current_objective['description']}.\n\n"
            f"Current State:\n"
            f"Thought: {executor_response['thought']}\n"
            f"Action: {executor_response['action']}\n\n"
            f"Current Tool Response:\n"
            f"Success: {tool_response['success']}\n"
            f"Content: {tool_response['content']}\n\n"
            f"You must consider the current file structure when evaluating\n"
            f"Current file structure:\n"
            f"{list_file_structure(config.path)}\n\n"
            f"You should only respond in JSON format as described below:\n"
            f"Response Format: \n"
            f"{json.dumps(response_format, indent=4)}\n"
            f"Ensure the response can be parsed by Python json.loads. Only return the json!"
        )

        evaluator_response = llm.generate(prompt)

        return evaluator_response
