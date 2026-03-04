from agents.coder_agent import CoderAgent
from executor.executor import Executor
from config import MAX_RETRIES
from utils.code_extractor import extract_code


class Orchestrator:

    def __init__(self):
        self.agent = CoderAgent()
        self.executor = Executor()

    def run_task(self, task: str):

        error = None
        code = None

        for attempt in range(MAX_RETRIES):

            print(f"\nAttempt {attempt + 1}\n")

            raw_output = self.agent.generate_code(task, code, error)

            code = extract_code(raw_output)

            print("Generated Code:\n")
            print(code)

            self.executor.write_code(code)

            result = self.executor.run_code()

            if result["success"]:
                print("\nExecution Success:\n")
                print(result["stdout"])
                return

            error = result["stderr"]

            print("\nExecution Error:\n")
            print("\nRetrying with error feedback...")
            print(f"\nRetry reason:\n{error}")

        print("\nMax retries reached. Task failed.")