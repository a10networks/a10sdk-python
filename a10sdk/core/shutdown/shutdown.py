from a10sdk.common.A10BaseClass import A10BaseClass


class Shutdown(A10BaseClass):
    
    """    :param day_of_month: {"description": "Day of the Month", "format": "number", "type": "number", "maximum": 31, "minimum": 1, "optional": true}
    :param reason_3: {"description": "Reason for Shutdown", "format": "string", "minLength": 1, "optional": true, "maxLength": 127, "type": "string"}
    :param reason_2: {"description": "Reason for Shutdown", "format": "string", "minLength": 1, "optional": true, "maxLength": 127, "type": "string"}
    :param in: {"optional": true, "type": "string", "description": "Delay before Shutdown (Time in hours and minutes)", "format": "time-hhmm"}
    :param month_2: {"optional": true, "enum": ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"], "type": "string", "description": "'January': Month of the year; 'February': Month of the year; 'March': Month of the year; 'April': Month of the year; 'May': Month of the year; 'June': Month of the year; 'July': Month of the year; 'August': Month of the year; 'September': Month of the year; 'October': Month of the year; 'November': Month of the year; 'December': Month of the year; ", "format": "enum"}
    :param month: {"optional": true, "enum": ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"], "type": "string", "description": "'January': Month of the year; 'February': Month of the year; 'March': Month of the year; 'April': Month of the year; 'May': Month of the year; 'June': Month of the year; 'July': Month of the year; 'August': Month of the year; 'September': Month of the year; 'October': Month of the year; 'November': Month of the year; 'December': Month of the year; ", "format": "enum"}
    :param reason: {"description": "Reason for Shutdown", "format": "string", "minLength": 1, "optional": true, "maxLength": 127, "type": "string"}
    :param at: {"default": 0, "optional": true, "type": "number", "description": "Shutdown at a specific time/date", "format": "flag"}
    :param time: {"optional": true, "type": "string", "description": "Time to Shutdown (hh:mm)", "format": "time-hhmm"}
    :param cancel: {"default": 0, "optional": true, "type": "number", "description": "Cancel Pending Shutdown", "format": "flag"}
    :param day_of_month_2: {"description": "Day of the Month", "format": "number", "type": "number", "maximum": 31, "minimum": 1, "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Shutdown the System.

    Class shutdown supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/shutdown`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "shutdown"
        self.a10_url="/axapi/v3/shutdown"
        self.DeviceProxy = ""
        self.day_of_month = ""
        self.reason_3 = ""
        self.reason_2 = ""
        self.A10WW_in = ""
        self.month_2 = ""
        self.month = ""
        self.reason = ""
        self.at = ""
        self.time = ""
        self.cancel = ""
        self.day_of_month_2 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


