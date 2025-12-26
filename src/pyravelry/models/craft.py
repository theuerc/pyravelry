"""Model for Craft type.

https://www.ravelry.com/api#Craft_result
"""

from .base import BaseRavelryModel


class CraftModel(BaseRavelryModel):
    """Represents a Ravelry Craft results object.

    Defined at:
        https://www.ravelry.com/api#Craft_result
    """

    id: int
    name: str
    permalink: str


class CraftsModel(BaseRavelryModel):
    """Wrapper for the crafts.json response."""

    crafts: list[CraftModel]
