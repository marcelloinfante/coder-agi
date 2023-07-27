class ObjectivesSerializer:
    @classmethod
    def serialize(self, objectives):
        serialized_objectives = ""

        for objective in objectives:
            serialized_objective = (
                f"Title: {objective['title']}\n"
                f"Description: {objective['description']}\n\n"
            )
            serialized_objectives += serialized_objective

        return serialized_objectives
