from a10sdk.common.A10BaseClass import A10BaseClass


class AddressList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param link_local: {"default": 0, "type": "number", "description": "Configure an IPv6 link local address", "format": "flag"}
    :param anycast: {"default": 0, "type": "number", "description": "Configure an IPv6 anycast address", "format": "flag"}
    :param ipv6_addr: {"type": "string", "description": "Set the IPv6 address of an interface", "format": "ipv6-address-plen"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "address-list"
        self.DeviceProxy = ""
        self.link_local = ""
        self.anycast = ""
        self.ipv6_addr = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Ipv6(A10BaseClass):
    
    """Class Description::
    Global IPv6 configuration subcommands.

    Class ipv6 supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param address_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"link-local": {"default": 0, "type": "number", "description": "Configure an IPv6 link local address", "format": "flag"}, "anycast": {"default": 0, "type": "number", "description": "Configure an IPv6 anycast address", "format": "flag"}, "ipv6-addr": {"type": "string", "description": "Set the IPv6 address of an interface", "format": "ipv6-address-plen"}, "optional": true}}]}
    :param ipv6_enable: {"default": 0, "optional": true, "type": "number", "description": "Enable IPv6 processing", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/interface/loopback/{ifnum}/ipv6`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "ipv6"
        self.a10_url="/axapi/v3/interface/loopback/{ifnum}/ipv6"
        self.DeviceProxy = ""
        self.uuid = ""
        self.address_list = []
        self.rip = {}
        self.ipv6_enable = ""
        self.router = {}
        self.ospf = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


