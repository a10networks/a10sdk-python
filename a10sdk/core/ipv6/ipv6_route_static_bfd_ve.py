from a10sdk.common.A10BaseClass import A10BaseClass


class Ve(A10BaseClass):
    
    """Class Description::
    Virtual ethernet interface.

    Class ve supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param nexthop_ipv6_ll: {"optional": false, "type": "string", "description": "Nexthop IPv6 address (Link-local)", "format": "ipv6-address"}
    :param ve_num: {"optional": false, "type": "number", "description": "Virtual ethernet interface", "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/ipv6/route/static/bfd/ve/{ve_num}+{nexthop_ipv6_ll}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "ve_num","nexthop_ipv6_ll"]

        self.b_key = "ve"
        self.a10_url="/axapi/v3/ipv6/route/static/bfd/ve/{ve_num}+{nexthop_ipv6_ll}"
        self.DeviceProxy = ""
        self.nexthop_ipv6_ll = ""
        self.ve_num = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


