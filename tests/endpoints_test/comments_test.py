from typing import Any

import pytest

from pyravelry.endpoints import CommentsResource
from pyravelry.models import CommentCreateModel, CommentFullModel, CommentHistoryModel


@pytest.mark.vcr
class TestSearchResource:
    @pytest.fixture(autouse=True)
    def setup(self, api_info: Any) -> None:
        """Automatically sets up the resource for every test in this class."""
        self.obj = CommentsResource(api_info["client"])

    def test_initialization(self) -> None:
        assert self.obj is not None

    @pytest.mark.dependency(name="comment_create")
    def test_create(self) -> None:
        data = CommentCreateModel(type="project", commented_id=12489643, body="This is a reply comment", reply_to_id=1)

        results = self.obj.create(data=data)

        pytest.shared = results.id

        assert isinstance(results, CommentFullModel)

    @pytest.mark.dependency(depends=["comment_create"])
    def test_delete(self) -> None:
        results = self.obj.delete(id_=pytest.shared)

        assert isinstance(results, CommentFullModel)

    def test_list(self) -> None:
        results = self.obj.list(username="cltheuer")

        assert isinstance(results, list)
        assert isinstance(results[0], CommentHistoryModel)
