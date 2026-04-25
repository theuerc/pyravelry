from typing import Any

import pytest

from pyravelry.endpoints import PeopleResource
from pyravelry.models import UserModel


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

        pd_df = results.to_pandas()
        pl_df = results.to_polars()

        assert not pd_df.empty
        assert not pl_df.is_empty()

    def test_update_description(self) -> None:
        old_user = self.obj.update(username="cltheuer", fave_colors="Blue")

        new_user = self.obj.update(username="cltheuer", fave_colors="Red")

        assert old_user != new_user

        pd_df = old_user.to_pandas()
        pl_df = old_user.to_polars()

        assert not pd_df.empty
        assert not pl_df.is_empty()
