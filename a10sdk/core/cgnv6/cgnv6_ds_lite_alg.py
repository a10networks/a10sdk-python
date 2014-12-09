from a10sdk.common.A10BaseClass import A10BaseClass


class Alg(A10BaseClass):
    
    """Class Description::
    DS-Lite ALG Parameters.

    Class alg supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/ds-lite/alg`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "alg"
        self.a10_url="/axapi/v3/cgnv6/ds-lite/alg"
        self.DeviceProxy = ""
        self.pptp = {}
        self.ftp = {}
        self.tftp = {}
        self.rtsp = {}
        self.sip = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


