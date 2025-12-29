from pyravelry.endpoints.base import BaseEndpoint
from pyravelry.models import YarnWeightModel, YarnWeightsModel


class YarnWeightsResource(BaseEndpoint):
    """Endpoint for Color Families.

    Attributes:
        BaseEndpoint (AnyUrl): The endpoint for yarn weights.

    Methods:
        list (list[YarnWeightModel]): returns all yarn weights.

    [Yarn Weights Ravelry API documentation](https://www.ravelry.com/api#/_yarn_weights)
    """

    endpoint: str = "/yarn_weights.json"
    output_model = YarnWeightsModel

    def list(self) -> list[YarnWeightModel]:
        """
        List the current yarn weights.

        Endpoint: GET /yarn_weights.json
        """
        cls = YarnWeightsResource
        response_dict = self._fetch(http_client=self._http, endpoint=cls.endpoint)
        data = cls.output_model.model_validate(response_dict)
        return data.yarn_weights
