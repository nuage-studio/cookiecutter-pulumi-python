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
