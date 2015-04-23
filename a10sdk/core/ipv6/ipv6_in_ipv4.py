from a10sdk.common.A10BaseClass import A10BaseClass


class Ipv6InIpv4(A10BaseClass):
    
    """    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Global IPv4-in-IPv6 configuration subcommands.

    Class ipv6-in-ipv4 supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/ipv6-in-ipv4`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "ipv6-in-ipv4"
        self.a10_url="/axapi/v3/ipv6-in-ipv4"
        self.DeviceProxy = ""
        self.frag = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


