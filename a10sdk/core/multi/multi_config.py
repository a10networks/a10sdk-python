from a10sdk.common.A10BaseClass import A10BaseClass


class MultiConfig(A10BaseClass):
    
    """Class Description::
    Set multi-config enable/disable.

    Class multi-config supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param enable: {"default": 0, "optional": true, "type": "number", "description": "Enable multiple configuration mode", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/multi-config`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "multi-config"
        self.a10_url="/axapi/v3/multi-config"
        self.DeviceProxy = ""
        self.enable = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


