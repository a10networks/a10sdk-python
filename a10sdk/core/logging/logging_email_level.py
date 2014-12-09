from a10sdk.common.A10BaseClass import A10BaseClass


class Level(A10BaseClass):
    
    """Class Description::
    Set logging level which sent to email address.

    Class level supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param email_levelname: {"optional": true, "enum": ["emergency", "alert", "critical", "notification"], "type": "string", "description": "'emergency': System unusable log messages      (severity=0); 'alert': Action must be taken immediately   (severity=1); 'critical': Critical conditions      (severity=2); 'notification': Normal but significant conditions (severity=5); ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/logging/email/level`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "level"
        self.a10_url="/axapi/v3/logging/email/level"
        self.DeviceProxy = ""
        self.email_levelname = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


