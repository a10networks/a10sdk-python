from a10sdk.common.A10BaseClass import A10BaseClass


class PeriodCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param week: {"default": 0, "type": "number", "description": "Most recent week", "format": "flag"}
    :param all: {"default": 0, "type": "number", "description": "all log", "format": "flag"}
    :param period: {"default": 0, "type": "number", "description": "Specify backup period", "format": "flag"}
    :param month: {"default": 0, "type": "number", "description": " Most recent day", "format": "flag"}
    :param date: {"description": "specify number of days", "minimum": 1, "type": "number", "maximum": 31, "format": "number"}
    :param day: {"default": 0, "type": "number", "description": "Most recent day", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "period-cfg"
        self.DeviceProxy = ""
        self.week = ""
        self.A10WW_all = ""
        self.period = ""
        self.month = ""
        self.date = ""
        self.day = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class ExpediteCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param stats_data: {"default": 0, "type": "number", "description": "Backup web statistical data", "format": "flag"}
    :param use_mgmt_port: {"default": 0, "type": "number", "description": "Use management port as source port", "format": "flag"}
    :param expedite: {"default": 0, "type": "number", "description": "Expedite the Backup", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "expedite-cfg"
        self.DeviceProxy = ""
        self.stats_data = ""
        self.period_cfg = {}
        self.use_mgmt_port = ""
        self.expedite = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Log(A10BaseClass):
    
    """    :param store_name: {"description": "Save backup store information", "format": "string", "minLength": 1, "optional": true, "maxLength": 128, "type": "string"}
    :param remote_file: {"optional": true, "type": "string", "description": "profile name for remote url", "format": "url"}
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
        self.store_name = ""
        self.remote_file = ""
        self.expedite_cfg = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


