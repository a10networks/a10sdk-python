from a10sdk.common.A10BaseClass import A10BaseClass


class SystemBuffDebug(A10BaseClass):
    
    """Class Description::
    System buff debug config.

    Class system-buff-debug supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param enable_buff_debug: {"default": 0, "optional": true, "type": "number", "description": "Enable fpga buffer debugging", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/system-buff-debug`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "system-buff-debug"
        self.a10_url="/axapi/v3/system-buff-debug"
        self.DeviceProxy = ""
        self.enable_buff_debug = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


