from types import SimpleNamespace
from typing import cast

from pyravelry.endpoints.base import Action, BaseEndpoint
from pyravelry.models import FiberCategoriesModel


class FiberCategoriesResource(BaseEndpoint):
    """Endpoint for Fiber Categories.

    Attributes:
        BaseEndpoint (AnyUrl): The endpoint for fiber categories.

    Methods:
        list (list[FiberCategoryModel]): returns all fiber categories.

    [Fiber Categories Ravelry API documentation](https://www.ravelry.com/api#/_fiber_categories)
    """

    actions = SimpleNamespace(list=Action("/fiber_categories.json", FiberCategoriesModel))

    def list(self) -> FiberCategoriesModel:
        """
        List the current fiber categories
        Endpoint: GET /fiber_categories.json
        """
        response_dict = self._fetch(self._http.get(self.actions.list.url))
        return cast(FiberCategoriesModel, self.actions.list.model.model_validate(response_dict))
