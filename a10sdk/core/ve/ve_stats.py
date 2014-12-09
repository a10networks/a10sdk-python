from a10sdk.common.A10BaseClass import A10BaseClass


class VeStats(A10BaseClass):
    
    """Class Description::
    Enables/Disables vlan ve interface stats generation.

    Class ve-stats supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param enable: {"default": 0, "optional": true, "type": "number", "description": "Enable vlan ve interface stats generation", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/ve-stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "ve-stats"
        self.a10_url="/axapi/v3/ve-stats"
        self.DeviceProxy = ""
        self.enable = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


