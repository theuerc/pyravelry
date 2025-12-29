"""Model for YarnWeight type."""

from typing import Optional

from pydantic import Field

from .base import BaseRavelryModel


class YarnWeightModel(BaseRavelryModel):
    """Represents a Ravelry YarnWeight results object.

    [Yarn Weight Ravelry API documentation](https://www.ravelry.com/api#YarnWeight_result)
    """

    id: int
    name: str

    # These are typically strings or floats representing gauges/thickness
    crochet_gauge: Optional[str] = Field(None, description="Typical crochet gauge")
    knit_gauge: Optional[str] = Field(None, description="Typical knitting gauge")

    max_gauge: Optional[float] = Field(None, description="Maximum recommended gauge")
    min_gauge: Optional[float] = Field(None, description="Minimum recommended gauge")

    ply: Optional[str] = Field(None, description="Number of plies associated with this weight")
    wpi: Optional[str] = Field(None, description="Wraps per inch")


class YarnWeightsModel(BaseRavelryModel):
    """Wrapper for the yarn_weights.json response.

    [Yarn Weight Ravelry API documentation](https://www.ravelry.com/api#YarnWeight_result)
    """

    yarn_weights: list[YarnWeightModel]
