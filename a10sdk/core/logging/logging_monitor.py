from a10sdk.common.A10BaseClass import A10BaseClass


class Monitor(A10BaseClass):
    
    """    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param monitor_levelname: {"description": "'disable': Do not send log to monitor; 'emergency': System unusable log messages      (severity=0); 'alert': Action must be taken immediately  (severity=1); 'critical': Critical conditions               (severity=2); 'error': Error conditions                  (severity=3); 'warning': Warning conditions                (severity=4); 'notification': Normal but significant conditions (severity=5); 'information': Informational messages            (severity=6); 'debugging': Debug level messages              (severity=7); ", "format": "enum", "default": "disable", "type": "string", "enum": ["disable", "emergency", "alert", "critical", "error", "warning", "notification", "information", "debugging"], "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Set terminal monitor logging level.

    Class monitor supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/logging/monitor`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "monitor"
        self.a10_url="/axapi/v3/logging/monitor"
        self.DeviceProxy = ""
        self.uuid = ""
        self.monitor_levelname = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


