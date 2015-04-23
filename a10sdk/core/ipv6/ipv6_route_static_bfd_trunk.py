from a10sdk.common.A10BaseClass import A10BaseClass


class Trunk(A10BaseClass):
    
    """Class Description::
    Trunk interface.

    Class trunk supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param nexthop_ipv6_ll: {"optional": false, "type": "string", "description": "Nexthop IPv6 address (Link-local)", "format": "ipv6-address"}
    :param trunk_num: {"optional": false, "type": "number", "description": "Trunk interface", "format": "number"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/ipv6/route/static/bfd/trunk/{trunk_num}+{nexthop_ipv6_ll}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "trunk_num","nexthop_ipv6_ll"]

        self.b_key = "trunk"
        self.a10_url="/axapi/v3/ipv6/route/static/bfd/trunk/{trunk_num}+{nexthop_ipv6_ll}"
        self.DeviceProxy = ""
        self.nexthop_ipv6_ll = ""
        self.trunk_num = ""
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


