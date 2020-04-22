from pathlib import Path

if __name__ == "__main__":

    if "{{cookiecutter.use_default_base_class}}" != "yes":
        Path(
            "{{cookiecutter.project_slug|snakecase}}/base_dynamic_provider.py"
        ).unlink()
