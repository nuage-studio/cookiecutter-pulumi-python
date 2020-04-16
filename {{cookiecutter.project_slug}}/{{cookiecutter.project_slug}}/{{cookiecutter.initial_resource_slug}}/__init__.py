from .{{cookiecutter.initial_resource_slug}} import {{cookiecutter.initial_resource_slug | pascalcase}}
from .{{cookiecutter.initial_resource_slug}}_provider import {{cookiecutter.initial_resource_slug | pascalcase}}Provider

__all__ = ["{{cookiecutter.initial_resource_slug | pascalcase}}", "{{cookiecutter.initial_resource_slug | pascalcase}}Provider"]
