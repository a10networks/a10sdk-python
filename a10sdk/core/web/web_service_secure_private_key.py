from a10sdk.common.A10BaseClass import A10BaseClass


class PrivateKey(A10BaseClass):
    
    """    :param load: {"default": 0, "optional": true, "type": "number", "description": "Load WEB private-key", "format": "flag"}
    :param file_url: {"optional": true, "type": "string", "description": "File URL", "format": "url"}
    :param use_mgmt_port: {"default": 0, "optional": true, "type": "number", "description": "Use management port as source port", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Web-service secure private-key operation.

    Class private-key supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/web-service/secure/private-key`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "private-key"
        self.a10_url="/axapi/v3/web-service/secure/private-key"
        self.DeviceProxy = ""
        self.load = ""
        self.file_url = ""
        self.use_mgmt_port = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


