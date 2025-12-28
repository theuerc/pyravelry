"""Search results models

https://www.ravelry.com/api#/_search
"""

from typing import Optional

from pydantic import Field

from pyravelry.models.base import BaseRavelryModel


class SearchRecordModel(BaseRavelryModel):
    """Details about the specific record found in the search."""

    type: str
    id: int
    permalink: str
    uri: Optional[str] = None


class SearchResultModel(BaseRavelryModel):
    """Represents an individual result from the global search."""

    title: str
    type_name: str = Field(..., alias="type_name")
    caption: Optional[str] = None
    tiny_image_url: Optional[str] = None
    image_url: Optional[str] = None
    record: SearchRecordModel


class GlobalSearchResponseModel(BaseRavelryModel):
    """Wrapper for the search.json response."""

    results: list[SearchResultModel]
