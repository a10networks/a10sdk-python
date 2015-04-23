from a10sdk.common.A10BaseClass import A10BaseClass


class Clock(A10BaseClass):
    
    """    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Configure time-of-day Clock.

    Class clock supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/clock`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "clock"
        self.a10_url="/axapi/v3/clock"
        self.DeviceProxy = ""
        self.A10WW_set = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


