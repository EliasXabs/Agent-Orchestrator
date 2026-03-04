from llm.ollama_client import OllamaClient


class CoderAgent:

    def __init__(self):
        self.client = OllamaClient()

    def build_prompt(self, task: str, previous_code: str = None, error: str = None):

        if previous_code is not None and error is not None:
            return f"""
                    You are a professional Python developer.

                    The following Python code failed.

                    TASK:
                    {task}

                    CODE:
                    {previous_code}

                    ERROR:
                    {error}

                    Fix the code and return the FULL corrected Python code.

                    Rules:
                    - Return ONLY valid Python code
                    - No explanations
                    - No markdown
                    """

        return f"""
                You are a professional Python developer.

                Write Python code for the following task.

                TASK:
                {task}

                Rules:
                - Return ONLY valid Python code
                - No explanations
                - No markdown
                """

    def generate_code(self, task: str, previous_code: str = None, error: str = None):

        prompt = self.build_prompt(task, previous_code, error)

        response = self.client.generate(prompt)

        return response.strip()