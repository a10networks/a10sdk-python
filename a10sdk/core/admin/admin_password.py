from a10sdk.common.A10BaseClass import A10BaseClass


class Password(A10BaseClass):
    
    """Class Description::
    Config admin user password.

    Class password supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param password_in_module: {"description": "Config admin user password", "format": "password", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param encrypted_in_module: {"optional": true, "type": "encrypted", "description": "Specify an ENCRYPTED password string (System admin user password)", "format": "encrypted"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/admin/{user}/password`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "password"
        self.a10_url="/axapi/v3/admin/{user}/password"
        self.DeviceProxy = ""
        self.password_in_module = ""
        self.encrypted_in_module = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


