from typing import Any

import pytest

import pyravelry
from pyravelry.endpoints import YarnsResource


@pytest.mark.vcr
class TestYarnsResource:
    @pytest.fixture(autouse=True)
    def setup(self, api_info: Any) -> None:
        """Automatically sets up the resource for every test in this class."""
        self.obj = YarnsResource(api_info["client"])

    def test_initialization(self) -> None:
        assert self.obj is not None

    def test_comments(self) -> None:

        obj = self.obj.comments(id_=100)

        with pytest.raises(NotImplementedError):
            obj.to_pandas()
        with pytest.raises(NotImplementedError):
            obj.to_polars()

        assert isinstance(obj.comments, pyravelry.models.comment.CommentListModel)
        assert isinstance(obj.paginator, pyravelry.models.custom_models.paginator.PaginatorModel)

        pd_com_df = obj.comments.to_pandas()
        pl_com_df = obj.comments.to_polars()

        pd_pag_df = obj.paginator.to_pandas()
        pl_pag_df = obj.paginator.to_polars()

        assert not pd_com_df.empty
        assert not pl_com_df.is_empty()
        assert not pd_pag_df.empty
        assert not pl_pag_df.is_empty()

    def test_search(self) -> None:
        obj = self.obj.search(query="merino")

        with pytest.raises(NotImplementedError):
            obj.to_pandas()
        with pytest.raises(NotImplementedError):
            obj.to_polars()

        assert isinstance(obj.yarns, pyravelry.models.yarn.YarnListListModel)
        assert isinstance(obj.paginator, pyravelry.models.custom_models.paginator.PaginatorModel)

        pd_yarns_df = obj.yarns.to_pandas()
        pl_yarns_df = obj.yarns.to_polars()

        pd_pag_df = obj.paginator.to_pandas()
        pl_pag_df = obj.paginator.to_polars()

        assert not pd_yarns_df.empty
        assert not pl_yarns_df.is_empty()
        assert not pd_pag_df.empty
        assert not pl_pag_df.is_empty()

    def test_show(self) -> None:
        obj = self.obj.show(id_=100)

        with pytest.raises(NotImplementedError):
            obj.to_pandas()
        with pytest.raises(NotImplementedError):
            obj.to_polars()

        assert isinstance(obj.yarn, pyravelry.models.yarn.YarnFullModel)
        assert obj.paginator is None

        pd_yarns_df = obj.yarn.to_pandas()
        pl_yarns_df = obj.yarn.to_polars()

        assert not pd_yarns_df.empty
        assert not pl_yarns_df.is_empty()

    def test_yarns(self) -> None:
        obj = self.obj.yarns(ids=[101, 102])

        assert isinstance(obj.yarns, dict)
        assert isinstance(obj.yarns.get(101), pyravelry.models.yarn.YarnFullModel)

        pd_df = obj.to_pandas()
        pl_df = obj.to_polars()

        assert not pd_df.empty
        assert not pl_df.is_empty()
