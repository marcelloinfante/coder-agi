from src.tools.index import Tool


class TestMain:
    def test_execute(self):
        llm_response = {
            "action": {
                "name": "write_file",
                "args": {
                    "file_path": "test.txt",
                    "content": "Hello world!",
                },
            }
        }

        tool_response = Tool.execute(llm_response)

        assert tool_response["success"]

    def test_list_tools(self):
        tools_infos = Tool.list_tools()

        info_missing = False
        for tool in tools_infos:
            if not (tool["name"] or tool["description"] or tool["schema"]):
                info_missing = True

        assert not info_missing
