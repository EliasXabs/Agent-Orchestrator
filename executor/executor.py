import subprocess
from pathlib import Path
from config import WORKSPACE_PATH


class Executor:

    def __init__(self):
        self.workspace = Path(WORKSPACE_PATH)
        self.file_path = self.workspace / "generated_code.py"

        self.workspace.mkdir(exist_ok=True)

    def write_code(self, code: str):

        with open(self.file_path, "w", encoding="utf-8") as f:
            f.write(code)

    def run_code(self):

        result = subprocess.run(
            ["python", str(self.file_path)],
            capture_output=True,
            text=True
        )

        return {
            "success": result.returncode == 0,
            "stdout": result.stdout,
            "stderr": result.stderr
        }