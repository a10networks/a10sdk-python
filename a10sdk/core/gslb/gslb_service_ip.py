from a10sdk.common.A10BaseClass import A10BaseClass


class SamplingEnable(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param counters1: {"enum": ["all", "hits", "recent"], "type": "string", "description": "'all': all; 'hits': Number of times the service IP has been selected; 'recent': Recent hits; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "sampling-enable"
        self.DeviceProxy = ""
        self.counters1 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class ServiceIp(A10BaseClass):
    
    """Class Description::
    Service IP.

    Class service-ip supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param health_check_disable: {"description": "Disable Health Check Monitor", "format": "flag", "default": 0, "optional": true, "not": "health-check", "type": "number"}
    :param port_list: {"minItems": 1, "items": {"type": "port"}, "uniqueItems": true, "array": [{"required": ["port-num", "port-proto"], "properties": {"port-proto": {"optional": false, "enum": ["tcp", "udp"], "type": "string", "description": "'tcp': TCP Port; 'udp': UDP Port; ", "format": "enum"}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}, "port-num": {"description": "Port Number", "format": "number", "type": "number", "maximum": 65534, "minimum": 0, "optional": false}, "health-check-disable": {"description": "Disable Health Check Monitor", "format": "flag", "default": 0, "optional": true, "not-list": ["health-check", "health-check-follow-port"], "type": "number"}, "follow-port-protocol": {"optional": true, "enum": ["tcp", "udp"], "type": "string", "description": "'tcp': TCP Port; 'udp': UDP Port; ", "format": "enum"}, "sampling-enable": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "active", "current"], "type": "string", "description": "'all': all; 'active': Active Servers; 'current': Current Connections; ", "format": "enum"}}}]}, "action": {"description": "'enable': Enable this GSLB server port; 'disable': Disable this GSLB server port; ", "format": "enum", "default": "enable", "type": "string", "enum": ["enable", "disable"], "optional": true}, "health-check-follow-port": {"description": "Specify which port to follow for health status (Port Number)", "format": "number", "optional": true, "not-list": ["health-check", "health-check-disable"], "maximum": 65534, "minimum": 1, "type": "number"}, "health-check-protocol-disable": {"default": 0, "optional": true, "type": "number", "description": "Disable GSLB Protocol Health Monitor", "format": "flag"}, "health-check": {"description": "Health Check Monitor (Monitor Name)", "format": "string", "minLength": 1, "not-list": ["health-check-follow-port", "health-check-disable"], "optional": true, "maxLength": 31, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/gslb/service-ip/{node-name}/port/{port-num}+{port-proto}"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param external_ip: {"optional": true, "type": "string", "description": "External IP address for NAT", "format": "ipv4-address"}
    :param health_check: {"description": "Health Check Monitor (Monitor Name)", "format": "string", "minLength": 1, "optional": true, "maxLength": 31, "not": "health-check-disable", "type": "string"}
    :param node_name: {"description": "Service-IP Name", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param sampling_enable: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "hits", "recent"], "type": "string", "description": "'all': all; 'hits': Number of times the service IP has been selected; 'recent': Recent hits; ", "format": "enum"}}}]}
    :param ip_address: {"optional": true, "modify-not-allowed": 1, "type": "string", "description": "IP address", "format": "ipv4-address"}
    :param ipv6: {"optional": true, "type": "string", "description": "IPv6 address Mapping", "format": "ipv6-address"}
    :param ipv6_address: {"optional": true, "modify-not-allowed": 1, "type": "string", "description": "IPV6 address", "format": "ipv6-address"}
    :param health_check_protocol_disable: {"default": 0, "optional": true, "type": "number", "description": "Disable GSLB Protocol Health Monitor", "format": "flag"}
    :param action: {"description": "'enable': Enable this GSLB server; 'disable': Disable this GSLB server; ", "format": "enum", "default": "enable", "type": "string", "enum": ["enable", "disable"], "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/gslb/service-ip/{node_name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "node_name"]

        self.b_key = "service-ip"
        self.a10_url="/axapi/v3/gslb/service-ip/{node_name}"
        self.DeviceProxy = ""
        self.health_check_disable = ""
        self.port_list = []
        self.uuid = ""
        self.external_ip = ""
        self.health_check = ""
        self.node_name = ""
        self.sampling_enable = []
        self.ip_address = ""
        self.ipv6 = ""
        self.ipv6_address = ""
        self.health_check_protocol_disable = ""
        self.action = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


