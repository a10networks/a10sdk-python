from a10sdk.common.A10BaseClass import A10BaseClass


class Access(A10BaseClass):
    
    """Class Description::
    Config access type.

    Class access supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param access_type: {"default": "axapi,cli,web", "optional": true, "enum": ["axapi", "cli", "web"], "type": "string", "format": "enum-list"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/admin/{user}/access`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "access"
        self.a10_url="/axapi/v3/admin/{user}/access"
        self.DeviceProxy = ""
        self.access_type = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


