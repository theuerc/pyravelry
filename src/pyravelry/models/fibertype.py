from pydantic import Field

from .base import BaseRavelryModel


class FiberTypeModel(BaseRavelryModel):
    """Represents a Ravelry FiberType results object.

    [Fiber Type Ravelry API documentation](https://www.ravelry.com/api#FiberType_result)
    """

    id: int
    name: str
    animal_fiber: bool = Field(..., description="Whether the fiber is animal-based")
    synthetic: bool = Field(..., description="Whether the fiber is synthetic")
    vegetable_fiber: bool = Field(..., description="Whether the fiber is vegetable-based")


class FiberTypesModel(BaseRavelryModel):
    """Wrapper for the fiber_types.json response.

    [Fiber Type Ravelry API documentation](https://www.ravelry.com/api#FiberType_result)
    """

    fiber_types: list[FiberTypeModel]
