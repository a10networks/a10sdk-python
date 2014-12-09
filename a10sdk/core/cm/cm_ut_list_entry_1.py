from a10sdk.common.A10BaseClass import A10BaseClass


class EntryCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param distance: {"minimum": 1, "type": "number", "maximum": 255, "format": "number"}
    :param protocol: {"enum": ["any", "static", "dynamic"], "type": "string", "description": "any: \"any\"; static: \"static\"; dynamic: \"dynamic\"; ", "format": "enum"}
    :param weight: {"minimum": 1, "type": "number", "maximum": 255, "format": "number"}
    :param dst: {"type": "string", "format": "ipv4-address"}
    :param mask: {"type": "string", "format": "ipv4-netmask"}
    :param gateway: {"type": "string", "format": "ipv4-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "entry-cfg"
        self.DeviceProxy = ""
        self.distance = ""
        self.protocol = ""
        self.weight = ""
        self.dst = ""
        self.mask = ""
        self.gateway = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class List(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param entry_cfg: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"distance": {"minimum": 1, "type": "number", "maximum": 255, "format": "number"}, "protocol": {"enum": ["any", "static", "dynamic"], "type": "string", "description": "any: \"any\"; static: \"static\"; dynamic: \"dynamic\"; ", "format": "enum"}, "weight": {"minimum": 1, "type": "number", "maximum": 255, "format": "number"}, "dst": {"type": "string", "format": "ipv4-address"}, "mask": {"type": "string", "format": "ipv4-netmask"}, "optional": true, "gateway": {"type": "string", "format": "ipv4-address"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "list"
        self.DeviceProxy = ""
        self.entry_cfg = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class ListEntry1(A10BaseClass):
    
    """Class Description::
    Unit test CM list where entry fields are mandatory for one.

    Class list-entry-1 supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cm-ut/list-entry-1`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "list-entry-1"
        self.a10_url="/axapi/v3/cm-ut/list-entry-1"
        self.DeviceProxy = ""
        self.A10WW_list = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


