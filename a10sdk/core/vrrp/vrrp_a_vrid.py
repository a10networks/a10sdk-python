from a10sdk.common.A10BaseClass import A10BaseClass


class Ipv6AddressPartCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ethernet: {"partition-visibility": "private", "type": "number", "description": "Ethernet (for link-local address only)", "format": "interface"}
    :param ipv6_address_partition: {"partition-visibility": "private", "platform-specific-default": 1, "type": "string", "description": "IPV6 address", "format": "ipv6-address"}
    :param ve: {"description": "VE interface (for link-local address only)", "partition-visibility": "private", "format": "number", "maximum": 4094, "minimum": 2, "type": "number"}
    :param trunk: {"description": "Trunk interface (for link-local address only)", "partition-visibility": "private", "format": "number", "maximum": 4096, "minimum": 1, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ipv6-address-part-cfg"
        self.DeviceProxy = ""
        self.ethernet = ""
        self.ipv6_address_partition = ""
        self.ve = ""
        self.trunk = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class IpAddressCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ip_address: {"partition-visibility": "shared", "platform-specific-default": 1, "type": "string", "description": "IP Address", "format": "ipv4-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ip-address-cfg"
        self.DeviceProxy = ""
        self.ip_address = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class IpAddressPartCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ip_address_partition: {"partition-visibility": "private", "platform-specific-default": 1, "type": "string", "description": "IP Address", "format": "ipv4-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ip-address-part-cfg"
        self.DeviceProxy = ""
        self.ip_address_partition = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Ipv6AddressCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ipv6_address: {"partition-visibility": "shared", "platform-specific-default": 1, "type": "string", "description": "IPV6 address", "format": "ipv6-address"}
    :param ethernet: {"partition-visibility": "shared", "type": "number", "description": "Ethernet (for link-local address only)", "format": "interface"}
    :param ve: {"description": "VE interface (for link-local address only)", "partition-visibility": "shared", "format": "number", "maximum": 4094, "minimum": 2, "type": "number"}
    :param trunk: {"description": "Trunk interface (for link-local address only)", "partition-visibility": "shared", "format": "number", "maximum": 4096, "minimum": 1, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ipv6-address-cfg"
        self.DeviceProxy = ""
        self.ipv6_address = ""
        self.ethernet = ""
        self.ve = ""
        self.trunk = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class FloatingIp(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ipv6_address_part_cfg: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"ethernet": {"partition-visibility": "private", "type": "number", "description": "Ethernet (for link-local address only)", "format": "interface"}, "ipv6-address-partition": {"partition-visibility": "private", "platform-specific-default": 1, "type": "string", "description": "IPV6 address", "format": "ipv6-address"}, "optional": true, "ve": {"description": "VE interface (for link-local address only)", "partition-visibility": "private", "format": "number", "maximum": 4094, "minimum": 2, "type": "number"}, "trunk": {"description": "Trunk interface (for link-local address only)", "partition-visibility": "private", "format": "number", "maximum": 4096, "minimum": 1, "type": "number"}}}]}
    :param ip_address_cfg: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "ip-address": {"partition-visibility": "shared", "platform-specific-default": 1, "type": "string", "description": "IP Address", "format": "ipv4-address"}}}]}
    :param ip_address_part_cfg: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"ip-address-partition": {"partition-visibility": "private", "platform-specific-default": 1, "type": "string", "description": "IP Address", "format": "ipv4-address"}, "optional": true}}]}
    :param ipv6_address_cfg: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"ipv6-address": {"partition-visibility": "shared", "platform-specific-default": 1, "type": "string", "description": "IPV6 address", "format": "ipv6-address"}, "ethernet": {"partition-visibility": "shared", "type": "number", "description": "Ethernet (for link-local address only)", "format": "interface"}, "optional": true, "ve": {"description": "VE interface (for link-local address only)", "partition-visibility": "shared", "format": "number", "maximum": 4094, "minimum": 2, "type": "number"}, "trunk": {"description": "Trunk interface (for link-local address only)", "partition-visibility": "shared", "format": "number", "maximum": 4096, "minimum": 1, "type": "number"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "floating-ip"
        self.DeviceProxy = ""
        self.ipv6_address_part_cfg = []
        self.ip_address_cfg = []
        self.ip_address_part_cfg = []
        self.ipv6_address_cfg = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class PreemptMode(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param threshold: {"description": "preemption threshold (preemption threshhold (1-255), default 1)", "format": "number", "default": 1, "maximum": 255, "minimum": 1, "type": "number"}
    :param disable: {"default": 0, "type": "number", "description": "disable preemption", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "preempt-mode"
        self.DeviceProxy = ""
        self.threshold = ""
        self.disable = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Follow(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param vrid_lead: {"description": "Define a VRRP-A VRID leader", "partition-visibility": "private", "minLength": 1, "format": "string", "maxLength": 128, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "follow"
        self.DeviceProxy = ""
        self.vrid_lead = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Vrid(A10BaseClass):
    
    """    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param vrid_val: {"description": "Specify ha VRRP-A vrid", "format": "number", "default": 0, "optional": false, "maximum": 31, "minimum": 0, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Specify VRRP-A vrid.

    Class vrid supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/vrrp-a/vrid/{vrid_val}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "vrid_val"]

        self.b_key = "vrid"
        self.a10_url="/axapi/v3/vrrp-a/vrid/{vrid_val}"
        self.DeviceProxy = ""
        self.blade_parameters = {}
        self.uuid = ""
        self.floating_ip = {}
        self.vrid_val = ""
        self.preempt_mode = {}
        self.follow = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


