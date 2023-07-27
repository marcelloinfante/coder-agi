import pytest

from src.config import Config
from src.memory import Memory


class TestMemory:
    config = Config("tests/config_files/default.json")
    memory = Memory(config)

    def test_initialization(self):
        assert isinstance(self.memory, Memory)

    def test_config_not_provided(self):
        with pytest.raises(Exception):
            Memory()

    def test_config_variable(self):
        assert self.memory.config == self.config

    def test_initial_states(self):
        assert self.memory.states == []

    def test_initial_error_states(self):
        assert self.memory.error_states == []

    def test_add_state_method(self):
        new_state = "123456789"
        self.memory.add_state(new_state, register=False)
        assert self.memory.states.pop() == new_state

    def test_add_error_state_method(self):
        new_error_state = "123456789"
        self.memory.add_error_state(new_error_state, register=False)
        assert self.memory.error_states.pop() == new_error_state

    def test_update_states_method(self):
        new_states = ["123", "abc", "xyz"]
        self.memory.update_states(new_states, register=False)
        assert self.memory.states == new_states

    def test_update_error_states_method(self):
        new_error_states = ["123", "abc", "xyz"]
        self.memory.update_error_states(new_error_states, register=False)
        assert self.memory.error_states == new_error_states
