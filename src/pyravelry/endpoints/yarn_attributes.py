from typing import cast

from pyravelry.endpoints.base import Action, BaseEndpoint, TypedNamespace
from pyravelry.models import YarnAttributesModel


class YarnAttributesResource(BaseEndpoint):
    """Endpoint for Color Families.

    Attributes:
        BaseEndpoint (AnyUrl): The endpoint for yarn attributes.

    Methods:
        list (list[YarnAttributeModel]): returns all yarn attributes.

    [Yarn Attributes Ravelry API documentation](https://www.ravelry.com/api#yarn_attributes_list)
    """

    actions = TypedNamespace(list=Action("/yarn_attributes/groups.json", YarnAttributesModel))

    def list(self) -> YarnAttributesModel:
        """
        List the current yarn attributes.

        Endpoint: GET /yarn_attributes/groups.json
        """
        response_dict = self._fetch(self._http.get(self.actions.list.url))
        return cast(YarnAttributesModel, self.actions.list.model.model_validate(response_dict))
