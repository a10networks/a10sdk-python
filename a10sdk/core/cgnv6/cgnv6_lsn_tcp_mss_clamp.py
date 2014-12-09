from a10sdk.common.A10BaseClass import A10BaseClass


class MssClamp(A10BaseClass):
    
    """Class Description::
    LSN TCP MSS Clamping.

    Class mss-clamp supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param mss_subtract: {"description": "Specify the value to subtract from the TCP MSS (default: not configured)", "format": "number", "type": "number", "maximum": 1460, "minimum": 0, "optional": true}
    :param mss_value: {"description": "The max value allowed for the TCP MSS (default: not configured)},", "format": "number", "type": "number", "maximum": 1460, "minimum": 0, "optional": true}
    :param mss_clamp_type: {"description": "'fixed': Specify a fixed max value for the TCP MSS; 'subtract': Specify the value to subtract from the TCP MSS; 'none': No TCP MSS clamping (default); ", "format": "enum", "default": "none", "type": "string", "enum": ["fixed", "subtract", "none"], "optional": true}
    :param min: {"description": "Specify the min value allowed for the TCP MSS (Specify the min value allowed for the TCP MSS (default: ((576 - 60 - 60))))", "format": "number", "default": 456, "optional": true, "maximum": 1460, "minimum": 0, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/lsn/tcp/mss-clamp`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "mss-clamp"
        self.a10_url="/axapi/v3/cgnv6/lsn/tcp/mss-clamp"
        self.DeviceProxy = ""
        self.mss_subtract = ""
        self.mss_value = ""
        self.mss_clamp_type = ""
        self.A10WW_min = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


