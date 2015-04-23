from a10sdk.common.A10BaseClass import A10BaseClass


class Reminder(A10BaseClass):
    
    """Class Description::
    Set the reminder for grace time.

    Class reminder supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param reminder_value: {"description": "Configure reminder for grace time (Hour)", "format": "number", "type": "number", "maximum": 1000000, "minimum": 1, "optional": false}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/license-manager/reminder/{reminder_value}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "reminder_value"]

        self.b_key = "reminder"
        self.a10_url="/axapi/v3/license-manager/reminder/{reminder_value}"
        self.DeviceProxy = ""
        self.reminder_value = ""
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


