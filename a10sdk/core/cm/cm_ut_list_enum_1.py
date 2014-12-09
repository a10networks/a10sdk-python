from a10sdk.common.A10BaseClass import A10BaseClass


class List(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param a1: {"minimum": 1, "type": "number", "maximum": 10, "format": "number"}
    :param a2: {"minLength": 1, "maxLength": 32, "type": "string", "description": "other fields for choice of a", "format": "string"}
    :param b1: {"minLength": 1, "maxLength": 32, "type": "string", "format": "string"}
    :param b2: {"description": "other fields for choice of b", "minimum": 1, "type": "number", "maximum": 100, "format": "number"}
    :param c2: {"type": "string", "description": "a compound key for choice of c", "format": "ipv4-netmask"}
    :param c3: {"minLength": 1, "maxLength": 128, "type": "string", "description": "other field for choice of c", "format": "string"}
    :param entry: {"enum": ["a", "b", "c"], "type": "string", "description": "a: \"a\"; b: \"b\"; c: \"c\"; ", "format": "enum"}
    :param c1: {"type": "string", "format": "ipv4-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "list"
        self.DeviceProxy = ""
        self.a1 = ""
        self.a2 = ""
        self.b1 = ""
        self.b2 = ""
        self.c2 = ""
        self.c3 = ""
        self.entry = ""
        self.c1 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class ListEnum1(A10BaseClass):
    
    """Class Description::
    Unit test CM list with different types of entries.

    Class list-enum-1 supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"a1": {"minimum": 1, "type": "number", "maximum": 10, "format": "number"}, "a2": {"minLength": 1, "maxLength": 32, "type": "string", "description": "other fields for choice of a", "format": "string"}, "b1": {"minLength": 1, "maxLength": 32, "type": "string", "format": "string"}, "b2": {"description": "other fields for choice of b", "minimum": 1, "type": "number", "maximum": 100, "format": "number"}, "c2": {"type": "string", "description": "a compound key for choice of c", "format": "ipv4-netmask"}, "c3": {"minLength": 1, "maxLength": 128, "type": "string", "description": "other field for choice of c", "format": "string"}, "entry": {"enum": ["a", "b", "c"], "type": "string", "description": "a: \"a\"; b: \"b\"; c: \"c\"; ", "format": "enum"}, "c1": {"type": "string", "format": "ipv4-address"}, "optional": true}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cm-ut/list-enum-1`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "list-enum-1"
        self.a10_url="/axapi/v3/cm-ut/list-enum-1"
        self.DeviceProxy = ""
        self.A10WW_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


