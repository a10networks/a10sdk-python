from a10sdk.common.A10BaseClass import A10BaseClass


class Icmp(A10BaseClass):
    
    """Class Description::
    Global ICMP commands.

    Class icmp supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param redirect: {"default": 0, "optional": true, "type": "number", "description": "Disable outbound ICMP redirect messages", "format": "flag"}
    :param unreachable: {"default": 0, "optional": true, "type": "number", "description": "Disable outbound ICMP unreachable messages", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/ip/icmp`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "icmp"
        self.a10_url="/axapi/v3/ip/icmp"
        self.DeviceProxy = ""
        self.redirect = ""
        self.unreachable = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


