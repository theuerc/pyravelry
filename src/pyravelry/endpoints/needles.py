from typing import Literal, Optional, cast

from pydantic import validate_call

from pyravelry.endpoints.base import Action, BaseEndpoint, TypedNamespace
from pyravelry.models import (
    NeedleRecordListModel,
    NeedleSizesModel,
    NeedleTypesModel,
)


class NeedlesResource(BaseEndpoint):
    """Needles endpoint for Ravelry.

    Handles user needle inventories, global needle sizes, and needle types.
    """

    actions = TypedNamespace(
        list=Action("/people/{}/needles/list.json", NeedleRecordListModel),
        sizes=Action("/needles/sizes.json", NeedleSizesModel),
        types=Action("/needles/types.json", NeedleTypesModel),
    )

    @validate_call
    def list(self, username: str) -> NeedleRecordListModel:
        """
        Get needle records for a specific user.

        Args:
            username (str): Username or integer ID of the user to retrieve needles for.

        Returns:
            NeedleRecordsListModel: The user's list of needle records.
        """
        response_dict = self._fetch(self._http.get(self.actions.list.url.format(username)))

        return cast(NeedleRecordListModel, self.actions.list.model.model_validate(response_dict))

    @validate_call
    def sizes(self, craft: Optional[Literal["crochet", "knitting"]] = None) -> NeedleSizesModel:
        """
        Get available sizes for each needle type.

        Args:
            craft (str | None): Filter by tool type. "crochet" for hooks only,
                                "knitting" for knitting needles only. Defaults to None.

        Returns:
            NeedleSizesListModel: The list of available needle sizes.
        """
        params = {"craft": craft} if craft else {}

        response_dict = self._fetch(self._http.get(self.actions.sizes.url, params=params))

        return cast(NeedleSizesModel, self.actions.sizes.model.model_validate(response_dict))

    @validate_call
    def types(self) -> NeedleTypesModel:
        """
        Get all global needle types.

        Returns:
            NeedleTypesModel: The list of available needle types.
        """
        response_dict = self._fetch(self._http.get(self.actions.types.url))

        return cast(NeedleTypesModel, self.actions.types.model.model_validate(response_dict))
