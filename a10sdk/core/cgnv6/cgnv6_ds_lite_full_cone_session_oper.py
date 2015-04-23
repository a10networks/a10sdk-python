from a10sdk.common.A10BaseClass import A10BaseClass


class SessionList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param protocol: {"type": "string", "format": "string"}
    :param inside_v6_address: {"type": "string", "format": "ipv6-address"}
    :param inbound: {"type": "number", "format": "number"}
    :param age: {"type": "string", "format": "string"}
    :param cpu: {"type": "number", "format": "number"}
    :param nat_address: {"type": "string", "format": "ipv4-address"}
    :param nat_port: {"type": "number", "format": "number"}
    :param flags: {"type": "string", "format": "string"}
    :param nat_pool_name: {"type": "string", "format": "string"}
    :param inside_port: {"type": "number", "format": "number"}
    :param outbound: {"type": "number", "format": "number"}
    :param inside_address: {"type": "string", "format": "ipv4-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "session-list"
        self.DeviceProxy = ""
        self.protocol = ""
        self.inside_v6_address = ""
        self.inbound = ""
        self.age = ""
        self.cpu = ""
        self.nat_address = ""
        self.nat_port = ""
        self.flags = ""
        self.nat_pool_name = ""
        self.inside_port = ""
        self.outbound = ""
        self.inside_address = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param all_paritions: {"enum": ["true"], "type": "string", "format": "enum"}
    :param partition: {"type": "string", "format": "string"}
    :param session_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"protocol": {"type": "string", "format": "string"}, "inside-v6-address": {"type": "string", "format": "ipv6-address"}, "inbound": {"type": "number", "format": "number"}, "age": {"type": "string", "format": "string"}, "cpu": {"type": "number", "format": "number"}, "nat-address": {"type": "string", "format": "ipv4-address"}, "nat-port": {"type": "number", "format": "number"}, "flags": {"type": "string", "format": "string"}, "nat-pool-name": {"type": "string", "format": "string"}, "inside-port": {"type": "number", "format": "number"}, "outbound": {"type": "number", "format": "number"}, "optional": true, "inside-address": {"type": "string", "format": "ipv4-address"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.all_paritions = ""
        self.partition = ""
        self.session_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class FullConeSession(A10BaseClass):
    
    """Class Description::
    Operational Status for the object full-cone-session.

    Class full-cone-session supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/ds-lite/full-cone-session/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "full-cone-session"
        self.a10_url="/axapi/v3/cgnv6/ds-lite/full-cone-session/oper"
        self.DeviceProxy = ""
        self.oper = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


