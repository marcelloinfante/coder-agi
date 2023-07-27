from src.tools.enum import ToolsEnum


class Tool:
    @classmethod
    def execute(self, executor_response, *args):
        tool = ToolsEnum[executor_response["action"]["name"]].value
        tool_response = tool.run(executor_response["action"]["args"], *args)

        return tool_response

    @classmethod
    def list_tools(self):
        serialized_tools = []

        for tool in list(ToolsEnum):
            tool_class = tool.value

            serialized_tools.append(tool_class.infos)

        return serialized_tools
