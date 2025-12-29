from types import TracebackType
from typing import Optional, Self

from hishel.httpx import SyncCacheClient

from pyravelry.endpoints import (
    ColorFamiliesResource,
    FiberAttributesResource,
    FiberCategoriesResource,
    SearchResource,
    YarnCompaniesResource,
    YarnWeightsResource,
)

from .settings import RavelrySettings


class RavelryClient:
    """Client to get data from the revelry api.

    Attributes:
        settings (RavelrySettings): Authentication for the Ravelry API.
        _http (SyncCacheClient): Httpx client with persistent caching
        color_families (ColorFamiliesResource): Color Families endpoint
        fiber_categories (FiberCategoriesResource): Fiber Categories endpoint
        yarn_weights (YarnWeightsResource): Yarn Weights endpoint
        search (SearchResource): Search endpoint
        fiber_attributes (FiberAttributesResource): Fiber Attributes endpoint
        yarn_companies (YarnCompaniesResource): Yarn Companies endpoint
    """

    def __init__(self, settings: RavelrySettings) -> None:
        """Instantiates a revelry httpx client.

        Args:
            settings (RavelrySettings): Authentication and other settings.
        """
        self.settings = settings
        # Initialize the persistent httpx client with auth
        self._http = SyncCacheClient(
            base_url=str(settings.base_url),
            auth=settings.auth_tuple,
            timeout=10.0,
        )
        self.color_families = ColorFamiliesResource(self._http)
        self.fiber_categories = FiberCategoriesResource(self._http)
        self.yarn_weights = YarnWeightsResource(self._http)
        self.search = SearchResource(self._http)
        self.fiber_attributes = FiberAttributesResource(self._http)
        self.yarn_companies = YarnCompaniesResource(self._http)

    def close(self) -> None:
        """Closes the httpx client."""
        self._http.close()

    def __enter__(self) -> Self:
        """Method to enter context manager."""
        return self

    def __exit__(
        self,
        exc_type: Optional[type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> None:
        """Method to exit context manager, ensuring the client is closed."""
        self.close()
