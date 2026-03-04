import re


import re


def extract_code(text: str) -> str:
    """
    Extract Python code from LLM output.
    """

    # Markdown code block
    match = re.search(r"```(?:python)?\n(.*?)```", text, re.DOTALL)
    if match:
        return match.group(1).strip()

    # Remove leading explanations
    lines = text.split("\n")

    cleaned = []
    for line in lines:
        if line.strip().startswith(("Here", "The", "Explanation", "Corrected")):
            continue
        cleaned.append(line)

    return "\n".join(cleaned).strip()