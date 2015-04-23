from a10sdk.common.A10BaseClass import A10BaseClass


class IcmpRateLimit(A10BaseClass):
    
    """Class Description::
    Limit the rate of ICMP packet.

    Class icmp-rate-limit supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param icmp_normal_rate_limit: {"description": "Normal rate limit. If exceeds this limit, drop the ICMP packet that goes over the limit", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": true}
    :param icmp_lockup: {"description": "Enter lockup state when ICMP rate exceeds lockup rate limit (Maximum rate limit. If exceeds this limit, drop all ICMP packet for a time period)", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": true}
    :param icmp_lockup_period: {"description": "Lockup period (second)", "format": "number", "type": "number", "maximum": 16383, "minimum": 1, "optional": true}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/network/icmp-rate-limit`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "icmp-rate-limit"
        self.a10_url="/axapi/v3/network/icmp-rate-limit"
        self.DeviceProxy = ""
        self.icmp_normal_rate_limit = ""
        self.icmp_lockup = ""
        self.icmp_lockup_period = ""
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


