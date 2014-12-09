from a10sdk.common.A10BaseClass import A10BaseClass


class Ddos(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param outside: {"default": 0, "type": "number", "description": "DDoS outside (untrusted) interface", "format": "flag"}
    :param inside: {"default": 0, "type": "number", "description": "DDoS inside (trusted) interface", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ddos"
        self.DeviceProxy = ""
        self.outside = ""
        self.inside = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class AccessList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param acl_name: {"minLength": 1, "maxLength": 16, "type": "string", "description": "Apply an access list (Named Access List)", "format": "string"}
    :param acl_id: {"description": "ACL id", "format": "number", "maximum": 199, "minimum": 1, "type": "number", "$ref": "/axapi/v3/access-list/standard"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "access-list"
        self.DeviceProxy = ""
        self.acl_name = ""
        self.acl_id = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Icmpv6RateLimit(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param lockup_period_v6: {"description": "Lockup period (second)", "minimum": 1, "type": "number", "maximum": 16383, "format": "number"}
    :param normal_v6: {"description": "Normal rate limit. If exceeds this limit, drop the ICMP packet that goes over the limit", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}
    :param lockup_v6: {"description": "Enter lockup state when ICMP rate exceeds lockup rate limit (Maximum rate limit. If exceeds this limit, drop all ICMP packet for a time period)", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "icmpv6-rate-limit"
        self.DeviceProxy = ""
        self.lockup_period_v6 = ""
        self.normal_v6 = ""
        self.lockup_v6 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class MonitorList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param monitor_vlan: {"description": "VLAN number", "format": "number", "maximum": 4094, "minimum": 2, "type": "number", "plat-neg-list": ["non-fpga"]}
    :param monitor: {"description": "'input': Incoming packets; 'output': Outgoing packets; 'both': Both incoming and outgoing packets; ", "partition-visibility": "shared", "format": "enum", "enum": ["input", "output", "both"], "type": "string", "plat-neg-list": ["soft-ax"]}
    :param mirror_index: {"description": "Mirror index", "format": "number", "maximum": 4, "minimum": 1, "type": "number", "plat-neg-list": ["soft-ax"], "$ref": "/axapi/v3/mirror-port"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "monitor-list"
        self.DeviceProxy = ""
        self.monitor_vlan = ""
        self.monitor = ""
        self.mirror_index = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class IcmpRateLimit(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param lockup: {"description": "Enter lockup state when ICMP rate exceeds lockup rate limit (Maximum rate limit. If exceeds this limit, drop all ICMP packet for a time period)", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}
    :param lockup_period: {"description": "Lockup period (second)", "minimum": 1, "type": "number", "maximum": 16383, "format": "number"}
    :param normal: {"description": "Normal rate limit. If exceeds this limit, drop the ICMP packet that goes over the limit", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "icmp-rate-limit"
        self.DeviceProxy = ""
        self.lockup = ""
        self.lockup_period = ""
        self.normal = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Ethernet(A10BaseClass):
    
    """Class Description::
    Ethernet interface.

    Class ethernet supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param trap_source: {"default": 0, "optional": true, "type": "number", "description": "The trap source", "format": "flag"}
    :param speed: {"description": "'10': 10; '100': 100; '1000': 1000; 'auto': auto; ", "format": "enum", "default": "auto", "optional": true, "enum": ["10", "100", "1000", "auto"], "type": "string", "plat-neg-list": ["soft-ax"]}
    :param media_type_copper: {"description": "Set the media type to copper", "format": "flag", "default": 0, "type": "number", "optional": true, "plat-neg-list": ["non-fpga", "soft-ax"]}
    :param remove_vlan_tag: {"description": "Remove the vlan tag for egressing packets", "format": "flag", "default": 0, "type": "number", "optional": true, "plat-neg-list": ["non-fpga", "soft-ax"]}
    :param load_interval: {"description": "Configure Load Interval (Seconds (5-300, Multiple of 5), default 300)", "format": "number", "default": 300, "optional": true, "maximum": 300, "minimum": 5, "type": "number"}
    :param cpu_process: {"description": "All Packets to this port are processed by CPU", "format": "flag", "default": 0, "type": "number", "optional": true, "plat-neg-list": ["non-fpga", "soft-ax"]}
    :param trunk_group_list: {"minItems": 1, "items": {"type": "trunk-group"}, "uniqueItems": true, "array": [{"required": ["trunk-number"], "properties": {"trunk-number": {"description": "Trunk Number", "format": "number", "type": "number", "maximum": 16, "minimum": 1, "optional": false}, "udld-timeout-cfg": {"type": "object", "properties": {"slow": {"description": "slow timeout in unit of seconds", "format": "number", "default": 1, "maximum": 60, "minimum": 1, "not": "fast", "type": "number"}, "fast": {"description": "fast timeout in unit of milli-seconds", "format": "number", "default": 1000, "maximum": 1000, "minimum": 100, "not": "slow", "type": "number"}}}, "mode": {"description": "'active': enable initiation of LACP negotiation on a port(default); 'passive': disable initiation of LACP negotiation on a port; ", "format": "enum", "default": "active", "type": "string", "enum": ["active", "passive"], "optional": true}, "timeout": {"description": "'long': Set LACP long timeout (default); 'short': Set LACP short timeout; ", "format": "enum", "default": "long", "type": "string", "enum": ["long", "short"], "optional": true}, "type": {"description": "'static': Static (default); 'lacp': lacp; 'lacp-udld': lacp-udld; ", "format": "enum", "default": "static", "optional": true, "enum": ["static", "lacp", "lacp-udld"], "modify-not-allowed": 1, "type": "string"}, "admin-key": {"description": "LACP admin key (Admin key value)", "format": "number", "type": "number", "maximum": 65535, "minimum": 10000, "optional": true}, "port-priority": {"description": "Set LACP priority for a port (LACP port priority)", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": true}}}], "type": "array", "$ref": "/axapi/v3/interface/ethernet/{ifnum}/trunk-group/{trunk-number}"}
    :param l3_vlan_fwd_disable: {"default": 0, "optional": true, "type": "number", "format": "flag"}
    :param name: {"description": "Name for the interface", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 32, "type": "string"}
    :param duplexity: {"description": "'Full': Full; 'Half': Half; 'auto': auto; ", "format": "enum", "default": "auto", "optional": true, "enum": ["Full", "Half", "auto"], "type": "string", "plat-neg-list": ["soft-ax"]}
    :param mtu: {"platform-specific-range": 1, "platform-specific-default": 1, "description": "Interface mtu (Interface MTU, default 1500 (min MTU is 1280 for IPv6))", "format": "number", "optional": true, "type": "number"}
    :param ifnum: {"optional": false, "type": "number", "description": "Ethernet interface number", "format": "interface"}
    :param monitor_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "monitor-vlan": {"description": "VLAN number", "format": "number", "maximum": 4094, "minimum": 2, "type": "number", "plat-neg-list": ["non-fpga"]}, "monitor": {"description": "'input': Incoming packets; 'output': Outgoing packets; 'both': Both incoming and outgoing packets; ", "partition-visibility": "shared", "format": "enum", "enum": ["input", "output", "both"], "type": "string", "plat-neg-list": ["soft-ax"]}, "mirror-index": {"description": "Mirror index", "format": "number", "maximum": 4, "minimum": 1, "type": "number", "plat-neg-list": ["soft-ax"], "$ref": "/axapi/v3/mirror-port"}}}]}
    :param action: {"description": "'enable': Enable; 'disable': Disable; ", "format": "enum", "default": "disable", "type": "string", "enum": ["enable", "disable"], "optional": true}
    :param flow_control: {"description": "Enable 802.3x flow control on full duplex port", "format": "flag", "default": 0, "type": "number", "optional": true, "plat-neg-list": ["soft-ax"]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/interface/ethernet/{ifnum}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "ifnum"]

        self.b_key = "ethernet"
        self.a10_url="/axapi/v3/interface/ethernet/{ifnum}"
        self.DeviceProxy = ""
        self.trap_source = ""
        self.ip = {}
        self.ddos = {}
        self.access_list = {}
        self.speed = ""
        self.lldp = {}
        self.bfd = {}
        self.media_type_copper = ""
        self.remove_vlan_tag = ""
        self.load_interval = ""
        self.cpu_process = ""
        self.ipv6 = {}
        self.trunk_group_list = []
        self.l3_vlan_fwd_disable = ""
        self.isis = {}
        self.name = ""
        self.duplexity = ""
        self.icmpv6_rate_limit = {}
        self.mtu = ""
        self.ifnum = ""
        self.monitor_list = []
        self.lw_4o6 = {}
        self.action = ""
        self.icmp_rate_limit = {}
        self.flow_control = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


