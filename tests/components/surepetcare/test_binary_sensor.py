"""The tests for the Sure Petcare binary sensor platform."""
from homeassistant.components.surepetcare.const import DOMAIN
from homeassistant.setup import async_setup_component

from . import MOCK_CONFIG, _patch_api, _patch_sensor_setup


async def test_unique_ids(hass, surepetcare) -> None:
    """Test the generation of unique ids."""
    with _patch_api(surepetcare), _patch_sensor_setup():
        assert await async_setup_component(hass, DOMAIN, MOCK_CONFIG)

    assert hass.states.get("binary_sensor.hub_hub")

    assert hass.states.get("binary_sensor.cat_flap_cat_flap")
    assert hass.states.get("binary_sensor.cat_flap_cat_flap_connectivity")

    assert hass.states.get("binary_sensor.pet_flap_pet_flap")
    assert hass.states.get("binary_sensor.pet_flap_pet_flap_connectivity")

    assert hass.states.get("binary_sensor.feeder_feeder")
    assert hass.states.get("binary_sensor.feeder_feeder_connectivity")

    assert hass.states.get("binary_sensor.pet_pet")
