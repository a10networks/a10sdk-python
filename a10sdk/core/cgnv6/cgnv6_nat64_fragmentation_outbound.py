from a10sdk.common.A10BaseClass import A10BaseClass


class Outbound(A10BaseClass):
    
    """Class Description::
    Fragmentation Behavior from NAT inside to NAT outside.

    Class outbound supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param frag_action: {"description": "'drop': Drop Silently; 'ipv4': Use IPv4 fragmentation (default); 'send-icmpv6': Send ICMPv6 Type 2 Code 0 (Packet Too Big); ", "format": "enum", "default": "ipv4", "type": "string", "enum": ["drop", "ipv4", "send-icmpv6"], "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/nat64/fragmentation/outbound`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "outbound"
        self.a10_url="/axapi/v3/cgnv6/nat64/fragmentation/outbound"
        self.DeviceProxy = ""
        self.frag_action = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


