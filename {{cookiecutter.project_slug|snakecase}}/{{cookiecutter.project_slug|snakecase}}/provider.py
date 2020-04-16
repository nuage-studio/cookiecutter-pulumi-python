from typing import Optional

from pulumi import Config


class Provider:
    """
    This class should represent the configuration required by the backend provider.  Typically
    this would include account numbers, credentials, service urls, database names, etc.
    The recommended pattern, as shown below, is to allow a default instance to be created which reads
    everything from the config, but optionally allow parameters to be overridden.  See
    the `example` folder for an illustration of how this might be used.
    """

    provider_param1: str
    provider_param2: str

    def __init__(
        self,
        provider_param1: Optional[str] = None,
        provider_param2: Optional[str] = None,
    ):
        config = Config()
        self.provider_param1 = (
            provider_param1 if provider_param1 else config.require("provider_param1")
        )
        self.provider_param2 = (
            provider_param2 if provider_param2 else config.require("provider_param2")
        )
