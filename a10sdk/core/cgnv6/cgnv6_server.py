from a10sdk.common.A10BaseClass import A10BaseClass


class Server(A10BaseClass):
    
    """Class Description::
    CGNV6 logging Server.

    Class server supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param health_check_disable: {"description": "Disable configured health check configuration", "format": "flag", "default": 0, "optional": true, "not": "health-check", "type": "number"}
    :param port_list: {"minItems": 1, "items": {"type": "port"}, "uniqueItems": true, "array": [{"required": ["port-number", "protocol"], "properties": {"action": {"description": "'enable': enable; 'disable': disable; ", "format": "enum", "default": "enable", "type": "string", "enum": ["enable", "disable"], "optional": true}, "health-check-disable": {"description": "Disable health check", "format": "flag", "default": 0, "optional": true, "not": "health-check", "type": "number"}, "protocol": {"optional": false, "enum": ["tcp", "udp"], "type": "string", "description": "'tcp': TCP Port; 'udp': UDP Port; ", "format": "enum"}, "health-check": {"description": "Health Check (Monitor Name)", "format": "string", "minLength": 1, "optional": true, "maxLength": 31, "not": "health-check-disable", "type": "string", "$ref": "/axapi/v3/health/monitor"}, "port-number": {"description": "Port Number", "format": "number", "type": "number", "maximum": 65534, "minimum": 0, "optional": false}}}], "type": "array", "$ref": "/axapi/v3/cgnv6/server/{name}/port/{port-number}+{protocol}"}
    :param name: {"description": "Server Name", "format": "string-rlx", "minLength": 1, "optional": false, "maxLength": 127, "type": "string"}
    :param fqdn_name: {"description": "Server hostname", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param host: {"optional": true, "modify-not-allowed": 1, "type": "string", "description": "IP Address", "format": "ipv4-address"}
    :param action: {"description": "'enable': Enable this Real Server; 'disable': Disable this Real Server; ", "format": "enum", "default": "enable", "type": "string", "enum": ["enable", "disable"], "optional": true}
    :param server_ipv6_addr: {"optional": true, "modify-not-allowed": 1, "type": "string", "description": "IPV6 address", "format": "ipv6-address"}
    :param health_check: {"description": "Health Check Monitor (Health monitor name)", "format": "string", "minLength": 1, "optional": true, "maxLength": 31, "not": "health-check-disable", "type": "string", "$ref": "/axapi/v3/health/monitor"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/server/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "server"
        self.a10_url="/axapi/v3/cgnv6/server/{name}"
        self.DeviceProxy = ""
        self.health_check_disable = ""
        self.port_list = []
        self.name = ""
        self.fqdn_name = ""
        self.host = ""
        self.action = ""
        self.server_ipv6_addr = ""
        self.health_check = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


