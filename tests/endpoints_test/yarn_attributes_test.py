from typing import Any

import pytest

from pyravelry.endpoints import YarnAttributesResource
from pyravelry.models import YarnAttributeModel


@pytest.mark.vcr
class TestYarnAttributesResource:
    @pytest.fixture(autouse=True)
    def setup(self, api_info: Any) -> None:
        """Automatically sets up the resource for every test in this class."""
        self.obj = YarnAttributesResource(api_info["client"])

    def test_initialization(self) -> None:
        assert self.obj is not None

    def test_list(self) -> None:
        list_of_yarn_attributes_ = self.obj.list()
        list_of_yarn_attributes = list_of_yarn_attributes_.yarn_attribute_groups

        assert isinstance(list_of_yarn_attributes, list)
        assert len(list_of_yarn_attributes) > 0
        assert isinstance(list_of_yarn_attributes[0], YarnAttributeModel)

        pd_df = list_of_yarn_attributes_.pandas
        pl_df = list_of_yarn_attributes_.polars

        assert not pd_df.empty
        assert not pl_df.is_empty()
