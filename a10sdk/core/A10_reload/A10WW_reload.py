from a10sdk.common.A10BaseClass import A10BaseClass


class Reload(A10BaseClass):
    
    """    :param device: {"platform-specific-range": 1, "platform-specific-default": 1, "description": "Reload a specific device when VCS is enabled (device id)", "format": "number", "optional": true, "type": "number"}
    :param all: {"default": 0, "optional": true, "type": "number", "description": "Reload all devices when VCS is enabled, or only this device itself if VCS is not enabled", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Reload the system without rebooting.

    Class reload supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/reload`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "reload"
        self.a10_url="/axapi/v3/reload"
        self.DeviceProxy = ""
        self.device = ""
        self.A10WW_all = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


