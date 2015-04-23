from a10sdk.common.A10BaseClass import A10BaseClass


class BackupPeriodic(A10BaseClass):
    
    """Class Description::
    Configure backup periodically.

    Class backup-periodic supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param week: {"description": "Specify interval weeks", "format": "number", "optional": true, "not-list": ["day", "hour"], "maximum": 199, "minimum": 1, "type": "number"}
    :param use_mgmt_port: {"default": 0, "optional": true, "type": "number", "description": "Use management port as source port", "format": "flag"}
    :param hour: {"description": "Specify interval hours", "format": "number", "optional": true, "not-list": ["day", "week"], "maximum": 65534, "minimum": 1, "type": "number"}
    :param system: {"default": 0, "optional": false, "type": "number", "description": "Backup system files", "format": "flag"}
    :param store_name: {"description": "profile name to store remote url", "format": "string", "minLength": 1, "optional": true, "maxLength": 31, "type": "string"}
    :param remote_file: {"optional": true, "type": "string", "description": "profile name for remote url", "format": "url"}
    :param day: {"description": "Specify interval days", "format": "number", "optional": true, "not-list": ["hour", "week"], "maximum": 199, "minimum": 1, "type": "number"}
    :param log: {"default": 0, "optional": false, "type": "number", "description": "Backup log files", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/backup-periodic/{system}+{log}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "system","log"]

        self.b_key = "backup-periodic"
        self.a10_url="/axapi/v3/backup-periodic/{system}+{log}"
        self.DeviceProxy = ""
        self.week = ""
        self.use_mgmt_port = ""
        self.hour = ""
        self.system = ""
        self.store_name = ""
        self.remote_file = ""
        self.day = ""
        self.log = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


