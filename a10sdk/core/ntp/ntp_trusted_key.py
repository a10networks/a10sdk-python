from a10sdk.common.A10BaseClass import A10BaseClass


class TrustedKey(A10BaseClass):
    
    """Class Description::
    trusted key.

    Class trusted-key supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param key: {"description": "trusted key", "format": "number", "optional": false, "maximum": 65535, "minimum": 1, "type": "number", "$ref": "/axapi/v3/ntp/auth-key"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/ntp/trusted-key/{key}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "key"]

        self.b_key = "trusted-key"
        self.a10_url="/axapi/v3/ntp/trusted-key/{key}"
        self.DeviceProxy = ""
        self.uuid = ""
        self.key = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


