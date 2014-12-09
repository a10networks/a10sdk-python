from a10sdk.common.A10BaseClass import A10BaseClass


class Icmpv6RateLimit(A10BaseClass):
    
    """Class Description::
    Limit the rate of ICMPv6 packet.

    Class icmpv6-rate-limit supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param icmpv6_lockup_period: {"description": "Lockup period (second)", "format": "number", "type": "number", "maximum": 16383, "minimum": 1, "optional": true}
    :param icmpv6_lockup: {"description": "Enter lockup state when ICMP rate exceeds lockup rate limit. help-val Maximum rate limit. If exceeds this limit, drop all ICMP packet for a time period", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": true}
    :param icmpv6_normal_rate_limit: {"description": "Normal rate limit. If exceeds this limit, drop the ICMP packet that goes over the limit", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/icmpv6-rate-limit`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "icmpv6-rate-limit"
        self.a10_url="/axapi/v3/icmpv6-rate-limit"
        self.DeviceProxy = ""
        self.icmpv6_lockup_period = ""
        self.icmpv6_lockup = ""
        self.icmpv6_normal_rate_limit = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


