"""Defines the base subclass endpoint"""

from abc import ABC, abstractmethod
from typing import Any, Optional

from hishel.httpx import SyncCacheClient


class BaseEndpoint(ABC):
    """Base endpoint that other endpoints inherit."""

    @property
    @abstractmethod
    def endpoint(self) -> str:
        """Each child must define this string (e.g., '/patterns')."""
        pass

    @property
    @abstractmethod
    def output_model(self) -> Any:
        """Each child must define this output pydantic model"""
        pass

    def __init__(self, http_client: SyncCacheClient) -> None:
        """Initializes the base endpoint for Ravelry.

        Args:
            http_client (hishel.httpx.SyncCacheClient): httpx Client used for requests.
        """
        self._http = http_client

    @staticmethod
    def _fetch(
        http_client: SyncCacheClient,
        endpoint: str,
        params: Optional[dict[str, str]] = None,
    ) -> Any:
        """Fetches all data from the API or the cache.

        Args:
            http_client (SyncCacheClient): httpx Client to use.
            endpoint (str): endpoint to hit for the request.

        Returns:
            Any: JSON object with the requested data.
        """
        response = http_client.get(endpoint, params=params)
        response.raise_for_status()
        return response.json()
