from a10sdk.common.A10BaseClass import A10BaseClass


class LicenseManager(A10BaseClass):
    
    """Class Description::
    Configure license manager.

    Class license-manager supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param reminder_list: {"minItems": 1, "items": {"type": "reminder"}, "uniqueItems": true, "array": [{"required": ["reminder-value"], "properties": {"reminder-value": {"description": "Configure reminder for grace time (Hour)", "format": "number", "type": "number", "maximum": 1000000, "minimum": 1, "optional": false}}}], "type": "array", "$ref": "/axapi/v3/license-manager/reminder/{reminder-value}"}
    :param bandwidth_base: {"description": "Configure feature bandwidth base (Mb)", "format": "number", "type": "number", "maximum": 102400, "minimum": 10, "optional": true}
    :param use_mgmt_port: {"description": "Use management port to connect license server", "partition-visibility": "shared", "default": 0, "type": "number", "format": "flag", "optional": true}
    :param interval: {"description": "Configure interval profile (1 monthly, 2 daily, 3 hourly)", "format": "number", "type": "number", "maximum": 3, "minimum": 1, "optional": true}
    :param sn: {"description": "serial number", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param host_list: {"minItems": 1, "items": {"type": "host"}, "uniqueItems": true, "array": [{"required": ["host-ipv4"], "properties": {"host-ipv4": {"description": "license server ip address (length:1-31)", "format": "host", "minLength": 1, "optional": false, "maxLength": 31, "type": "string"}, "port": {"description": "Configure the license manager port, default is 443", "format": "number", "default": 443, "optional": true, "maximum": 65535, "minimum": 1, "type": "number"}}}], "type": "array", "$ref": "/axapi/v3/license-manager/host/{host-ipv4}"}
    :param bandwidth_unrestricted: {"default": 0, "optional": true, "type": "number", "description": "Set the bandwidth to maximum", "format": "flag"}
    :param instance_name: {"description": "Configure instance name [format: (string).(string).(string).(string)]", "format": "string", "minLength": 7, "optional": true, "maxLength": 63, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/license-manager`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "license-manager"
        self.a10_url="/axapi/v3/license-manager"
        self.DeviceProxy = ""
        self.reminder_list = []
        self.bandwidth_base = ""
        self.use_mgmt_port = ""
        self.interval = ""
        self.overage = {}
        self.sn = ""
        self.host_list = []
        self.bandwidth_unrestricted = ""
        self.instance_name = ""
        self.connect = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


