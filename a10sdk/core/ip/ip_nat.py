from a10sdk.common.A10BaseClass import A10BaseClass


class RangeListList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

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

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "range-list-list"
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


class Nat(A10BaseClass):
    
    """Class Description::
    Configure NAT.

    Class nat supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param range_list_list: {"minItems": 1, "items": {"type": "range-list"}, "uniqueItems": true, "array": [{"required": ["name"], "properties": {"global-start-ipv6-addr": {"optional": true, "modify-not-allowed": 1, "type": "string", "description": "Global Start IPv6 Address of this list", "format": "ipv6-address-plen"}, "v4-vrid": {"description": "VRRP-A vrid (Specify ha VRRP-A vrid)", "format": "number", "optional": true, "maximum": 31, "minimum": 1, "modify-not-allowed": 1, "type": "number"}, "global-netmaskv4": {"optional": true, "modify-not-allowed": 1, "type": "string", "description": "Mask for this Address range", "format": "ipv4-netmask"}, "local-start-ipv6-addr": {"optional": true, "modify-not-allowed": 1, "type": "string", "description": "Local Start IPv6 Address of this list", "format": "ipv6-address-plen"}, "local-netmaskv4": {"optional": true, "modify-not-allowed": 1, "type": "string", "description": "Mask for this Address range", "format": "ipv4-netmask"}, "local-start-ipv4-addr": {"optional": true, "modify-not-allowed": 1, "type": "string", "description": "Local Start IPv4 Address of this list", "format": "ipv4-address"}, "global-start-ipv4-addr": {"optional": true, "modify-not-allowed": 1, "type": "string", "description": "Global Start IPv4 Address of this list", "format": "ipv4-address"}, "v6-vrid": {"description": "VRRP-A vrid (Specify ha VRRP-A vrid)", "format": "number", "optional": true, "maximum": 31, "minimum": 1, "modify-not-allowed": 1, "type": "number"}, "v4-count": {"description": "Number of addresses to be translated in this range", "format": "number", "optional": true, "maximum": 200000, "minimum": 1, "modify-not-allowed": 1, "type": "number"}, "v6-count": {"description": "Number of addresses to be translated in this range", "format": "number", "optional": true, "maximum": 200000, "minimum": 1, "modify-not-allowed": 1, "type": "number"}, "name": {"description": "Name for this Static List", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/ip/nat/range-list/{name}"}
    :param pool_group_list: {"minItems": 1, "items": {"type": "pool-group"}, "uniqueItems": true, "array": [{"required": ["pool-group-name"], "properties": {"member-list": {"minItems": 1, "items": {"type": "member"}, "uniqueItems": true, "array": [{"required": ["pool-name"], "properties": {"pool-name": {"description": "Specify NAT pool name", "format": "string-rlx", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/ip/nat/pool-group/{pool-group-name}/member/{pool-name}"}, "pool-group-name": {"description": "Specify pool group name", "format": "string-rlx", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}, "vrid": {"description": "Specify VRRP-A vrid (Specify ha VRRP-A vrid)", "format": "number", "optional": true, "maximum": 31, "minimum": 1, "modify-not-allowed": 1, "type": "number"}}}], "type": "array", "$ref": "/axapi/v3/ip/nat/pool-group/{pool-group-name}"}
    :param pool_list: {"minItems": 1, "items": {"type": "pool"}, "uniqueItems": true, "array": [{"required": ["pool-name"], "properties": {"use-if-ip": {"description": "Use Interface IP", "format": "flag", "default": 0, "type": "number", "plat-pos-list": ["soft-ax"], "optional": true}, "start-address": {"optional": true, "modify-not-allowed": 1, "type": "string", "description": "Configure start IP address of NAT pool", "format": "ipv4-address"}, "vrid": {"description": "Configure VRRP-A vrid (Specify ha VRRP-A vrid)", "format": "number", "optional": true, "maximum": 31, "minimum": 1, "modify-not-allowed": 1, "type": "number"}, "netmask": {"optional": true, "modify-not-allowed": 1, "type": "string", "description": "Configure mask for pool", "format": "ipv4-netmask-brief"}, "end-address": {"optional": true, "modify-not-allowed": 1, "type": "string", "description": "Configure end IP address of NAT pool", "format": "ipv4-address"}, "ip-rr": {"description": "Use IP address round-robin behavior", "format": "flag", "default": 0, "type": "number", "modify-not-allowed": 1, "optional": true}, "ethernet": {"optional": true, "plat-pos-list": ["soft-ax"], "type": "number", "description": "Ethernet interface", "format": "interface"}, "gateway": {"optional": true, "modify-not-allowed": 1, "type": "string", "description": "Configure gateway IP", "format": "ipv4-address"}, "pool-name": {"description": "Specify pool name or pool group", "format": "string-rlx", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/ip/nat/pool/{pool-name}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/ip/nat`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "nat"
        self.a10_url="/axapi/v3/ip/nat"
        self.DeviceProxy = ""
        self.range_list_list = []
        self.alg = {}
        self.pool_group_list = []
        self.template = {}
        self.translation = {}
        self.icmp = {}
        self.inside = {}
        self.pool_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


