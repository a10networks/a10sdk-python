from a10sdk.common.A10BaseClass import A10BaseClass


class SystemBigBuffPool(A10BaseClass):
    
    """    :param big_buff_pool: {"default": 0, "optional": true, "type": "number", "description": "Configure big I/O buffer pool", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    System big buff pool config.

    Class system-big-buff-pool supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/system-big-buff-pool`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "system-big-buff-pool"
        self.a10_url="/axapi/v3/system-big-buff-pool"
        self.DeviceProxy = ""
        self.big_buff_pool = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


