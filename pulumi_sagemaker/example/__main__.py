import pulumi
from pulumi_sagemaker import Provider
from pulumi_sagemaker.auto_ml_job import AutoMlJob

"""
This example illustrates how Provider objects can be used to create resources under
different environmental configuration.
"""

# No provider given - uses default values from config (See Provider class for more info)

resource1 = AutoMlJob("ExampleResource1", param1="123", param2="abc")

pulumi.export("ResourceOutput1", resource1.output_param)


# Explicit provider given

provider = Provider(provider_param1="blah")

resource2 = AutoMlJob("ExampleResource2", param1="456", param2="xyz", provider=provider)

pulumi.export("ResourceOutput2", resource2.output_param)
