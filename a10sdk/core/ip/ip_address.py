from a10sdk.common.A10BaseClass import A10BaseClass


class Address(A10BaseClass):
    
    """Class Description::
    Transparent mode IP Address.

    Class address supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param ip_addr: {"optional": true, "type": "string", "description": "IP address", "format": "ipv4-address"}
    :param ip_mask: {"optional": true, "type": "string", "description": "IP subnet mask", "format": "ipv4-netmask"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/ip/address`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "address"
        self.a10_url="/axapi/v3/ip/address"
        self.DeviceProxy = ""
        self.ip_addr = ""
        self.ip_mask = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


