from a10sdk.common.A10BaseClass import A10BaseClass


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param use_gslb_state: {"type": "number", "format": "number"}
    :param gslb_protocol: {"type": "number", "format": "number"}
    :param service_port: {"type": "number", "format": "number"}
    :param dynamic: {"type": "number", "format": "number"}
    :param tcp: {"type": "number", "format": "number"}
    :param disabled: {"type": "number", "format": "number"}
    :param state: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param local_protocol: {"type": "number", "format": "number"}
    :param manually_health_check: {"type": "number", "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.use_gslb_state = ""
        self.gslb_protocol = ""
        self.service_port = ""
        self.dynamic = ""
        self.tcp = ""
        self.disabled = ""
        self.state = ""
        self.local_protocol = ""
        self.manually_health_check = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Port(A10BaseClass):
    
    """Class Description::
    Operational Status for the object port.

    Class port supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param port_proto: {"enum": ["tcp", "udp"], "description": "'tcp': TCP Port; 'udp': UDP Port; ", "format": "enum", "type": "string", "oid": "1002", "optional": false}
    :param port_num: {"description": "Port Number", "format": "number", "optional": false, "oid": "1001", "maximum": 65534, "minimum": 0, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/gslb/service-ip/{node_name}/port/{port_num}+{port_proto}/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "port"
        self.a10_url="/axapi/v3/gslb/service-ip/{node_name}/port/{port_num}+{port_proto}/oper"
        self.DeviceProxy = ""
        self.oper = {}
        self.port_proto = ""
        self.port_num = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


