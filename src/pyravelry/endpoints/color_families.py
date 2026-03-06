from pyravelry.endpoints.base import BaseEndpoint
from pyravelry.models import ColorFamiliesModel, ColorFamilyModel


class ColorFamiliesResource(BaseEndpoint):
    """Endpoint for Color Families.

    Attributes:
        BaseEndpoint (AnyUrl): The endpoint for colorfamily.
        output_model (ColorFamiliesModel): The pydantic model that the api output is validated against.

    Methods:
        list (list[ColorFamilyModel]): returns all color families.

    [Color Family Ravelry API documentation](https://www.ravelry.com/api#/_color_families)
    """

    endpoint: str = "/color_families.json"
    output_model = ColorFamiliesModel

    def list(self) -> list[ColorFamilyModel]:
        """
        Retrieves all color families from Ravelry.
        """
        cls = ColorFamiliesResource
        response_dict = self._fetch(http_client=self._http, endpoint=cls.endpoint)
        data = cls.output_model.model_validate(response_dict)
        return data.color_families
