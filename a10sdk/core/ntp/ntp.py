from a10sdk.common.A10BaseClass import A10BaseClass


class Ntp(A10BaseClass):
    
    """Class Description::
    Network Time Protocol configuration.

    Class ntp supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param auth_key_list: {"minItems": 1, "items": {"type": "auth-key"}, "uniqueItems": true, "array": [{"required": ["key"], "properties": {"uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}, "encrypted": {"not": "hex-encrypted", "optional": true, "type": "encrypted", "description": "Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED password string)", "format": "encrypted"}, "key-type": {"optional": true, "enum": ["ascii", "hex"], "type": "string", "description": "'ascii': key string in ASCII form; 'hex': key string in hex form; ", "format": "enum"}, "hex-encrypted": {"not": "encrypted", "optional": true, "type": "encrypted", "description": "Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED password string)", "format": "encrypted"}, "hex-key": {"format": "password", "minLength": 21, "optional": true, "maxLength": 40, "not": "asc-key", "type": "string"}, "alg-type": {"optional": true, "enum": ["M", "SHA", "SHA1"], "type": "string", "description": "'M': encryption using MD5; 'SHA': encryption using SHA; 'SHA1': encryption using SHA1; ", "format": "enum"}, "key": {"description": "authentication key", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": false}, "asc-key": {"format": "password", "minLength": 1, "optional": true, "maxLength": 20, "not": "hex-key", "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/ntp/auth-key/{key}"}
    :param trusted_key_list: {"minItems": 1, "items": {"type": "trusted-key"}, "uniqueItems": true, "array": [{"required": ["key"], "properties": {"uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}, "key": {"description": "trusted key", "format": "number", "optional": false, "maximum": 65535, "minimum": 1, "type": "number", "$ref": "/axapi/v3/ntp/auth-key"}}}], "type": "array", "$ref": "/axapi/v3/ntp/trusted-key/{key}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/ntp`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "ntp"
        self.a10_url="/axapi/v3/ntp"
        self.DeviceProxy = ""
        self.auth_key_list = []
        self.trusted_key_list = []
        self.server = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


