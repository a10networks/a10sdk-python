from a10sdk.common.A10BaseClass import A10BaseClass


class Logging(A10BaseClass):
    
    """Class Description::
    System logging configuration.

    Class logging supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param single_priority_list: {"minItems": 1, "items": {"type": "single-priority"}, "uniqueItems": true, "array": [{"required": ["levelname"], "properties": {"levelname": {"optional": false, "enum": ["emergency", "alert", "critical", "error", "warning", "notification", "information", "debugging"], "type": "string", "description": "'emergency': System unusable log messages      (severity=0); 'alert': Action must be taken immediately  (severity=1); 'critical': Critical conditions               (severity=2); 'error': Error conditions                  (severity=3); 'warning': Warning conditions                (severity=4); 'notification': Normal but significant conditions (severity=5); 'information': Informational messages            (severity=6); 'debugging': Debug level messages              (severity=7); ", "format": "enum"}}}], "type": "array", "$ref": "/axapi/v3/logging/single-priority/{levelname}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/logging`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "logging"
        self.a10_url="/axapi/v3/logging"
        self.DeviceProxy = ""
        self.buffered = {}
        self.email_address = {}
        self.console = {}
        self.monitor = {}
        self.facility = {}
        self.disable_partition_name = {}
        self.email = {}
        self.syslog = {}
        self.host = {}
        self.export = {}
        self.trap = {}
        self.auditlog = {}
        self.single_priority_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


