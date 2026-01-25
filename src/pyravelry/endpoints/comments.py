from pyravelry.endpoints.base import BaseEndpoint
from pyravelry.models import (
    CommentCreateModel,
    CommentFullModel,
    CommentHistoriesModel,
    CommentHistoryModel,
    Identifier,
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

    def create(self, data: CommentCreateModel) -> CommentFullModel:
        """
        Post a comment related to an object (project, pattern, yarn, or stash).

        Arguments:
            data (CommentCreateModel): the data for the comment being created.

        Returns:
            (CommentFullModel): The published comment
        """
        cls = CommentsResource

        url = "/".join([cls.endpoint, "create.json"])

        payload = data.model_dump(exclude_unset=True)

        response_dict = self._fetch(http_client=self._http, endpoint=url, method="POST", params=payload)

        return CommentFullModel.model_validate(response_dict["comment"])

    def delete(self, id_: int) -> CommentFullModel:
        """
        Delete a comment by its ID.

        Arguments:
            id_ (int): The comment ID to delete.

        Returns:
            (CommentFullModel): The deleted comment.
        """
        cls = CommentsResource

        verified_id = Identifier(id=id_).id

        url = "/".join([cls.endpoint, f"{verified_id}.json"])

        response_dict = self._fetch(http_client=self._http, endpoint=url, method="DELETE")

        return CommentFullModel.model_validate(response_dict["comment"])

    def list(self, username: str, page: int = 1, page_size: int = 25) -> list[CommentHistoryModel]:
        """
        Get list of comments left by a specific user.
        """
        cls = CommentsResource

        validated_username = Identifier(id=username).id

        params = cls.paginator_model(page=page, page_size=page_size)

        url = "/".join(["people", str(validated_username), "comments", "list.json"])
        response_dict = self._fetch(http_client=self._http, endpoint=url, params=params.model_dump())

        data = CommentHistoriesModel.model_validate(response_dict)
        return data.comments
