from a10sdk.common.A10BaseClass import A10BaseClass


class Overage(A10BaseClass):
    
    """Class Description::
    Set overage parameters.

    Class overage supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param kb: {"description": "Number of KB", "format": "number", "type": "number", "maximum": 1023, "minimum": 1, "optional": true}
    :param mb: {"description": "Number of MB", "format": "number", "type": "number", "maximum": 1023, "minimum": 1, "optional": true}
    :param seconds: {"description": "Number of seconds", "format": "number", "type": "number", "maximum": 59, "minimum": 0, "optional": true}
    :param bytes: {"description": "Number of bytes", "format": "number", "type": "number", "maximum": 1023, "minimum": 1, "optional": true}
    :param days: {"description": "Number of days", "format": "number", "type": "number", "maximum": 365, "minimum": 0, "optional": true}
    :param hours: {"description": "Number of hours", "format": "number", "type": "number", "maximum": 23, "minimum": 0, "optional": true}
    :param gb: {"description": "Number of GB", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": true}
    :param minutes: {"description": "Number of minutes", "format": "number", "type": "number", "maximum": 59, "minimum": 0, "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/license-manager/overage`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "overage"
        self.a10_url="/axapi/v3/license-manager/overage"
        self.DeviceProxy = ""
        self.kb = ""
        self.mb = ""
        self.seconds = ""
        self.A10WW_bytes = ""
        self.days = ""
        self.hours = ""
        self.gb = ""
        self.minutes = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


