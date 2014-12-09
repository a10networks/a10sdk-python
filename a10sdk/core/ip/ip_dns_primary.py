from a10sdk.common.A10BaseClass import A10BaseClass


class Primary(A10BaseClass):
    
    """Class Description::
    Primary DNS server.

    Class primary supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param ip_v4_addr: {"not": "ip-v6-addr", "optional": true, "type": "string", "description": "DNS server address", "format": "ipv4-address"}
    :param ip_v6_addr: {"not": "ip-v4-addr", "optional": true, "type": "string", "description": "DNS server address", "format": "ipv6-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/ip/dns/primary`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "primary"
        self.a10_url="/axapi/v3/ip/dns/primary"
        self.DeviceProxy = ""
        self.ip_v4_addr = ""
        self.ip_v6_addr = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


