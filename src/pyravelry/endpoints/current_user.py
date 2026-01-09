from pyravelry.endpoints.base import BaseEndpoint
from pyravelry.models import UserFullModel, UserModel


class CurrentUserResource(BaseEndpoint):
    """Endpoint for the currently authenticated user.

    Attributes:
        endpoint (str): The endpoint for current_user.
        output_model (UserModel): The pydantic model that the api output is validated against.

    Methods:
        get (UserModel): Returns the authenticated user's details.

    [Current User Ravelry API documentation](https://www.ravelry.com/api#/_current_user)
    """

    endpoint: str = "/current_user.json"
    output_model = UserModel

    def get(self) -> UserFullModel:
        """
        Retrieves the details of the currently authenticated user.
        """
        cls = CurrentUserResource
        response_dict = self._fetch(http_client=self._http, endpoint=cls.endpoint)
        data = cls.output_model.model_validate(response_dict)
        return data.user
