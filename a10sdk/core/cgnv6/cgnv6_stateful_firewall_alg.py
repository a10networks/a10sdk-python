from a10sdk.common.A10BaseClass import A10BaseClass


class Alg(A10BaseClass):
    
    """Class Description::
    Configure ALGs for stateful firewall.

    Class alg supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/stateful-firewall/alg`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "alg"
        self.a10_url="/axapi/v3/cgnv6/stateful-firewall/alg"
        self.DeviceProxy = ""
        self.ftp = {}
        self.sip = {}
        self.pptp = {}
        self.rtsp = {}
        self.rtp = {}
        self.tftp = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


