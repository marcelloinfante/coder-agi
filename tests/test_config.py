from src.config import Config
import pytest


class TestConfig:
    config = Config("tests/config_files/default.json")

    def test_initialization(self):
        assert isinstance(self.config, Config)

    def test_file_path_not_provided(self):
        with pytest.raises(Exception):
            Config()

    def test_max_steps_exists(self):
        assert self.config.max_steps

    def test_max_steps_default(self):
        assert self.config.max_steps == 10

    def test_max_steps_custom(self):
        config = Config("tests/config_files/custom.json")
        assert config.max_steps == 5

    def test_model_exists(self):
        assert self.config.model

    def test_model_default(self):
        assert self.config.model == "gpt-3.5-turbo"

    def test_model_custom(self):
        config = Config("tests/config_files/custom.json")
        assert config.model == "text-davinci-003"

    def test_use_chat_model_exists(self):
        assert self.config.use_chat_model

    def test_use_chat_model_default(self):
        assert self.config.use_chat_model == True

    def test_use_chat_model_custom(self):
        config = Config("tests/config_files/custom.json")
        assert config.use_chat_model == False

    def test_time_now_exists(self):
        assert self.config.time_now

    def test_time_now_default_type(self):
        assert isinstance(self.config.time_now, str)

    def test_app_description_exists(self):
        assert self.config.app_description

    def test_app_description(self):
        assert self.config.app_description == "Test"

    def test_app_description_not_provided(self):
        with pytest.raises(Exception):
            Config("tests/config_files/missing_values.json")

    def test_api_key_exists(self):
        assert self.config.api_key

    def test_api_key_default_type(self):
        assert isinstance(self.config.api_key, str)
