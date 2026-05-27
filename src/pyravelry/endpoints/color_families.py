from types import SimpleNamespace
from typing import cast

from pyravelry.endpoints.base import Action, BaseEndpoint
from pyravelry.models import ColorFamiliesModel


class ColorFamiliesResource(BaseEndpoint):
    """Endpoint for Color Families.

    Attributes:
        BaseEndpoint (AnyUrl): The endpoint for colorfamily.
        output_model (ColorFamiliesModel): The pydantic model that the api output is validated against.

    Methods:
        list (list[ColorFamilyModel]): returns all color families.

    [Color Family Ravelry API documentation](https://www.ravelry.com/api#/_color_families)
    """

    actions = SimpleNamespace(
        list=Action("/color_families.json", ColorFamiliesModel),
    )

    def list(self) -> ColorFamiliesModel:
        """
        Retrieves all color families from Ravelry.
        """
        response_dict = self._fetch(self._http.get(self.actions.list.url))
        return cast(ColorFamiliesModel, self.actions.list.model.model_validate(response_dict))
