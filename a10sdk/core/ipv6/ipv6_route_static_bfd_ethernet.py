from a10sdk.common.A10BaseClass import A10BaseClass


class Ethernet(A10BaseClass):
    
    """Class Description::
    Ethernet interface.

    Class ethernet supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param eth_num: {"description": "Ethernet (not a member of vlan or trunk)", "format": "number", "type": "number", "maximum": 2147483647, "minimum": 0, "optional": false}
    :param nexthop_ipv6_ll: {"optional": false, "type": "string", "description": "Nexthop IPv6 address (Link-local)", "format": "ipv6-address"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/ipv6/route/static/bfd/ethernet/{eth_num}+{nexthop_ipv6_ll}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "eth_num","nexthop_ipv6_ll"]

        self.b_key = "ethernet"
        self.a10_url="/axapi/v3/ipv6/route/static/bfd/ethernet/{eth_num}+{nexthop_ipv6_ll}"
        self.DeviceProxy = ""
        self.eth_num = ""
        self.nexthop_ipv6_ll = ""
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


