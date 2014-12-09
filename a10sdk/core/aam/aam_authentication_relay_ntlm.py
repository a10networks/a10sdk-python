from a10sdk.common.A10BaseClass import A10BaseClass


class Ntlm(A10BaseClass):
    
    """Class Description::
    NTLM Authentication Relay.

    Class ntlm supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param domain: {"description": "Specify NTLM domain, default is null", "format": "string", "minLength": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param version: {"description": "Specify NTLM version, default is NTLM 2", "format": "number", "default": 2, "optional": true, "maximum": 2, "minimum": 1, "type": "number"}
    :param name: {"description": "Specify NTLM authentication relay name", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/aam/authentication/relay/ntlm/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "ntlm"
        self.a10_url="/axapi/v3/aam/authentication/relay/ntlm/{name}"
        self.DeviceProxy = ""
        self.domain = ""
        self.version = ""
        self.name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


