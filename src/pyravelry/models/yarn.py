from typing import Any, Optional

from pydantic import Field

from .base import BaseRavelryModel

# Assuming these are implemented in separate files as requested
from .photo import PhotoModel
from .yarnattributegroup import YarnAttributeGroupModel
from .yarncompany import YarnCompanyModel
from .yarnfiber import YarnFiberFullModel
from .yarnprovenance import YarnProvenanceModel
from .yarnweight import YarnWeightModel


class YarnBaseModel(BaseRavelryModel):
    """Base fields shared across all Yarn result types.

    [Yarn Ravelry API documentation](https://www.ravelry.com/api#Yarn_result)
    """

    id: int
    name: str
    permalink: str
    certified_organic: Optional[bool] = None
    discontinued: Optional[bool] = None
    gauge_divisor: Optional[int] = None
    grams: Optional[int] = Field(None, description="weight of a skein/ball of the yarn in grams")
    machine_washable: Optional[bool] = None
    max_gauge: Optional[int] = None
    min_gauge: Optional[int] = None
    rating_average: Optional[float] = None
    rating_count: Optional[int] = None
    rating_total: Optional[int] = None
    texture: Optional[str] = Field(None, description="Obsolete, superseded by yarn attributes")
    thread_size: Optional[Any] = None
    wpi: Optional[int] = Field(None, description="wraps per inch")
    yardage: Optional[int] = None
    yarn_company_name: Optional[str] = None
    organic: Optional[Any] = None


class YarnModel(YarnBaseModel):
    """Represents a Ravelry Yarn result object.

    [Yarn Ravelry API documentation](https://www.ravelry.com/api#Yarn_result)
    """

    first_photo: Optional[PhotoModel] = None
    yarn_weight: Optional[YarnWeightModel] = None


class YarnlistModel(YarnModel):
    """Represents a Ravelry Yarn (list) result object.

    Includes personal_attributes found in search results.

    [Yarn Ravelry API documentation](https://www.ravelry.com/api#Yarn_result)
    """

    personal_attributes: Optional[dict] = Field(None, description="Hash containing favorited, bookmark_id, stash_ids")


class YarnStashlistModel(YarnBaseModel):
    """Represents a Ravelry Yarn (stash_list) result object."""

    yarn_company: Optional[YarnCompanyModel] = None
    yarn_weight: Optional[YarnWeightModel] = None


class YarnFullModel(YarnBaseModel):
    """Represents a Ravelry Yarn (full) result object.

    [Yarn Ravelry API documentation](https://www.ravelry.com/api#Yarn_result)
    """

    max_hook_size: Optional[Any] = None
    max_needle_size: Optional[Any] = None
    min_hook_size: Optional[Any] = None
    min_needle_size: Optional[Any] = None
    notes_html: Optional[str] = None
    personal_attributes: Optional[dict] = None
    photos: list[PhotoModel] = Field(default_factory=list)
    yarn_attributes: list[YarnAttributeGroupModel] = Field(
        default_factory=list, description='Examples: "Superwash", "Gradient"'
    )
    yarn_company: Optional[YarnCompanyModel] = None
    yarn_fibers: list[YarnFiberFullModel] = Field(default_factory=list)
    yarn_provenance: list[YarnProvenanceModel] = Field(default_factory=list, description="Location and processing info")
    yarn_weight: Optional[YarnWeightModel] = None
