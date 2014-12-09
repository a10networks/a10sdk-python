from a10sdk.common.A10BaseClass import A10BaseClass


class MacAgeTime(A10BaseClass):
    
    """Class Description::
    Set Aging period for all MAC Interfaces.

    Class mac-age-time supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param aging_time: {"description": "Set aging period in seconds for all MAC interfaces (default 300 seconds)", "format": "number", "default": 300, "optional": true, "maximum": 600, "minimum": 10, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/mac-age-time`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "mac-age-time"
        self.a10_url="/axapi/v3/mac-age-time"
        self.DeviceProxy = ""
        self.aging_time = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


