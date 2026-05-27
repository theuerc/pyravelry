from types import SimpleNamespace
from typing import cast

from pyravelry.endpoints.base import Action, BaseEndpoint
from pyravelry.models import FiberAttributesModel


class FiberAttributesResource(BaseEndpoint):
    """Endpoint for Fiber Attributes.

    Attributes:
        BaseEndpoint (AnyUrl): The endpoint for fiber attributes.

    Methods:
        list (list[FiberAttributeModel]): returns all fiber attributes.

    [Fiber Attributes Ravelry API documentation](https://www.ravelry.com/api#/_fiber_attributes)
    """

    actions = SimpleNamespace(list=Action("/fiber_attributes.json", FiberAttributesModel))

    def list(self) -> FiberAttributesModel:
        """
        List the current fiber attributes

        Endpoint: GET /fiber_attributes.json
        """
        response_dict = self._fetch(self._http.get(self.actions.list.url))
        return cast(FiberAttributesModel, self.actions.list.model.model_validate(response_dict))
