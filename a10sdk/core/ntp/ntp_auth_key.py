from a10sdk.common.A10BaseClass import A10BaseClass


class AuthKey(A10BaseClass):
    
    """Class Description::
    authentication key.

    Class auth-key supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param encrypted: {"not": "hex-encrypted", "optional": true, "type": "encrypted", "description": "Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED password string)", "format": "encrypted"}
    :param key_type: {"optional": true, "enum": ["ascii", "hex"], "type": "string", "description": "'ascii': key string in ASCII form; 'hex': key string in hex form; ", "format": "enum"}
    :param hex_encrypted: {"not": "encrypted", "optional": true, "type": "encrypted", "description": "Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED password string)", "format": "encrypted"}
    :param hex_key: {"format": "password", "minLength": 21, "optional": true, "maxLength": 40, "not": "asc-key", "type": "string"}
    :param alg_type: {"optional": true, "enum": ["M", "SHA", "SHA1"], "type": "string", "description": "'M': encryption using MD5; 'SHA': encryption using SHA; 'SHA1': encryption using SHA1; ", "format": "enum"}
    :param key: {"description": "authentication key", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": false}
    :param asc_key: {"format": "password", "minLength": 1, "optional": true, "maxLength": 20, "not": "hex-key", "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/ntp/auth-key/{key}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "key"]

        self.b_key = "auth-key"
        self.a10_url="/axapi/v3/ntp/auth-key/{key}"
        self.DeviceProxy = ""
        self.uuid = ""
        self.encrypted = ""
        self.key_type = ""
        self.hex_encrypted = ""
        self.hex_key = ""
        self.alg_type = ""
        self.key = ""
        self.asc_key = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


