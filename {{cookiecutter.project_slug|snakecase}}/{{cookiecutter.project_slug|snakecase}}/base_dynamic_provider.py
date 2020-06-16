from pulumi.dynamic import ResourceProvider

from .provider import Provider


class BaseDynamicProvider(ResourceProvider):
    """
    This is the base class for dynamic providers.  Place shared funtionality in here
    and have any new dynamic providers extend from this class.
    """

    def __init__(self, provider_params: Provider):
        super(BaseDynamicProvider, self).__init__()
        self.provider_params = provider_params
