class FinishTool:
    infos = {
        "name": "finish",
        "description": "Use this tool if you finished the app and accomplished the goal of developing the app.",
        "schema": {
            "message": "Should return a final message to the user saying what was accomplished."
        },
    }

    @classmethod
    def run(self, payload, config):
        response = {"content": payload["message"], "success": True}
        return response
