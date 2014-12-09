from a10sdk.common.A10BaseClass import A10BaseClass


class Outbound(A10BaseClass):
    
    """Class Description::
    sixrd fragmentation rules for outbound oversize packets (default: ipv6).

    Class outbound supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param count: {"description": "Configure number of ICMP messages sent when DF set. Default is 1", "format": "number", "type": "number", "maximum": 5, "minimum": 1, "optional": true}
    :param action: {"description": "'drop': Drop Silently; 'ipv6': Use IPv6 Fragmentation for oversize packets (default); 'send-icmp': Send ICMP Type 3 Code 4 (Fragmentation Needed and DF Set); 'send-icmpv6': Send ICMP Type 2 Code 0 (Packet Too Big); ", "format": "enum", "default": "ipv6", "type": "string", "enum": ["drop", "ipv6", "send-icmp", "send-icmpv6"], "optional": true}
    :param df_set: {"description": "'drop': Drop Silently; 'ipv6': Use IPv6 Fragmentation for oversize packets; 'send-icmp': Send ICMP Type 3 Code 4 (Fragmentation Needed and DF Set) (default); 'send-icmpv6': Send ICMP Type 2 Code 0 (Packet Too Big); ", "format": "enum", "default": "send-icmp", "type": "string", "enum": ["drop", "ipv6", "send-icmp", "send-icmpv6"], "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/sixrd/fragmentation/outbound`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "outbound"
        self.a10_url="/axapi/v3/cgnv6/sixrd/fragmentation/outbound"
        self.DeviceProxy = ""
        self.count = ""
        self.action = ""
        self.df_set = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


