from a10sdk.common.A10BaseClass import A10BaseClass


class Qos(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param policy: {"description": "Policy name", "format": "string", "minLength": 1, "maxLength": 31, "type": "string", "$ref": "/axapi/v3/qos/policy"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "qos"
        self.DeviceProxy = ""
        self.policy = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class VeCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param port_ve_start: {"type": "number", "description": "Virtual Ethernet Interface", "format": "number"}
    :param port_ve_end: {"type": "number", "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ve-cfg"
        self.DeviceProxy = ""
        self.port_ve_start = ""
        self.port_ve_end = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class EthernetCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param port_ethernet_end: {"type": "number", "format": "interface"}
    :param port_ethernet_start: {"type": "number", "description": "Ethernet Interface", "format": "interface"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ethernet-cfg"
        self.DeviceProxy = ""
        self.port_ethernet_end = ""
        self.port_ethernet_start = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class TrunkCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param port_trunk_end: {"type": "number", "format": "number"}
    :param port_trunk_start: {"type": "number", "description": "Trunk Interface", "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "trunk-cfg"
        self.DeviceProxy = ""
        self.port_trunk_end = ""
        self.port_trunk_start = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Port(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ve_cfg: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"port-ve-start": {"type": "number", "description": "Virtual Ethernet Interface", "format": "number"}, "optional": true, "port-ve-end": {"type": "number", "format": "number"}}}]}
    :param ethernet_cfg: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "port-ethernet-end": {"type": "number", "format": "interface"}, "port-ethernet-start": {"type": "number", "description": "Ethernet Interface", "format": "interface"}}}]}
    :param trunk_cfg: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"port-trunk-end": {"type": "number", "format": "number"}, "optional": true, "port-trunk-start": {"type": "number", "description": "Trunk Interface", "format": "number"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "port"
        self.DeviceProxy = ""
        self.ve_cfg = []
        self.ethernet_cfg = []
        self.trunk_cfg = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Interface(A10BaseClass):
    
    """Class Description::
    QoS interface.

    Class interface supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param shape: {"description": "Shape traffic rate on the interface", "format": "number", "type": "number", "maximum": 1000000000, "minimum": 0, "optional": true}
    :param name: {"description": "QoS interface name", "format": "string", "minLength": 1, "optional": false, "maxLength": 31, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/qos/interface/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "interface"
        self.a10_url="/axapi/v3/qos/interface/{name}"
        self.DeviceProxy = ""
        self.uuid = ""
        self.shape = ""
        self.qos = {}
        self.name = ""
        self.port = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


