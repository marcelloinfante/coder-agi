class Logger:
    colors = {
        "header": "\033[95m",
        "okblue": "\033[94m",
        "okcyan": "\033[96m",
        "okgreen": "\033[92m",
        "warning": "\033[93m",
        "fail": "\033[91m",
        "endc": "\033[0m",
        "bold": "\033[1m",
        "underline": "\033[4m",
        "red": "\033[31m",
        "green": "\033[32m",
        "yellow": "\033[33m",
        "blue": "\033[34m",
        "magenta": "\033[35m",
        "cyan": "\033[36m",
    }

    @classmethod
    def log_plan(self, memory):
        for index, step in enumerate(memory.plan):
            self._log_message(f"{index + 1}. {step['title']}", self.colors["cyan"])
        print(" ")

    @classmethod
    def log_executor_response(self, log_executor_response):
        self._log_message(
            f"Thought: {log_executor_response['thought']}",
            self.colors["green"],
        )
        self._log_message(
            f"Action: {log_executor_response['action']}\n", self.colors["green"]
        )

    @classmethod
    def log_tool_response(self, tool_response):
        self._log_message(
            f"Success: {tool_response['success']}",
            self.colors["warning"],
        )
        self._log_message(
            f"Content: {tool_response['content']}\n",
            self.colors["warning"],
        )

    @classmethod
    def log_evaluation_response(self, evaluator_response):
        self._log_message(
            f"Observation: {evaluator_response['observation']}",
            self.colors["okblue"],
        )
        self._log_message(
            f"Is Valid: {evaluator_response['is_valid']}",
            self.colors["okblue"],
        )
        self._log_message(
            f"Is Finish: {evaluator_response['is_finish']}\n",
            self.colors["okblue"],
        )

    def _log_message(message, property):
        print(f"{property}{message}\033[0m")
