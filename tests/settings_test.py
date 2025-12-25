from pyravelry.settings import RavelrySettings


class TestRavelrySettings:
    def test_initialization__valid_credentials(self) -> None:
        # this should run without error if
        # RAVELRY_USERNAME and RAVELRY_API_KEY
        # are set on the command line.
        RavelrySettings()
