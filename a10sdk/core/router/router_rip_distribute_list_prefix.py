from a10sdk.common.A10BaseClass import A10BaseClass


class PrefixCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ve: {"type": "number", "description": "Virtual ethernet interface (Virtual ethernet interface number)", "format": "interface"}
    :param loopback: {"type": "number", "description": "Loopback interface (Port number)", "format": "interface"}
    :param prefix_list: {"minLength": 1, "maxLength": 128, "type": "string", "description": "Filter prefixes in routing updates (Name of a prefix list)", "format": "string"}
    :param trunk: {"type": "number", "description": "Trunk interface (Trunk interface number)", "format": "interface"}
    :param prefix_list_direction: {"enum": ["in", "out"], "type": "string", "description": "'in': Filter incoming routing updates; 'out': Filter outgoing routing updates; ", "format": "enum"}
    :param ethernet: {"type": "number", "description": "Ethernet interface (Port number)", "format": "interface"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "prefix-cfg"
        self.DeviceProxy = ""
        self.ve = ""
        self.loopback = ""
        self.prefix_list = ""
        self.trunk = ""
        self.prefix_list_direction = ""
        self.ethernet = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Prefix(A10BaseClass):
    
    """Class Description::
    Filter prefixes in routing updates.

    Class prefix supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param prefix_cfg: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"ve": {"type": "number", "description": "Virtual ethernet interface (Virtual ethernet interface number)", "format": "interface"}, "loopback": {"type": "number", "description": "Loopback interface (Port number)", "format": "interface"}, "prefix-list": {"minLength": 1, "maxLength": 128, "type": "string", "description": "Filter prefixes in routing updates (Name of a prefix list)", "format": "string"}, "trunk": {"type": "number", "description": "Trunk interface (Trunk interface number)", "format": "interface"}, "prefix-list-direction": {"enum": ["in", "out"], "type": "string", "description": "'in': Filter incoming routing updates; 'out': Filter outgoing routing updates; ", "format": "enum"}, "ethernet": {"type": "number", "description": "Ethernet interface (Port number)", "format": "interface"}, "optional": true}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/router/rip/distribute-list/prefix`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "prefix"
        self.a10_url="/axapi/v3/router/rip/distribute-list/prefix"
        self.DeviceProxy = ""
        self.uuid = ""
        self.prefix_cfg = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


