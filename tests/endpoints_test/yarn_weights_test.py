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
        list_of_yarn_weights_ = self.obj.list()

        list_of_yarn_weights = list_of_yarn_weights_.yarn_weights

        assert isinstance(list_of_yarn_weights, list)
        assert len(list_of_yarn_weights) > 0
        assert isinstance(list_of_yarn_weights[0], YarnWeightModel)

        pd_df = list_of_yarn_weights_.pandas
        pl_df = list_of_yarn_weights_.polars

        assert not pd_df.empty
        assert not pl_df.is_empty()
