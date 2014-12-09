from a10sdk.common.A10BaseClass import A10BaseClass


class BootBlockFix(A10BaseClass):
    
    """    :param cf: {"default": 0, "optional": true, "type": "number", "description": "Compact flash", "format": "flag"}
    :param hd: {"default": 0, "optional": true, "type": "number", "description": "Hard disk", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Fix booting problem.

    Class boot-block-fix supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/boot-block-fix`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "boot-block-fix"
        self.a10_url="/axapi/v3/boot-block-fix"
        self.DeviceProxy = ""
        self.cf = ""
        self.hd = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


