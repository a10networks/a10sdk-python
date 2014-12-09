from a10sdk.common.A10BaseClass import A10BaseClass


class AdminLockout(A10BaseClass):
    
    """Class Description::
    Admin user lockout configuration.

    Class admin-lockout supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param duration: {"description": "Admin user lockout duration, in minutes, by default 10 (Admin user lockout duration in minutes, 0 means forever)", "format": "number", "default": 10, "optional": true, "maximum": 1440, "minimum": 0, "type": "number"}
    :param threshold: {"description": "Admin user lockout threshold, by default 5", "format": "number", "default": 5, "optional": true, "maximum": 10, "minimum": 1, "type": "number"}
    :param enable: {"default": 0, "optional": true, "type": "number", "description": "Enable admin user lockout", "format": "flag"}
    :param reset_time: {"description": "After how long to reset the lockout counter, in minutes, by default 10 (Time in minutes after which to reset the lockout counter)", "format": "number", "default": 10, "optional": true, "maximum": 1440, "minimum": 1, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/admin-lockout`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "admin-lockout"
        self.a10_url="/axapi/v3/admin-lockout"
        self.DeviceProxy = ""
        self.duration = ""
        self.threshold = ""
        self.enable = ""
        self.reset_time = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


