from datetime import datetime
from typing import Optional

from pydantic import Field

from .base import BaseRavelryModel


class ToolModel(BaseRavelryModel):
    """Represents a Ravelry Tool object.

    [Tool Ravelry API documentation](https://www.ravelry.com/api/#Tool_result)
    """

    id: int
    name: Optional[str] = Field(None, description="The name of the tool")
    make: Optional[str] = Field(None, description="The manufacturer/brand of the tool")
    model: Optional[str] = Field(None, description="The specific model of the tool")
    notes: Optional[str] = Field(None, description="User notes regarding the tool")
    created_at: datetime
    updated_at: datetime


class ToolsModel(BaseRavelryModel):
    """Wrapper for the tools.json response.

    [Tool Ravelry API documentation](https://www.ravelry.com/api/#Tool_result)
    """

    tools: list[ToolModel]
