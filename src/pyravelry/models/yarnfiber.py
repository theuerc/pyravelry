"""Model for YarnFiber types."""

from typing import Optional

from pydantic import Field

from .base import BaseRavelryModel
from .fibercategory import FiberCategoryModel
from .fibertype import FiberTypeModel


class YarnFiberFullModel(BaseRavelryModel):
    """Represents a YarnFiber (full) object.

    https://www.ravelry.com/api#YarnFiber_result
    """

    id: int
    percentage: Optional[int] = Field(None, description="Percentage of this fiber in the yarn")
    fiber_category: FiberCategoryModel
    fiber_type: FiberTypeModel


class YarnFiberPublicModel(BaseRavelryModel):
    """Represents a YarnFiber (public) object.

    https://www.ravelry.com/api#YarnFiber_result
    """

    id: int
    percentage: Optional[int] = Field(None, description="Percentage of this fiber in the yarn")
    fiber_category_id: int
    fiber_type_id: int
