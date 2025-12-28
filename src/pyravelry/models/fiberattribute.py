"""Model for FiberAttribute type."""

from .base import BaseRavelryModel


class FiberAttributeModel(BaseRavelryModel):
    """Represents a Ravelry FiberAttribute result object.

    https://www.ravelry.com/api#FiberAttribute_result
    """

    fiber_attribute_group_id: int
    id: int
    name: str  # Short category name
    permalink: str


class FiberAttributesModel(BaseRavelryModel):
    """Wrapper for the fiber_attributes.json response.

    https://www.ravelry.com/api#FiberAttribute_result
    """

    fiber_attributes: list[FiberAttributeModel]
