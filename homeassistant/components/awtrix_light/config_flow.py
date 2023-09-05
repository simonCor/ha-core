"""Config flow for Awtrix_Light."""
# import my_pypi_dependency
import voluptuous as vol

from homeassistant import config_entries
from homeassistant.core import HomeAssistant
from homeassistant.helpers import config_entry_flow

from .const import DOMAIN


async def _async_has_devices(hass: HomeAssistant) -> bool:
    return True


#    """Return if there are devices that can be discovered."""
#    # TODO Check if there are any devices that can be discovered in the network.
#    devices = await hass.async_add_executor_job(my_pypi_dependency.discover)
#   return len(devices) > 0


config_entry_flow.register_discovery_flow(DOMAIN, "Awtrix_Light", _async_has_devices)


class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    async def async_step_user(self, info):
        if info is not None:
            pass  # TODO: process info

        return self.async_show_form(
            step_id="awtrixTopic",
            data_schema=vol.Schema({vol.Required("MQTT topic"): str}),
        )

    async def async_step_awtrixTopic(self, info):
        if info is not None:
            print(info["MQTT topic"])

            pass  # TODO: process info
