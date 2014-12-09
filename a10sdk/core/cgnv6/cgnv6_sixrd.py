from a10sdk.common.A10BaseClass import A10BaseClass


class Sixrd(A10BaseClass):
    
    """Class Description::
    Configure IPv6 Rapid Deployment (sixrd).

    Class sixrd supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param domain_list: {"minItems": 1, "items": {"type": "domain"}, "uniqueItems": true, "array": [{"required": ["name"], "properties": {"ipv6-prefix": {"optional": true, "type": "string", "description": "IPv6 prefix", "format": "ipv6-address-plen"}, "name": {"description": "6rd Domain name", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}, "mtu": {"description": "Tunnel MTU", "format": "number", "type": "number", "maximum": 1480, "minimum": 1280, "optional": true}, "ce-ipv4-netmask": {"optional": true, "type": "string", "description": "Mask length", "format": "ipv4-netmask-brief"}, "ce-ipv4-network": {"optional": true, "type": "string", "description": "Customer Edge IPv4 network", "format": "ipv4-address"}, "br-ipv4-address": {"optional": true, "type": "string", "description": "6rd BR IPv4 address", "format": "ipv4-address"}}}], "type": "array", "$ref": "/axapi/v3/cgnv6/sixrd/domain/{name}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/sixrd`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "sixrd"
        self.a10_url="/axapi/v3/cgnv6/sixrd"
        self.DeviceProxy = ""
        self.domain_list = []
        self.fragmentation = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


