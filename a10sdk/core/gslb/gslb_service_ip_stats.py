from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param hits: {"description": "Number of times the service IP has been selected", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}
    :param recent: {"description": "Recent hits", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "8"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.hits = ""
        self.recent = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class ServiceIp(A10BaseClass):
    
    """Class Description::
    Statistics for the object service-ip.

    Class service-ip supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param node_name: {"description": "Service-IP Name", "format": "string", "minLength": 1, "oid": "1001", "optional": false, "maxLength": 63, "type": "string"}
    :param port_list: {"minItems": 1, "items": {"type": "port"}, "uniqueItems": true, "array": [{"required": ["port-num", "port-proto"], "properties": {"port-proto": {"enum": ["tcp", "udp"], "description": "'tcp': TCP Port; 'udp': UDP Port; ", "format": "enum", "type": "string", "oid": "1002", "optional": false}, "stats": {"type": "object", "properties": {"active": {"description": "Active Servers", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}, "current": {"description": "Current Connections", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "8"}}}, "port-num": {"description": "Port Number", "format": "number", "optional": false, "oid": "1001", "maximum": 65534, "minimum": 0, "type": "number"}}}], "type": "array", "$ref": "/axapi/v3/gslb/service-ip/{node-name}/port/{port-num}+{port-proto}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/gslb/service-ip/{node_name}/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "node_name"]

        self.b_key = "service-ip"
        self.a10_url="/axapi/v3/gslb/service-ip/{node_name}/stats"
        self.DeviceProxy = ""
        self.node_name = ""
        self.port_list = []
        self.stats = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


