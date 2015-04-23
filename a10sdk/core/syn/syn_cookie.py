from a10sdk.common.A10BaseClass import A10BaseClass


class SynCookie(A10BaseClass):
    
    """Class Description::
    Global Syn-Cookie Protection.

    Class syn-cookie supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param on_threshold: {"description": "on-threshold for Syn-cookie (Decimal number)", "partition-visibility": "shared", "default": 0, "optional": true, "format": "number", "maximum": 2147483647, "minimum": 0, "type": "number"}
    :param enable: {"default": 0, "optional": true, "type": "number", "description": "Global Syn-Cookie Protection", "format": "flag"}
    :param off_threshold: {"description": "off-threshold for Syn-cookie (Decimal number)", "partition-visibility": "shared", "default": 0, "optional": true, "format": "number", "maximum": 2147483647, "minimum": 0, "type": "number"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/syn-cookie`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "syn-cookie"
        self.a10_url="/axapi/v3/syn-cookie"
        self.DeviceProxy = ""
        self.on_threshold = ""
        self.enable = ""
        self.off_threshold = ""
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


