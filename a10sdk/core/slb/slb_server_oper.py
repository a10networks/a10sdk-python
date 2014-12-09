from a10sdk.common.A10BaseClass import A10BaseClass


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param state: {"enum": ["UP", "DOWN", "DELETE", "DISABLED", "MAINTENANCE"], "type": "string", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.state = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Server(A10BaseClass):
    
    """Class Description::
    Operational Status for the object server.

    Class server supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param port_list: {"minItems": 1, "items": {"type": "port"}, "uniqueItems": true, "array": [{"required": ["port-number", "protocol"], "properties": {"oper": {"type": "object", "properties": {"alloc_failed": {"type": "number", "format": "number"}, "vrid": {"enum": ["default"], "type": "string", "format": "enum"}, "ha_group_id": {"enum": ["default"], "type": "string", "format": "enum"}, "ip": {"type": "string", "format": "ipv4-address"}, "ports_consumed": {"type": "number", "format": "number"}, "state": {"enum": ["UP", "DOWN", "DELETE", "DISABLED", "MAINTENANCE"], "type": "string", "format": "enum"}, "ipv6": {"type": "string", "format": "ipv6-address"}, "ports_freed_total": {"type": "number", "format": "number"}, "ports_consumed_total": {"type": "number", "format": "number"}}}, "protocol": {"enum": ["tcp", "udp"], "description": "'tcp': TCP Port; 'udp': UDP Port; ", "format": "enum", "type": "string", "oid": "1002", "optional": false}, "port-number": {"description": "Port Number", "format": "number", "optional": false, "oid": "1001", "maximum": 65534, "minimum": 0, "type": "number"}}}], "type": "array", "$ref": "/axapi/v3/slb/server/{name}/port/{port-number}+{protocol}"}
    :param name: {"description": "Server Name", "format": "string-rlx", "minLength": 1, "oid": "1001", "optional": false, "maxLength": 127, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/server/{name}/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "server"
        self.a10_url="/axapi/v3/slb/server/{name}/oper"
        self.DeviceProxy = ""
        self.oper = {}
        self.port_list = []
        self.name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


