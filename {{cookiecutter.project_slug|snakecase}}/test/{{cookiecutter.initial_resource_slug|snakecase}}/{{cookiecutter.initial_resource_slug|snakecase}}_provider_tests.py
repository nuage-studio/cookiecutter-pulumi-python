import unittest

from {{cookiecutter.project_slug|snakecase}}.{{cookiecutter.initial_resource_slug|snakecase}}.{{cookiecutter.initial_resource_slug|snakecase}}_provider import {{cookiecutter.initial_resource_slug | pascalcase}}Provider


class {{cookiecutter.initial_resource_slug | pascalcase}}ProviderProviderTests(unittest.TestCase):
    def test_outputs_are_set(self):
        provider = MockProvider(provider_param1="value1", provider_param2="value2")
        {{cookiecutter.initial_resource_slug|snakecase}}_provider = {{cookiecutter.initial_resource_slug | pascalcase}}Provider(provider)

        result = {{cookiecutter.initial_resource_slug|snakecase}}_provider.create({"param1": "123", "param2": "456"})

        self.assertDictEqual(
            result.outs,
            {"param1": "123", "param2": "456", "output_param": "my_output_value"},
        )


class MockProvider:
    def __init__(self, provider_param1, provider_param2):
        self.provider_param1 = provider_param1
        self.provider_param2 = provider_param2
