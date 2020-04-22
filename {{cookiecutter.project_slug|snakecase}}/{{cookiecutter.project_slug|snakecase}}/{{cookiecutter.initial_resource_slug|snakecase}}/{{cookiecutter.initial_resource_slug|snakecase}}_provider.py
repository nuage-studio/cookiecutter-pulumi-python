import pulumi
from pulumi.dynamic import CreateResult, {% if cookiecutter.use_default_base_class != "yes" %}ResourceProvider, {% endif %}UpdateResult

{% if cookiecutter.use_default_base_class == "yes" %}from ..base_dynamic_provider import BaseDynamicProvider
{% endif -%}
from ..provider import Provider

{% if cookiecutter.use_default_base_class == "yes" %}
class {{cookiecutter.initial_resource_slug | pascalcase}}Provider(BaseDynamicProvider):
    """
    The provider for a {{cookiecutter.initial_resource_slug | pascalcase}} resource.
    
    TODO: USE THIS TEMPLATE TO CREATE RESOURCE PROVIDERS FOR YOUR DYNAMIC PROVIDER.

    You should implement the `create`, `diff`, `update` and `delete` methods as
    necessary.  The `Provider` instance which is passed through the constructor should
    define the configuration used to commuciate with the backend service.  It is made
    available by the base class through the
    `provider_params` attribute.

    See https://www.pulumi.com/docs/intro/concepts/programming-model/#dynamicproviders
    for more information.
    """

    def __init__(self, provider_params: Provider):
        super().__init__(provider_params)
{% else %}
class {{cookiecutter.initial_resource_slug | pascalcase}}Provider(ResourceProvider):
    """
    The provider for a {{cookiecutter.initial_resource_slug | pascalcase}} resource.
    
    TODO: USE THIS TEMPLATE TO CREATE RESOURCE PROVIDERS FOR YOUR DYNAMIC PROVIDER.

    You should implement the `create`, `diff`, `update` and `delete` methods as
    necessary.  The `Provider` instance which is passed through the constructor should
    define the configuration used to commuciate with the backend service.

    See https://www.pulumi.com/docs/intro/concepts/programming-model/#dynamicproviders
    for more information.
    """

    def __init__(self, provider_params: Provider):
        self.provider_params = provider_params
{% endif %}

    def create(self, inputs):

        pulumi.info(
            f"Creating {{cookiecutter.initial_resource_slug | pascalcase}} resource (param1={inputs.get('param1')},param2={inputs.get('param2')})..."
        )
        pulumi.info(
            f"Using provider parameters ({self.provider_params.provider_param1},{self.provider_params.provider_param2})"
        )

        return CreateResult(
            id_="resource_id_12345", outs={**inputs, "output_param": "my_output_value"}
        )

    def update(self, id, _olds, props):

        pulumi.info(
            f"Updating {{cookiecutter.initial_resource_slug | pascalcase}}[{id}] to (param1={props.get('param1')},param2={props.get('param2')})..."
        )
        pulumi.info(
            f"Using provider parameters ({self.provider_params.provider_param1},{self.provider_params.provider_param2})"
        )

        return UpdateResult(outs={**props, "output_param": "my_output_value"})

    def delete(self, id, props):
        pulumi.info(f"Deleting {{cookiecutter.initial_resource_slug | pascalcase}}[{id}]")
        pulumi.info(
            f"Using provider parameters ({self.provider_params.provider_param1},{self.provider_params.provider_param2})"
        )
