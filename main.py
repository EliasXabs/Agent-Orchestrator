from llm.ollama_client import OllamaClient

def main():

    client = OllamaClient()

    prompt = """
                Write a Python function that adds two numbers.
                Return only the code.
             """

    result = client.generate(prompt)

    print("\nModel Output:\n")
    print(result)


if __name__ == "__main__":
    main()