# Plkfglfkg

_**TODO: Update this section of README.md with a description of your project**_

_You should also do the following:_
* _Update the `pulumi_sagemaker/provider.py` file with the parameters required by your backend provider._
* _Update the `pulumi_sagemaker/auto_ml_job` folder by implementing the AutoMlJob resource and provider_
* _Update the `test/auto_ml_job` folder with unit tests for your resource_
* _Implement any additional resources using the same pattern_
* _Update the `example` folder with an example of the `pulumi_sagemaker` package being used_

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

## Unit tests

To run the unit tests, use the following command:

```
python setup.py test
```

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

## Folder structure

```
.
├── example                                 An example program which uses this provider package
│   ├── __main__.py
│   ├── Pulumi.dev.yaml
│   ├── Pulumi.yaml
│   └── README.md
├── Makefile
├── pulumi_sagemaker                        The main package folder with a subfolder for each resource type
│   ├── auto_ml_job                         The folder for a particular resource type
│   │   ├── auto_ml_job_provider.py         The Pulumi resource object
│   │   └── auto_ml_job.py                  The Dynamic Provider for the resource
│   └── provider.py                         The backend provider configuration object
├── README.md
├── requirements_dev.txt
├── setup.cfg
└── setup.py
```
