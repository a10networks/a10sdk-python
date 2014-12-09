from a10sdk.common.A10BaseClass import A10BaseClass


class AuthPortal(A10BaseClass):
    
    """    :param portal_name: {"description": "Local File Name", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Portal file for http authentication.

    Class auth-portal supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/delete/auth-portal`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "auth-portal"
        self.a10_url="/axapi/v3/delete/auth-portal"
        self.DeviceProxy = ""
        self.portal_name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


