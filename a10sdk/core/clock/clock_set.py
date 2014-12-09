from a10sdk.common.A10BaseClass import A10BaseClass


class TimeCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param day_of_month: {"description": "Day of the Month", "minimum": 1, "type": "number", "maximum": 31, "format": "number"}
    :param time: {"type": "string", "description": "Current Time", "format": "time"}
    :param month_2: {"enum": ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"], "type": "string", "description": "'January': Month of the year; 'February': Month of the year; 'March': Month of the year; 'April': Month of the year; 'May': Month of the year; 'June': Month of the year; 'July': Month of the year; 'August': Month of the year; 'September': Month of the year; 'October': Month of the year; 'November': Month of the year; 'December': Month of the year; ", "format": "enum"}
    :param month: {"enum": ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"], "type": "string", "description": "'January': Month of the year; 'February': Month of the year; 'March': Month of the year; 'April': Month of the year; 'May': Month of the year; 'June': Month of the year; 'July': Month of the year; 'August': Month of the year; 'September': Month of the year; 'October': Month of the year; 'November': Month of the year; 'December': Month of the year; ", "format": "enum"}
    :param year: {"description": "Year", "minimum": 2005, "type": "number", "maximum": 2035, "format": "number"}
    :param day_of_month_2: {"description": "Day of the Month", "minimum": 1, "type": "number", "maximum": 31, "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "time-cfg"
        self.DeviceProxy = ""
        self.day_of_month = ""
        self.time = ""
        self.month_2 = ""
        self.month = ""
        self.year = ""
        self.day_of_month_2 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Set(A10BaseClass):
    
    """    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Set the Time and Date.

    Class set supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/clock/set`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "set"
        self.a10_url="/axapi/v3/clock/set"
        self.DeviceProxy = ""
        self.time_cfg = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


