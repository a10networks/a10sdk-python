from a10sdk.common.A10BaseClass import A10BaseClass


class Domain(A10BaseClass):
    
    """Class Description::
    sixrd Domain.

    Class domain supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param ipv6_prefix: {"optional": true, "type": "string", "description": "IPv6 prefix", "format": "ipv6-address-plen"}
    :param name: {"description": "6rd Domain name", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param mtu: {"description": "Tunnel MTU", "format": "number", "type": "number", "maximum": 1480, "minimum": 1280, "optional": true}
    :param ce_ipv4_netmask: {"optional": true, "type": "string", "description": "Mask length", "format": "ipv4-netmask-brief"}
    :param ce_ipv4_network: {"optional": true, "type": "string", "description": "Customer Edge IPv4 network", "format": "ipv4-address"}
    :param br_ipv4_address: {"optional": true, "type": "string", "description": "6rd BR IPv4 address", "format": "ipv4-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/sixrd/domain/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "domain"
        self.a10_url="/axapi/v3/cgnv6/sixrd/domain/{name}"
        self.DeviceProxy = ""
        self.ipv6_prefix = ""
        self.name = ""
        self.mtu = ""
        self.ce_ipv4_netmask = ""
        self.ce_ipv4_network = ""
        self.br_ipv4_address = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


