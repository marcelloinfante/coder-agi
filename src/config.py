import os
from datetime import datetime

import git
import json


from dotenv import load_dotenv

load_dotenv()


class Config:
    def __init__(self, file_path):
        with open(file_path, "r") as file:
            config = json.loads(file.read())

        self.max_steps = config["max_steps"] or 10

        self.model = config["model"] or "gpt-3.5-turbo"
        self.use_chat_model = "gpt" in self.model

        self.time_now = datetime.now().strftime("%Y%m%d%H%M%S")

        self.path = f"./generated/{self.time_now}/"

        self.repo = git.Repo.init(self.path)

        self.app_description = self._set_app_description(config)
        self.api_key = self._set_openai_api_key()

        self.threshold = 0.5

    def _set_app_description(self, config):
        app_description = config["app_description"]

        if not app_description:
            raise Exception("Please provide app_description")

        return app_description

    def _set_openai_api_key(self):
        api_key = os.environ.get("OPENAI_API_KEY", "")

        if not api_key:
            raise Exception("Please provide OpenAI API key")

        return api_key
