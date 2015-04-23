from a10sdk.common.A10BaseClass import A10BaseClass


class SamplingEnable(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param counters1: {"enum": ["all", "Request-send", "Response-get", "Timeout-error", "Other-error"], "type": "string", "description": "'all': all; 'Request-send': Total Request Send; 'Response-get': Total Response Get; 'Timeout-error': Total Timeout; 'Other-error': Total Other Error; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "sampling-enable"
        self.DeviceProxy = ""
        self.counters1 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Kerberos(A10BaseClass):
    
    """    :param sampling_enable: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "Request-send", "Response-get", "Timeout-error", "Other-error"], "type": "string", "description": "'all': all; 'Request-send': Total Request Send; 'Response-get': Total Response Get; 'Timeout-error': Total Timeout; 'Other-error': Total Other Error; ", "format": "enum"}}}]}
    :param instance_list: {"minItems": 1, "items": {"type": "instance"}, "uniqueItems": true, "array": [{"required": ["name"], "properties": {"kerberos-account": {"description": "Specify the kerberos account name", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 127, "type": "string"}, "name": {"description": "Specify Kerberos authentication relay name", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}, "encrypted": {"optional": true, "type": "encrypted", "description": "Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED secret string)", "format": "encrypted"}, "kerberos-realm": {"description": "Specify the kerberos realm", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}, "kerberos-kdc-service-group": {"description": "Specify an authentication service group as multiple KDCs", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 127, "not": "kerberos-kdc", "type": "string", "$ref": "/axapi/v3/aam/authentication/service-group"}, "timeout": {"description": "Specify timeout for kerberos transport, default is 10 seconds (The timeout, default is 10 seconds)", "format": "number", "default": 10, "optional": true, "maximum": 255, "minimum": 1, "type": "number"}, "password": {"default": 0, "optional": true, "type": "number", "description": "Specify password of Kerberos password", "format": "flag"}, "kerberos-kdc": {"description": "Specify the kerberos kdc ip or host name", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "not": "kerberos-kdc-service-group", "type": "string"}, "port": {"description": "Specify The KDC port, default is 88", "format": "number", "default": 88, "optional": true, "maximum": 65535, "minimum": 1, "type": "number"}, "secret-string": {"description": "The kerberos client password", "format": "password", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/aam/authentication/relay/kerberos/instance/{name}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Kerberos Authentication Relay.

    Class kerberos supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/aam/authentication/relay/kerberos`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "kerberos"
        self.a10_url="/axapi/v3/aam/authentication/relay/kerberos"
        self.DeviceProxy = ""
        self.sampling_enable = []
        self.instance_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


