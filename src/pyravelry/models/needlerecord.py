from typing import Optional

from pydantic import Field

from .base import BaseRavelryModel
from .needletype import NeedleTypeFullModel


class NeedleRecordSmallModel(BaseRavelryModel):
    """Wrapper for the NeedleRecord (small) response.

    [Needle Record Ravelry API documentation](https://www.ravelry.com/api#NeedleRecord_result)
    """

    id: int = Field(..., description="The unique identifier for the needle record.")
    comment: Optional[str] = Field(None, description="User comments about the needle.")
    needle_type_id: int = Field(..., description="The ID referencing the type of needle.")


class NeedleRecordFullModel(NeedleRecordSmallModel):
    """Wrapper for the NeedleRecord (full) response.
    Extends the small model to include full needle type details.

    [Needle Record Ravelry API documentation](https://www.ravelry.com/api#NeedleRecord_result)
    """

    needle_type: NeedleTypeFullModel = Field(..., description="Detailed information about the needle type.")


class NeedleRecordListModel(BaseRavelryModel):
    """Wrapper for the needle record responses.

    [Needle Record Ravelry API documentation](https://www.ravelry.com/api#NeedleRecord_result)
    """

    needle_records: list[NeedleRecordFullModel]
