from a10sdk.common.A10BaseClass import A10BaseClass


class SystemReset(A10BaseClass):
    
    """    :param reboot_flag: {"default": 0, "optional": true, "type": "number", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Reset system to the default configuration.

    Class system-reset supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/system-reset`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "system-reset"
        self.a10_url="/axapi/v3/system-reset"
        self.DeviceProxy = ""
        self.reboot_flag = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


