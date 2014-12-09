from a10sdk.common.A10BaseClass import A10BaseClass


class Rtsp(A10BaseClass):
    
    """Class Description::
    Configure RTSP ALG for NAT stateful firewall (default: enabled).

    Class rtsp supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param rtsp_value: {"optional": true, "enum": ["disable"], "type": "string", "description": "'disable': Disable ALG; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/stateful-firewall/alg/rtsp`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "rtsp"
        self.a10_url="/axapi/v3/cgnv6/stateful-firewall/alg/rtsp"
        self.DeviceProxy = ""
        self.rtsp_value = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


