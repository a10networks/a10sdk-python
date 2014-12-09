from a10sdk.common.A10BaseClass import A10BaseClass


class UntaggedTrunkList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param untagged_trunk_start: {"type": "number", "description": "Trunk groups", "format": "number"}
    :param untagged_trunk_end: {"type": "number", "description": "Trunk Group", "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "untagged-trunk-list"
        self.DeviceProxy = ""
        self.untagged_trunk_start = ""
        self.untagged_trunk_end = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class UntaggedEthList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param untagged_ethernet_end: {"type": "number", "description": "Ethernet port", "format": "interface"}
    :param untagged_ethernet_start: {"$ref": "/axapi/v3/interface/ethernet", "type": "number", "description": "Ethernet port (Interface number)", "format": "interface"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "untagged-eth-list"
        self.DeviceProxy = ""
        self.untagged_ethernet_end = ""
        self.untagged_ethernet_start = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class TaggedEthList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param tagged_ethernet_end: {"type": "number", "description": "Ethernet port", "format": "interface"}
    :param tagged_ethernet_start: {"$ref": "/axapi/v3/interface/ethernet", "type": "number", "description": "Ethernet port (Interface number)", "format": "interface"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "tagged-eth-list"
        self.DeviceProxy = ""
        self.tagged_ethernet_end = ""
        self.tagged_ethernet_start = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class TaggedTrunkList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param tagged_trunk_start: {"type": "number", "description": "Trunk groups", "format": "number"}
    :param tagged_trunk_end: {"type": "number", "description": "Trunk Group", "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "tagged-trunk-list"
        self.DeviceProxy = ""
        self.tagged_trunk_start = ""
        self.tagged_trunk_end = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Vlan(A10BaseClass):
    
    """Class Description::
    Configure VLAN.

    Class vlan supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param ve: {"description": "ve number", "format": "number", "type": "number", "maximum": 4094, "minimum": 2, "optional": true}
    :param untagged_trunk_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"untagged-trunk-start": {"type": "number", "description": "Trunk groups", "format": "number"}, "optional": true, "untagged-trunk-end": {"type": "number", "description": "Trunk Group", "format": "number"}}}]}
    :param untagged_lif: {"description": "Logical tunnel interface (Logical tunnel interface number)", "format": "number", "type": "number", "maximum": 128, "minimum": 1, "optional": true}
    :param untagged_eth_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"untagged-ethernet-end": {"type": "number", "description": "Ethernet port", "format": "interface"}, "untagged-ethernet-start": {"$ref": "/axapi/v3/interface/ethernet", "type": "number", "description": "Ethernet port (Interface number)", "format": "interface"}, "optional": true}}]}
    :param tagged_eth_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"tagged-ethernet-end": {"type": "number", "description": "Ethernet port", "format": "interface"}, "optional": true, "tagged-ethernet-start": {"$ref": "/axapi/v3/interface/ethernet", "type": "number", "description": "Ethernet port (Interface number)", "format": "interface"}}}]}
    :param tagged_trunk_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "tagged-trunk-start": {"type": "number", "description": "Trunk groups", "format": "number"}, "tagged-trunk-end": {"type": "number", "description": "Trunk Group", "format": "number"}}}]}
    :param vlan_num: {"description": "VLAN number", "format": "number", "type": "number", "maximum": 4094, "minimum": 2, "optional": false}
    :param name: {"description": "VLAN name", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/network/vlan/{vlan_num}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "vlan_num"]

        self.b_key = "vlan"
        self.a10_url="/axapi/v3/network/vlan/{vlan_num}"
        self.DeviceProxy = ""
        self.ve = ""
        self.untagged_trunk_list = []
        self.untagged_lif = ""
        self.untagged_eth_list = []
        self.tagged_eth_list = []
        self.tagged_trunk_list = []
        self.vlan_num = ""
        self.name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


