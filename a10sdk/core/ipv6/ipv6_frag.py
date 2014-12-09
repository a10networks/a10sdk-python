from a10sdk.common.A10BaseClass import A10BaseClass


class Frag(A10BaseClass):
    
    """Class Description::
    IPv6 fragmentation parameters.

    Class frag supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param frag_timeout: {"description": "in milliseconds 4 - 16000 (default is 1000)", "format": "number", "type": "number", "maximum": 16000, "minimum": 4, "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/ipv6/frag`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "frag"
        self.a10_url="/axapi/v3/ipv6/frag"
        self.DeviceProxy = ""
        self.frag_timeout = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


