from typing import Optional

from pydantic import Field

from .base import BaseRavelryModel
from .socialsite import SocialSiteModel


class UserSiteModel(BaseRavelryModel):
    """Represents a Ravelry UserSite object.

    [UserSite Ravelry API documentation](https://www.ravelry.com/api#UserSite_result)
    """

    id: int
    social_site: SocialSiteModel = Field(..., description="Details about the external site")
    url: Optional[str] = Field(None, description="URL to profile page on an external site")
    username: Optional[str] = Field(None, description="Username on an external site")


class UserSitesModel(BaseRavelryModel):
    """Wrapper for a list of user sites, often found in user profile responses.

    [UserSite Ravelry API documentation](https://www.ravelry.com/api#UserSite_result)
    """

    user_sites: list[UserSiteModel]
