from pathlib import Path
from shutil import rmtree

if __name__ == "__main__":

    if "{{cookiecutter.use_default_base_class}}" != "yes":
        Path(
            "{{cookiecutter.project_slug|snakecase}}/base_dynamic_provider.py"
        ).unlink()

    if "{{cookiecutter.use_github_actions_workflow}}" != "yes":
        rmtree(".github")
