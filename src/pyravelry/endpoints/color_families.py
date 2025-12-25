"""Endpoint for color families

https://www.ravelry.com/api#/_color_families
"""

from pyravelry.endpoints.base import BaseEndpoint
from pyravelry.models import ColorFamiliesModel, ColorFamilyModel


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

    def list(self) -> list[ColorFamilyModel]:
        """
        Retrieves all color families from Ravelry.
        Endpoint: GET /color_families.json

        Defined at:
            https://www.ravelry.com/api#/_color_families
        """
        response_dict = self._fetch(http_client=self._http, endpoint=ColorFamiliesResource.endpoint)
        data = ColorFamiliesModel.model_validate(response_dict)
        return data.color_families
