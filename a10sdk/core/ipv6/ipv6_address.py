from a10sdk.common.A10BaseClass import A10BaseClass


class Address(A10BaseClass):
    
    """Class Description::
    Transparent mode IPv6 Address.

    Class address supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param ipv6_address: {"optional": true, "type": "string", "description": "IPV6 address", "format": "ipv6-address-plen"}
    :param link_local: {"default": 0, "optional": true, "type": "number", "description": "Configure an IPv6 link local address", "format": "flag"}
    :param anycast: {"default": 0, "optional": true, "type": "number", "description": "Configure an IPv6 anycast address", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/ipv6/address`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "address"
        self.a10_url="/axapi/v3/ipv6/address"
        self.DeviceProxy = ""
        self.ipv6_address = ""
        self.link_local = ""
        self.anycast = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


