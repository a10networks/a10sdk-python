from a10sdk.common.A10BaseClass import A10BaseClass


class Port(A10BaseClass):
    
    """Class Description::
    Real Server Port.

    Class port supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param action: {"description": "'enable': enable; 'disable': disable; ", "format": "enum", "default": "enable", "type": "string", "enum": ["enable", "disable"], "optional": true}
    :param health_check_disable: {"description": "Disable health check", "format": "flag", "default": 0, "optional": true, "not": "health-check", "type": "number"}
    :param protocol: {"optional": false, "enum": ["tcp", "udp"], "type": "string", "description": "'tcp': TCP Port; 'udp': UDP Port; ", "format": "enum"}
    :param health_check: {"description": "Health Check (Monitor Name)", "format": "string", "minLength": 1, "optional": true, "maxLength": 31, "not": "health-check-disable", "type": "string", "$ref": "/axapi/v3/health/monitor"}
    :param port_number: {"description": "Port Number", "format": "number", "type": "number", "maximum": 65534, "minimum": 0, "optional": false}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/server/{name}/port/{port_number}+{protocol}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "port_number","protocol"]

        self.b_key = "port"
        self.a10_url="/axapi/v3/cgnv6/server/{name}/port/{port_number}+{protocol}"
        self.DeviceProxy = ""
        self.action = ""
        self.health_check_disable = ""
        self.protocol = ""
        self.health_check = ""
        self.port_number = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


