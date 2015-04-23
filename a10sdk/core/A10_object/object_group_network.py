from a10sdk.common.A10BaseClass import A10BaseClass


class Rules(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param host_v6: {"type": "string", "description": "IPv6 Host Address", "format": "ipv6-address"}
    :param subnet: {"type": "string", "description": "IPv4 Network Address", "format": "ipv4-address"}
    :param host_v4: {"type": "string", "description": "IPv4 Host Address", "format": "ipv4-address"}
    :param ipv6_subnet: {"type": "string", "description": "IPv6 Network Address", "format": "ipv6-address-plen"}
    :param seq_num: {"description": "Sequence number", "minimum": 1, "type": "number", "maximum": 8192, "format": "number"}
    :param rev_subnet_mask: {"type": "string", "description": "Network Mask. 0=apply, 255=ignore", "format": "ipv4-rev-netmask"}
    :param any: {"default": 0, "type": "number", "description": "Any host", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "rules"
        self.DeviceProxy = ""
        self.host_v6 = ""
        self.subnet = ""
        self.host_v4 = ""
        self.ipv6_subnet = ""
        self.seq_num = ""
        self.rev_subnet_mask = ""
        self.A10WW_any = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Network(A10BaseClass):
    
    """Class Description::
    Configure Network Object Group.

    Class network supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param rules: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"host-v6": {"type": "string", "description": "IPv6 Host Address", "format": "ipv6-address"}, "subnet": {"type": "string", "description": "IPv4 Network Address", "format": "ipv4-address"}, "host-v4": {"type": "string", "description": "IPv4 Host Address", "format": "ipv4-address"}, "ipv6-subnet": {"type": "string", "description": "IPv6 Network Address", "format": "ipv6-address-plen"}, "seq-num": {"description": "Sequence number", "minimum": 1, "type": "number", "maximum": 8192, "format": "number"}, "rev-subnet-mask": {"type": "string", "description": "Network Mask. 0=apply, 255=ignore", "format": "ipv4-rev-netmask"}, "optional": true, "any": {"default": 0, "type": "number", "description": "Any host", "format": "flag"}}}]}
    :param net_name: {"description": "Network Object Name", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param description: {"description": "Description of the object-group instance", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 128, "type": "string"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/object-group/network/{net_name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "net_name"]

        self.b_key = "network"
        self.a10_url="/axapi/v3/object-group/network/{net_name}"
        self.DeviceProxy = ""
        self.rules = []
        self.net_name = ""
        self.description = ""
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


