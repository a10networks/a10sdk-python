from a10sdk.common.A10BaseClass import A10BaseClass


class Secondary(A10BaseClass):
    
    """Class Description::
    Secondary DNS server.

    Class secondary supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param ip_v4_addr: {"not": "ip-v6-addr", "optional": true, "type": "string", "description": "DNS server address", "format": "ipv4-address"}
    :param ip_v6_addr: {"not": "ip-v4-addr", "optional": true, "type": "string", "description": "DNS server address", "format": "ipv6-address"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/ip/dns/secondary`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "secondary"
        self.a10_url="/axapi/v3/ip/dns/secondary"
        self.DeviceProxy = ""
        self.ip_v4_addr = ""
        self.ip_v6_addr = ""
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


