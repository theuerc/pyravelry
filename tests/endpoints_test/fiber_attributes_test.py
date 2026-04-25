from typing import Any

import pytest

from pyravelry.endpoints import FiberAttributesResource
from pyravelry.models import FiberAttributeModel


@pytest.mark.vcr
class TestFiberAttributesResource:
    @pytest.fixture(autouse=True)
    def setup(self, api_info: Any) -> None:
        """Automatically sets up the resource for every test in this class."""
        self.obj = FiberAttributesResource(api_info["client"])

    def test_initialization(self) -> None:
        assert self.obj is not None

    def test_list(self) -> None:
        list_of_fiber_attributes_ = self.obj.list()

        list_of_fiber_attributes = list_of_fiber_attributes_.fiber_attributes

        assert isinstance(list_of_fiber_attributes, list)
        assert len(list_of_fiber_attributes) > 0
        assert isinstance(list_of_fiber_attributes[0], FiberAttributeModel)

        pd_df = list_of_fiber_attributes_.to_pandas()
        pl_df = list_of_fiber_attributes_.to_polars()

        assert not pd_df.empty
        assert not pl_df.is_empty()
