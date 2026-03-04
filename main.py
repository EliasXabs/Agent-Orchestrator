from orchestrator.orchestrator import Orchestrator


def main():

    orchestrator = Orchestrator()

    task = "Write a Python program that prints numbers from 1 to 5 but divide each number by zero."

    orchestrator.run_task(task)


if __name__ == "__main__":
    main()