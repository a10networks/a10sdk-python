from a10sdk.common.A10BaseClass import A10BaseClass


class Icmp(A10BaseClass):
    
    """Class Description::
    ICMP type.

    Class icmp supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param ip: {"not": "ipv6", "optional": true, "type": "string", "description": "Specify IPv4 address of destination behind monitored node", "format": "ipv4-address"}
    :param icmp: {"default": 0, "optional": true, "type": "number", "description": "ICMP type", "format": "flag"}
    :param transparent: {"default": 0, "optional": true, "type": "number", "description": "Apply transparent mode", "format": "flag"}
    :param ipv6: {"not": "ip", "optional": true, "type": "string", "description": "Specify IPv6 address of destination behind monitored node", "format": "ipv6-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/health/monitor/{name}/method/icmp`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "icmp"
        self.a10_url="/axapi/v3/health/monitor/{name}/method/icmp"
        self.DeviceProxy = ""
        self.ip = ""
        self.icmp = ""
        self.transparent = ""
        self.ipv6 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


