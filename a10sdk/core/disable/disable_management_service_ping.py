from a10sdk.common.A10BaseClass import A10BaseClass


class VeCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ve_end: {"type": "number", "description": "VE port", "format": "number"}
    :param ve_start: {"type": "number", "description": "VE port (VE Interface number)", "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ve-cfg"
        self.DeviceProxy = ""
        self.ve_end = ""
        self.ve_start = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class EthCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ethernet_start: {"type": "number", "description": "Ethernet port (Ethernet Interface number)", "format": "interface"}
    :param ethernet_end: {"type": "number", "description": "Ethernet port", "format": "interface"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "eth-cfg"
        self.DeviceProxy = ""
        self.ethernet_start = ""
        self.ethernet_end = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Ping(A10BaseClass):
    
    """Class Description::
    Ping service.

    Class ping supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param management: {"description": "Management port", "partition-visibility": "shared", "default": 0, "type": "number", "format": "flag", "optional": true}
    :param ve_cfg: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"ve-end": {"type": "number", "description": "VE port", "format": "number"}, "ve-start": {"type": "number", "description": "VE port (VE Interface number)", "format": "number"}, "optional": true}}]}
    :param eth_cfg: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"ethernet-start": {"type": "number", "description": "Ethernet port (Ethernet Interface number)", "format": "interface"}, "ethernet-end": {"type": "number", "description": "Ethernet port", "format": "interface"}, "optional": true}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/disable-management/service/ping`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "ping"
        self.a10_url="/axapi/v3/disable-management/service/ping"
        self.DeviceProxy = ""
        self.management = ""
        self.ve_cfg = []
        self.eth_cfg = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


