from a10sdk.common.A10BaseClass import A10BaseClass


class Rtsp(A10BaseClass):
    
    """Class Description::
    DS-Lite RTSP ALG (default: disabled).

    Class rtsp supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param rtsp_enable: {"optional": true, "enum": ["enable"], "type": "string", "description": "'enable': Enable ALG; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/ds-lite/alg/rtsp`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "rtsp"
        self.a10_url="/axapi/v3/cgnv6/ds-lite/alg/rtsp"
        self.DeviceProxy = ""
        self.rtsp_enable = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


