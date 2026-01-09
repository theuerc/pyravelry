from typing import Any, Union

from pydantic import field_validator

from pyravelry.models.base import BaseRavelryModel


class Identifier(BaseRavelryModel):
    """
    Validates that the input is either a string (username)
    or an integer (user ID).

    [Identifier Documentation (URI Parameters)](https://www.ravelry.com/api#people_show)
    """

    id: Union[str, int]

    @field_validator("id")
    @classmethod
    def validate_id(cls, v: Any) -> Any:
        if isinstance(v, str) and not v.strip():
            err = "Username cannot be an empty string"
            raise TypeError(err)
        return v
