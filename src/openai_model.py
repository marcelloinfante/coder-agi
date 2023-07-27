import json
import openai


class OpenAIModel:
    def __init__(self, config):
        self.config = config
        openai.api_key = config.api_key

    def generate(self, prompt, is_json=True, n=1):
        while True:
            # try:
            messages = [{"role": "user", "content": prompt}]
            response = openai.ChatCompletion.create(
                model=self.config.model,
                messages=messages,
                max_tokens=6000,
                temperature=0.4,
                n=n,
            )

            self._register_logs(prompt, response)

            llm_responses = []

            for choice in response["choices"]:
                llm_response = choice["message"]["content"]

                if is_json:
                    llm_response = json.loads(llm_response)

                llm_responses.append(llm_response)

            if n == 1:
                llm_responses = llm_responses[0]

            return llm_responses

        # except json.decoder.JSONDecodeError:
        #     continue
        # except openai.error.RateLimitError:
        #     continue

    def _register_logs(self, prompt, response):
        file_path = f"./logs/{self.config.time_now}.txt"

        with open(file_path, "a") as log_file:
            log_file.write(f"-----------\nPrompt: {prompt}\n\nResponse: {response}\n\n")
