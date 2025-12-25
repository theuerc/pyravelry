"""Defines the base subclass endpoint"""

import httpx

from abc import ABC, abstractmethod


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
            http_client (httpx.Client): _description_
        """
        self._http = http_client
