from a10sdk.common.A10BaseClass import A10BaseClass


class Syslog(A10BaseClass):
    
    """    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param syslog_levelname: {"description": "'disable': Do not send log to syslog; 'emergency': System unusable log messages      (severity=0); 'alert': Action must be taken immediately  (severity=1); 'critical': Critical conditions               (severity=2); 'error': Error conditions                  (severity=3); 'warning': Warning conditions                (severity=4); 'notification': Normal but significant conditions (severity=5); 'information': Informational messages            (severity=6); 'debugging': Debug level messages              (severity=7); ", "format": "enum", "default": "disable", "type": "string", "enum": ["disable", "emergency", "alert", "critical", "error", "warning", "notification", "information", "debugging"], "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Set logging level which sent to syslog host.

    Class syslog supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/logging/syslog`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "syslog"
        self.a10_url="/axapi/v3/logging/syslog"
        self.DeviceProxy = ""
        self.uuid = ""
        self.syslog_levelname = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


