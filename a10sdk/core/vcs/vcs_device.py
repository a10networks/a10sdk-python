from a10sdk.common.A10BaseClass import A10BaseClass


class EthernetCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ethernet: {"type": "number", "description": "Ethernet (Ethernet interface number)", "format": "interface"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ethernet-cfg"
        self.DeviceProxy = ""
        self.ethernet = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class VeCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ve: {"description": "VE interface (VE interface number)", "minimum": 2, "type": "number", "maximum": 4094, "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ve-cfg"
        self.DeviceProxy = ""
        self.ve = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class TrunkCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param trunk: {"description": "Trunk interface (Trunk interface number)", "minimum": 1, "type": "number", "maximum": 16, "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "trunk-cfg"
        self.DeviceProxy = ""
        self.trunk = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Device(A10BaseClass):
    
    """Class Description::
    VCS Device.

    Class device supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param management: {"default": 0, "optional": true, "type": "number", "description": "Management interface", "format": "flag"}
    :param ethernet_cfg: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"ethernet": {"type": "number", "description": "Ethernet (Ethernet interface number)", "format": "interface"}, "optional": true}}]}
    :param priority: {"description": "Device priority", "format": "number", "type": "number", "maximum": 255, "minimum": 1, "optional": true}
    :param enable: {"default": 0, "optional": true, "type": "number", "description": "Enable", "format": "flag"}
    :param ve_cfg: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "ve": {"description": "VE interface (VE interface number)", "minimum": 2, "type": "number", "maximum": 4094, "format": "number"}}}]}
    :param device: {"description": "Device ID", "format": "number", "type": "number", "maximum": 8, "minimum": 1, "optional": false}
    :param affinity_vrrp_a_vrid: {"description": "vrid-group", "format": "number", "type": "number", "maximum": 31, "minimum": 0, "optional": true}
    :param unicast_port: {"description": "Port used in unicast communication (Port number)", "format": "number", "type": "number", "maximum": 65535, "minimum": 1024, "optional": true}
    :param trunk_cfg: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "trunk": {"description": "Trunk interface (Trunk interface number)", "minimum": 1, "type": "number", "maximum": 16, "format": "number"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/vcs/device/{device}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "device"]

        self.b_key = "device"
        self.a10_url="/axapi/v3/vcs/device/{device}"
        self.DeviceProxy = ""
        self.management = ""
        self.ethernet_cfg = []
        self.priority = ""
        self.enable = ""
        self.ve_cfg = []
        self.device = ""
        self.affinity_vrrp_a_vrid = ""
        self.unicast_port = ""
        self.trunk_cfg = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


