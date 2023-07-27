import os

from src.serializers.files_serializer import FilesSerializer


class WriteFileTool:
    infos = {
        "name": "write_file",
        "description": "Use this tool if you want to create, upgrade or change a file.",
        "schema": {
            "file_path": "Should indicate the file path and the file name that you want to write. Required.",
            "thoughts": "Think step by step how you can create the code and make it work",
            "code": "Return the code of the this file. You should detail about the imports, dependencies, classes, functions, variables, types, and other important informations. Remove all comments. Required",
        },
    }

    @classmethod
    def run(self, payload, config, llm, query_response):
        try:
            file_path = f"{config.path}{payload['file_path'].replace('./', '')}"

            file_new_content = payload["code"]

            if os.path.exists(file_path):
                with open(file_path, "r") as file:
                    current_file_content = file.read()

                prompt_string = (
                    "Merge this two files:\n"
                    "File one:\n"
                    f"{current_file_content}\n\n"
                    "File two:\n"
                    f"{payload['code']}\n\n"
                    "Return only the code and remove all comments:"
                )

                file_new_content = llm.generate(prompt_string, is_json=False)

            directory = os.path.dirname(file_path)
            os.makedirs(directory, exist_ok=True)

            with open(file_path, "w+") as file:
                file.write(file_new_content)

            response = {
                "file_name": file_path,
                "content": file_new_content,
                "show_result": False,
                "success": True,
            }

            return response

        except Exception as error_message:
            response = {
                "file_name": file_path,
                "content": error_message,
                "show_result": False,
                "success": False,
            }

            return response
