from typing import Optional

from pyravelry.models.base import BaseRavelryModel
from pyravelry.models.yarncompany import YarnCompanyModel

from .paginator import PaginatorModel


class YarnCompanySearchParams(BaseRavelryModel):
    """Parameters for the yarn_companies/search endpoint.

    [Yarn Companies Ravelry API documentation](https://www.ravelry.com/api#yarn_companies_search)
    """

    query: Optional[str] = None
    page: int = 1
    page_size: int = 48
    sort: Optional[str] = "best"


class YarnCompanySearchResponseModel(BaseRavelryModel):
    """Response returned by /yarn_companies/search.json.

    [Yarn Companies Ravelry API documentation](https://www.ravelry.com/api#yarn_companies_search)
    """

    yarn_companies: list[YarnCompanyModel]
    paginator: PaginatorModel
