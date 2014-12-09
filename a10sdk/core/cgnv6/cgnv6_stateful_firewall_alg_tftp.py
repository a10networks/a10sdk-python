from a10sdk.common.A10BaseClass import A10BaseClass


class Tftp(A10BaseClass):
    
    """Class Description::
    Configure TFTP ALG for NAT stateful firewall (default: enabled).

    Class tftp supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param tftp_value: {"optional": true, "enum": ["disable"], "type": "string", "description": "'disable': Disable ALG; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/stateful-firewall/alg/tftp`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "tftp"
        self.a10_url="/axapi/v3/cgnv6/stateful-firewall/alg/tftp"
        self.DeviceProxy = ""
        self.tftp_value = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


