from a10sdk.common.A10BaseClass import A10BaseClass


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param use_gslb_state: {"type": "number", "format": "number"}
    :param gslb_protocol: {"type": "number", "format": "number"}
    :param ip: {"type": "string", "format": "string"}
    :param dynamic: {"type": "number", "format": "number"}
    :param manually_health_check: {"type": "number", "format": "number"}
    :param disabled: {"type": "number", "format": "number"}
    :param state: {"type": "string", "format": "string"}
    :param service_ip: {"type": "string", "format": "string"}
    :param port_count: {"type": "number", "format": "number"}
    :param local_protocol: {"type": "number", "format": "number"}
    :param virtual_server: {"type": "number", "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.use_gslb_state = ""
        self.gslb_protocol = ""
        self.ip = ""
        self.dynamic = ""
        self.manually_health_check = ""
        self.disabled = ""
        self.state = ""
        self.service_ip = ""
        self.port_count = ""
        self.local_protocol = ""
        self.virtual_server = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class ServiceIp(A10BaseClass):
    
    """Class Description::
    Operational Status for the object service-ip.

    Class service-ip supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param node_name: {"description": "Service-IP Name", "format": "string", "minLength": 1, "oid": "1001", "optional": false, "maxLength": 63, "type": "string"}
    :param port_list: {"minItems": 1, "items": {"type": "port"}, "uniqueItems": true, "array": [{"required": ["port-num", "port-proto"], "properties": {"oper": {"type": "object", "properties": {"use_gslb_state": {"type": "number", "format": "number"}, "gslb-protocol": {"type": "number", "format": "number"}, "service-port": {"type": "number", "format": "number"}, "dynamic": {"type": "number", "format": "number"}, "tcp": {"type": "number", "format": "number"}, "disabled": {"type": "number", "format": "number"}, "state": {"type": "string", "format": "string"}, "local-protocol": {"type": "number", "format": "number"}, "manually-health-check": {"type": "number", "format": "number"}}}, "port-proto": {"enum": ["tcp", "udp"], "description": "'tcp': TCP Port; 'udp': UDP Port; ", "format": "enum", "type": "string", "oid": "1002", "optional": false}, "port-num": {"description": "Port Number", "format": "number", "optional": false, "oid": "1001", "maximum": 65534, "minimum": 0, "type": "number"}}}], "type": "array", "$ref": "/axapi/v3/gslb/service-ip/{node-name}/port/{port-num}+{port-proto}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/gslb/service-ip/{node_name}/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "service-ip"
        self.a10_url="/axapi/v3/gslb/service-ip/{node_name}/oper"
        self.DeviceProxy = ""
        self.oper = {}
        self.node_name = ""
        self.port_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


