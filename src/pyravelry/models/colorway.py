from typing import Optional

from pydantic import Field

from .base import BaseRavelryModel


class ColorwayModel(BaseRavelryModel):
    """Represents a Ravelry Colorway results object.

    This includes the basic attributes shared by both the standard
    and full colorway objects.

    [Colorway Ravelry API documentation](https://www.ravelry.com/api#Colorway_result)
    """

    id: int
    name: str
    yarn_id: int
    code: Optional[str] = Field(None, description="Numeric or alphanumeric color code")


class ColorwayFullModel(ColorwayModel):
    """Represents the full Colorway object with usage statistics.

    Extends ColorwayModel to include project counts and photo URLs.

    [Colorway Ravelry API documentation](https://www.ravelry.com/api#Colorway_result)
    """

    photo_url: Optional[str] = Field(None, description="URL to the colorway image")
    projects_count: int = Field(0, description="Number of projects using this colorway")
    stashes_count: int = Field(0, description="Number of stashes using this colorway")
    usage_count: int = Field(0, description="Total usage count")


class ColorwaysModel(BaseRavelryModel):
    """Wrapper for responses returning a list of colorways.

    [Colorway Ravelry API documentation](https://www.ravelry.com/api#Colorway_result)
    """

    colorways: list[ColorwayModel]
