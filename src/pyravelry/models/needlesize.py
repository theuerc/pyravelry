from typing import Optional

from pydantic import Field

from .base import BaseRavelryModel


class NeedleSizePostModel(BaseRavelryModel):
    """Wrapper for the NeedleSize (POST) payload.

    [Needle Size Ravelry API documentation](https://www.ravelry.com/api#NeedleSize_result)
    """

    metric: float = Field(..., description="Metric designation for hook size.")


class NeedleSizeListModel(NeedleSizePostModel):
    """Wrapper for the NeedleSize (list) response.

    [Needle Size Ravelry API documentation](https://www.ravelry.com/api#NeedleSize_result)
    """

    id: int = Field(..., description="Needle size ID.")
    hook: Optional[str] = Field(
        None,
        description="Crochet hook designation corresponding to this metric size, if one exists.",
    )
    us: Optional[str] = Field(
        None,
        description="US size number corresponding to this metric size, if one exists.",
    )


class NeedleSizeFullModel(NeedleSizeListModel):
    """Wrapper for the NeedleSize (full) response.

    [Needle Size Ravelry API documentation](https://www.ravelry.com/api#NeedleSize_result)
    """

    # The documentation provides the exact same fields as the list view,
    # but inherits from NeedleSizeListModel to maintain structural separation.
    pass


class NeedleSizesModel(BaseRavelryModel):
    """Wrapper for the needle size responses.

    [Needle Size Ravelry API documentation](https://www.ravelry.com/api#NeedleSize_result)
    """

    needle_sizes: list[NeedleSizeFullModel]
