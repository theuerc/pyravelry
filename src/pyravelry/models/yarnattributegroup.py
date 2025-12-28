"""Yarn Attribute Group model"""

from typing import Optional

from pydantic import Field

from .base import BaseRavelryModel


class YarnAttributeGroupModel(BaseRavelryModel):
    """
    Represents a YarnAttributeGroup.
    This model handles both the 'full' and 'list' versions by making
    the children field optional.

    https://www.ravelry.com/api#YarnAttributeGroup_result
    """

    id: int
    name: str = Field(..., description="Attribute group name")
    permalink: str

    # Self-referencing field for nested subgroups
    children: Optional[list["YarnAttributeGroupModel"]] = Field(
        default=None, description="Child yarn attribute groups (subgroups)"
    )


# This is required for Pydantic to resolve the recursive "YarnAttributeGroupModel" reference
YarnAttributeGroupModel.model_rebuild()


class YarnAttributeGroupsModel(BaseRavelryModel):
    """Wrapper for responses containing multiple yarn attribute groups.

    https://www.ravelry.com/api#YarnAttributeGroup_result
    """

    yarn_attribute_groups: list[YarnAttributeGroupModel]
