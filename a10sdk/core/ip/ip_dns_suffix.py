from a10sdk.common.A10BaseClass import A10BaseClass


class Suffix(A10BaseClass):
    
    """Class Description::
    DNS suffix.

    Class suffix supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param domain_name: {"description": "DNS suffix", "format": "string", "minLength": 1, "optional": true, "maxLength": 32, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/ip/dns/suffix`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "suffix"
        self.a10_url="/axapi/v3/ip/dns/suffix"
        self.DeviceProxy = ""
        self.domain_name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


