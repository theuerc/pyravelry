from __future__ import annotations

from datetime import datetime
from typing import Any, Literal

from pydantic import Field, field_validator

from .base import BaseRavelryModel
from .project import ProjectModel
from .user import UserSmallModel


class CommentCreateModel(BaseRavelryModel):
    """Input parameters for model.

    [Comments Endpoint Ravelry API documentation](https://www.ravelry.com/api/#comments_create)
    """

    type: Literal["project", "pattern", "yarn", "stash"] = Field(
        ..., alias="type", description="The type of item being commented on."
    )
    commented_id: int = Field(..., description="ID of the item being commented on.")
    body: str = Field(..., description="Comment body. Supports Text, Markdown, or HTML.")
    reply_to_id: int | None = Field(None, description="ID of the comment being replied to. Restricted to item owners.")


class CreatedAtBase(BaseRavelryModel):
    """Has an additional created at attribute for handling custom Ravelry parsing.

    [Comments Ravelry API documentation](https://www.ravelry.com/api/#Comment_result)
    """

    created_at: datetime = Field(..., description="Creation time")

    @field_validator("created_at", mode="before")
    @classmethod
    def parse_slashed_datetime(cls, v: Any) -> Any:
        """Parses custom datetime from ravelry."""
        if isinstance(v, str) and "/" in v:
            v = v.replace("/", "-")
            try:
                return datetime.strptime(v, "%Y-%m-%d %H:%M:%S %z")
            except ValueError:
                return v
        return v


class CommentModel(CreatedAtBase):
    """Represents the standard Ravelry Comment object.

    [Comments Ravelry API documentation](https://www.ravelry.com/api/#Comment_result)
    """

    id: int
    comment_html: str = Field(..., description="Comment body (HTML formatted)")
    user: UserSmallModel = Field(..., description="The user who posted the comment")
    highlighted_project: ProjectModel | None = Field(None, description="Related project, if requested and available")


class CommentHistoryModel(CreatedAtBase):
    """Represents a Comment in a history context.

    [Comments Ravelry API documentation](https://www.ravelry.com/api/#Comment_result)
    """

    id: int
    comment_html: str | None = None
    user_id: int = Field(..., description="The ID of the user who posted the comment")
    commentable: Any | None = None  # Polymorphic type depending on context


class CommentHistoriesModel(BaseRavelryModel):
    """Represents multiple Comment in a history context.

    [Comments Ravelry API documentation](https://www.ravelry.com/api/#Comment_result)
    """

    comments: list[CommentHistoryModel]


class CommentFullModel(CommentModel):
    """Represents a full Ravelry Comment with nested replies.

    [Comments Ravelry API documentation](https://www.ravelry.com/api/#Comment_result)
    """

    # Replies are limited to 1 level deep per API docs
    replies: list[CommentModel] = Field(
        default_factory=list, description="Replies to the comment (nesting limited to 1 level)"
    )


class CommentExportModel(CreatedAtBase):
    """Simplified Comment model for export purposes.

    [Comments Ravelry API documentation](https://www.ravelry.com/api/#Comment_result)
    """

    id: int
    comment_html: str
