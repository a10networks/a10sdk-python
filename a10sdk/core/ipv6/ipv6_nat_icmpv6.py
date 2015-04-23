from a10sdk.common.A10BaseClass import A10BaseClass


class Icmpv6(A10BaseClass):
    
    """Class Description::
    ICMPv6 configuration for IPv6 NAT.

    Class icmpv6 supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param respond_to_ping: {"default": 0, "optional": true, "type": "number", "description": "Respond to ICMPv6 echo requests to NAT pool IPs (default: disabled)", "format": "flag"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/ipv6/nat/icmpv6`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "icmpv6"
        self.a10_url="/axapi/v3/ipv6/nat/icmpv6"
        self.DeviceProxy = ""
        self.respond_to_ping = ""
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


