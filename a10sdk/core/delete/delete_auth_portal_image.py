from a10sdk.common.A10BaseClass import A10BaseClass


class AuthPortalImage(A10BaseClass):
    
    """    :param image_name: {"description": "Local File Name", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Image file for default portal.

    Class auth-portal-image supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/delete/auth-portal-image`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "auth-portal-image"
        self.a10_url="/axapi/v3/delete/auth-portal-image"
        self.DeviceProxy = ""
        self.image_name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


