import os
from src.utils.gitignore_template import GIT_IGNORE_TEMPLATE


class Initializer:
    @classmethod
    def initialize(self, config):
        os.makedirs(config.path, exist_ok=True)
        with open(f"{config.path}.gitignore", "w") as file:
            file.write(GIT_IGNORE_TEMPLATE)

        config.repo.index.commit("First commit")
