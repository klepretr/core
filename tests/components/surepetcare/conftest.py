"""Define fixtures available for all tests."""
from pytest import fixture
from surepy import SurePetcare

from homeassistant.helpers.aiohttp_client import async_get_clientsession

from tests.async_mock import AsyncMock


@fixture()
def surepetcare(hass):
    """Mock the SurePetcare for easier testing.""""
    api = SurePetcare(
        "test-username",
        "test-password",
        hass.loop,
        async_get_clientsession(hass),
        api_timeout=1
    )

    api.get_data = AsyncMock(return_value=None)

    return api
