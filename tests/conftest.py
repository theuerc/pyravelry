from typing import Any, TypedDict

import httpx
import pytest

from pyravelry.settings import RavelrySettings


class APIInfo(TypedDict):
    """Type definition for the api_info fixture return value."""

    settings: RavelrySettings
    client: httpx.Client


@pytest.fixture(scope="session")
def api_info() -> APIInfo:
    """Gets the basic info required for an API call.

    Returns:
        APIInfo: A dictionary with auth and an httpx client.
    """
    settings = RavelrySettings()
    client = httpx.Client(
        base_url=str(settings.base_url),
        auth=settings.auth_tuple,
        timeout=10.0,
    )
    return {"settings": settings, "client": client}


@pytest.fixture(scope="module")
def vcr_config() -> dict[str, Any]:
    return {
        "filter_headers": [("authorization", "Basic <REDACTED>")],
        "decode_compressed_response": True,
    }
