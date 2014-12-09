from a10sdk.common.A10BaseClass import A10BaseClass


class Erase(A10BaseClass):
    
    """    :param preserve_accounts: {"description": "preserve admin accounts", "partition-visibility": "shared", "default": 0, "type": "number", "format": "flag", "optional": true}
    :param reload: {"description": "reload after erase", "partition-visibility": "shared", "default": 0, "type": "number", "format": "flag", "optional": true}
    :param preserve_management: {"description": "preserve managememt ip and default gateway", "partition-visibility": "shared", "default": 0, "type": "number", "format": "flag", "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Erase Configuration.

    Class erase supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/erase`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "erase"
        self.a10_url="/axapi/v3/erase"
        self.DeviceProxy = ""
        self.preserve_accounts = ""
        self.A10WW_reload = ""
        self.preserve_management = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


