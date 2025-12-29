"""Yarn company models."""

from typing import Optional

from pydantic import Field

from .base import BaseRavelryModel


class YarnCompanyPublicModel(BaseRavelryModel):
    """Represents the 'Public' version of a YarnCompany."""

    id: int
    name: str
    permalink: str
    url: Optional[str] = None


class YarnCompanyModel(YarnCompanyPublicModel):
    """
    Represents the standard, Full, and List versions of a YarnCompany.
    These share the same fields in the current documentation.

    [Yarn Company Ravelry API documentation](https://www.ravelry.com/api#YarnCompany_result)
    """

    logo_url: Optional[str] = Field(None, description="URL to the company logo")
    yarns_count: int = Field(0, description="Total number of yarns by this company")


class YarnCompanyShopModel(BaseRavelryModel):
    """Represents the 'Shop' version of a YarnCompany.

    [Yarn Company Ravelry API documentation](https://www.ravelry.com/api#YarnCompany_result)
    """

    id: int
    name: str
    permalink: str
    advertised: bool = False
    most_recent_purchase: Optional[str] = None
    # Assuming 'purchases' is an integer or a list;
    # Ravelry docs usually imply a count or a list of objects here.
    purchases: Optional[int] = 0


class YarnCompaniesModel(BaseRavelryModel):
    """Wrapper for responses returning multiple yarn companies.

    https://www.ravelry.com/api#YarnCompany_result
    """

    yarn_companies: list[YarnCompanyModel]
