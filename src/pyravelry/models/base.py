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

    def to_pandas(self) -> pd.DataFrame:
        """Converts the pyravelry model into a pandas dataframe.

        Returns:
            pd.DataFrame: pandas Dataframe with pyravelry content.
        """
        import pyarrow  # noqa: F401

        data = self.model_dump()
        if len(data.keys()) == 1:
            data = next(data.values().__iter__())
        return pd.json_normalize(data)

    def to_polars(self) -> pl.DataFrame:
        """Converts the pyravelry model into a polars dataframe.

        This is very hacky and converts to pandas then polars,
        but the data is sufficiently small to where this doesn't
        matter much.

        Returns:
            pl.DataFrame: polars Dataframe with pyravelry content.
        """
        return pl.from_pandas(self.to_pandas())


class BaseParentRavelryModel(BaseRavelryModel):
    """Base Ravelry Results object class"""

    def to_pandas(self) -> None:  # type: ignore[override]
        """Throws error for models that can't use `to_pandas()`"""
        raise NotImplementedError(
            "to_pandas() is not implemented for this model because "
            "this endpoint returns a composite structure. Please call .to_pandas() "
            "directly on the submodels (e.g., self.[submodel].to_pandas()) instead."
        )

    def to_polars(self) -> None:  # type: ignore[override]
        """Throws error for models that can't use `to_pandas()`"""
        raise NotImplementedError(
            "to_polars() is not implemented for this model because "
            "this endpoint returns a composite structure. Please call .to_pandas() "
            "directly on the submodels (e.g., self.[submodel].to_polars()) instead."
        )
