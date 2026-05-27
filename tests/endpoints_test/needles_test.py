from typing import Any

import pytest

from pyravelry.endpoints import NeedlesResource
from pyravelry.models import NeedleRecordFullModel, NeedleSizeFullModel, NeedleTypeFullModel


@pytest.mark.vcr
class TestNeedlesResource:
    @pytest.fixture(autouse=True)
    def setup(self, api_info: Any) -> None:
        """Automatically sets up the resource for every test in this class."""
        self.obj = NeedlesResource(api_info["client"])

    def test_initialization(self) -> None:
        assert self.obj is not None

    def test_list(self) -> None:
        obj = self.obj.list(username="maryheatherb")

        obj_list = obj.needle_records

        assert isinstance(obj_list, list)
        assert len(obj_list) > 0
        assert isinstance(obj_list[0], NeedleRecordFullModel)

        pd_df = obj.to_pandas()
        pl_df = obj.to_polars()

        assert not pd_df.empty
        assert not pl_df.is_empty()

    def test_sizes(self) -> None:
        obj = self.obj.sizes()

        obj_sizes = obj.needle_sizes

        assert isinstance(obj_sizes, list)
        assert len(obj_sizes) > 0
        assert isinstance(obj_sizes[0], NeedleSizeFullModel)

        pd_df = obj.to_pandas()
        pl_df = obj.to_polars()

        assert not pd_df.empty
        assert not pl_df.is_empty()

    def test_types(self) -> None:
        obj = self.obj.types()

        obj_types = obj.needle_types

        assert isinstance(obj_types, list)
        assert len(obj_types) > 0
        assert isinstance(obj_types[0], NeedleTypeFullModel)

        pd_df = obj.to_pandas()
        pl_df = obj.to_polars()

        assert not pd_df.empty
        assert not pl_df.is_empty()
