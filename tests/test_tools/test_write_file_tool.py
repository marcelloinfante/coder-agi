from src.tools.write_file_tool import WriteFileTool


class TestWriteFileTool:
    def test_tool_infos(self):
        tool_infos = WriteFileTool.infos
        assert tool_infos

    def test_tool_infos_name_param(self):
        tool_infos = WriteFileTool.infos
        assert tool_infos["name"]

    def test_tool_infos_description_param(self):
        tool_infos = WriteFileTool.infos
        assert tool_infos["description"]

    def test_tool_infos_schema_param(self):
        tool_infos = WriteFileTool.infos
        assert tool_infos["schema"]

    def test_tool_run(self):
        payload = {
            "file_path": "test.txt",
            "content": "Hello world!",
        }

        tool_response = WriteFileTool.run(payload)

        assert tool_response["success"]
