from a10sdk.common.A10BaseClass import A10BaseClass


class WriteToNonVolatileMemory(A10BaseClass):
    
    """    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/write/memory`.

    Class Write to Non-volatile Memory supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "Write to Non-volatile Memory"
        self.a10_url="/axapi/v3/write/memory"
        self.DeviceProxy = ""
        
        for keys, value in kwargs.items():
            setattr(self,keys, value)


