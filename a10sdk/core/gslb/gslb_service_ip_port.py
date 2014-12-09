from a10sdk.common.A10BaseClass import A10BaseClass


class Port(A10BaseClass):
    
    """Class Description::
    Server Port.

    Class port supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param port_proto: {"optional": false, "enum": ["tcp", "udp"], "type": "string", "description": "'tcp': TCP Port; 'udp': UDP Port; ", "format": "enum"}
    :param port_num: {"description": "Port Number", "format": "number", "type": "number", "maximum": 65534, "minimum": 0, "optional": false}
    :param health_check_disable: {"description": "Disable Health Check Monitor", "format": "flag", "default": 0, "optional": true, "not-list": ["health-check", "health-check-follow-port"], "type": "number"}
    :param follow_port_protocol: {"optional": true, "enum": ["tcp", "udp"], "type": "string", "description": "'tcp': TCP Port; 'udp': UDP Port; ", "format": "enum"}
    :param action: {"description": "'enable': Enable this GSLB server port; 'disable': Disable this GSLB server port; ", "format": "enum", "default": "enable", "type": "string", "enum": ["enable", "disable"], "optional": true}
    :param health_check_follow_port: {"description": "Specify which port to follow for health status (Port Number)", "format": "number", "optional": true, "not-list": ["health-check", "health-check-disable"], "maximum": 65534, "minimum": 1, "type": "number"}
    :param health_check_protocol_disable: {"default": 0, "optional": true, "type": "number", "description": "Disable GSLB Protocol Health Monitor", "format": "flag"}
    :param health_check: {"description": "Health Check Monitor (Monitor Name)", "format": "string", "minLength": 1, "not-list": ["health-check-follow-port", "health-check-disable"], "optional": true, "maxLength": 31, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/gslb/service-ip/{node_name}/port/{port_num}+{port_proto}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "port_num","port_proto"]

        self.b_key = "port"
        self.a10_url="/axapi/v3/gslb/service-ip/{node_name}/port/{port_num}+{port_proto}"
        self.DeviceProxy = ""
        self.port_proto = ""
        self.port_num = ""
        self.health_check_disable = ""
        self.follow_port_protocol = ""
        self.action = ""
        self.health_check_follow_port = ""
        self.health_check_protocol_disable = ""
        self.health_check = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


