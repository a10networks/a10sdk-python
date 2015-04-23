from a10sdk.common.A10BaseClass import A10BaseClass


class SamplingEnable(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param counters1: {"enum": ["all", "Authen_success", "Authen_failure", "Authorize_success", "Authorize_failure", "Access_challenge", "Timeout_error", "Other_error", "Request"], "type": "string", "description": "'all': all; 'Authen_success': Total Authentication Success; 'Authen_failure': Total Authentication Failure; 'Authorize_success': Total Authorization Success; 'Authorize_failure': Total Authorization Failure; 'Access_challenge': Total Access-Challenge Message Receive; 'Timeout_error': Total Timeout; 'Other_error': Total Other Error; 'Request': Total Request; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "sampling-enable"
        self.DeviceProxy = ""
        self.counters1 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Radius(A10BaseClass):
    
    """    :param sampling_enable: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "Authen_success", "Authen_failure", "Authorize_success", "Authorize_failure", "Access_challenge", "Timeout_error", "Other_error", "Request"], "type": "string", "description": "'all': all; 'Authen_success': Total Authentication Success; 'Authen_failure': Total Authentication Failure; 'Authorize_success': Total Authorization Success; 'Authorize_failure': Total Authorization Failure; 'Access_challenge': Total Access-Challenge Message Receive; 'Timeout_error': Total Timeout; 'Other_error': Total Other Error; 'Request': Total Request; ", "format": "enum"}}}]}
    :param instance_list: {"minItems": 1, "items": {"type": "instance"}, "uniqueItems": true, "array": [{"required": ["name"], "properties": {"health-check-string": {"description": "Health monitor name", "format": "string", "minLength": 1, "optional": true, "maxLength": 31, "type": "string", "$ref": "/axapi/v3/health/monitor"}, "retry": {"description": "Specify the retry number for resend the request, default is 5 (The retry number, default is 5)", "format": "number", "default": 5, "optional": true, "maximum": 32, "minimum": 1, "type": "number"}, "port-hm": {"description": "Check port's health status", "format": "string", "minLength": 1, "optional": true, "maxLength": 31, "not": "port-hm-disable", "type": "string", "$ref": "/axapi/v3/health/monitor"}, "name": {"description": "Specify RADIUS authentication server name", "format": "string-rlx", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}, "port-hm-disable": {"description": "Disable configured port health check configuration", "format": "flag", "default": 0, "optional": true, "not": "port-hm", "type": "number"}, "encrypted": {"optional": true, "type": "encrypted", "description": "Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED secret string)", "format": "encrypted"}, "interval": {"description": "Specify the interval time for resend the request (second), default is 3 seconds (The interval time(second), default is 3 seconds)", "format": "number", "default": 3, "optional": true, "maximum": 1024, "minimum": 1, "type": "number"}, "secret": {"default": 0, "optional": true, "type": "number", "description": "Specify the RADIUS server's secret", "format": "flag"}, "health-check": {"description": "Check server's health status", "format": "flag", "default": 0, "optional": true, "not": "health-check-disable", "type": "number"}, "host": {"type": "object", "properties": {"hostipv6": {"not": "hostip", "type": "string", "description": "Server's IPV6 address", "format": "ipv6-address"}, "hostip": {"description": "Server's hostname(Length 1-31) or IP address", "format": "host", "minLength": 1, "maxLength": 31, "not": "hostipv6", "type": "string"}}}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}, "health-check-disable": {"description": "Disable configured health check configuration", "format": "flag", "default": 0, "optional": true, "not": "health-check", "type": "number"}, "port": {"description": "Specify the RADIUS server's authentication port, default is 1812", "format": "number", "default": 1812, "optional": true, "maximum": 65534, "minimum": 1, "type": "number"}, "secret-string": {"description": "The RADIUS server's secret", "format": "password", "minLength": 1, "optional": true, "maxLength": 128, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/aam/authentication/server/radius/instance/{name}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    RADIUS Authentication Server.

    Class radius supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/aam/authentication/server/radius`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "radius"
        self.a10_url="/axapi/v3/aam/authentication/server/radius"
        self.DeviceProxy = ""
        self.sampling_enable = []
        self.instance_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


