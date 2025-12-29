from __future__ import annotations

from pydantic import Field, HttpUrl, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class RavelrySettings(BaseSettings):
    """Initializes the settings from which to call the Ravelry API.

    Attributes:
        ravelry_auth_username (str): username for Ravelry.
        ravelry_auth_api_key (SecretStr): read-only API token for accessing Ravelry.
        auth_tuple (tuple[str, str]): formatted Revelry auth tuple for httpx.
    """

    # Use the 'read-only' credentials from your Ravelry App control panel
    ravelry_auth_username: str = Field(..., alias="RAVELRY_USERNAME")
    ravelry_auth_api_key: SecretStr = Field(..., alias="RAVELRY_API_KEY")

    # The API requires SSL (HTTPS) for all requests
    base_url: HttpUrl = HttpUrl("https://api.ravelry.com")

    # Configuration to read from a .env file
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    @property
    def auth_tuple(self) -> tuple[str, str]:
        """Returns credentials in the (username, password) format for httpx."""
        return (
            self.ravelry_auth_username,
            self.ravelry_auth_api_key.get_secret_value(),
        )
