from a10sdk.common.A10BaseClass import A10BaseClass


class Log(A10BaseClass):
    
    """    :param week: {"default": 0, "optional": true, "type": "number", "description": "Most recent week", "format": "flag"}
    :param all: {"default": 0, "optional": true, "type": "number", "description": "all log", "format": "flag"}
    :param remote_file: {"optional": true, "type": "string", "description": "profile name for remote url", "format": "url"}
    :param use_mgmt_port: {"default": 0, "optional": true, "type": "number", "description": "Use management port as source port", "format": "flag"}
    :param period: {"default": 0, "optional": true, "type": "number", "description": "Specify backup period", "format": "flag"}
    :param month: {"default": 0, "optional": true, "type": "number", "description": " Most recent month", "format": "flag"}
    :param stats_data: {"default": 0, "optional": true, "type": "number", "description": "Backup web statistical data", "format": "flag"}
    :param date: {"description": "specify number of days", "format": "number", "type": "number", "maximum": 31, "minimum": 1, "optional": true}
    :param store_name: {"description": "Save backup store information", "format": "string", "minLength": 1, "optional": true, "maxLength": 128, "type": "string"}
    :param day: {"default": 0, "optional": true, "type": "number", "description": "Most recent day", "format": "flag"}
    :param expedite: {"default": 0, "optional": true, "type": "number", "description": "Expedite the Backup", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Backup log files.

    Class log supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/backup/log`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "log"
        self.a10_url="/axapi/v3/backup/log"
        self.DeviceProxy = ""
        self.week = ""
        self.A10WW_all = ""
        self.remote_file = ""
        self.use_mgmt_port = ""
        self.period = ""
        self.month = ""
        self.stats_data = ""
        self.date = ""
        self.store_name = ""
        self.day = ""
        self.expedite = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


