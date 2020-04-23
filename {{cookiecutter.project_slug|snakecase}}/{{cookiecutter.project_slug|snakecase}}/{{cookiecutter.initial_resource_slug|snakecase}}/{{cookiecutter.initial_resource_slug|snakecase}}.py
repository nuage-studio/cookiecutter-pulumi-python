from typing import Optional

from pulumi import Input, Output, ResourceOptions
from pulumi.dynamic import Resource

from ..provider import Provider
from .{{cookiecutter.initial_resource_slug|snakecase}}_provider import {{cookiecutter.initial_resource_slug | pascalcase}}Provider


class {{cookiecutter.initial_resource_slug | pascalcase}}(Resource):
    """
    A {{cookiecutter.initial_resource_slug | pascalcase}} resource.

    TODO: USE THIS TEMPLATE TO CREATE RESOURCES FOR YOUR DYNAMIC PROVIDER.
    
    Parameters are passed into the constructor, which are subsequently placed into the
    `props` dictionary.  Also note that a `Provider` configuration object may be
    optionally passed in.  If it is not given, a default instance is constructed.

    Any Pulumi outputs should be declared as instance variables to allow
    for strong typing.  Note that this typically includes some of the inputs as well,
    to allow for other resources to access their values.  Due to a quirk of Pulumi,
    output parameters must also be specified in the `props` dictionary with a value set
    to `None` to avoid `AttributeError`s.

    See https://www.pulumi.com/docs/intro/concepts/programming-model/#custom-resources
    for more information.
    """

    param1: Output[str]
    """
    An input parameter made available as an output
    """

    param2: Output[str]
    """
    An input parameter made available as an output
    """

    output_param: Output[str]
    """
    An output parameter
    """

    def __init__(
        self,
        resource_name: str,
        param1: Input[str] = None,
        param2: Input[str] = None,
        provider: Provider = None,
        opts: Optional[ResourceOptions] = None,
    ):
        provider = provider if provider else Provider()
        super().__init__(
            provider={{cookiecutter.initial_resource_slug | pascalcase}}Provider(provider),
            name=resource_name,
            props={"param1": param1, "param2": param2, "output_param": None},
            opts=opts,
        )
