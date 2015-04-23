from a10sdk.common.A10BaseClass import A10BaseClass


class Buffered(A10BaseClass):
    
    """    :param buffersize: {"description": "Logging buffer size (in items), default 30000", "partition-visibility": "shared", "default": 30000, "optional": true, "format": "number", "maximum": 50000, "minimum": 10000, "type": "number"}
    :param levelname: {"description": "'disable': Do not send log to console; 'emergency': System unusable log messages      (severity=0); 'alert': Action must be taken immediately  (severity=1); 'critical': Critical conditions               (severity=2); 'error': Error conditions                  (severity=3); 'warning': Warning conditions                (severity=4); 'notification': Normal but significant conditions (severity=5); 'information': Informational messages            (severity=6); 'debugging': Debug level messages              (severity=7); ", "format": "enum", "default": "debugging", "type": "string", "enum": ["disable", "emergency", "alert", "critical", "error", "warning", "notification", "information", "debugging"], "optional": true}
    :param partition_buffersize: {"description": "Logging buffer size (in items), default 3000", "partition-visibility": "private", "default": 3000, "optional": true, "format": "number", "maximum": 5000, "minimum": 1000, "type": "number"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Set buffered logging parameters.

    Class buffered supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/logging/buffered`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "buffered"
        self.a10_url="/axapi/v3/logging/buffered"
        self.DeviceProxy = ""
        self.buffersize = ""
        self.levelname = ""
        self.partition_buffersize = ""
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


