import pytest

from src.config import Config
from src.memory import Memory
from src.openai_model import OpenAIModel
from src.coder_agi import TreeOfThoughts


class TestTreeOfThoughts:
    config_path = "./tests/config_files/default.json"
    tot = TreeOfThoughts(config_path)

    def test_initialization(self):
        assert isinstance(self.tot, TreeOfThoughts)

    def test_config_path_not_provided(self):
        with pytest.raises(Exception):
            TreeOfThoughts()

    def test_config_variable(self):
        assert isinstance(self.tot.config, Config)

    def test_memory_variable(self):
        assert isinstance(self.tot.memory, Memory)

    def test_llm_variable(self):
        assert isinstance(self.tot.llm, OpenAIModel)
