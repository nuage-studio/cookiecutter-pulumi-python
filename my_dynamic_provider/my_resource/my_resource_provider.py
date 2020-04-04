from pulumi import info
from pulumi.dynamic import CreateResult, ResourceProvider, UpdateResult

from ..provider import Provider


class MyResourceProvider(ResourceProvider):
    """
    An example Dynamic Provider for a Pulumi resource.  You should implement the
    `create`, `diff`, `update` and `delete` methods as necessary.  The `Provider`
    instance which is passed through the constructor should define the configuration
    used to commuciate with the backend service.

    See https://www.pulumi.com/docs/intro/concepts/programming-model/#dynamicproviders
    for more information.
    """

    def __init__(self, provider_params: Provider):
        self.provider_params = provider_params

    def create(self, inputs):

        info(
            f"Creating MyResource (param1={inputs.get('param1')},param2={inputs.get('param2')})..."
        )
        info(
            f"Using provider parameters ({self.provider_params.provider_param1},{self.provider_params.provider_param2})"
        )

        return CreateResult(
            id_="resource_id_12345", outs={**inputs, "output_param": "my_output_value"}
        )

    def update(self, id, _olds, props):

        info(
            f"Updating MyResource[{id}] to (param1={props.get('param1')},param2={props.get('param2')})..."
        )
        info(
            f"Using provider parameters ({self.provider_params.provider_param1},{self.provider_params.provider_param2})"
        )

        return UpdateResult(outs={**props, "output_param": "my_output_value"})

    def delete(self, id, props):
        info(f"Deleting MyResource[{id}]")
        info(
            f"Using provider parameters ({self.provider_params.provider_param1},{self.provider_params.provider_param2})"
        )
