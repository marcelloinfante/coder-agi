class StatesSerializer:
    @classmethod
    def serialize(self, states):
        serialized_states = ""

        for state in states:
            serialized_state = (
                f"Thought: {state['executor']['thought']}\n"
                f"Action: {state['executor']['action']}\n"
                f"Observation: {state['evaluator']['observation']}\n\n"
            )
            serialized_states += serialized_state

        return serialized_states
