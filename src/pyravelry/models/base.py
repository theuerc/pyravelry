from pydantic import BaseModel, ConfigDict
import pandas as pd
import polars as pl


class BaseRavelryModel(BaseModel):
    """Base Ravelry Results object class"""

    model_config = ConfigDict(
        validate_by_name=True,
        validate_by_alias=True,
        extra="allow",
    )

    def to_pandas(self) -> pd.DataFrame:
        """Convert the model to a pandas DataFrame.

        Returns:
            pd.DataFrame: Pydantic model converted to DataFrame.
        """
        return pd.DataFrame([self.model_dump()])

    def to_polars(self) -> pd.DataFrame:
        """Convert the model to a polars DataFrame.

        Returns:
            pl.DataFrame: Pydantic model converted to DataFrame.
        """
        return pl.DataFrame([self.model_dump()])
