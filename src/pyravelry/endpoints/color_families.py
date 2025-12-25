"""Endpoint for color families

https://www.ravelry.com/api#/_color_families
"""

from functools import cache

from pydantic import HttpUrl

from pyravelry.models import ColorFamiliesModel, ColorFamilyModel
from pyravelry.endpoints.base import BaseEndpoint


class ColorFamiliesResource(BaseEndpoint):
    """Endpoint for Color Families.

    Attributes:
        BaseEndpoint (AnyUrl): The endpoint for colorfamily.

    Methods:
        list (list[ColorFamilyModel]): returns all color families.

    Described at:
        https://www.ravelry.com/api#/_color_families
    """

    endpoint: str = "/color_families.json"

    @cache
    def list(self) -> list[ColorFamilyModel]:
        """
        Retrieves all color families from Ravelry.
        Endpoint: GET /color_families.json

        Defined at:
            https://www.ravelry.com/api#/_color_families
        """
        response = self._http.get(ColorFamiliesResource.endpoint)
        response.raise_for_status()
        data = ColorFamiliesModel.model_validate(response.json())
        return data.color_families
