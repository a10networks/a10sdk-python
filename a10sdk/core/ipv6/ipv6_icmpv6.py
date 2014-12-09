from a10sdk.common.A10BaseClass import A10BaseClass


class Icmpv6(A10BaseClass):
    
    """Class Description::
    Global ICMPv6 commands.

    Class icmpv6 supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param redirect: {"default": 0, "optional": true, "type": "number", "description": "Disable outbound ICMPv6 redirect messages", "format": "flag"}
    :param unreachable: {"default": 0, "optional": true, "type": "number", "description": "Disable outbound ICMPv6 unreachable messages", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/ipv6/icmpv6`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "icmpv6"
        self.a10_url="/axapi/v3/ipv6/icmpv6"
        self.DeviceProxy = ""
        self.redirect = ""
        self.unreachable = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


