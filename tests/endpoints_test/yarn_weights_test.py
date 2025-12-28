from typing import Any

import pytest

from pyravelry.endpoints import YarnWeightsResource
from pyravelry.models import YarnWeightModel


@pytest.mark.vcr
class TestYarnWeightsResource:
    @pytest.fixture(autouse=True)
    def setup(self, api_info: Any) -> None:
        """Automatically sets up the resource for every test in this class."""
        self.obj = YarnWeightsResource(api_info["client"])

    def test_initialization(self) -> None:
        assert self.obj is not None

    def test_list(self) -> None:
        list_of_fiber_categories = self.obj.list()

        assert isinstance(list_of_fiber_categories, list)
        assert len(list_of_fiber_categories) > 0
        assert isinstance(list_of_fiber_categories[0], YarnWeightModel)
