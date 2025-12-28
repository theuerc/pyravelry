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

        assert isinstance(list_of_color_families, list)
        assert len(list_of_color_families) > 0
        assert isinstance(list_of_color_families[0], ColorFamilyModel)
