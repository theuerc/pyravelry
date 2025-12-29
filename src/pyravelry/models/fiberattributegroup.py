from typing import Optional

from pydantic import Field

from .base import BaseRavelryModel


class FiberAttributeGroupModel(BaseRavelryModel):
    """Represents a Ravelry FiberAttributeGroup object.

    [Fiber Attribute Group Ravelry API documentation](https://www.ravelry.com/api#FiberAttributeGroup_result)
    """

    id: int
    name: str = Field(..., description="Short category name")
    permalink: str

    # Using Optional because parent_id is often null for top-level groups
    parent_id: Optional[int] = Field(None, description="ID of the parent group, if applicable")


class FiberAttributeGroupsModel(BaseRavelryModel):
    """Wrapper for the fiber_attribute_groups.json response.

    [Fiber Attribute Group Ravelry API documentation](https://www.ravelry.com/api#FiberAttributeGroup_result)
    """

    fiber_attribute_groups: list[FiberAttributeGroupModel]
