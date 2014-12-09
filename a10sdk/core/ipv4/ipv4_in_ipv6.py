from a10sdk.common.A10BaseClass import A10BaseClass


class Ipv4InIpv6(A10BaseClass):
    
    """Class Description::
    Global IPv4-in-IPv6 configuration subcommands.

    Class ipv4-in-ipv6 supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/ipv4-in-ipv6`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "ipv4-in-ipv6"
        self.a10_url="/axapi/v3/ipv4-in-ipv6"
        self.DeviceProxy = ""
        
        for keys, value in kwargs.items():
            setattr(self,keys, value)


