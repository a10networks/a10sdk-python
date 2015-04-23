from a10sdk.common.A10BaseClass import A10BaseClass


class EnablePassword(A10BaseClass):
    
    """    :param password: {"description": "The password", "format": "password", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Modify enable password parameters.

    Class enable-password supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/enable-password`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "enable-password"
        self.a10_url="/axapi/v3/enable-password"
        self.DeviceProxy = ""
        self.password = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


