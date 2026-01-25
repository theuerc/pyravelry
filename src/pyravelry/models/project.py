from __future__ import annotations

from datetime import date, datetime
from typing import Any

from pydantic import Field

from .base import BaseRavelryModel
from .pack import PackFullModel, PackPostModel

# Assuming these are imported from your other modules
from .photo import PhotoFullModel
from .tool import ToolModel
from .user import UserSmallModel


class ProjectBaseModel(BaseRavelryModel):
    """Base fields shared across most Project variations.

    [Project Ravelry API documentation](https://www.ravelry.com/api#Project_result)
    """

    id: int
    name: str
    permalink: str
    comments_count: int
    favorites_count: int
    photos_count: int
    created_at: datetime
    updated_at: datetime

    craft_id: int | None = None
    craft_name: str | None = None
    progress: int | None = Field(None, ge=0, le=100)
    rating: int | None = None

    started: date | None = None
    started_day_set: bool = True
    completed: date | None = None
    completed_day_set: bool = True

    gauge: float | None = None
    gauge_divisor: int | None = None
    gauge_pattern: str | None = None
    gauge_repeats: int | None = None
    row_gauge: float | None = None

    ends_per_inch: float | None = None
    picks_per_inch: float | None = None

    size: str | None = None
    made_for: str | None = None
    made_for_user_id: int | None = None

    pattern_id: int | None = None
    pattern_name: str | None = None
    status_name: str | None = None
    project_status_id: int | None = None
    project_status_changed: Any | None = None  # Type not specified in docs

    tag_names: list[str] | None = Field(default_factory=list)
    links: dict | None = None


class ProjectSmallModel(ProjectBaseModel):
    """Simplified project view."""

    user_id: int


class ProjectModel(ProjectBaseModel):
    """The standard Project object."""

    user_id: int | None = None
    user: UserSmallModel | None = None
    first_photo: PhotoFullModel | None = None


class ProjectNotesModel(ProjectModel):
    """Project with public notes included."""

    notes: str | None = None
    notes_html: str | None = None


class ProjectFullModel(ProjectNotesModel):
    """Comprehensive project data including packs and tools."""

    packs: list[PackFullModel] | None = Field(default_factory=list)
    photos: list[PhotoFullModel] | None = Field(default_factory=list)
    tools: list[ToolModel] | None = Field(default_factory=list)
    needle_sizes: list[Any] | None = None
    personal_attributes: dict | None = None


class ProjectFullForOwnerModel(ProjectFullModel):
    """Project data with private notes and owner-specific pack info."""

    private_notes: str | None = None
    private_notes_html: str | None = None
    # Overriding packs to use the owner-specific version if necessary
    packs: list[PackFullModel] | None = Field(default_factory=list)


class ProjectPostModel(BaseRavelryModel):
    """Model used for creating or updating a project via POST.

    [Project POST Ravelry API documentation](https://www.ravelry.com/api#Project_update)
    """

    name: str
    craft_id: int | None = None
    made_for: str | None = None
    made_for_user_id: int | None = None
    notes: str | None = None
    private_notes: str | None = None
    progress: int | None = None
    project_status_id: int | None = None
    rating: int | None = None
    started: date | None = None
    completed: date | None = None
    pattern_id: int | None = None
    personal_pattern_name: str | None = None
    size: str | None = None
    tag_names: list[str] | None = None
    needle_sizes: list[int] | None = Field(None, description="List of needle size IDs")
    packs: list[PackPostModel] | None = None


class ProjectsModel(BaseRavelryModel):
    """Wrapper for plural project responses."""

    projects: list[ProjectModel]
