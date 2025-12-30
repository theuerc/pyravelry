from typing import Optional

from pydantic import Field

from .base import BaseRavelryModel


class SocialSiteModel(BaseRavelryModel):
    """Represents a Ravelry SocialSite object.

    [Social Site Ravelry API documentation](https://www.ravelry.com/api#SocialSite_result)
    """

    id: int
    name: str = Field(..., description="Name of the site")
    active: bool = Field(..., description="True if the site is currently shown on Ravelry profile pages")

    # favicon_url is marked as nullable in the spec
    favicon_url: Optional[str] = Field(None, description="URL to the site's favicon")


class SocialSitesModel(BaseRavelryModel):
    """Wrapper for the social_sites.json response."""

    social_sites: list[SocialSiteModel]
