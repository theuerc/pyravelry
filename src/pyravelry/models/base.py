import pandas as pd
import polars as pl
from pydantic import BaseModel, ConfigDict


class BaseRavelryModel(BaseModel):
    """Base Ravelry Results object class"""

    model_config = ConfigDict(
        validate_by_name=True,
        validate_by_alias=True,
        extra="allow",
    )

    @property
    def pandas(self) -> pd.DataFrame:
        """Converts the pyravelry model into a pandas dataframe.

        Returns:
            pd.DataFrame: pandas Dataframe with pyravelry content.
        """
        import pyarrow  # noqa: F401

        data = self.model_dump()
        if len(data.keys()) == 1:
            data = next(data.values().__iter__())
        return pd.json_normalize(data)

    @property
    def polars(self) -> pl.DataFrame:
        """Converts the pyravelry model into a polars dataframe.

        This is very hacky and converts to pandas then polars,
        but the data is sufficiently small to where this doesn't
        matter much.

        Returns:
            pl.DataFrame: polars Dataframe with pyravelry content.
        """
        return pl.from_pandas(self.pandas)
