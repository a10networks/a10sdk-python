from a10sdk.common.A10BaseClass import A10BaseClass


class V6NeighborList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param Age: {"type": "number", "format": "number"}
    :param Vlan: {"minimum": 1, "type": "number", "maximum": 4094, "format": "number"}
    :param Interface: {"enum": ["Management", "ethernet", "trunk"], "type": "string", "format": "enum"}
    :param State: {"type": "string", "format": "string"}
    :param IPV6_Address: {"type": "string", "format": "ipv6-address"}
    :param Type: {"enum": ["Incomplete", "Dynamic", "Static"], "type": "string", "format": "enum"}
    :param MAC_Address: {"minLength": 11, "maxLength": 17, "type": "string", "format": "mac-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "v6neighbor-list"
        self.DeviceProxy = ""
        self.Age = ""
        self.Vlan = ""
        self.Interface = ""
        self.State = ""
        self.IPV6_Address = ""
        self.Type = ""
        self.MAC_Address = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param v6neighbor_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "Age": {"type": "number", "format": "number"}, "Vlan": {"minimum": 1, "type": "number", "maximum": 4094, "format": "number"}, "Interface": {"enum": ["Management", "ethernet", "trunk"], "type": "string", "format": "enum"}, "State": {"type": "string", "format": "string"}, "IPV6-Address": {"type": "string", "format": "ipv6-address"}, "Type": {"enum": ["Incomplete", "Dynamic", "Static"], "type": "string", "format": "enum"}, "MAC-Address": {"minLength": 11, "maxLength": 17, "type": "string", "format": "mac-address"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.v6neighbor_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Dynamic(A10BaseClass):
    
    """Class Description::
    Operational Status for the object dynamic.

    Class dynamic supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/ipv6/neighbor/dynamic/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "dynamic"
        self.a10_url="/axapi/v3/ipv6/neighbor/dynamic/oper"
        self.DeviceProxy = ""
        self.oper = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


