from typing import Literal, Optional

from pydantic import BaseModel, Field, field_validator

from pyravelry.models.base import BaseRavelryModel


class SearchParams(BaseModel):
    """Parameters for the /search.json endpoint.

    [Search Ravelry API documentation](https://www.ravelry.com/api#/_search)
    """

    query: str = Field(...)
    limit: int = Field(50, ge=1, le=500)

    # Using Literal ensures only valid Ravelry types are passed
    types: Optional[
        list[
            Literal[
                "User",
                "PatternAuthor",
                "PatternSource",
                "Pattern",
                "YarnCompany",
                "Yarn",
                "Group",
                "Event",
                "Project",
                "Page",
                "Topic",
                "Shop",
            ]
        ]
    ] = None

    @field_validator("types", mode="before")
    @classmethod
    def format_types(cls, v: str) -> list[str]:
        """Formats the passed in string to be a list.

        Args:
            v (str): space delineated string

        Returns:
            _type_: _description_
        """
        # Allow users to pass a single string instead of a list for convenience
        if isinstance(v, str):
            return v.strip().split(" ")
        return v


class SearchRecordModel(BaseRavelryModel):
    """Details about the specific record found in the search.

    [Search Ravelry API documentation](https://www.ravelry.com/api#/_search)
    """

    type: str
    id: int
    permalink: str
    uri: Optional[str] = None


class SearchResultModel(BaseRavelryModel):
    """Represents an individual result from the global search.

    [Search Ravelry API documentation](https://www.ravelry.com/api#/_search)
    """

    title: str
    type_name: str = Field(..., alias="type_name")
    caption: Optional[str] = None
    tiny_image_url: Optional[str] = None
    image_url: Optional[str] = None
    record: SearchRecordModel


class GlobalSearchResponseModel(BaseRavelryModel):
    """Wrapper for the search.json response.

    [Search Ravelry API documentation](https://www.ravelry.com/api#/_search)
    """

    results: list[SearchResultModel]
