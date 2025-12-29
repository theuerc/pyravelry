from .base import BaseRavelryModel


class CraftModel(BaseRavelryModel):
    """Represents a Ravelry Craft results object.

    [Craft Ravelry API documentation](https://www.ravelry.com/api#Craft_result)
    """

    id: int
    name: str
    permalink: str


class CraftsModel(BaseRavelryModel):
    """Wrapper for the crafts.json response.

    [Craft Ravelry API documentation](https://www.ravelry.com/api#Craft_result)
    """

    crafts: list[CraftModel]
