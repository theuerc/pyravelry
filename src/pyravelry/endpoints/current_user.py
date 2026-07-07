from typing import cast

from pyravelry.endpoints.base import Action, BaseEndpoint, TypedNamespace
from pyravelry.models import UserModel


class CurrentUserResource(BaseEndpoint):
    """Endpoint for the currently authenticated user.

    Attributes:
        endpoint (str): The endpoint for current_user.
        output_model (UserModel): The pydantic model that the api output is validated against.

    Methods:
        get (UserModel): Returns the authenticated user's details.

    [Current User Ravelry API documentation](https://www.ravelry.com/api#/_current_user)
    """

    actions = TypedNamespace(get=Action("/current_user.json", UserModel))

    def get(self) -> UserModel:
        """
        Retrieves the details of the currently authenticated user.
        """
        response_dict = self._fetch(self._http.get(self.actions.get.url))
        return cast(UserModel, self.actions.get.model.model_validate(response_dict))
