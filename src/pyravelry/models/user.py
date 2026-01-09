from __future__ import annotations

from pydantic import Field

from .base import BaseRavelryModel
from .usersite import UserSiteModel


class PatternAuthorForUserModel(BaseRavelryModel):
    """Represents a PatternAuthor (for_user) object.

    [Ravelry API documentation](https://www.ravelry.com/api#PatternAuthor_result)
    """

    id: int
    name: str = Field(..., description="Designer's full name or alias")
    permalink: str
    favorites_count: int | None = Field(None, description="Number of times the designer has been favorited")
    patterns_count: int | None = Field(None, description="Number of patterns attributed to the designer")


class UserSmallModel(BaseRavelryModel):
    """Represents the User (small) object."""

    id: int
    username: str
    tiny_photo_url: str | None = None
    small_photo_url: str | None = None
    photo_url: str | None = None
    large_photo_url: str | None = None
    profile_country_code: str | None = None


class UserFullModel(UserSmallModel):
    """Represents the User (full/export) object.

    Includes all fields from User (small) plus extended profile information.
    """

    first_name: str | None = None
    about_me: str | None = Field(None, description="Raw 'About me' text")
    about_me_html: str | None = Field(None, description="Rendered HTML 'About me' text")
    fave_colors: str | None = None
    fave_curse: str | None = None
    location: str | None = None

    # Relationships
    pattern_author: PatternAuthorForUserModel | None = Field(None, description="The designer linked to this user")
    user_sites: list[UserSiteModel] | None = Field(None, description="External social/etc sites added to profile")


class UserPostModel(BaseRavelryModel):
    """Model used for updating a User profile via POST.

    [Ravelry API documentation](https://www.ravelry.com/api#User_result)
    """

    first_name: str | None = Field(None, description="User's first name")
    about_me: str | None = Field(None, description='raw "About me" text. Can contain markdown and/or HTML')
    fave_colors: str | None = Field(None, description="User's favorite colors")
    fave_curse: str | None = Field(None, description="User's favorite curse word")
    location: str | None = Field(None, description="User's geographic location")


class UserModel(BaseRavelryModel):
    user: UserFullModel
