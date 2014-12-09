from a10sdk.common.A10BaseClass import A10BaseClass


class Sip(A10BaseClass):
    
    """Class Description::
    Change LSN SIP ALG Settings.

    Class sip supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param sip_value: {"optional": true, "enum": ["enable"], "type": "string", "description": "'enable': Enable SIP ALG for LSN; ", "format": "enum"}
    :param rtp_stun_timeout: {"description": "RTP/RTCP STUN timeout in minutes (Default is 5 minutes)", "format": "number", "default": 5, "optional": true, "maximum": 10, "minimum": 2, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/lsn/alg/sip`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "sip"
        self.a10_url="/axapi/v3/cgnv6/lsn/alg/sip"
        self.DeviceProxy = ""
        self.sip_value = ""
        self.rtp_stun_timeout = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


