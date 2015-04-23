from a10sdk.common.A10BaseClass import A10BaseClass


class SinglePriority(A10BaseClass):
    
    """Class Description::
    Set single-priority logging.

    Class single-priority supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param levelname: {"optional": false, "enum": ["emergency", "alert", "critical", "error", "warning", "notification", "information", "debugging"], "type": "string", "description": "'emergency': System unusable log messages      (severity=0); 'alert': Action must be taken immediately  (severity=1); 'critical': Critical conditions               (severity=2); 'error': Error conditions                  (severity=3); 'warning': Warning conditions                (severity=4); 'notification': Normal but significant conditions (severity=5); 'information': Informational messages            (severity=6); 'debugging': Debug level messages              (severity=7); ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/logging/single-priority/{levelname}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "levelname"]

        self.b_key = "single-priority"
        self.a10_url="/axapi/v3/logging/single-priority/{levelname}"
        self.DeviceProxy = ""
        self.uuid = ""
        self.levelname = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


