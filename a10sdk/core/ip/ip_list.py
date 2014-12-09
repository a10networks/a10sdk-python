from a10sdk.common.A10BaseClass import A10BaseClass


class Ipv6PrefixConfig(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ipv6_prefix_to: {"type": "string", "description": "IPv6 Prefix Range End", "format": "ipv6-address-plen"}
    :param count: {"type": "number", "description": "Number of IPv6 prefixes", "format": "number"}
    :param ipv6_addr_prefix: {"type": "string", "description": "IPv6 Prefix Range Start / IPv6 Prefix", "format": "ipv6-address-plen"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ipv6-prefix-config"
        self.DeviceProxy = ""
        self.ipv6_prefix_to = ""
        self.count = ""
        self.ipv6_addr_prefix = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Ipv6Config(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ipv6_end_addr: {"type": "string", "description": "IPv6 Range End Address", "format": "ipv6-address"}
    :param ipv6_start_addr: {"type": "string", "description": "IPv6 Range Start Address / IPv6 Address", "format": "ipv6-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ipv6-config"
        self.DeviceProxy = ""
        self.ipv6_end_addr = ""
        self.ipv6_start_addr = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Ipv4Config(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ipv4_start_addr: {"type": "string", "description": "IPv4 Range Start Address / IPv4 Address", "format": "ipv4-address"}
    :param ipv4_end_addr: {"type": "string", "description": "IPv4 Range End Address", "format": "ipv4-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ipv4-config"
        self.DeviceProxy = ""
        self.ipv4_start_addr = ""
        self.ipv4_end_addr = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class IpList(A10BaseClass):
    
    """Class Description::
    Configure ip list.

    Class ip-list supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param ipv6_prefix_config: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"ipv6-prefix-to": {"type": "string", "description": "IPv6 Prefix Range End", "format": "ipv6-address-plen"}, "count": {"type": "number", "description": "Number of IPv6 prefixes", "format": "number"}, "optional": true, "ipv6-addr-prefix": {"type": "string", "description": "IPv6 Prefix Range Start / IPv6 Prefix", "format": "ipv6-address-plen"}}}]}
    :param name: {"description": "Specify name of the ip list", "format": "string-rlx", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param ipv6_config: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"ipv6-end-addr": {"type": "string", "description": "IPv6 Range End Address", "format": "ipv6-address"}, "optional": true, "ipv6-start-addr": {"type": "string", "description": "IPv6 Range Start Address / IPv6 Address", "format": "ipv6-address"}}}]}
    :param ipv4_config: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"ipv4-start-addr": {"type": "string", "description": "IPv4 Range Start Address / IPv4 Address", "format": "ipv4-address"}, "ipv4-end-addr": {"type": "string", "description": "IPv4 Range End Address", "format": "ipv4-address"}, "optional": true}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/ip-list/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "ip-list"
        self.a10_url="/axapi/v3/ip-list/{name}"
        self.DeviceProxy = ""
        self.ipv6_prefix_config = []
        self.name = ""
        self.ipv6_config = []
        self.ipv4_config = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


