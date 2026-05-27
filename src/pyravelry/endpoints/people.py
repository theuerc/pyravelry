from types import SimpleNamespace
from typing import cast

from pydantic import validate_call

from pyravelry.endpoints.base import Action, BaseEndpoint
from pyravelry.models import UserModel, UserPostModel


class PeopleResource(BaseEndpoint):
    """People endpoint for Ravelry.

    [People Ravelry API documentation](https://www.ravelry.com/api#people_show)
    """

    actions = SimpleNamespace(
        show=Action("/people/{}.json", UserModel),
        update=Action("/people/{}.json", UserModel),
    )

    @validate_call
    def show(self, username: str) -> UserModel:
        """
        Get a user's profile information.

        Args:
            username (str): Username or integer ID of the user to lookup.

        Returns:
            UserFullModel: The full user profile data.
        """
        response_dict = self._fetch(self._http.get(self.actions.show.url.format(username)))

        return cast(UserModel, self.actions.show.model.model_validate(response_dict))

    @validate_call
    def update(
        self,
        username: str,
        first_name: str | None = None,
        about_me: str | None = None,
        fave_colors: str | None = None,
        fave_curse: str | None = None,
        location: str | None = None,
    ) -> UserModel:
        """
        Update a user's profile. Requires profile-write permission.

        Args:
            username (str): Username or integer ID of the user to update.
            first_name (str | None): User's first name.
            about_me (str | None): User's "About Me" description.
            fave_colors (str | None): User's favorite colors.
            fave_curse (str | None): User's favorite curse word.
            location (str | None): User's location.

        Returns:
            UserFullModel: The updated user profile.
        """
        update_data = {
            "first_name": first_name,
            "about_me": about_me,
            "fave_colors": fave_colors,
            "fave_curse": fave_curse,
            "location": location,
        }

        payload = UserPostModel(**update_data).model_dump(exclude_unset=True)

        response_dict = self._fetch(self._http.post(self.actions.update.url.format(username), json=payload))

        return cast(UserModel, self.actions.update.model.model_validate(response_dict))
