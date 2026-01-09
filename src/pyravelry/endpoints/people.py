from pyravelry.endpoints.base import BaseEndpoint
from pyravelry.models import Identifier, UserModel, UserPostModel


class PeopleResource(BaseEndpoint):
    """People endpoint for Ravelry.

    [People Ravelry API documentation](https://www.ravelry.com/api#people_show)
    """

    endpoint: str = "/people"
    output_model = UserModel

    def show(self, username: str) -> UserModel:
        """
        Get a user's profile information.

        Args:
            username (str): Username or integer ID of the user to lookup.

        Returns:
            UserFullModel: The full user profile data.
        """
        cls = PeopleResource

        validated_username = Identifier(id=username).id
        url = "/".join([cls.endpoint, f"{validated_username}.json"])

        response_dict = self._fetch(http_client=self._http, endpoint=url, method="GET")

        return cls.output_model.model_validate(response_dict)

    def update(self, username: str, data: UserPostModel) -> UserModel:
        """
        Update a user's profile. Requires profile-write permission.

        Args:
            username (str): Username or integer ID of the user to update.
            data (UserPostModel): User object containing fields to update (e.g., about_me).

        Returns:
            UserFullModel: The updated user profile.
        """
        cls = PeopleResource

        validated_username = Identifier(id=username).id
        url = "/".join([cls.endpoint, f"{validated_username}.json"])

        payload = data.model_dump(exclude_unset=True)

        response_dict = self._fetch(
            http_client=self._http,
            endpoint=url,
            method="POST",
            json=payload,
        )

        return cls.output_model.model_validate(response_dict)
