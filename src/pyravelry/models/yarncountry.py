"""Yarn country models"""

from typing import Optional

from pydantic import Field

from .base import BaseRavelryModel


class YarnCountryModel(BaseRavelryModel):
    """Represents a Ravelry YarnCountry object.

    Attributes based on the YarnCountry (basic) specification.

    [Yarn Country Ravelry API documentation](https://www.ravelry.com/api#YarnCountry_result)
    """

    id: int
    yarn_id: int = Field(..., description="Yarn identifier")
    country_id: int = Field(..., description="Country identifier")

    advertising_shops: int = Field(..., description="Number of shops that are advertising this yarn")
    shops_with_patrons: int = Field(..., description="Total unique shops where this yarn was purchased")
    shops_with_patrons_30days: int = Field(..., description="Shops with purchases in the last 30 days")
    shops_with_patrons_60days: int = Field(..., description="Shops with purchases in the last 60 days")
    shops_with_patrons_90days: int = Field(..., description="Shops with purchases in the last 90 days")


class YarnCountryFullModel(YarnCountryModel):
    """Represents the YarnCountry (full) object.

    Inherits all fields from YarnCountryModel and adds the country name.

    [Yarn Country Ravelry API documentation](https://www.ravelry.com/api#YarnCountry_result)
    """

    # The documentation didn't specify a type, but country_name is expected to be a string.
    country_name: Optional[str] = None
