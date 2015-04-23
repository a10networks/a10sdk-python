from a10sdk.common.A10BaseClass import A10BaseClass


class Pptp(A10BaseClass):
    
    """Class Description::
    PPTP ALG Settings.

    Class pptp supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param pptp: {"description": "'disable': Disable PPTP NAT ALG; 'enable': Enable PPTP NAT ALG; ", "format": "enum", "default": "disable", "type": "string", "enum": ["disable", "enable"], "optional": true}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/ip/nat/alg/pptp`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "pptp"
        self.a10_url="/axapi/v3/ip/nat/alg/pptp"
        self.DeviceProxy = ""
        self.pptp = ""
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


