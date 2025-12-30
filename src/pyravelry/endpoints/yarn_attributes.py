from pyravelry.endpoints.base import BaseEndpoint
from pyravelry.models import YarnAttributeModel, YarnAttributesModel


class YarnAttributesResource(BaseEndpoint):
    """Endpoint for Color Families.

    Attributes:
        BaseEndpoint (AnyUrl): The endpoint for yarn attributes.

    Methods:
        list (list[YarnAttributeModel]): returns all yarn attributes.

    [Yarn Attributes Ravelry API documentation](https://www.ravelry.com/api#yarn_attributes_list)
    """

    endpoint: str = "/yarn_attributes/groups.json"
    output_model = YarnAttributesModel

    def list(self) -> list[YarnAttributeModel]:
        """
        List the current yarn attributes.

        Endpoint: GET /yarn_attributes/groups.json
        """
        cls = YarnAttributesResource
        response_dict = self._fetch(http_client=self._http, endpoint=cls.endpoint)
        data = cls.output_model.model_validate(response_dict)
        return data.yarn_attribute_groups
