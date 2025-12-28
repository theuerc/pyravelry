"""Search parameter models

https://www.ravelry.com/api#/_search
"""

from typing import Literal, Optional

from pydantic import BaseModel, Field, field_validator


class SearchParams(BaseModel):
    """Parameters for the /search.json endpoint."""

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
