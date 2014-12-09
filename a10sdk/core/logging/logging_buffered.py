from a10sdk.common.A10BaseClass import A10BaseClass


class Buffered(A10BaseClass):
    
    """Class Description::
    Set buffered logging parameters.

    Class buffered supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param buffersize: {"description": "Logging buffer size (in items), default 30000", "partition-visibility": "shared", "default": 30000, "optional": true, "format": "number", "maximum": 50000, "minimum": 10000, "type": "number"}
    :param buffered_disable: {"description": "Do not send log to console", "format": "flag", "default": 0, "optional": true, "not": "levelname", "type": "number"}
    :param levelname: {"description": "'emergency': System unusable log messages      (severity=0); 'alert': Action must be taken immediately  (severity=1); 'critical': Critical conditions               (severity=2); 'error': Error conditions                  (severity=3); 'warning': Warning conditions                (severity=4); 'notification': Normal but significant conditions (severity=5); 'information': Informational messages            (severity=6); 'debugging': Debug level messages              (severity=7); ", "format": "enum", "default": "debugging", "optional": true, "enum": ["emergency", "alert", "critical", "error", "warning", "notification", "information", "debugging"], "not": "buffered-disable", "type": "string"}
    :param partition_buffersize: {"description": "Logging buffer size (in items), default 3000", "partition-visibility": "private", "default": 3000, "optional": true, "format": "number", "maximum": 5000, "minimum": 1000, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

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
        self.buffered_disable = ""
        self.levelname = ""
        self.partition_buffersize = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


