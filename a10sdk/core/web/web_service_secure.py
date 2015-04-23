from a10sdk.common.A10BaseClass import A10BaseClass


class Secure(A10BaseClass):
    
    """    :param wipe: {"default": 0, "optional": true, "type": "number", "description": "Wipe WEB private-key and certificate", "format": "flag"}
    :param restart: {"default": 0, "optional": true, "type": "number", "description": "Restart WEB service", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Web-service secure operation.

    Class secure supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/web-service/secure`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "secure"
        self.a10_url="/axapi/v3/web-service/secure"
        self.DeviceProxy = ""
        self.certificate = {}
        self.regenerate = {}
        self.generate = {}
        self.private_key = {}
        self.wipe = ""
        self.restart = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


