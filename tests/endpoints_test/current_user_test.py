from typing import Any

import pytest

from pyravelry.endpoints import CurrentUserResource
from pyravelry.models import UserFullModel


@pytest.mark.vcr
class TestCurrentUserResource:
    @pytest.fixture(autouse=True)
    def setup(self, api_info: Any) -> None:
        """Automatically sets up the resource for every test in this class."""
        self.obj = CurrentUserResource(api_info["client"])

    def test_initialization(self) -> None:
        assert self.obj is not None

    def test_list(self) -> None:
        current_user = self.obj.get()

        assert isinstance(current_user, UserFullModel)
