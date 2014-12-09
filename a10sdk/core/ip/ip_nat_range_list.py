from a10sdk.common.A10BaseClass import A10BaseClass


class RangeList(A10BaseClass):
    
    """Class Description::
    IP Source NAT Static range list.

    Class range-list supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param global_start_ipv6_addr: {"optional": true, "modify-not-allowed": 1, "type": "string", "description": "Global Start IPv6 Address of this list", "format": "ipv6-address-plen"}
    :param v4_vrid: {"description": "VRRP-A vrid (Specify ha VRRP-A vrid)", "format": "number", "optional": true, "maximum": 31, "minimum": 1, "modify-not-allowed": 1, "type": "number"}
    :param global_netmaskv4: {"optional": true, "modify-not-allowed": 1, "type": "string", "description": "Mask for this Address range", "format": "ipv4-netmask"}
    :param local_start_ipv6_addr: {"optional": true, "modify-not-allowed": 1, "type": "string", "description": "Local Start IPv6 Address of this list", "format": "ipv6-address-plen"}
    :param local_netmaskv4: {"optional": true, "modify-not-allowed": 1, "type": "string", "description": "Mask for this Address range", "format": "ipv4-netmask"}
    :param local_start_ipv4_addr: {"optional": true, "modify-not-allowed": 1, "type": "string", "description": "Local Start IPv4 Address of this list", "format": "ipv4-address"}
    :param global_start_ipv4_addr: {"optional": true, "modify-not-allowed": 1, "type": "string", "description": "Global Start IPv4 Address of this list", "format": "ipv4-address"}
    :param v6_vrid: {"description": "VRRP-A vrid (Specify ha VRRP-A vrid)", "format": "number", "optional": true, "maximum": 31, "minimum": 1, "modify-not-allowed": 1, "type": "number"}
    :param v4_count: {"description": "Number of addresses to be translated in this range", "format": "number", "optional": true, "maximum": 200000, "minimum": 1, "modify-not-allowed": 1, "type": "number"}
    :param v6_count: {"description": "Number of addresses to be translated in this range", "format": "number", "optional": true, "maximum": 200000, "minimum": 1, "modify-not-allowed": 1, "type": "number"}
    :param name: {"description": "Name for this Static List", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/ip/nat/range-list/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "range-list"
        self.a10_url="/axapi/v3/ip/nat/range-list/{name}"
        self.DeviceProxy = ""
        self.global_start_ipv6_addr = ""
        self.v4_vrid = ""
        self.global_netmaskv4 = ""
        self.local_start_ipv6_addr = ""
        self.local_netmaskv4 = ""
        self.local_start_ipv4_addr = ""
        self.global_start_ipv4_addr = ""
        self.v6_vrid = ""
        self.v4_count = ""
        self.v6_count = ""
        self.name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


