# Pulumi Dynamic Provider Template

This project is a template for creating Pulumi Dynamic Providers in Python.  It represents
a provider for the fictional "ACME" service, and allows creation of a dummy "database"
resource.  You should replace this section with a description of your project, and should
make sure to update the following:
* The folder `pulumi_acme` should be changed to your package name
* The package name and URL in `setup.py` should be updated
* The `Provider` class should be modified to represent your backend provider's configuration parameters
* The resources and Dynamic Providers should be created following the template in the `database` folder
* The example program in `example` should be updated to demonstrate how your package is used
* The folder structure at the bottom of this document should be updated

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

## Folder structure

```
.
├── example                                 An example program which uses this provider package
│   ├── __main__.py
│   ├── Pulumi.dev.yaml
│   ├── Pulumi.yaml
│   └── README.md
├── Makefile
├── pulumi_acme                             The main package folder with a subfolder for each resource type
│   ├── database                            The folder for a particular resource type
│   │   ├── database_provider.py            The Pulumi resource object
│   │   └── database.py                     The Dynamic Provider for the resource
│   └── provider.py                         The backend provider configuration object
├── README.md
├── requirements_dev.txt
├── setup.cfg
└── setup.py
```
