from a10sdk.common.A10BaseClass import A10BaseClass


class SystemPollMode(A10BaseClass):
    
    """    :param enable: {"default": 0, "optional": true, "type": "number", "description": "Enable/Disable System Polling mode", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Enable/Disable System Polling Mode.

    Class system-poll-mode supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/system-poll-mode`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "system-poll-mode"
        self.a10_url="/axapi/v3/system-poll-mode"
        self.DeviceProxy = ""
        self.enable = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


