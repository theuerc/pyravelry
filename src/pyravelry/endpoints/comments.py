from typing import Literal

from pydantic import validate_call

from pyravelry.endpoints.base import BaseEndpoint
from pyravelry.models import (
    CommentFullModel,
    CommentHistoriesModel,
    SimplifiedPaginator,
)


class CommentsResource(BaseEndpoint):
    """Endpoint for Comments.

    Methods:
        create (CommentFullModel): Post a comment related to an object.
        delete (CommentFullModel): Delete a specific comment by ID.
        list (list[CommentHistoryModel]): Get list of comments left by a user.

    [Comments Ravelry API documentation](https://www.ravelry.com/api#/_comments)
    """

    endpoint = "/comments"
    paginator_model = SimplifiedPaginator
    output_model = CommentFullModel
    list_model = CommentHistoriesModel

    @validate_call
    def create(
        self, type_: Literal["project", "pattern", "yarn", "stash"], commented_id: int, body: str, reply_to_id: int
    ) -> CommentFullModel:
        """
        Post a comment related to an object (project, pattern, yarn, or stash).

        Arguments:
            type_ (Literal["project", "pattern", "yarn", "stash"]): The type of item being commented on.
            commented_id (int): ID of the item being commented on.
            body (str): Comment body.
            reply_to_id (int): ID of the comment being replied to. Restricted to item owners.

        Returns:
            (CommentFullModel): The published comment
        """
        cls = CommentsResource

        url = "/".join([cls.endpoint, "create.json"])

        payload = {
            "type": type_,
            "commented_id": commented_id,
            "body": body,
            "reply_to_id": reply_to_id,
        }

        response_dict = self._fetch(http_client=self._http, endpoint=url, method="POST", params=payload)

        return CommentFullModel.model_validate(response_dict["comment"])

    @validate_call
    def delete(self, id_: int) -> CommentFullModel:
        """
        Delete a comment by its ID.

        Arguments:
            id_ (int): The comment ID to delete.

        Returns:
            (CommentFullModel): The deleted comment.
        """
        cls = CommentsResource

        url = "/".join([cls.endpoint, f"{id_}.json"])

        response_dict = self._fetch(http_client=self._http, endpoint=url, method="DELETE")

        return CommentFullModel.model_validate(response_dict["comment"])

    @validate_call
    def list(self, username: str, page: int = 1, page_size: int = 25) -> CommentHistoriesModel:
        """
        Get list of comments left by a specific user.
        """
        cls = CommentsResource

        params = cls.paginator_model(page=page, page_size=page_size)

        url = "/".join(["people", str(username), "comments", "list.json"])
        response_dict = self._fetch(http_client=self._http, endpoint=url, params=params.model_dump())

        data = CommentHistoriesModel.model_validate(response_dict)
        return data
