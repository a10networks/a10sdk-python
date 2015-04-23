from a10sdk.common.A10BaseClass import A10BaseClass


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param state: {"enum": ["All Up", "Functional Up", "Partial Up", "Down", "Disabled", "Unknown"], "type": "string", "format": "enum"}
    :param servers_down: {"type": "number", "format": "number"}
    :param servers_up: {"type": "number", "format": "number"}
    :param servers_disable: {"type": "number", "format": "number"}
    :param servers_total: {"type": "number", "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.state = ""
        self.servers_down = ""
        self.servers_up = ""
        self.servers_disable = ""
        self.servers_total = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class ServiceGroup(A10BaseClass):
    
    """Class Description::
    Operational Status for the object service-group.

    Class service-group supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param member_list: {"minItems": 1, "items": {"type": "member"}, "uniqueItems": true, "array": [{"required": ["name", "port"], "properties": {"oper": {"type": "object", "properties": {"state": {"enum": ["UP", "DOWN", "MAINTENANCE"], "type": "string", "format": "enum"}}}, "name": {"description": "Member name", "format": "comp-string", "minLength": 1, "oid": "1001", "optional": false, "maxLength": 127, "type": "string"}, "port": {"description": "Port number", "format": "number", "default": 65534, "optional": false, "oid": "1002", "maximum": 65534, "minimum": 0, "type": "number"}}}], "type": "array", "$ref": "/axapi/v3/cgnv6/service-group/{name}/member/{name}+{port}"}
    :param name: {"description": "CGNV6 Service Name", "format": "string-rlx", "minLength": 1, "oid": "1001", "optional": false, "maxLength": 127, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/service-group/{name}/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "service-group"
        self.a10_url="/axapi/v3/cgnv6/service-group/{name}/oper"
        self.DeviceProxy = ""
        self.oper = {}
        self.member_list = []
        self.name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


