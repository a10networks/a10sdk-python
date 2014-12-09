from a10sdk.common.A10BaseClass import A10BaseClass


class BfdIpv6(A10BaseClass):
    
    """Class Description::
    Bidirectional Forwarding Detection.

    Class bfd-ipv6 supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param local_ipv6: {"optional": false, "type": "string", "description": "Local IPv6 address", "format": "ipv6-address"}
    :param nexthop_ipv6: {"optional": false, "type": "string", "description": "Nexthop IPv6 address", "format": "ipv6-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/ipv6/route/static/bfd/bfd-ipv6/{local_ipv6}+{nexthop_ipv6}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "local_ipv6","nexthop_ipv6"]

        self.b_key = "bfd-ipv6"
        self.a10_url="/axapi/v3/ipv6/route/static/bfd/bfd-ipv6/{local_ipv6}+{nexthop_ipv6}"
        self.DeviceProxy = ""
        self.local_ipv6 = ""
        self.nexthop_ipv6 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


