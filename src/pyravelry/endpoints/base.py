"""Defines the base subclass endpoint"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
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


class TypedNamespace:
    """Accepts an arbitrary number of typed kwargs.

    This is my solution to SimpleNamespace not working well
    with mypy while still maintaining dot notation.
    """

    def __init__(self, **kwargs: Action) -> None:
        """Takes an unlimited number str:Action kwargs.

        Raises:
            TypeError: Errors if the value isn't Action
        """
        for key, value in kwargs.items():
            if not isinstance(value, Action):
                msg = f"Expected value of type 'Action' for keyword argument '{key}', "
                f"but got '{type(value).__name__}' instead."
                raise TypeError(msg)
            setattr(self, key, value)


class BaseEndpoint(ABC):
    """Base endpoint that other endpoints inherit."""

    @property
    @abstractmethod
    def actions(self) -> TypedNamespace:
        """Each child must define an action (e.g., Action('/patterns', PatternModel))."""
        pass

    def __init__(self, http_client: SyncCacheClient) -> None:
        """Initializes the base endpoint for Ravelry.

        Args:
            http_client (hishel.httpx.SyncCacheClient): httpx Client used for requests.
        """
        self._http = http_client

    @staticmethod
    def _validate(response_dict: dict[str, Any], action: Action) -> dict[str, type[BaseRavelryModel]]:
        """Validates all of the models in the associated action.

        This is specifically for models that are nested within other models. Usually not needed.

        Args:
            response_dict (dict[str, Any]): The raw response from the Ravelry api.
            action (Action): The action that has corresponding models to the raw response.

        Returns:
            dict[str, type[BaseRavelryModel]]: returns a dict with validated data.
        """
        models = action.model

        for key_, model_ in models.model_fields.items():
            vals = response_dict.get(key_)
            model_anno: Any = model_.annotation

            if vals is None:
                continue
            # this is all to keep the `to_pandas()` function
            if len(model_anno.model_json_schema()["properties"].keys()) == 1:
                temp_dict = {key_: vals}
                response_dict[key_] = model_anno.model_validate(temp_dict)
            else:
                response_dict[key_] = model_anno.model_validate(vals)
        return response_dict

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
