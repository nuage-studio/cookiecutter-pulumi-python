import pulumi
from my_dynamic_provider import Provider
from my_dynamic_provider.my_resource import MyResource

"""
This example illustrates how provider objects can be used to create resources in
different environments.
"""

# No provider given - uses default values from config

resource1 = MyResource("ExampleResource1", param1="123", param2="abc")

pulumi.export("ResourceOutput1", resource1.output_param)


# Explicit provider given

provider = Provider(provider_param1="blah")

resource2 = MyResource(
    "ExampleResource2", param1="456", param2="xyz", provider=provider
)

pulumi.export("ResourceOutput2", resource2.output_param)
