"""Httpx client for getting data."""

from types import TracebackType
from typing import Optional, Type, Self
import httpx
from .settings import RavelrySettings
from pyravelry.endpoints import ColorFamiliesResource


class RavelryClient:
    """Client to get data from the revelry api."""

    def __init__(self, settings: RavelrySettings) -> None:
        """_summary_

        Args:
            settings (RavelrySettings): _description_
        """
        self.settings = settings
        # Initialize the persistent httpx client with auth
        self._http = httpx.Client(
            base_url=str(settings.base_url),
            auth=settings.auth_tuple,
            timeout=10.0,
        )
        self.color_families = ColorFamiliesResource(self._http)

    def close(self) -> None:
        """Closes the httpx client."""
        self._http.close()

    def __enter__(self) -> Self:
        """Method to enter context manager."""
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> None:
        """Method to exit context manager, ensuring the client is closed."""
        self.close()
