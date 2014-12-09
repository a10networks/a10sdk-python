from a10sdk.common.A10BaseClass import A10BaseClass


class Rtsp(A10BaseClass):
    
    """Class Description::
    RTSP type.

    Class rtsp supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param rtsp_port: {"description": "Specify RTSP port, default is 554 (Port Number (default 554))", "format": "number", "default": 554, "optional": true, "maximum": 65534, "minimum": 1, "type": "number"}
    :param rtsp: {"default": 0, "optional": true, "type": "number", "description": "RTSP type", "format": "flag"}
    :param rtspurl: {"description": "Specify URL string (Specify the path on the server)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 127, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/health/monitor/{name}/method/rtsp`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "rtsp"
        self.a10_url="/axapi/v3/health/monitor/{name}/method/rtsp"
        self.DeviceProxy = ""
        self.rtsp_port = ""
        self.rtsp = ""
        self.rtspurl = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


