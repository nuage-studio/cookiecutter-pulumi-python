import unittest

from pulumi_acme.database.database_provider import DatabaseProvider


class DatabaseProviderTests(unittest.TestCase):
    def test_create_database_simple_args(self):
        provider = MockProvider(provider_param1="value1", provider_param2="value2")
        database_provider = DatabaseProvider(provider)

        result = database_provider.create({"param1": "123", "param2": "456"})

        self.assertDictEqual(
            result.outs,
            {"param1": "123", "param2": "456", "output_param": "my_output_value"},
        )


class MockProvider:
    def __init__(self, provider_param1, provider_param2):
        self.provider_param1 = provider_param1
        self.provider_param2 = provider_param2
