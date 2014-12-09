from a10sdk.common.A10BaseClass import A10BaseClass


class Relay(A10BaseClass):
    
    """Class Description::
    Authentication relay configuration.

    Class relay supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param ntlm_list: {"minItems": 1, "items": {"type": "ntlm"}, "uniqueItems": true, "array": [{"required": ["name"], "properties": {"domain": {"description": "Specify NTLM domain, default is null", "format": "string", "minLength": 1, "optional": true, "maxLength": 64, "type": "string"}, "version": {"description": "Specify NTLM version, default is NTLM 2", "format": "number", "default": 2, "optional": true, "maximum": 2, "minimum": 1, "type": "number"}, "name": {"description": "Specify NTLM authentication relay name", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/aam/authentication/relay/ntlm/{name}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/aam/authentication/relay`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "relay"
        self.a10_url="/axapi/v3/aam/authentication/relay"
        self.DeviceProxy = ""
        self.ntlm_list = []
        self.form_based = {}
        self.kerberos = {}
        self.http_basic = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


