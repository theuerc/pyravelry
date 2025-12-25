from typing import Any
import pytest
from pyravelry.endpoints import ColorFamiliesResource


class TestColorFamiliesResource:
    def test_initialization(self, api_info: Any) -> Any:
        settings = api_info["settings"]
        client = api_info["client"]

        cfr = ColorFamiliesResource(client)
        breakpoint()
