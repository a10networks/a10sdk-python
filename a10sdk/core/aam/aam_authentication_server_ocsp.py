from a10sdk.common.A10BaseClass import A10BaseClass


class Ocsp(A10BaseClass):
    
    """Class Description::
    OCSP Authentication Server.

    Class ocsp supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param instance_list: {"minItems": 1, "items": {"type": "instance"}, "uniqueItems": true, "array": [{"required": ["name"], "properties": {"health-check-string": {"description": "Health monitor name", "format": "string", "minLength": 1, "optional": true, "maxLength": 31, "type": "string", "$ref": "/axapi/v3/health/monitor"}, "responder-cert": {"description": "Specify the trusted OCSP responder's cert filename", "format": "string", "minLength": 1, "optional": true, "maxLength": 255, "type": "string"}, "name": {"description": "Specify OCSP authentication server name", "format": "string-rlx", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}, "url": {"description": "Specify the OCSP server's address (Format: http://host[:port]/) (The OCSP server's address(Format: http://host[:port]/))", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 255, "type": "string"}, "responder-ca": {"description": "Specify the trusted OCSP responder's CA cert filename", "format": "string", "minLength": 1, "optional": true, "maxLength": 255, "type": "string"}, "health-check-disable": {"description": "Disable configured health check configuration", "format": "flag", "default": 0, "optional": true, "not": "health-check", "type": "number"}, "port-health-check-disable": {"description": "Disable configured port health check configuration", "format": "flag", "default": 0, "optional": true, "not": "port-health-check", "type": "number"}, "port-health-check": {"description": "Check port's health status", "format": "string", "minLength": 1, "optional": true, "maxLength": 31, "not": "port-health-check-disable", "type": "string", "$ref": "/axapi/v3/health/monitor"}, "health-check": {"description": "Check server's health status", "format": "flag", "default": 0, "optional": true, "not": "health-check-disable", "type": "number"}}}], "type": "array", "$ref": "/axapi/v3/aam/authentication/server/ocsp/instance/{name}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/aam/authentication/server/ocsp`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "ocsp"
        self.a10_url="/axapi/v3/aam/authentication/server/ocsp"
        self.DeviceProxy = ""
        self.instance_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


