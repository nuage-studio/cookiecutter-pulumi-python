from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="{{cookiecutter.project_slug|snakecase}}",
    version="0.0.1",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="{{cookiecutter.project_url}}",
    packages=find_packages(exclude=("example")),
    python_requires=">=3.7",
    install_requires=["pulumi>=1.8.1",{% if cookiecutter.backend_provider == "aws" %}"pulumi-aws>=1.0.0",{% endif %}],
    test_requires=["pulumi>=1.8.1",{% if cookiecutter.backend_provider == "aws" %}"pulumi-aws>=1.0.0",{% endif %}],
    test_suite="test",
)
