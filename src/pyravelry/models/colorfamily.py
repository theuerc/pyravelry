"""Model for Colorfamily type."""

from typing import Optional

from pydantic import Field

from .base import BaseRavelryModel


class ColorFamilyModel(BaseRavelryModel):
    """Represents a Ravelry ColorFamily results object.

    https://www.ravelry.com/api#ColorFamily_result
    """

    id: int
    name: str
    permalink: str

    # Using Optional because the docs say "Nullable: Yes"
    color: Optional[str] = Field(None, description="HTML color code (e.g., #FFFFFF)")

    spectrum_order: int = Field(..., description="Sort order, (mostly) based on the spectrum")


class ColorFamiliesModel(BaseRavelryModel):
    """Wrapper for the color_families.json response.

    https://www.ravelry.com/api#ColorFamily_result
    """

    color_families: list[ColorFamilyModel]
