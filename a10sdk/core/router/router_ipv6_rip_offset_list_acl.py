from a10sdk.common.A10BaseClass import A10BaseClass


class AclCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ve: {"type": "number", "description": "Virtual ethernet interface. help-val Virtual ethernet interface number", "format": "interface"}
    :param loopback: {"type": "number", "description": "Loopback interface. help-val Port number", "format": "interface"}
    :param metric: {"description": "Metric value", "minimum": 0, "type": "number", "maximum": 16, "format": "number"}
    :param trunk: {"type": "number", "description": "Trunk interface. help-val Trunk interface number", "format": "interface"}
    :param acl: {"minLength": 1, "maxLength": 128, "type": "string", "description": "Access-list name", "format": "string"}
    :param offset_list_direction: {"enum": ["in", "out"], "type": "string", "description": "in: \"Filter incoming updates\"; out: \"Filter outgoing updates\"; ", "format": "enum"}
    :param ethernet: {"type": "number", "description": "Ethernet interface. help-val Port number", "format": "interface"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "acl-cfg"
        self.DeviceProxy = ""
        self.ve = ""
        self.loopback = ""
        self.metric = ""
        self.trunk = ""
        self.acl = ""
        self.offset_list_direction = ""
        self.ethernet = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Acl(A10BaseClass):
    
    """Class Description::
    acl.

    Class acl supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param acl_cfg: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"ve": {"type": "number", "description": "Virtual ethernet interface. help-val Virtual ethernet interface number", "format": "interface"}, "loopback": {"type": "number", "description": "Loopback interface. help-val Port number", "format": "interface"}, "metric": {"description": "Metric value", "minimum": 0, "type": "number", "maximum": 16, "format": "number"}, "trunk": {"type": "number", "description": "Trunk interface. help-val Trunk interface number", "format": "interface"}, "acl": {"minLength": 1, "maxLength": 128, "type": "string", "description": "Access-list name", "format": "string"}, "offset-list-direction": {"enum": ["in", "out"], "type": "string", "description": "in: \"Filter incoming updates\"; out: \"Filter outgoing updates\"; ", "format": "enum"}, "ethernet": {"type": "number", "description": "Ethernet interface. help-val Port number", "format": "interface"}, "optional": true}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/router/ipv6/rip/offset-list/acl`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "acl"
        self.a10_url="/axapi/v3/router/ipv6/rip/offset-list/acl"
        self.DeviceProxy = ""
        self.acl_cfg = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


