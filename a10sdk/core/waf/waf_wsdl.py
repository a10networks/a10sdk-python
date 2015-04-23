from a10sdk.common.A10BaseClass import A10BaseClass


class Wsdl(A10BaseClass):
    
    """Class Description::
    Manage Web Services Definition Language files.

    Class wsdl supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param max_filesize: {"description": "Set maximum WSDL file size (Maximum file size in KBytes, default is 32K)", "partition-visibility": "shared", "default": 32, "optional": true, "format": "number", "maximum": 256, "minimum": 16, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/waf/wsdl`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "wsdl"
        self.a10_url="/axapi/v3/waf/wsdl"
        self.DeviceProxy = ""
        self.uuid = ""
        self.max_filesize = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


