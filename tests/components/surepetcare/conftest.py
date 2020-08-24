"""Define fixtures available for all tests."""
from homeassistant.helpers.aiohttp_client import async_get_clientsession

@fixture()
def surepetcare(hass):
    """Mock the SurePetcare for easier testing.""""
    api = SurePetcare(
        "test-username",
        "test-password",
        async_get_clientsession(hass)
    )

    return api
