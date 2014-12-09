from a10sdk.common.A10BaseClass import A10BaseClass


class ExtcommunityLStdCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param exact_match: {"default": 0, "type": "number", "description": "Do exact matching of ecommunities", "format": "flag"}
    :param l_std: {"description": "Community-list number (standard)", "format": "number", "not-list": ["l-ext", "name"], "maximum": 99, "minimum": 1, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "extcommunity-l-std-cfg"
        self.DeviceProxy = ""
        self.exact_match = ""
        self.l_std = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class ExtcommunityLName(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param exact_match: {"default": 0, "type": "number", "description": "Do exact matching of ecommunities", "format": "flag"}
    :param name: {"description": "Community-list name", "format": "string", "minLength": 1, "not-list": ["l-std", "l-ext"], "maxLength": 128, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "extcommunity-l-name"
        self.DeviceProxy = ""
        self.exact_match = ""
        self.name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class ExtcommunityLExtCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param exact_match: {"default": 0, "type": "number", "description": "Do exact matching of ecommunities", "format": "flag"}
    :param l_ext: {"description": "Community-list number (expanded)", "format": "number", "not-list": ["l-std", "name"], "maximum": 199, "minimum": 100, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "extcommunity-l-ext-cfg"
        self.DeviceProxy = ""
        self.exact_match = ""
        self.l_ext = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Extcommunity(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "extcommunity"
        self.DeviceProxy = ""
        self.extcommunity_l_std_cfg = {}
        self.extcommunity_l_name = {}
        self.extcommunity_l_ext_cfg = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Origin(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param egp: {"default": 0, "not-list": ["igp", "incomplete"], "type": "number", "description": "remote EGP", "format": "flag"}
    :param incomplete: {"default": 0, "not-list": ["egp", "igp"], "type": "number", "description": "unknown heritage", "format": "flag"}
    :param igp: {"default": 0, "not-list": ["egp", "incomplete"], "type": "number", "description": "local IGP", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "origin"
        self.DeviceProxy = ""
        self.egp = ""
        self.incomplete = ""
        self.igp = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Group(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param group_id: {"description": "HA or VRRP-A group id", "minimum": 0, "type": "number", "maximum": 31, "format": "number"}
    :param ha_state: {"enum": ["active", "standby"], "type": "string", "description": "'active': HA or VRRP-A in Active State; 'standby': HA or VRRP-A in Standby State; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "group"
        self.DeviceProxy = ""
        self.group_id = ""
        self.ha_state = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Peer(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param acl1: {"description": "IP access-list number", "format": "number", "not-list": ["acl2", "name"], "maximum": 199, "minimum": 1, "type": "number"}
    :param acl2: {"description": "IP access-list number (expanded range)", "format": "number", "not-list": ["acl1", "name"], "maximum": 2699, "minimum": 1300, "type": "number"}
    :param name: {"description": "IP access-list name", "format": "string", "minLength": 1, "not-list": ["acl1", "acl2"], "maxLength": 128, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "peer"
        self.DeviceProxy = ""
        self.acl1 = ""
        self.acl2 = ""
        self.name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class PrefixList1(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param name: {"minLength": 1, "maxLength": 128, "type": "string", "description": "IP prefix-list name", "format": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "prefix-list-1"
        self.DeviceProxy = ""
        self.name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class NextHop(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param acl1: {"description": "IP access-list number", "format": "number", "not-list": ["acl2", "name"], "maximum": 199, "minimum": 1, "type": "number"}
    :param acl2: {"description": "IP access-list number (expanded range)", "format": "number", "not-list": ["acl1", "name"], "maximum": 2699, "minimum": 1300, "type": "number"}
    :param name: {"description": "IP access-list name", "format": "string", "minLength": 1, "not-list": ["acl1", "acl2"], "maxLength": 128, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "next-hop"
        self.DeviceProxy = ""
        self.acl1 = ""
        self.acl2 = ""
        self.name = ""
        self.prefix_list_1 = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class PrefixList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param name: {"minLength": 1, "maxLength": 128, "type": "string", "description": "IP prefix-list name", "format": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "prefix-list"
        self.DeviceProxy = ""
        self.name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Address(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param acl1: {"description": "IP access-list number", "format": "number", "not-list": ["acl2", "name"], "maximum": 199, "minimum": 1, "type": "number"}
    :param acl2: {"description": "IP access-list number (expanded range)", "format": "number", "not-list": ["acl1", "name"], "maximum": 2699, "minimum": 1300, "type": "number"}
    :param name: {"description": "IP access-list name", "format": "string", "minLength": 1, "not-list": ["acl1", "acl2"], "maxLength": 128, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "address"
        self.DeviceProxy = ""
        self.acl1 = ""
        self.acl2 = ""
        self.prefix_list = {}
        self.name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Ip(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ip"
        self.DeviceProxy = ""
        self.peer = {}
        self.next_hop = {}
        self.address = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Metric(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param value: {"description": "Metric value", "minimum": 0, "type": "number", "maximum": 4294967295, "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "metric"
        self.DeviceProxy = ""
        self.value = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class NextHop1(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param prefix_list_name: {"minLength": 1, "maxLength": 128, "type": "string", "description": "IPv6 prefix-list name", "format": "string"}
    :param v6_addr: {"not": "next-hop-acl-name", "type": "string", "description": "IPv6 address of next hop", "format": "ipv6-address"}
    :param next_hop_acl_name: {"description": "IPv6 access-list name", "format": "string", "minLength": 1, "maxLength": 128, "not": "v6-addr", "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "next-hop-1"
        self.DeviceProxy = ""
        self.prefix_list_name = ""
        self.v6_addr = ""
        self.next_hop_acl_name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Peer1(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param acl1: {"description": "IPv6 access-list number", "format": "number", "not-list": ["acl2", "name"], "maximum": 199, "minimum": 1, "type": "number"}
    :param acl2: {"description": "IP access-list number (expanded range)", "format": "number", "not-list": ["acl1", "name"], "maximum": 2699, "minimum": 1300, "type": "number"}
    :param name: {"description": "IP access-list name", "format": "string", "minLength": 1, "not-list": ["acl1", "acl2"], "maxLength": 128, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "peer-1"
        self.DeviceProxy = ""
        self.acl1 = ""
        self.acl2 = ""
        self.name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class PrefixList2(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param name: {"minLength": 1, "maxLength": 128, "type": "string", "description": "IPv6 prefix-list name", "format": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "prefix-list-2"
        self.DeviceProxy = ""
        self.name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Address1(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param name: {"minLength": 1, "maxLength": 128, "type": "string", "description": "IPv6 access-list name", "format": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "address-1"
        self.DeviceProxy = ""
        self.name = ""
        self.prefix_list_2 = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Ipv6(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ipv6"
        self.DeviceProxy = ""
        self.next_hop_1 = {}
        self.peer_1 = {}
        self.address_1 = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class LStdCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param exact_match: {"default": 0, "type": "number", "description": "Do exact matching of ecommunities", "format": "flag"}
    :param l_std: {"description": "Community-list number (standard)", "format": "number", "not-list": ["l-ext", "name"], "maximum": 99, "minimum": 1, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "l-std-cfg"
        self.DeviceProxy = ""
        self.exact_match = ""
        self.l_std = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class NameCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param exact_match: {"default": 0, "type": "number", "description": "Do exact matching of ecommunities", "format": "flag"}
    :param name: {"description": "Community-list name", "format": "string", "minLength": 1, "not-list": ["l-std", "l-ext"], "maxLength": 128, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "name-cfg"
        self.DeviceProxy = ""
        self.exact_match = ""
        self.name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class LExtCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param exact_match: {"default": 0, "type": "number", "description": "Do exact matching of ecommunities", "format": "flag"}
    :param l_ext: {"description": "Community-list number (expanded)", "format": "number", "not-list": ["l-std", "name"], "maximum": 199, "minimum": 100, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "l-ext-cfg"
        self.DeviceProxy = ""
        self.exact_match = ""
        self.l_ext = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Community(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "community"
        self.DeviceProxy = ""
        self.l_std_cfg = {}
        self.name_cfg = {}
        self.l_ext_cfg = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class LocalPreference(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param val: {"description": "Preference value", "minimum": 0, "type": "number", "maximum": 4294967295, "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "local-preference"
        self.DeviceProxy = ""
        self.val = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class External(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param value: {"enum": ["type-1", "type-2"], "type": "string", "description": "'type-1': Match OSPF External Type 1 metrics; 'type-2': Match OSPF External Type 2 metrics; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "external"
        self.DeviceProxy = ""
        self.value = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class RouteType(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "route-type"
        self.DeviceProxy = ""
        self.external = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Tag(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param value: {"description": "Tag value", "minimum": 0, "type": "number", "maximum": 4294967295, "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "tag"
        self.DeviceProxy = ""
        self.value = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class AsPath(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param name: {"minLength": 1, "maxLength": 128, "type": "string", "description": "AS path access-list name", "format": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "as-path"
        self.DeviceProxy = ""
        self.name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Interface(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ethernet: {"not-list": ["loopback", "trunk", "ve"], "type": "number", "description": "Ethernet interface (Port number)", "format": "interface"}
    :param trunk: {"description": "Trunk Interface (Trunk interface number)", "format": "number", "not-list": ["ethernet", "loopback", "ve"], "maximum": 16, "minimum": 1, "type": "number"}
    :param ve: {"description": "Virtual ethernet interface (Virtual ethernet interface number)", "format": "number", "not-list": ["ethernet", "loopback", "trunk"], "maximum": 4094, "minimum": 2, "type": "number"}
    :param loopback: {"description": "Loopback interface (Port number)", "format": "number", "not-list": ["ethernet", "trunk", "ve"], "maximum": 10, "minimum": 1, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "interface"
        self.DeviceProxy = ""
        self.ethernet = ""
        self.trunk = ""
        self.ve = ""
        self.loopback = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Match(A10BaseClass):
    
    """Class Description::
    Match values from routing table.

    Class match supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/route-map/{tag}+{action}+{sequence}/match`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "match"
        self.a10_url="/axapi/v3/route-map/{tag}+{action}+{sequence}/match"
        self.DeviceProxy = ""
        self.extcommunity = {}
        self.origin = {}
        self.group = {}
        self.ip = {}
        self.metric = {}
        self.ipv6 = {}
        self.community = {}
        self.local_preference = {}
        self.route_type = {}
        self.tag = {}
        self.as_path = {}
        self.interface = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


