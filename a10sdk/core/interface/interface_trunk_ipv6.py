from a10sdk.common.A10BaseClass import A10BaseClass


class AddressList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param address_type: {"enum": ["anycast", "link-local"], "type": "string", "description": "'anycast': Configure an IPv6 anycast address; 'link-local': Configure an IPv6 link local address; ", "format": "enum"}
    :param ipv6_addr: {"type": "string", "description": "Set the IPv6 address of an interface", "format": "ipv6-address-plen"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "address-list"
        self.DeviceProxy = ""
        self.address_type = ""
        self.ipv6_addr = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Vrid(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param use_floating_ip_default_vrid: {"default": 0, "type": "number", "description": "Use a floating IP as the source address for Router advertisements", "format": "flag"}
    :param adver_vrid: {"description": "Specify ha VRRP-A vrid", "format": "number", "maximum": 31, "minimum": 1, "not": "adver-vrid-default", "type": "number"}
    :param floating_ip_default_vrid: {"type": "string", "description": "Use a floating IP as the source address for Router advertisements", "format": "ipv6-address"}
    :param adver_vrid_default: {"default": 0, "not": "adver-vrid", "type": "number", "description": "Default VRRP-A vrid", "format": "flag"}
    :param floating_ip: {"type": "string", "description": "Use a floating IP as the source address for Router advertisements", "format": "ipv6-address"}
    :param use_floating_ip: {"default": 0, "type": "number", "description": "Use a floating IP as the source address for Router advertisements", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "vrid"
        self.DeviceProxy = ""
        self.use_floating_ip_default_vrid = ""
        self.adver_vrid = ""
        self.floating_ip_default_vrid = ""
        self.adver_vrid_default = ""
        self.floating_ip = ""
        self.use_floating_ip = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class PrefixList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param not_autonomous: {"default": 0, "type": "number", "description": "Specify that the Prefix is not usable for autoconfiguration (default:autonomous)", "format": "flag"}
    :param valid_lifetime: {"description": "Specify Valid Lifetime (default:2592000) (Prefix Advertised Valid Lifetime (default: 2592000))", "format": "number", "default": 2592000, "maximum": 4294967295, "minimum": 0, "type": "number"}
    :param not_on_link: {"default": 0, "type": "number", "description": "Specify that the Prefix is not On-Link (default: on-link)", "format": "flag"}
    :param prefix: {"type": "string", "description": "Set Router Advertisement On-Link Prefix (IPv6 On-Link Prefix)", "format": "ipv6-address-plen"}
    :param preferred_lifetime: {"description": "Specify Prefix Preferred Lifetime (default:604800) (Prefix Advertised Preferred Lifetime (default: 604800))", "format": "number", "default": 604800, "maximum": 4294967295, "minimum": 0, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "prefix-list"
        self.DeviceProxy = ""
        self.not_autonomous = ""
        self.valid_lifetime = ""
        self.not_on_link = ""
        self.prefix = ""
        self.preferred_lifetime = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Mtu(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param adver_mtu: {"platform-specific-range": 1, "platform-specific-default": 1, "description": "Set Router Advertisement MTU Option", "format": "number", "not": "adver-mtu-disable", "type": "number"}
    :param adver_mtu_disable: {"default": 0, "not": "adver-mtu", "type": "number", "description": "Disable Router Advertisement MTU Option", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "mtu"
        self.DeviceProxy = ""
        self.adver_mtu = ""
        self.adver_mtu_disable = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class HaGroupId(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ha_use_floating_ip: {"default": 0, "type": "number", "description": "Use a floating IP as the source address for Router advertisements", "format": "flag"}
    :param adver_ha_group_id: {"description": "HA Group ID", "minimum": 1, "type": "number", "maximum": 31, "format": "number"}
    :param ha_floating_ip: {"type": "string", "description": "Use a floating IP as the source address for Router advertisements", "format": "ipv6-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ha-group-id"
        self.DeviceProxy = ""
        self.ha_use_floating_ip = ""
        self.adver_ha_group_id = ""
        self.ha_floating_ip = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class RouterAdver(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param max_interval: {"description": "Set Router Advertisement Max Interval (default: 600) (Min Router Advertisement Interval (seconds))", "format": "number", "default": 600, "maximum": 1800, "minimum": 4, "type": "number"}
    :param default_lifetime: {"description": "Set Router Advertisement Default Lifetime (default: 1800) (Default Lifetime (seconds))", "format": "number", "default": 1800, "maximum": 9000, "minimum": 0, "type": "number"}
    :param reachable_time: {"description": "Set Router Advertisement Reachable ime (default: 0) (Reachable Time (milliseconds))", "format": "number", "default": 0, "maximum": 3600000, "minimum": 0, "type": "number"}
    :param prefix_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"not-autonomous": {"default": 0, "type": "number", "description": "Specify that the Prefix is not usable for autoconfiguration (default:autonomous)", "format": "flag"}, "valid-lifetime": {"description": "Specify Valid Lifetime (default:2592000) (Prefix Advertised Valid Lifetime (default: 2592000))", "format": "number", "default": 2592000, "maximum": 4294967295, "minimum": 0, "type": "number"}, "not-on-link": {"default": 0, "type": "number", "description": "Specify that the Prefix is not On-Link (default: on-link)", "format": "flag"}, "prefix": {"type": "string", "description": "Set Router Advertisement On-Link Prefix (IPv6 On-Link Prefix)", "format": "ipv6-address-plen"}, "preferred-lifetime": {"description": "Specify Prefix Preferred Lifetime (default:604800) (Prefix Advertised Preferred Lifetime (default: 604800))", "format": "number", "default": 604800, "maximum": 4294967295, "minimum": 0, "type": "number"}, "optional": true}}]}
    :param rate_limit: {"description": "Rate Limit the processing of incoming Router Solicitations (Max Number of Router Solicitations to process per second)", "format": "number", "default": 100000, "maximum": 100000, "minimum": 1, "type": "number"}
    :param min_interval: {"description": "Set Router Advertisement Min Interval (default: 200) (Max Number of Router Solicitations to process per second)", "format": "number", "default": 200, "maximum": 1350, "minimum": 3, "type": "number"}
    :param action: {"default": "enable", "enum": ["enable", "disable"], "type": "string", "description": "'enable': Enable Router Advertisements on this interface; 'disable': Disable Router Advertisements on this interface; ", "format": "enum"}
    :param retransmit_timer: {"description": "Set Router Advertisement Retransmit Timer (default: 0)", "format": "number", "default": 0, "maximum": 4294967295, "minimum": 0, "type": "number"}
    :param hop_limit: {"description": "Set Router Advertisement Hop Limit (default: 255) (Max Router Advertisement Interval (seconds))", "format": "number", "default": 255, "maximum": 255, "minimum": 0, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "router-adver"
        self.DeviceProxy = ""
        self.max_interval = ""
        self.default_lifetime = ""
        self.reachable_time = ""
        self.vrid = {}
        self.prefix_list = []
        self.rate_limit = ""
        self.mtu = {}
        self.min_interval = ""
        self.action = ""
        self.retransmit_timer = ""
        self.ha_group_id = {}
        self.hop_limit = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Nat(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param inside: {"default": 0, "type": "number", "description": "Configure interface as NAT inside", "format": "flag"}
    :param outside: {"default": 0, "type": "number", "description": "Configure interface as NAT outside", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "nat"
        self.DeviceProxy = ""
        self.inside = ""
        self.outside = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class AccessListCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param inbound: {"default": 0, "type": "number", "description": "ACL applied on incoming packets to this interface", "format": "flag"}
    :param v6_acl_name: {"description": "Apply ACL rules to incoming packets on this interface (Named Access List)", "format": "string", "minLength": 1, "maxLength": 16, "type": "string", "$ref": "/axapi/v3/ipv6/access-list"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "access-list-cfg"
        self.DeviceProxy = ""
        self.inbound = ""
        self.v6_acl_name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Ipv6(A10BaseClass):
    
    """Class Description::
    Global IPv6 configuration subcommands.

    Class ipv6 supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param address_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"address-type": {"enum": ["anycast", "link-local"], "type": "string", "description": "'anycast': Configure an IPv6 anycast address; 'link-local': Configure an IPv6 link local address; ", "format": "enum"}, "ipv6-addr": {"type": "string", "description": "Set the IPv6 address of an interface", "format": "ipv6-address-plen"}, "optional": true}}]}
    :param ipv6_enable: {"default": 0, "optional": true, "type": "number", "description": "Enable IPv6 processing", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/interface/trunk/{ifnum}/ipv6`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "ipv6"
        self.a10_url="/axapi/v3/interface/trunk/{ifnum}/ipv6"
        self.DeviceProxy = ""
        self.uuid = ""
        self.address_list = []
        self.router_adver = {}
        self.rip = {}
        self.ipv6_enable = ""
        self.stateful_firewall = {}
        self.nat = {}
        self.router = {}
        self.access_list_cfg = {}
        self.ospf = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


