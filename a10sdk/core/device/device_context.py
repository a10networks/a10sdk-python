from a10sdk.common.A10BaseClass import A10BaseClass


class DeviceContext(A10BaseClass):
    
    """    :param device_id: {"platform-specific-range": 1, "platform-specific-default": 1, "description": "Device ID", "format": "number", "optional": true, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Switch context to a particular device for VCS config.

    Class device-context supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/device-context`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "device-context"
        self.a10_url="/axapi/v3/device-context"
        self.DeviceProxy = ""
        self.device_id = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


