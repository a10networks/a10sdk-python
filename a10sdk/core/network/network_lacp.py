from a10sdk.common.A10BaseClass import A10BaseClass


class Lacp(A10BaseClass):
    
    """Class Description::
    LACP commands.

    Class lacp supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param system_priority: {"description": "LACP system priority (LACP system priority, 1-65535, default 32768)", "format": "number", "default": 32768, "optional": true, "maximum": 65535, "minimum": 1, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/network/lacp`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "lacp"
        self.a10_url="/axapi/v3/network/lacp"
        self.DeviceProxy = ""
        self.system_priority = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


