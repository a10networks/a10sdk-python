from a10sdk.common.A10BaseClass import A10BaseClass


class RunningConfig(A10BaseClass):
    
    """Class Description::
    Configure the behaviour of show running config.

    Class running-config supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param aflex: {"default": 0, "optional": true, "type": "number", "description": "Show aFleX scripts", "format": "flag"}
    :param class_list: {"default": 0, "optional": true, "type": "number", "description": "Show class-list files", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/running-config`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "running-config"
        self.a10_url="/axapi/v3/running-config"
        self.DeviceProxy = ""
        self.aflex = ""
        self.class_list = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


