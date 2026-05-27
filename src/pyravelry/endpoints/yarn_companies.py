from types import SimpleNamespace
from typing import Optional, cast

from pydantic import validate_call

from pyravelry.endpoints.base import Action, BaseEndpoint
from pyravelry.models import YarnCompanySearchParams, YarnCompanySearchResponseModel


class YarnCompaniesResource(BaseEndpoint):
    """
    Endpoint for yarn company specific operations.

    [Yarn Companies Ravelry API documentation](https://www.ravelry.com/api#yarn_companies_search)
    """

    actions = SimpleNamespace(query=Action("/yarn_companies/search.json", YarnCompanySearchResponseModel))

    @validate_call
    def query(
        self,
        query: Optional[str] = None,
        page: int = 1,
        page_size: int = 48,
        sort: str = "best",
    ) -> YarnCompanySearchResponseModel:
        """
        Search the yarn company directory.

        Args:
            query: Search term for fulltext searching.
            page: Result page to retrieve.
            page_size: Number of results per page.
            sort: Sort order (e.g., 'best', 'best_'; reverse order with _ suffix)
        """
        params = YarnCompanySearchParams(query=query, page=page, page_size=page_size, sort=sort)

        response_dict = self._fetch(self._http.get(self.actions.query.url, params=params.model_dump(exclude_none=True)))

        return cast(YarnCompanySearchResponseModel, self.actions.query.model.model_validate(response_dict))
