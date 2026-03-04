from agents.coder_agent import CoderAgent


def main():

    agent = CoderAgent()

    task = "Write a Python function that computes the factorial of a number."

    code = agent.generate_code(task)

    print("\nGenerated Code:\n")
    print(code)


if __name__ == "__main__":
    main()