from a10sdk.common.A10BaseClass import A10BaseClass


class Pptp(A10BaseClass):
    
    """Class Description::
    NAT64 PPTP ALG (default: disabled).

    Class pptp supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param pptp_enable: {"optional": true, "enum": ["enable"], "type": "string", "description": "'enable': Enable NAT64 PPTP ALG; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/nat64/alg/pptp`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "pptp"
        self.a10_url="/axapi/v3/cgnv6/nat64/alg/pptp"
        self.DeviceProxy = ""
        self.uuid = ""
        self.pptp_enable = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


