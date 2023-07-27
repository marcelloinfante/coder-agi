from enum import Enum
from src.tools.write_file_tool import WriteFileTool
from src.tools.read_file_tool import ReadFileTool
from src.tools.terminal_tool import TerminalTool
from src.tools.finish_tool import FinishTool


class ToolsEnum(Enum):
    write_file = WriteFileTool
    # read_file = ReadFileTool
    terminal = TerminalTool
    # finish = FinishTool
