from pathlib import Path

if __name__ == "__main__":

    if "{{cookiecutter.use_base_class}}" != "yes":
        Path.cwd().resolve().joinpath(
            "{{cookiecutter.project_slug|snakecase}}"
        ).joinpath("base_dynamic_provider.py").unlink()
