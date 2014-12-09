from a10sdk.common.A10BaseClass import A10BaseClass


class System4X10GMode(A10BaseClass):
    
    """Class Description::
    To enable/disable 40G port to split into 4x10g ports.

    Class system-4x10g-mode supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param enable: {"default": 0, "optional": true, "type": "number", "description": "Enable/Disable 40G port to split into 4x10g ports", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/system-4x10g-mode`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "system-4x10g-mode"
        self.a10_url="/axapi/v3/system-4x10g-mode"
        self.DeviceProxy = ""
        self.enable = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


