from pyravelry.models.base import BaseRavelryModel


class PaginatorModel(BaseRavelryModel):
    """Standard Ravelry pagination object.

    [Slightly Below Pagination Ravelry API documentation](https://www.ravelry.com/api#/_color_families)
    """

    page_count: int
    page: int
    page_size: int
    results: int
    last_page: int
