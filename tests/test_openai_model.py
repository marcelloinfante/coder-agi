import pytest

from src.openai_model import OpenAIModel
from src.config import Config


class TestOpenAIModel:
    def test_initialization(self):
        config = Config("tests/config_files/default.json")
        llm = OpenAIModel(config)
        assert isinstance(llm, OpenAIModel)

    def test_config_not_provided(self):
        with pytest.raises(Exception):
            OpenAIModel()

    # def test_generate_result_chat_model(self):
    #     config = Config("tests/config_files/default.json")
    #     llm = OpenAIModel(config)

    #     text_generated = llm.generate("return a json example:")
    #     assert text_generated

    # def test_generate_result_not_chat_model(self):
    #     config = Config("tests/config_files/custom.json")
    #     llm = OpenAIModel(config)

    #     text_generated = llm.generate("return a json example:")
    #     assert text_generated
