from a10sdk.common.A10BaseClass import A10BaseClass


class TrunkMember(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param members: {"type": "number", "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "trunk-member"
        self.DeviceProxy = ""
        self.members = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param Hardware: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param trunk_member: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "members": {"type": "number", "format": "number"}}}]}
    :param state: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param line_protocol: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param Address: {"minLength": 11, "maxLength": 17, "type": "string", "format": "mac-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.Hardware = ""
        self.trunk_member = []
        self.state = ""
        self.line_protocol = ""
        self.Address = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Router(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "router"
        self.DeviceProxy = ""
        self.oper = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Ospf(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ospf"
        self.DeviceProxy = ""
        self.oper = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Ip(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ip"
        self.DeviceProxy = ""
        self.oper = {}
        self.router = {}
        self.ospf = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Router(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "router"
        self.DeviceProxy = ""
        self.oper = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Ipv6(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ipv6"
        self.DeviceProxy = ""
        self.oper = {}
        self.router = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Trunk(A10BaseClass):
    
    """Class Description::
    Operational Status for the object trunk.

    Class trunk supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param ifnum: {"optional": false, "oid": "1001", "type": "number", "description": "Trunk interface number", "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/interface/trunk/{ifnum}/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "trunk"
        self.a10_url="/axapi/v3/interface/trunk/{ifnum}/oper"
        self.DeviceProxy = ""
        self.oper = {}
        self.ip = {}
        self.ifnum = ""
        self.ipv6 = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


