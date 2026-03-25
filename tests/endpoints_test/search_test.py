from typing import Any

import pytest

from pyravelry.endpoints import SearchResource
from pyravelry.models import SearchResultModel


@pytest.mark.vcr
class TestSearchResource:
    @pytest.fixture(autouse=True)
    def setup(self, api_info: Any) -> None:
        """Automatically sets up the resource for every test in this class."""
        self.obj = SearchResource(api_info["client"])

    def test_initialization(self) -> None:
        assert self.obj is not None

    def test_query(self) -> None:
        results_ = self.obj.query(query="merino", limit=10, types=["Yarn"])

        results = results_.results

        assert isinstance(results, list)
        assert len(results) > 0
        assert isinstance(results[0], SearchResultModel)

        pd_df = results_.pandas
        pl_df = results_.polars

        assert not pd_df.empty
        assert not pl_df.is_empty()

    def test_query__multiple_types(self) -> None:
        # should split and strip types
        results_ = self.obj.query(query="merino", limit=10, types=["Yarn", "Group", "Event"])

        results = results_.results

        assert isinstance(results, list)
        assert len(results) > 0
        assert isinstance(results[0], SearchResultModel)

        pd_df = results_.pandas
        pl_df = results_.polars

        assert not pd_df.empty
        assert not pl_df.is_empty()
