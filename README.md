# Pulumi Dynamic Provider Template

This repository is a [Cookiecutter](https://cookiecutter.readthedocs.io/en/1.7.0/) project for creating new dynamic providers in Python.  You must ensure Cookiecutter is installed:

```
pip install cookiecutter
```

Then, use the following command to create a new dynamic provider project:

```
cookiecutter gh nuage-studio/pulumi-dynamic-provider-python
```

Cookiecutter will then prompt you for a number of inputs:

|                         |                                                                                                       |
| ---                     | ---                                                                                                   |
| `project_slug`          | The name of the project in `snake_case`, e.g. `pulumi_snowflake`                                      |
| `project_display_name`  | The friendly name of the project, e.g. "Pulumi Snowflake Dynamic Provider"                            |
| `project_url`           | The URL of the project, e.g. https://github.com/nuage-studio/pulumi-snowflake                         |
| `include_aws`           | If "yes", then `pulumi_aws` is included as a dependency                                               |
| `aws_region`            | The AWS region to be used in the config, e.g. "eu-west-1".  If AWS is not being used, enter "none".   |
| `use_base_class`        | If "yes", an empty base class for dynamic providers is created to keep shared functionality           |
| `initial_resource_slug` | The name of the first resource in `snake_case`, e.g. `table`                                          |

An example usage is as follows:

```
$ cookiecutter gh nuage-studio/pulumi-dynamic-provider-python
project_slug: pulumi_sagemaker
project_display_name: Pulumi Sagemaker Dynamic Provider
project_url: https://github.com/nuage-studio/pulumi-sagemaker
Select include_aws:
1 - yes
2 - no
Choose from 1, 2 [1]: 1
aws_region: eu-west-1
Select use_base_class:
1 - yes
2 - no
Choose from 1, 2 [1]: 1
initial_resource_slug: AutoMlJob
```

This will generate a directory with the chosen project name, with the following folder
structure:

```
├── pulumi_sagemaker                            Root project directory
│   ├── example                                 An example Pulumi program which uses this provider package
│   │   ├── __main__.py
│   │   ├── Pulumi.dev.yaml
│   │   ├── Pulumi.yaml
│   │   └── README.md
│   ├── Makefile
│   ├── pulumi_sagemaker                        The main package folder with a subfolder for each resource type
│   │   ├── auto_ml_job                         The folder for a particular resource type
│   │   │   ├── auto_ml_job_provider.py         The Pulumi resource object
│   │   │   └── auto_ml_job.py                  The Dynamic Provider for the resource
│   │   ├── base_dynamic_provider.py
│   │   └── provider.py
│   ├── README.md
│   ├── requirements_dev.txt
│   ├── setup.cfg
│   ├── setup.py
│   └── test                                    Unit tests for the dynamic providers
│       └── auto_ml_job
│           └── auto_ml_job_provider_tests.py
├── README.md
```

# Development

## Getting started

You need Python 3 (preferably 3.8) installed to start working on this project.

In order to install your virtualenv, just go to the root of the project and:
```bash
make install
```

## IDE

Nuage recommends [Visual Studio Code](https://code.visualstudio.com/download) to work on this project, and some default settings have been configured in the [.vscode/settings.json](.vscode/settings.json).

These settings merely enforce the code-quality guidelines defined below, but if you use another IDE it's probably worth taking a quick look at it to ensure compliance with the standard.

By default, we recommend:
1. Putting your virtualenv in a `venv` folder at the project root
2. Using a `.env` file to define your environment variables (cf. [python-dotenv](https://pypi.org/project/python-dotenv/))

## Code quality

This project has opinionated code-quality requirements:
- Code formatter: [black](https://black.readthedocs.io/en/stable/)
- Code linter: [pylint](https://www.pylint.org)
- Code style guidelines: [flake8](https://flake8.pycqa.org/en/latest/)

All of these tools are enforced at the commit-level via [pre-commit](https://pre-commit.com)

You can run the following command to apply code-quality to your project at any point:
```bash
make quality
```

Code quality configuration files:
- IDE-agnostic coding style settings are set in the [.editorconfig](.editorconfig) file
- Python-related settings are set in the [setup.cfg](setup.cfg) file
- Pre-commit-related settings are set in the [.pre-commit-config.yaml](.pre-commit-config.yaml) file

## Testing

You can run cookiecutter on the local directory with the following command:

```bash
cookiecutter .
```
