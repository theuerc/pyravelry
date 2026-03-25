from typing import Any

import pytest

from pyravelry.endpoints import FiberCategoriesResource
from pyravelry.models import FiberCategoryModel


@pytest.mark.vcr
class TestFiberCategoriesResource:
    @pytest.fixture(autouse=True)
    def setup(self, api_info: Any) -> None:
        """Automatically sets up the resource for every test in this class."""
        self.obj = FiberCategoriesResource(api_info["client"])

    def test_initialization(self) -> None:
        assert self.obj is not None

    def test_list(self) -> None:
        list_of_fiber_categories_ = self.obj.list()

        list_of_fiber_categories = list_of_fiber_categories_.fiber_categories

        assert isinstance(list_of_fiber_categories, list)
        assert len(list_of_fiber_categories) > 0
        assert isinstance(list_of_fiber_categories[0], FiberCategoryModel)

        pd_df = list_of_fiber_categories_.pandas
        pl_df = list_of_fiber_categories_.polars

        assert not pd_df.empty
        assert not pl_df.is_empty()
