from typing import Any

import pytest

from pyravelry.endpoints import CommentsResource
from pyravelry.models import CommentFullModel, CommentHistoryModel


@pytest.mark.vcr
class TestCommentsResource:
    @pytest.fixture(autouse=True)
    def setup(self, api_info: Any) -> None:
        """Automatically sets up the resource for every test in this class."""
        self.obj = CommentsResource(api_info["client"])

    def test_initialization(self) -> None:
        assert self.obj is not None

    @pytest.mark.dependency(name="comment_create")
    def test_create(self) -> None:
        results = self.obj.create(type_="project", commented_id=12489643, body="This is a reply comment", reply_to_id=1)

        pytest.shared = results.id

        assert isinstance(results, CommentFullModel)

        pd_df = results.to_pandas()
        pl_df = results.to_polars()

        assert not pd_df.empty
        assert not pl_df.is_empty()

    @pytest.mark.dependency(depends=["comment_create"])
    def test_delete(self) -> None:
        results = self.obj.delete(id_=pytest.shared)

        assert isinstance(results, CommentFullModel)

        pd_df = results.to_pandas()
        pl_df = results.to_polars()

        assert not pd_df.empty
        assert not pl_df.is_empty()

    def test_list(self) -> None:
        results = self.obj.list(username="cltheuer")

        data = results.comments

        assert isinstance(data, list)
        assert isinstance(data[0], CommentHistoryModel)

        pd_df = results.to_pandas()
        pl_df = results.to_polars()

        assert not pd_df.empty
        assert not pl_df.is_empty()
