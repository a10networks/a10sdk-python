from a10sdk.common.A10BaseClass import A10BaseClass


class LogBackup(A10BaseClass):
    
    """    :param week: {"default": 0, "optional": true, "type": "number", "description": "Most recent week", "format": "flag"}
    :param all: {"default": 0, "optional": true, "type": "number", "description": "all log", "format": "flag"}
    :param period: {"default": 0, "optional": true, "type": "number", "description": "Specify backup period", "format": "flag"}
    :param month: {"default": 0, "optional": true, "type": "number", "description": " Most recent month", "format": "flag"}
    :param stats_data: {"default": 0, "optional": true, "type": "number", "description": "Backup web statistical data", "format": "flag"}
    :param file_handle: {"description": "full path of the uploaded file", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 255, "type": "string"}
    :param date: {"description": "specify number of days", "format": "number", "type": "number", "maximum": 31, "minimum": 1, "optional": true}
    :param day: {"default": 0, "optional": true, "type": "number", "description": "Most recent day", "format": "flag"}
    :param expedite: {"default": 0, "optional": true, "type": "number", "description": "Expedite the Backup", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Backup system files.

    Class log-backup supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/file/log-backup`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "log-backup"
        self.a10_url="/axapi/v3/file/log-backup"
        self.DeviceProxy = ""
        self.week = ""
        self.A10WW_all = ""
        self.period = ""
        self.month = ""
        self.stats_data = ""
        self.file_handle = ""
        self.date = ""
        self.day = ""
        self.expedite = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


