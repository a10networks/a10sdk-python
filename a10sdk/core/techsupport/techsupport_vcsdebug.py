from a10sdk.common.A10BaseClass import A10BaseClass


class GeneratesAvcsDebugFile(A10BaseClass):
    
    """    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/techsupport/vcsdebug`.

    Class Generates aVCS debug file supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "Generates aVCS debug file"
        self.a10_url="/axapi/v3/techsupport/vcsdebug"
        self.DeviceProxy = ""
        
        for keys, value in kwargs.items():
            setattr(self,keys, value)


