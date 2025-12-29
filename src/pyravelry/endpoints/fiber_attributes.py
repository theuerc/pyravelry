from pyravelry.endpoints.base import BaseEndpoint
from pyravelry.models import FiberAttributeModel, FiberAttributesModel


class FiberAttributesResource(BaseEndpoint):
    """Endpoint for Fiber Attributes.

    Attributes:
        BaseEndpoint (AnyUrl): The endpoint for fiber attributes.

    Methods:
        list (list[FiberAttributeModel]): returns all fiber attributes.

    [Fiber Attributes Ravelry API documentation](https://www.ravelry.com/api#/_fiber_attributes)
    """

    endpoint: str = "/fiber_attributes.json"
    output_model = FiberAttributesModel

    def list(self) -> list[FiberAttributeModel]:
        """
        List the current fiber attributes

        Endpoint: GET /fiber_attributes.json
        """
        cls = FiberAttributesResource
        response_dict = self._fetch(http_client=self._http, endpoint=cls.endpoint)
        data = cls.output_model.model_validate(response_dict)
        return data.fiber_attributes
