from a10sdk.common.A10BaseClass import A10BaseClass


class Ripng(A10BaseClass):
    
    """Class Description::
    ripng.

    Class ripng supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param rip: {"default": 0, "optional": true, "type": "number", "description": "RIP Routing for IPv6", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/interface/trunk/{ifnum}/ipv6/router/ripng`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "ripng"
        self.a10_url="/axapi/v3/interface/trunk/{ifnum}/ipv6/router/ripng"
        self.DeviceProxy = ""
        self.rip = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


