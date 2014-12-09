from a10sdk.common.A10BaseClass import A10BaseClass


class Console(A10BaseClass):
    
    """Class Description::
    Set logging level which sent to console.

    Class console supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param console_levelname: {"description": "'emergency': System unusable log messages      (severity=0); 'alert': Action must be taken immediately  (severity=1); 'critical': Critical conditions               (severity=2); 'error': Error conditions                  (severity=3); 'warning': Warning conditions                (severity=4); 'notification': Normal but significant conditions (severity=5); 'information': Informational messages            (severity=6); 'debugging': Debug level messages              (severity=7); ", "format": "enum", "default": "error", "optional": true, "enum": ["emergency", "alert", "critical", "error", "warning", "notification", "information", "debugging"], "not": "console-disable", "type": "string"}
    :param console_disable: {"description": "Do not send log to console", "format": "flag", "default": 0, "optional": true, "not": "console-levelname", "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/logging/console`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "console"
        self.a10_url="/axapi/v3/logging/console"
        self.DeviceProxy = ""
        self.console_levelname = ""
        self.console_disable = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


