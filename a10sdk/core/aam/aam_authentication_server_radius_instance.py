from a10sdk.common.A10BaseClass import A10BaseClass


class Host(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param hostipv6: {"not": "hostip", "type": "string", "description": "Server's IPV6 address", "format": "ipv6-address"}
    :param hostip: {"description": "Server's hostname(Length 1-31) or IP address", "format": "host", "minLength": 1, "maxLength": 31, "not": "hostipv6", "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "host"
        self.DeviceProxy = ""
        self.hostipv6 = ""
        self.hostip = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Instance(A10BaseClass):
    
    """Class Description::
    Radius Authentication Server instance.

    Class instance supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param health_check_string: {"description": "Health monitor name", "format": "string", "minLength": 1, "optional": true, "maxLength": 31, "type": "string", "$ref": "/axapi/v3/health/monitor"}
    :param retry: {"description": "Specify the retry number for resend the request, default is 5 (The retry number, default is 5)", "format": "number", "default": 5, "optional": true, "maximum": 32, "minimum": 1, "type": "number"}
    :param port_hm: {"description": "Check port's health status", "format": "string", "minLength": 1, "optional": true, "maxLength": 31, "not": "port-hm-disable", "type": "string", "$ref": "/axapi/v3/health/monitor"}
    :param name: {"description": "Specify RADIUS authentication server name", "format": "string-rlx", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param port_hm_disable: {"description": "Disable configured port health check configuration", "format": "flag", "default": 0, "optional": true, "not": "port-hm", "type": "number"}
    :param encrypted: {"optional": true, "type": "encrypted", "description": "Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED secret string)", "format": "encrypted"}
    :param interval: {"description": "Specify the interval time for resend the request (second), default is 3 seconds (The interval time(second), default is 3 seconds)", "format": "number", "default": 3, "optional": true, "maximum": 1024, "minimum": 1, "type": "number"}
    :param secret: {"default": 0, "optional": true, "type": "number", "description": "Specify the RADIUS server's secret", "format": "flag"}
    :param health_check: {"description": "Check server's health status", "format": "flag", "default": 0, "optional": true, "not": "health-check-disable", "type": "number"}
    :param health_check_disable: {"description": "Disable configured health check configuration", "format": "flag", "default": 0, "optional": true, "not": "health-check", "type": "number"}
    :param port: {"description": "Specify the RADIUS server's authentication port, default is 1812", "format": "number", "default": 1812, "optional": true, "maximum": 65535, "minimum": 1, "type": "number"}
    :param secret_string: {"description": "The RADIUS server's secret", "format": "password", "minLength": 1, "optional": true, "maxLength": 128, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/aam/authentication/server/radius/instance/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "instance"
        self.a10_url="/axapi/v3/aam/authentication/server/radius/instance/{name}"
        self.DeviceProxy = ""
        self.health_check_string = ""
        self.retry = ""
        self.port_hm = ""
        self.name = ""
        self.port_hm_disable = ""
        self.encrypted = ""
        self.interval = ""
        self.secret = ""
        self.health_check = ""
        self.host = {}
        self.health_check_disable = ""
        self.port = ""
        self.secret_string = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


