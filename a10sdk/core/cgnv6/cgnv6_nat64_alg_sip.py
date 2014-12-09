from a10sdk.common.A10BaseClass import A10BaseClass


class Sip(A10BaseClass):
    
    """Class Description::
    NAT64 SIP ALG (default: disabled).

    Class sip supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param sip_enable: {"optional": true, "enum": ["enable"], "type": "string", "description": "'enable': Enable NAT64 SIP ALG; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/nat64/alg/sip`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "sip"
        self.a10_url="/axapi/v3/cgnv6/nat64/alg/sip"
        self.DeviceProxy = ""
        self.sip_enable = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


