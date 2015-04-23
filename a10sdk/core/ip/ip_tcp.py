from a10sdk.common.A10BaseClass import A10BaseClass


class SynCookie(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param threshold: {"description": "SYN cookie expire threshold (seconds (default is 4))", "format": "number", "default": 4, "maximum": 100, "minimum": 1, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "syn-cookie"
        self.DeviceProxy = ""
        self.threshold = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Tcp(A10BaseClass):
    
    """    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Global TCP parameters.

    Class tcp supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/ip/tcp`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "tcp"
        self.a10_url="/axapi/v3/ip/tcp"
        self.DeviceProxy = ""
        self.uuid = ""
        self.syn_cookie = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


