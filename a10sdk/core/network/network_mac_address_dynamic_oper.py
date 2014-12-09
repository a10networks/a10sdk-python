from a10sdk.common.A10BaseClass import A10BaseClass


class Macoper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param Index: {"type": "number", "format": "number"}
    :param Age: {"type": "number", "format": "number"}
    :param Vlan: {"minimum": 1, "type": "number", "maximum": 4094, "format": "number"}
    :param Port: {"type": "number", "format": "number"}
    :param Type: {"enum": ["Dynamic", "Static"], "type": "string", "format": "enum"}
    :param MAC_Address: {"minLength": 11, "maxLength": 17, "type": "string", "format": "mac-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "macoper"
        self.DeviceProxy = ""
        self.Index = ""
        self.Age = ""
        self.Vlan = ""
        self.Port = ""
        self.Type = ""
        self.MAC_Address = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param Age_time: {"type": "number", "format": "number"}
    :param macoper: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"Index": {"type": "number", "format": "number"}, "optional": true, "Age": {"type": "number", "format": "number"}, "Vlan": {"minimum": 1, "type": "number", "maximum": 4094, "format": "number"}, "Port": {"type": "number", "format": "number"}, "Type": {"enum": ["Dynamic", "Static"], "type": "string", "format": "enum"}, "MAC-Address": {"minLength": 11, "maxLength": 17, "type": "string", "format": "mac-address"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.Age_time = ""
        self.macoper = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Dynamic(A10BaseClass):
    
    """Class Description::
    Operational Status for the object dynamic.

    Class dynamic supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/network/mac-address/dynamic/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "dynamic"
        self.a10_url="/axapi/v3/network/mac-address/dynamic/oper"
        self.DeviceProxy = ""
        self.oper = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


