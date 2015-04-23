from a10sdk.common.A10BaseClass import A10BaseClass


class SamplingEnable(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param counters1: {"enum": ["all", "Stapling-Certificate-Good", "Stapling-Certificate-Revoked", "Stapling-Certificate-Unknown"], "type": "string", "description": "'all': all; 'Stapling-Certificate-Good': Total OCSP Stapling Good Certificate Response; 'Stapling-Certificate-Revoked': Total OCSP Stapling Revoked Certificate Response; 'Stapling-Certificate-Unknown': Total OCSP Stapling Unknown Certificate Response; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "sampling-enable"
        self.DeviceProxy = ""
        self.counters1 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Ocsp(A10BaseClass):
    
    """    :param sampling_enable: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "Stapling-Certificate-Good", "Stapling-Certificate-Revoked", "Stapling-Certificate-Unknown"], "type": "string", "description": "'all': all; 'Stapling-Certificate-Good': Total OCSP Stapling Good Certificate Response; 'Stapling-Certificate-Revoked': Total OCSP Stapling Revoked Certificate Response; 'Stapling-Certificate-Unknown': Total OCSP Stapling Unknown Certificate Response; ", "format": "enum"}}}]}
    :param instance_list: {"minItems": 1, "items": {"type": "instance"}, "uniqueItems": true, "array": [{"required": ["name"], "properties": {"health-check-string": {"description": "Health monitor name", "format": "string", "minLength": 1, "optional": true, "maxLength": 31, "type": "string", "$ref": "/axapi/v3/health/monitor"}, "responder-cert": {"description": "Specify the trusted OCSP responder's cert filename", "format": "string", "minLength": 1, "optional": true, "maxLength": 255, "type": "string"}, "name": {"description": "Specify OCSP authentication server name", "format": "string-rlx", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}, "url": {"description": "Specify the OCSP server's address (Format: http://host[:port]/) (The OCSP server's address(Format: http://host[:port]/))", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 255, "type": "string"}, "responder-ca": {"description": "Specify the trusted OCSP responder's CA cert filename", "format": "string", "minLength": 1, "optional": true, "maxLength": 255, "type": "string"}, "health-check-disable": {"description": "Disable configured health check configuration", "format": "flag", "default": 0, "optional": true, "not": "health-check", "type": "number"}, "port-health-check-disable": {"description": "Disable configured port health check configuration", "format": "flag", "default": 0, "optional": true, "not": "port-health-check", "type": "number"}, "port-health-check": {"description": "Check port's health status", "format": "string", "minLength": 1, "optional": true, "maxLength": 31, "not": "port-health-check-disable", "type": "string", "$ref": "/axapi/v3/health/monitor"}, "health-check": {"description": "Check server's health status", "format": "flag", "default": 0, "optional": true, "not": "health-check-disable", "type": "number"}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/aam/authentication/server/ocsp/instance/{name}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    OCSP Authentication Server.

    Class ocsp supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/aam/authentication/server/ocsp`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "ocsp"
        self.a10_url="/axapi/v3/aam/authentication/server/ocsp"
        self.DeviceProxy = ""
        self.sampling_enable = []
        self.instance_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


