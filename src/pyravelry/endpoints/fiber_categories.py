"""Endpoint for fiber categories.

https://www.ravelry.com/api#/_fiber_categories
"""

from pyravelry.endpoints.base import BaseEndpoint
from pyravelry.models import FiberCategoriesModel, FiberCategoryModel


class FiberCategoriesResource(BaseEndpoint):
    """Endpoint for Color Families.

    Attributes:
        BaseEndpoint (AnyUrl): The endpoint for fiber categories.

    Methods:
        list (list[FiberCategoryModel]): returns all fiber categories.
    """

    endpoint: str = "/fiber_categories.json"

    def list(self) -> list[FiberCategoryModel]:
        """
        List the current fiber categories
        Endpoint: GET /fiber_categories.json
        """
        response_dict = self._fetch(http_client=self._http, endpoint=FiberCategoriesResource.endpoint)
        data = FiberCategoriesModel.model_validate(response_dict)
        return data.fiber_categories
