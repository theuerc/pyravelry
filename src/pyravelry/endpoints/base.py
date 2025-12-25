"""Defines the base subclass endpoint"""

from abc import ABC, abstractmethod
from functools import cache
from typing import Any

import httpx


class BaseEndpoint(ABC):
    """Base endpoint that other endpoints inherit."""

    @property
    @abstractmethod
    def endpoint(self) -> str:
        """Each child must define this string (e.g., '/patterns')."""
        pass

    def __init__(self, http_client: httpx.Client) -> None:
        """Initializes the base endpoint for Ravelry.

        Args:
            http_client (httpx.Client): httpx Client used for requests.
        """
        self._http = http_client

    @staticmethod
    @cache
    def _fetch(http_client: httpx.Client, endpoint: str) -> Any:
        """Fetches all data from the API or the cache.

        Args:
            http_client (httpx.Client): httpx Client to use.
            endpoint (str): endpoint to hit for the request.

        Returns:
            Any: JSON object with the requested data.
        """
        response = http_client.get(endpoint)
        response.raise_for_status()
        return response.json()
