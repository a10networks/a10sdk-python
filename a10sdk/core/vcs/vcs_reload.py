from a10sdk.common.A10BaseClass import A10BaseClass


class Reload(A10BaseClass):
    
    """    :param disable_merge: {"default": 0, "optional": true, "type": "number", "description": "don't merge this vBlade's configuration to aVCS chassis", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    VCS reload.

    Class reload supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/vcs/reload`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "reload"
        self.a10_url="/axapi/v3/vcs/reload"
        self.DeviceProxy = ""
        self.disable_merge = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


