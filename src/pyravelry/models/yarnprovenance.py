"""Yarn provenance models."""

from typing import Optional

from pydantic import Field

from .base import BaseRavelryModel


class YarnProvenanceModel(BaseRavelryModel):
    """Represents a Ravelry YarnProvenance object.

    This model tracks the origin and processing phases of a yarn.

    [Yarn Provenance Ravelry API documentation](https://www.ravelry.com/api#YarnProvenance_result)
    """

    id: int = Field(..., description="Unique identifier for the provenance record")
    yarn_id: int = Field(..., description="Identifier for the associated yarn")

    # Locations and Descriptions
    country_id: Optional[int] = Field(None, description="Internal ID for the country")
    country_name: Optional[str] = Field(None, description="Name of the country of origin")
    state_id: Optional[int] = Field(None, description="Internal ID for the state/region")
    description: Optional[str] = Field(None, description="Additional details about this provenance phase")

    # Phase Information
    phase_name: Optional[str] = Field(None, description="Name of the production phase (e.g., Dyed, Spun)")
    yarn_phase_id: Optional[int] = Field(None, description="Identifier for the specific yarn phase")


class YarnProvenancesModel(BaseRavelryModel):
    """Wrapper for responses containing multiple yarn provenance records.

    [Yarn Provenance Ravelry API documentation](https://www.ravelry.com/api#YarnProvenance_result)
    """

    yarn_provenances: list[YarnProvenanceModel]
