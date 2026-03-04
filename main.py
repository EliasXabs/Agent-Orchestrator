from agents.coder_agent import CoderAgent
from executor.executor import Executor


def main():

    agent = CoderAgent()
    executor = Executor()

    task = "Write a Python program that bubble sorts a list of integers and prints the sorted list. The list of integers is [64, 34, 25, 12, 22, 11, 90] and statically defined in the code."

    code = agent.generate_code(task)

    print("\nGenerated Code:\n")
    print(code)

    executor.write_code(code)

    result = executor.run_code()

    print("\nExecution Result:\n")

    if result["success"]:
        print(result["stdout"])
    else:
        print("ERROR:")
        print(result["stderr"])


if __name__ == "__main__":
    main()