from typing import Any

import pytest

from pyravelry.endpoints import ColorFamiliesResource
from pyravelry.models import ColorFamilyModel


@pytest.mark.vcr
class TestColorFamiliesResource:
    @pytest.fixture(autouse=True)
    def setup(self, api_info: Any) -> None:
        """Automatically sets up the resource for every test in this class."""
        self.obj = ColorFamiliesResource(api_info["client"])

    def test_initialization(self) -> None:
        assert self.obj is not None

    def test_list(self) -> None:
        list_of_color_families = self.obj.list()

        color_family_list = list_of_color_families.color_families
        assert isinstance(color_family_list, list)
        assert len(color_family_list) > 0
        assert isinstance(color_family_list[0], ColorFamilyModel)

        pd_df = list_of_color_families.pandas
        pl_df = list_of_color_families.polars

        assert not pd_df.empty
        assert not pl_df.is_empty()
