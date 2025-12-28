from typing import Any

import pytest

from pyravelry.client import RavelryClient


class TestRavelryClient:
    @pytest.fixture(autouse=True)
    def setup(self, api_info: Any) -> None:
        """Automatically sets up the resource for every test in this class."""
        self.settings = api_info["settings"]
        self.client = RavelryClient(self.settings)

    def test_initialization(self) -> None:
        assert self.client is not None

    @pytest.mark.parametrize(
        "attribute",
        [
            "color_families",
            "fiber_categories",
            "yarn_weights",
            "search",
            "fiber_attributes",
            "yarn_companies",
        ],
    )
    def test_attributes__with_context_manager(self, attribute: str) -> None:
        with RavelryClient(self.settings) as client:
            assert hasattr(client, attribute), f"Client is missing the '{attribute}' attribute"
