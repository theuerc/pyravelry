"""Model for Craft type."""

from .base import BaseRavelryModel


class CraftModel(BaseRavelryModel):
    """Represents a Ravelry Craft results object.

    https://www.ravelry.com/api#Craft_result
    """

    id: int
    name: str
    permalink: str


class CraftsModel(BaseRavelryModel):
    """Wrapper for the crafts.json response.

    https://www.ravelry.com/api#Craft_result
    """

    crafts: list[CraftModel]
