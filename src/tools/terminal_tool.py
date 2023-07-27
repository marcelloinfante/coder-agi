import subprocess


class TerminalTool:
    infos = {
        "name": "terminal",
        "description": "Use this tool if you want to run a command in the terminal.",
        "schema": {
            "command": (
                "The command you want to run in a linux terminal."
                "Example: 'ls -l'. Your command will be concatenated like this 'cd ./generated/<dir_number> && {command}'."
                "Just run 1 command per step. You should consider the 'Current file structure' when running a command."
                "If you want to run a file write the right file path based on 'Current file structure.'"
                "All commands should be with non-interactive execution and all arguments should passed as flags."
                "Example 'command --args'"
            )
        },
    }

    @classmethod
    def run(self, payload, config, *args):
        command = f"cd {config.path} && {payload['command']}"

        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        if result.returncode == 0:
            response = {"show_result": False, "success": True, "content": ""}

            if result.stdout:
                response["content"] = result.stdout
        else:
            response = {"show_result": False, "success": False, "content": ""}

            if result.stderr:
                response["content"] = result.stderr

        return response
