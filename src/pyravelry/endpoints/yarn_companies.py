from typing import Optional

from pyravelry.endpoints.base import BaseEndpoint
from pyravelry.models import YarnCompanySearchParams, YarnCompanySearchResponseModel


class YarnCompaniesResource(BaseEndpoint):
    """
    Endpoint for yarn company specific operations.

    [Yarn Companies Ravelry API documentation](https://www.ravelry.com/api#yarn_companies_search)
    """

    endpoint = "/yarn_companies"
    input_model = YarnCompanySearchParams
    output_model = YarnCompanySearchResponseModel

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
        cls = YarnCompaniesResource

        url = "/".join([cls.endpoint, "/search.json"])

        params = cls.input_model(query=query, page=page, page_size=page_size, sort=sort)

        response_dict = self._fetch(
            http_client=self._http,
            endpoint=url,
            params=params.model_dump(exclude_none=True),
        )

        return cls.output_model.model_validate(response_dict)
