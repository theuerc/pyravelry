from pyravelry.endpoints.base import BaseEndpoint
from pyravelry.models import FiberCategoriesModel, FiberCategoryModel


class FiberCategoriesResource(BaseEndpoint):
    """Endpoint for Fiber Categories.

    Attributes:
        BaseEndpoint (AnyUrl): The endpoint for fiber categories.

    Methods:
        list (list[FiberCategoryModel]): returns all fiber categories.

    [Fiber Categories Ravelry API documentation](https://www.ravelry.com/api#/_fiber_categories)
    """

    endpoint: str = "/fiber_categories.json"
    output_model = FiberCategoriesModel

    def list(self) -> list[FiberCategoryModel]:
        """
        List the current fiber categories
        Endpoint: GET /fiber_categories.json
        """
        cls = FiberCategoriesResource
        response_dict = self._fetch(http_client=self._http, endpoint=cls.endpoint)
        data = cls.output_model.model_validate(response_dict)
        return data.fiber_categories
