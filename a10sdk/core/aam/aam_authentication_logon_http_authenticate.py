from a10sdk.common.A10BaseClass import A10BaseClass


class HttpAuthenticate(A10BaseClass):
    
    """    :param instance_list: {"minItems": 1, "items": {"type": "instance"}, "uniqueItems": true, "array": [{"required": ["name"], "properties": {"uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}, "retry": {"description": "Specify max. number of failure retry (1 ~ 32), default is 3", "format": "number", "default": 3, "optional": true, "maximum": 32, "minimum": 1, "type": "number"}, "name": {"description": "Specify HTTP-Authenticate logon name", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}, "auth-method": {"type": "object", "properties": {"ntlm": {"type": "object", "properties": {"ntlm-enable": {"default": 0, "type": "number", "description": "Enable NTLM logon", "format": "flag"}}}, "negotiate": {"type": "object", "properties": {"negotiate-enable": {"default": 0, "type": "number", "description": "Enable SPENGO logon", "format": "flag"}}}, "basic": {"type": "object", "properties": {"new-pin-page": {"minLength": 1, "maxLength": 63, "type": "string", "description": "Specify new PIN page name for RSA-RADIUS", "format": "string-rlx"}, "basic-enable": {"default": 0, "type": "number", "description": "Enable Basic logon", "format": "flag"}, "next-token-variable": {"minLength": 1, "maxLength": 63, "type": "string", "description": "Specify next-token variable name", "format": "string-rlx"}, "next-token-page": {"minLength": 1, "maxLength": 63, "type": "string", "description": "Specify next-token page name for RSA-RADIUS", "format": "string-rlx"}, "basic-realm": {"minLength": 1, "maxLength": 128, "type": "string", "description": "Specify realm for basic logon", "format": "string-rlx"}, "new-pin-variable": {"minLength": 1, "maxLength": 63, "type": "string", "description": "Specify new PIN variable name", "format": "string-rlx"}, "challenge-response-form": {"minLength": 1, "maxLength": 63, "type": "string", "description": "Specify challenge-response form for RSA-RADIUS authentication", "format": "string"}}}}}}}], "type": "array", "$ref": "/axapi/v3/aam/authentication/logon/http-authenticate/instance/{name}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    HTTP-authenticate Logon.

    Class http-authenticate supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/aam/authentication/logon/http-authenticate`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "http-authenticate"
        self.a10_url="/axapi/v3/aam/authentication/logon/http-authenticate"
        self.DeviceProxy = ""
        self.instance_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


