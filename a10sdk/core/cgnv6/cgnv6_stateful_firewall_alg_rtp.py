from a10sdk.common.A10BaseClass import A10BaseClass


class Rtp(A10BaseClass):
    
    """    :param rtp_stun_timeout: {"description": "RTP/RTCP STUN timeout (default: 5 minutes)}", "format": "number", "default": 5, "optional": true, "maximum": 10, "minimum": 2, "type": "number"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Configure FTP ALG for NAT stateful firewall (default: enabled).

    Class rtp supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/stateful-firewall/alg/rtp`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "rtp"
        self.a10_url="/axapi/v3/cgnv6/stateful-firewall/alg/rtp"
        self.DeviceProxy = ""
        self.rtp_stun_timeout = ""
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


