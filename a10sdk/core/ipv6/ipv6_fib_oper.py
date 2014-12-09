from a10sdk.common.A10BaseClass import A10BaseClass


class Ipv6Fib(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param Distance: {"type": "number", "format": "number"}
    :param Nexthop: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param Interface: {"enum": ["Management", "ethernet", "trunk"], "type": "string", "format": "enum"}
    :param Prefix: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param PrefixLen: {"type": "number", "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "IPv6-fib"
        self.DeviceProxy = ""
        self.Distance = ""
        self.Nexthop = ""
        self.Interface = ""
        self.Prefix = ""
        self.PrefixLen = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param Total: {"type": "number", "format": "number"}
    :param IPv6_fib: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"Distance": {"type": "number", "format": "number"}, "Nexthop": {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}, "Interface": {"enum": ["Management", "ethernet", "trunk"], "type": "string", "format": "enum"}, "Prefix": {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}, "PrefixLen": {"type": "number", "format": "number"}, "optional": true}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.Total = ""
        self.IPv6_fib = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Fib(A10BaseClass):
    
    """Class Description::
    Operational Status for the object fib.

    Class fib supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/ipv6/fib/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "fib"
        self.a10_url="/axapi/v3/ipv6/fib/oper"
        self.DeviceProxy = ""
        self.oper = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


