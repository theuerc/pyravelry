from typing import Any

import pytest

from pyravelry.endpoints import YarnCompaniesResource
from pyravelry.models import YarnCompanyModel, YarnCompanySearchResponseModel


@pytest.mark.vcr
class TestYarnCompanyResources:
    @pytest.fixture(autouse=True)
    def setup(self, api_info: Any) -> None:
        """Automatically sets up the resource for every test in this class."""
        self.obj = YarnCompaniesResource(api_info["client"])

    def test_initialization(self) -> None:
        assert self.obj is not None

    def test_query(self) -> None:
        results = self.obj.query(
            query="Lion",
            page=1,
            page_size=10,
            sort="best_",
        )
        assert isinstance(results, YarnCompanySearchResponseModel)
        assert len(results.yarn_companies) > 0
        assert isinstance(results.yarn_companies[0], YarnCompanyModel)
