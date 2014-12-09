from a10sdk.common.A10BaseClass import A10BaseClass


class FanSpeed(A10BaseClass):
    
    """Class Description::
    Control FAN Speed setting.

    Class fan-speed supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param action: {"description": "'auto': Set FAN Speed to automatic based on system temperature; 'max': Set FAN Speed to maximum; ", "format": "enum", "default": "auto", "type": "string", "enum": ["auto", "max"], "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/fan-speed`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "fan-speed"
        self.a10_url="/axapi/v3/fan-speed"
        self.DeviceProxy = ""
        self.action = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


