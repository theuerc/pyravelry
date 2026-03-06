from pydantic import BaseModel, ConfigDict


class BaseRavelryModel(BaseModel):
    """Base Ravelry Results object class"""

    model_config = ConfigDict(
        validate_by_name=True,
        validate_by_alias=True,
        extra="allow",
    )
