class ReadFileTool:
    infos = {
        "name": "read_file",
        "description": "Use this tool if you want to read a file.",
        "schema": {
            "file_path": "Should indicate the file path and the file name that you want to read. Required.",
        },
    }

    @classmethod
    def run(self, payload, config):
        try:
            with open(
                f"{config.path}{payload['file_path'].replace('./', '')}", "r"
            ) as file:
                file_content = file.read()

            response = {
                "file_name": f"{config.path}{payload['file_path'].replace('./', '')}",
                "content": file_content,
                "show_result": True,
                "success": True,
            }

            return response
        except Exception as error_message:
            response = {
                "file_name": f"{config.path}{payload['file_path'].replace('./', '')}",
                "error": error_message,
                "show_result": False,
                "success": False,
            }

            return response
