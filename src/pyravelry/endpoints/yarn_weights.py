from types import SimpleNamespace
from typing import cast

from pyravelry.endpoints.base import Action, BaseEndpoint
from pyravelry.models import YarnWeightsModel


class YarnWeightsResource(BaseEndpoint):
    """Endpoint for Color Families.

    Attributes:
        BaseEndpoint (AnyUrl): The endpoint for yarn weights.

    Methods:
        list (list[YarnWeightModel]): returns all yarn weights.

    [Yarn Weights Ravelry API documentation](https://www.ravelry.com/api#/_yarn_weights)
    """

    actions = SimpleNamespace(list=Action("/yarn_weights.json", YarnWeightsModel))

    def list(self) -> YarnWeightsModel:
        """
        List the current yarn weights.

        Endpoint: GET /yarn_weights.json
        """
        response_dict = self._fetch(self._http.get(self.actions.list.url))
        return cast(YarnWeightsModel, self.actions.list.model.model_validate(response_dict))
