from typing import Literal, Optional

from pyravelry.endpoints.base import BaseEndpoint
from pyravelry.models import GlobalSearchResponseModel, SearchParams, SearchResultModel


class SearchResource(BaseEndpoint):
    """Search endpoint for Ravelry.

    [Search Ravelry API documentation](https://www.ravelry.com/api#/_search)
    """

    endpoint: str = "/search.json"
    input_model = SearchParams
    output_model = GlobalSearchResponseModel

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
    ) -> list[SearchResultModel]:
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
        cls = SearchResource
        params_obj = cls.input_model(query=query, limit=limit, types=types)

        # Flatten the 'types' list into a space-delimited string
        params_dict = params_obj.model_dump(exclude_none=True)
        if "types" in params_dict:
            params_dict["types"] = " ".join(params_dict["types"])

        response_dict = self._fetch(
            http_client=self._http,
            endpoint=cls.endpoint,
            params=params_dict,
        )

        data = cls.output_model.model_validate(response_dict)
        return data.results
