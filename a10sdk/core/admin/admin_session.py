from a10sdk.common.A10BaseClass import A10BaseClass


class AdminSession(A10BaseClass):
    
    """    :param clear: {"default": 0, "optional": true, "type": "number", "description": "clear admin session", "format": "flag"}
    :param all: {"default": 0, "optional": true, "type": "number", "description": "Clear all admin sessions", "format": "flag"}
    :param sid: {"description": "Session ID", "format": "number", "default": 0, "optional": true, "maximum": 2147483647, "minimum": 0, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Admin session management.

    Class admin-session supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/admin-session`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "admin-session"
        self.a10_url="/axapi/v3/admin-session"
        self.DeviceProxy = ""
        self.clear = ""
        self.A10WW_all = ""
        self.sid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


