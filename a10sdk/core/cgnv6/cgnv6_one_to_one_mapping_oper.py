from a10sdk.common.A10BaseClass import A10BaseClass


class SessionMappingList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param sessions: {"type": "number", "format": "number"}
    :param age: {"type": "string", "format": "string"}
    :param nat_address: {"type": "string", "format": "ipv4-address"}
    :param inside_address: {"type": "string", "format": "ipv4-address"}
    :param pool: {"type": "string", "format": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "session-mapping-list"
        self.DeviceProxy = ""
        self.sessions = ""
        self.age = ""
        self.nat_address = ""
        self.inside_address = ""
        self.pool = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param session_mapping_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"sessions": {"type": "number", "format": "number"}, "age": {"type": "string", "format": "string"}, "nat-address": {"type": "string", "format": "ipv4-address"}, "optional": true, "inside-address": {"type": "string", "format": "ipv4-address"}, "pool": {"type": "string", "format": "string"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.session_mapping_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Mapping(A10BaseClass):
    
    """Class Description::
    Operational Status for the object mapping.

    Class mapping supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/one-to-one/mapping/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "mapping"
        self.a10_url="/axapi/v3/cgnv6/one-to-one/mapping/oper"
        self.DeviceProxy = ""
        self.oper = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


