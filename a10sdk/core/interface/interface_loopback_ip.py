from a10sdk.common.A10BaseClass import A10BaseClass


class AddressList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ipv4_address: {"type": "string", "description": "IP address", "format": "ipv4-address"}
    :param ipv4_netmask: {"type": "string", "description": "IP subnet mask", "format": "ipv4-netmask"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "address-list"
        self.DeviceProxy = ""
        self.ipv4_address = ""
        self.ipv4_netmask = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Ip(A10BaseClass):
    
    """Class Description::
    Global IP configuration subcommands.

    Class ip supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param address_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"ipv4-address": {"type": "string", "description": "IP address", "format": "ipv4-address"}, "optional": true, "ipv4-netmask": {"type": "string", "description": "IP subnet mask", "format": "ipv4-netmask"}}}]}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/interface/loopback/{ifnum}/ip`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "ip"
        self.a10_url="/axapi/v3/interface/loopback/{ifnum}/ip"
        self.DeviceProxy = ""
        self.address_list = []
        self.ospf = {}
        self.uuid = ""
        self.rip = {}
        self.router = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


