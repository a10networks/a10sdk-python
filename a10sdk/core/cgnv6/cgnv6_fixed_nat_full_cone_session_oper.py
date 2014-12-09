from a10sdk.common.A10BaseClass import A10BaseClass


class SessionList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param protocol: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param inside_v6_address: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param age: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param EIF: {"type": "number", "format": "number"}
    :param cpu: {"type": "number", "format": "number"}
    :param nat_address: {"type": "string", "format": "ipv4-address"}
    :param nat_port: {"type": "number", "format": "number"}
    :param flags: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param inside_port: {"type": "number", "format": "number"}
    :param EIM: {"type": "number", "format": "number"}
    :param inside_address: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "session-list"
        self.DeviceProxy = ""
        self.protocol = ""
        self.inside_v6_address = ""
        self.age = ""
        self.EIF = ""
        self.cpu = ""
        self.nat_address = ""
        self.nat_port = ""
        self.flags = ""
        self.inside_port = ""
        self.EIM = ""
        self.inside_address = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param session_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"protocol": {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}, "inside-v6-address": {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}, "optional": true, "age": {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}, "EIF": {"type": "number", "format": "number"}, "cpu": {"type": "number", "format": "number"}, "nat-address": {"type": "string", "format": "ipv4-address"}, "nat-port": {"type": "number", "format": "number"}, "flags": {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}, "inside-port": {"type": "number", "format": "number"}, "EIM": {"type": "number", "format": "number"}, "inside-address": {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}}}]}
    :param session_type: {"enum": ["nat44", "nat64", "ds-lite"], "type": "string", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.session_list = []
        self.session_type = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class FullConeSession(A10BaseClass):
    
    """Class Description::
    Operational Status for the object full-cone-session.

    Class full-cone-session supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/fixed-nat/full-cone-session/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "full-cone-session"
        self.a10_url="/axapi/v3/cgnv6/fixed-nat/full-cone-session/oper"
        self.DeviceProxy = ""
        self.oper = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


