from a10sdk.common.A10BaseClass import A10BaseClass


class Upgrade(A10BaseClass):
    
    """    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Upgrade System.

    Class upgrade supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/upgrade`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "upgrade"
        self.a10_url="/axapi/v3/upgrade"
        self.DeviceProxy = ""
        self.cf = {}
        self.hd = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


