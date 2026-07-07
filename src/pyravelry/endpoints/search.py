from typing import Literal, Optional, cast

from pydantic import validate_call

from pyravelry.endpoints.base import Action, BaseEndpoint, TypedNamespace
from pyravelry.models import GlobalSearchResponseModel, SearchParams


class SearchResource(BaseEndpoint):
    """Search endpoint for Ravelry.

    [Search Ravelry API documentation](https://www.ravelry.com/api#/_search)
    """

    actions = TypedNamespace(
        query=Action("/search.json", GlobalSearchResponseModel),
    )

    @validate_call
    def query(
        self,
        query: str,
        limit: int = 10,
        types: Optional[
            list[
                Literal[
                    "User",
                    "PatternAuthor",
                    "PatternSource",
                    "Pattern",
                    "YarnCompany",
                    "Yarn",
                    "Group",
                    "Event",
                    "Project",
                    "Page",
                    "Topic",
                    "Shop",
                ]
            ]
            | None
        ] = None,
    ) -> GlobalSearchResponseModel:
        """
        Perform a global search.

        Args:
            query (str): Any fulltext string
            limit (int): integer between 1 and 50
            types (str|list): Optional. space delineated string or list of strings
                for the types of categories that you are searching.
                See client.search.param_model.model_json_schema()
                for available types.

        Usage:
            search.query(query="merino", limit=10, types=["Yarn"])
        """
        params_obj = SearchParams(query=query, limit=limit, types=types)

        # Flatten the 'types' list into a space-delimited string
        params_dict = params_obj.model_dump(exclude_none=True)

        if "types" in params_dict:
            params_dict["types"] = " ".join(params_dict["types"])

        response_dict = self._fetch(self._http.get(self.actions.query.url, params=params_dict))

        return cast(GlobalSearchResponseModel, self.actions.query.model.model_validate(response_dict))
