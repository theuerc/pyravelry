from typing import Any, Optional

from pydantic import Field

from .base import BaseRavelryModel


class BasePackModel(BaseRavelryModel):
    """Base fields shared across most Pack response types.

    [Pack Ravelry API documentation](https://www.ravelry.com/api#Pack_result)
    """

    id: int
    color_family_id: Optional[str] = Field(None, description="Color family ID")
    colorway: Optional[str] = None
    dye_lot: Optional[str] = Field(None, description="Dye lot, name or number")
    grams_per_skein: Optional[float] = None
    meters_per_skein: Optional[float] = None
    ounces_per_skein: Optional[float] = None
    personal_name: Optional[str] = Field(None, description="Personal name if not linked to DB yarn")
    prefer_metric_length: Optional[bool] = None
    prefer_metric_weight: Optional[bool] = None
    primary_pack_id: Optional[int] = None
    project_id: Optional[int] = Field(None, description="Project ID affiliated with pack")
    quantity_description: Optional[str] = None
    shop_id: Optional[int] = Field(None, description="Shop ID where purchased")
    shop_name: Optional[str] = None
    skeins: Optional[str] = Field(None, description="Number of skeins")
    stash_id: Optional[int] = Field(None, description="Stash ID affiliated with pack")
    thread_size: Optional[str] = None
    total_grams: Optional[float] = None
    total_meters: Optional[float] = None
    total_ounces: Optional[float] = None
    total_yards: Optional[float] = None
    yards_per_skein: Optional[float] = None
    yarn_id: Optional[int] = Field(None, description="Linked Ravelry yarn ID")


class PackStashModel(BasePackModel):
    """Represents the 'Pack (stash)' and 'Pack (stash_for_owner)' objects.

    [Pack Ravelry API documentation](https://www.ravelry.com/api#Pack_result)
    """

    color_attributes: Optional[Any] = None
    total_paid: Optional[float] = None
    total_paid_currency: Optional[str] = None


class PackFullModel(PackStashModel):
    """Represents the 'Pack (full)' and 'Pack (full_for_owner)' objects.

    [Pack Ravelry API documentation](https://www.ravelry.com/api#Pack_result)
    """

    yarn: Optional[Any] = Field(None, description="Full Yarn object details")
    yarn_name: Optional[str] = None
    yarn_weight: Optional[Any] = None


class PackPublicModel(BaseRavelryModel):
    """Represents the minimal 'Pack (public)' object.

    [Pack Ravelry API documentation](https://www.ravelry.com/api#Pack_result)
    """

    id: int
    yarn_id: Optional[int] = None


class PackPostModel(BaseRavelryModel):
    """Model for creating or updating a Pack (Pack POST).

    [Pack Ravelry API documentation](https://www.ravelry.com/api#Pack_result)
    """

    color_family_id: Optional[str] = None
    colorway: Optional[str] = None
    dye_lot: Optional[str] = None
    length_units: Optional[str] = Field(None, description="One of 'yards', 'meters'")
    personal_gauge_divisor: Optional[str] = None
    personal_max_gauge: Optional[int] = None
    personal_min_gauge: Optional[int] = None
    personal_name: Optional[str] = None
    personal_shop_name: Optional[str] = None
    personal_thread_size: Optional[Any] = None
    personal_yarn_weight_id: Optional[int] = None
    project_id: Optional[int] = None
    purchased_city: Optional[str] = None
    purchased_country_id: Optional[int] = None
    purchased_date: Optional[str] = Field(None, description="YYYY-MM-DD")
    purchased_state_id: Optional[int] = None
    purchased_url: Optional[str] = None
    shop_id: Optional[int] = None
    skein_length: Optional[str] = None
    skein_weight: Optional[str] = None
    skeins: Optional[str] = None
    stash_id: Optional[int] = None
    total_length: Optional[str] = None
    total_paid: Optional[str] = None
    total_paid_currency: Optional[str] = None
    total_weight: Optional[str] = None
    weight_units: Optional[str] = Field(None, description="One of 'grams', 'ounces'")
    yarn_id: Optional[int] = None
