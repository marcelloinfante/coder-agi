import json

from src.tools.index import Tool
from src.utils.list_file_structure import list_file_structure

from src.serializers.objectives_serializer import ObjectivesSerializer
from src.serializers.states_serializer import StatesSerializer
from src.serializers.files_serializer import FilesSerializer


class Executor:
    @classmethod
    def execute(self, llm, memory, config, current_objective, query_response):
        if memory.states:
            response_format = {
                "thought": "Explain in details your current step and justify it",
                "action": {"name": "tool name", "args": {"arg name": "value"}},
            }

            prompt_string = (
                f"You are an AI developer and your goal is to execute this objective:\n"
                f"Title: {current_objective['title']}.\n"
                f"Description: {current_objective['description']}.\n"
                # f"Action Suggested: {current_objective['action']}\n\n"
                f"This objective is part of the development of this application:\n"
                f"{config.app_description}.\n\n"
                f"The following steps were sucessufully completed before the objective:\n"
                f"{ObjectivesSerializer.serialize(memory.objetives)}.\n\n"
                f"So you should not repeat the same steps you did in the past.\n"
                f"Think step by step, break the objective in intermediate steps and justify your step.\n"
                f"Make a action using tools if necessary. Your action should be align with your current step.\n"
                f"Each action should be independent from each other."
                f"Tools:\n"
                f"{json.dumps(Tool.list_tools(), indent=4)}\n\n"
                f"You must consider the current files when making an action.\n"
                f"Current files:\n"
                f"{list_file_structure(config.path)}\n\n"
                # f"Here you have files related to the current goal:\n"
                # f"{FilesSerializer.serialize(query_response)}\n\n\n"
                f"States history:\n"
                f"Your action should be a continuation of the following actions and learn from past actions:\n"
                f"{StatesSerializer.serialize(memory.states)}\n\n"
                f"You should only respond in JSON format as described below:\n"
                f"Response Format:\n"
                f"{json.dumps(response_format, indent=4)}\n"
                f"Ensure the response can be parsed by Python json.loads. Only return the json!\n"
            )

            executor_respone = llm.generate(prompt_string)
        else:
            executor_respone = {
                "thought": current_objective["description"],
                "action": current_objective["action"],
            }

        return executor_respone
