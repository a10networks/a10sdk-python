from a10sdk.common.A10BaseClass import A10BaseClass


class Instance(A10BaseClass):
    
    """Class Description::
    Specify OCSP authentication server name.

    Class instance supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param health_check_string: {"description": "Health monitor name", "format": "string", "minLength": 1, "optional": true, "maxLength": 31, "type": "string", "$ref": "/axapi/v3/health/monitor"}
    :param responder_cert: {"description": "Specify the trusted OCSP responder's cert filename", "format": "string", "minLength": 1, "optional": true, "maxLength": 255, "type": "string"}
    :param name: {"description": "Specify OCSP authentication server name", "format": "string-rlx", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param url: {"description": "Specify the OCSP server's address (Format: http://host[:port]/) (The OCSP server's address(Format: http://host[:port]/))", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 255, "type": "string"}
    :param responder_ca: {"description": "Specify the trusted OCSP responder's CA cert filename", "format": "string", "minLength": 1, "optional": true, "maxLength": 255, "type": "string"}
    :param health_check_disable: {"description": "Disable configured health check configuration", "format": "flag", "default": 0, "optional": true, "not": "health-check", "type": "number"}
    :param port_health_check_disable: {"description": "Disable configured port health check configuration", "format": "flag", "default": 0, "optional": true, "not": "port-health-check", "type": "number"}
    :param port_health_check: {"description": "Check port's health status", "format": "string", "minLength": 1, "optional": true, "maxLength": 31, "not": "port-health-check-disable", "type": "string", "$ref": "/axapi/v3/health/monitor"}
    :param health_check: {"description": "Check server's health status", "format": "flag", "default": 0, "optional": true, "not": "health-check-disable", "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/aam/authentication/server/ocsp/instance/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "instance"
        self.a10_url="/axapi/v3/aam/authentication/server/ocsp/instance/{name}"
        self.DeviceProxy = ""
        self.health_check_string = ""
        self.responder_cert = ""
        self.name = ""
        self.url = ""
        self.responder_ca = ""
        self.health_check_disable = ""
        self.port_health_check_disable = ""
        self.port_health_check = ""
        self.health_check = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


