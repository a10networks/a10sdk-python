from a10sdk.common.A10BaseClass import A10BaseClass


class HdMonitor(A10BaseClass):
    
    """Class Description::
    Enable HD monitoring.

    Class hd-monitor supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param enable: {"default": 0, "optional": true, "type": "number", "description": "Enable Hard disk monitoring", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/hd-monitor`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "hd-monitor"
        self.a10_url="/axapi/v3/hd-monitor"
        self.DeviceProxy = ""
        self.enable = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


