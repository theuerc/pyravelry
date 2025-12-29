from typing import Optional

from pydantic import Field

from .base import BaseRavelryModel


class FiberCategoryModel(BaseRavelryModel):
    """Represents a Ravelry FiberCategory results object.

    [Fiber Category Ravelry API documentation](https://www.ravelry.com/api#FiberCategory_result)
    """

    id: int
    name: str = Field(..., description="Short category name")
    permalink: str

    # Optional fields based on the different views of FiberCategory
    short_name: Optional[str] = Field(None, description="Abbreviated category name")

    # parent is listed in attributes but type is often an ID or a nested object
    parent_id: Optional[int] = Field(None, alias="parent", description="Parent category ID")

    # Self-referential list for subcategories
    children: Optional[list["FiberCategoryModel"]] = Field(
        default_factory=list, description="Child categories (subcategories)"
    )


# Required for Pydantic to resolve the recursive "FiberCategoryModel" reference
FiberCategoryModel.model_rebuild()


class FiberCategoriesModel(BaseRavelryModel):
    """Wrapper for the fiber_categories.json response.

    [Fiber Category Ravelry API documentation](https://www.ravelry.com/api#FiberCategory_result)
    """

    fiber_categories: list[FiberCategoryModel]
