from typing import Literal, Optional, cast

from pydantic import validate_call

from pyravelry.endpoints.base import Action, BaseEndpoint, TypedNamespace
from pyravelry.models import YarnResponseComments, YarnResponseSearch, YarnResponseShow, YarnResponseYarns


class YarnsResource(BaseEndpoint):
    """Yarns endpoint for Ravelry.

    Handles yarn searches, yarn details, batch fetches, and comments.

    [Yarn Ravelry API documentation](https://www.ravelry.com/api#yarns_comments)
    """

    actions = TypedNamespace(
        comments=Action("/yarns/{}/comments.json", YarnResponseComments),
        search=Action("/yarns/search.json", YarnResponseSearch),
        show=Action("/yarns/{}.json", YarnResponseShow),
        yarns=Action("/yarns.json", YarnResponseYarns),
    )

    @validate_call
    def comments(
        self,
        id_: int,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        sort: Optional[Literal["time", "helpful", "time_", "helpful_"]] = None,
        include: Optional[str] = None,
    ) -> YarnResponseComments:
        """
        Retrieve a yarn's comments.

        Args:
            id_ (int): Yarn ID to retrieve comments for.
            page (int | None): Result page to retrieve. Defaults to first page.
            page_size (int | None): Defaults to 25 comments per page. Maximum is 100.
            sort (str | None): Sort order options: time, helpful, time_, helpful_.
            include (str | None): Space-delimited extra results. e.g. "highlighted_project".

        Returns:
            YarnResponseComments: Comments associated with this type of yarn.
        """

        params = {
            "page": page,
            "page_size": page_size,
            "sort": sort,
            "include": include,
        }
        params = {k: v for k, v in params.items() if v is not None}

        response_dict = self._fetch(self._http.get(self.actions.comments.url.format(id_), params=params))
        transformed_dict = self._validate(response_dict, self.actions.comments)
        return cast(YarnResponseComments, self.actions.comments.model.model_validate(transformed_dict))

    @validate_call
    def search(
        self,
        query: str,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        sort: Optional[Literal["best", "rating", "projects"]] = None,
        personal_attributes: Optional[bool] = None,
    ) -> YarnResponseSearch:
        """
        Search yarn database.

        Args:
            query (str): Search term for fulltext searching yarns.
            page (int | None): Result page to retrieve. Defaults to first page.
            page_size (int | None): Defaults to 50 results per page.
            sort (str | None): Sort order options: best, rating, projects.
            personal_attributes (bool | None): Set to True (returns 1) to fetch personal data hashes.

        Returns:
            YarnResponseSearch: search results with pagination information.
        """
        params = {
            "query": query,
            "page": page,
            "page_size": page_size,
            "sort": sort,
            "personal_attributes": 1 if personal_attributes else 0,
        }
        params = {k: v for k, v in params.items() if v is not None}

        response_dict = self._fetch(self._http.get(self.actions.search.url, params=params))
        transformed_dict = self._validate(response_dict, self.actions.search)
        return cast(YarnResponseSearch, self.actions.search.model.model_validate(transformed_dict))

    @validate_call
    def show(self, id_: int, include: Optional[str] = None) -> YarnResponseShow:
        """
        Get yarn details.

        Args:
            id_ (int): Yarn ID to retrieve.
            include (str | None): Space-delimited extra results. Accepted: "colorways", "availability".

        Returns:
            YarnResponseShow: pydantic model of yarn ids and data
        """
        params = {"include": include} if include else {}

        response_dict = self._fetch(self._http.get(self.actions.show.url.format(id_), params=params))

        transformed_dict = self._validate(response_dict, self.actions.show)
        return cast(YarnResponseShow, self.actions.show.model.model_validate(transformed_dict))

    @validate_call
    def yarns(self, ids: list[int]) -> YarnResponseYarns:
        """
        Get yarn details for multiple yarns.

        Args:
            ids (list[int]): List of yarn IDs to retrieve.

        Returns:
            dict[int, YarnFullModel]: Map of YarnFullModel results, indexed by yarn ID.
        """
        # Formulate space-delimited string as required (e.g., 600+601 handling via HTTP layers or raw string join)
        space_delimited_ids = " ".join(map(str, ids))
        params = {"ids": space_delimited_ids}

        response_dict = self._fetch(self._http.get(self.actions.yarns.url, params=params))

        return cast(YarnResponseYarns, self.actions.yarns.model.model_validate(response_dict))
