from typing import Any

import pytest

from pyravelry.endpoints import PeopleResource
from pyravelry.models import UserModel, UserPostModel


@pytest.mark.vcr
class TestSearchResource:
    @pytest.fixture(autouse=True)
    def setup(self, api_info: Any) -> None:
        """Automatically sets up the resource for every test in this class."""
        self.obj = PeopleResource(api_info["client"])

    def test_initialization(self) -> None:
        assert self.obj is not None

    def test_show(self) -> None:
        results = self.obj.show(username="cltheuer")

        assert isinstance(results, UserModel)

    def test_update_description(self) -> None:
        data = UserPostModel(fave_colors="Blue")

        old_user = self.obj.update(username="cltheuer", data=data)

        data = UserPostModel(fave_colors="Red")

        new_user = self.obj.update(username="cltheuer", data=data)

        assert old_user != new_user
