from typing import Optional

from pydantic import Field

from .base import BaseRavelryModel


class NeedleTypeModel(BaseRavelryModel):
    """Wrapper for the NeedleType response.

    [Needle Type Ravelry API documentation](https://www.ravelry.com/api#NeedleType_result)
    """

    id: int = Field(..., description="The unique identifier for the needle type.")
    name: Optional[str] = Field(..., description="The name of the needle type.")
    description: Optional[str] = Field(None, description="Detailed description of the needle type.")
    length: Optional[int] = Field(None, description="The length of the needle (if applicable).")
    metric_name: str = Field(..., description="The metric name designation for the needle size.")
    needle_size_id: int = Field(..., description="The ID referencing the specific needle size.")
    type_name: str = Field(..., description="The specific classification name of the needle type.")


class NeedleTypeFullModel(NeedleTypeModel):
    """Wrapper for the NeedleType (full) response.

    The documentation provides the exact same fields as the standard view,
    but inherits from NeedleTypeModel to maintain structural consistency.

    [Needle Type Ravelry API documentation](https://www.ravelry.com/api#NeedleType_result)
    """

    pass


class NeedleTypesModel(BaseRavelryModel):
    """Wrapper for the needle type responses.

    [Needle Type Ravelry API documentation](https://www.ravelry.com/api#NeedleType_result)
    """

    needle_types: list[NeedleTypeFullModel]
