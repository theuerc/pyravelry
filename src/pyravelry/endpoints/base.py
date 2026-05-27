"""Defines the base subclass endpoint"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from types import SimpleNamespace
from typing import TYPE_CHECKING, Any

from hishel.httpx import SyncCacheClient

from pyravelry.models import BaseRavelryModel

if TYPE_CHECKING:
    from httpx import Response


@dataclass(frozen=True)
class Action:
    """Holds information about endpoints and models."""

    url: str
    model: type[BaseRavelryModel]


class BaseEndpoint(ABC):
    """Base endpoint that other endpoints inherit."""

    @property
    @abstractmethod
    def actions(self) -> SimpleNamespace:
        """Each child must define an action (e.g., Action('/patterns', PatternModel))."""
        pass

    # @property
    # @abstractmethod
    # def endpoint(self) -> str:
    #     """Each child must define this string (e.g., '/patterns')."""
    #     pass

    # @property
    # @abstractmethod
    # def output_model(self) -> Any:
    #     """Each child must define this output pydantic model"""
    #     pass

    def __init__(self, http_client: SyncCacheClient) -> None:
        """Initializes the base endpoint for Ravelry.

        Args:
            http_client (hishel.httpx.SyncCacheClient): httpx Client used for requests.
        """
        self._http = http_client

    @staticmethod
    def _fetch(response: "Response") -> Any:
        """Fetches all data from the API or the cache.

        This just reduces boilderplate.

        Example of people talking about this:
        <https://github.com/encode/httpx/discussions/2336>

        Args:
            response (Response): httpx Reponse to process.

        Returns:
            Any: JSON object with the requested data from the response.
        """
        response.raise_for_status()
        return response.json()
