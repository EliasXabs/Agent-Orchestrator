from llm.ollama_client import OllamaClient


class CoderAgent:

    def __init__(self):
        self.client = OllamaClient()

    def build_prompt(self, task: str) -> str:
        return f"""
                You are a professional Python developer.

                Your task is to write Python code that solves the following problem.

                Rules:
                - Return ONLY valid Python code
                - No explanations
                - No markdown
                - No comments outside the code
                - The code must be executable

                Task:
                {task}
                """

    def generate_code(self, task: str) -> str:

        prompt = self.build_prompt(task)

        response = self.client.generate(prompt)

        return response.strip()