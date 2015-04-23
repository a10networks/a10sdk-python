from a10sdk.common.A10BaseClass import A10BaseClass


class Reboot(A10BaseClass):
    
    """    :param all: {"default": 0, "optional": true, "type": "number", "description": "Reboot all devices when VCS is enabled, or only this device itself if VCS is not enabled", "format": "flag"}
    :param day_of_month: {"description": "Day of the Month", "format": "number", "type": "number", "maximum": 31, "minimum": 1, "optional": true}
    :param reason_3: {"description": "Reason for Reboot", "format": "string", "minLength": 1, "optional": true, "maxLength": 127, "type": "string"}
    :param reason_2: {"description": "Reason for Reboot", "format": "string", "minLength": 1, "optional": true, "maxLength": 127, "type": "string"}
    :param time: {"optional": true, "type": "string", "description": "Time to Reboot (hh:mm)", "format": "time-hhmm"}
    :param month_2: {"optional": true, "enum": ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"], "type": "string", "description": "'January': Month of the year; 'February': Month of the year; 'March': Month of the year; 'April': Month of the year; 'May': Month of the year; 'June': Month of the year; 'July': Month of the r; 'August': Month of the year; 'September': Month of the year; 'October': Month of the year; 'November': Month of the year; 'December': Month of the year; ", "format": "enum"}
    :param month: {"optional": true, "enum": ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"], "type": "string", "description": "'January': Month of the year; 'February': Month of the year; 'March': Month of the year; 'April': Month of the year; 'May': Month of the year; 'June': Month of the year; 'July': Month of the year; 'August': Month of the year; 'September': Month of the year; 'October': Month of the year; 'November': Month of the year; 'December': Month of the year; ", "format": "enum"}
    :param cancel: {"default": 0, "optional": true, "type": "number", "description": "Cancel Pending Reboot", "format": "flag"}
    :param reason: {"description": "Reason for Reboot", "format": "string", "minLength": 1, "optional": true, "maxLength": 127, "type": "string"}
    :param at: {"default": 0, "optional": true, "type": "number", "description": "Reboot at a Specific time/date", "format": "flag"}
    :param in: {"optional": true, "type": "string", "description": "Reboot after a time interval (Time in hours and minutes)", "format": "time-hhmm"}
    :param device: {"platform-specific-range": 1, "platform-specific-default": 1, "description": "Reboot a specific device when VCS is enabled (device id)", "format": "number", "optional": true, "type": "number"}
    :param day_of_month_2: {"description": "Day of the Month", "format": "number", "type": "number", "maximum": 31, "minimum": 1, "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Reboot the System.

    Class reboot supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/reboot`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "reboot"
        self.a10_url="/axapi/v3/reboot"
        self.DeviceProxy = ""
        self.A10WW_all = ""
        self.day_of_month = ""
        self.reason_3 = ""
        self.reason_2 = ""
        self.time = ""
        self.month_2 = ""
        self.month = ""
        self.cancel = ""
        self.reason = ""
        self.at = ""
        self.A10WW_in = ""
        self.device = ""
        self.day_of_month_2 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


