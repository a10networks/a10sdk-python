from a10sdk.common.A10BaseClass import A10BaseClass


class IcmpRateLimit(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param lockup: {"description": "Enter lockup state when ICMP rate exceeds lockup rate limit (Maximum rate limit. If exceeds this limit, drop all ICMP packet for a time period)", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}
    :param lockup_period: {"description": "Maximum rate limit. If exceeds this limit, drop all ICMP packet for a time period", "minimum": 1, "type": "number", "maximum": 16383, "format": "number"}
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


class Ddos(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param outside: {"default": 0, "type": "number", "description": "DDoS inside (trusted) or outside (untrusted) interface", "format": "flag"}
    :param inside: {"default": 0, "type": "number", "description": "DDoS inside (trusted) or outside (untrusted) interface", "format": "flag"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ddos"
        self.DeviceProxy = ""
        self.outside = ""
        self.inside = ""
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Trunk(A10BaseClass):
    
    """Class Description::
    Trunk interface.

    Class trunk supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param name: {"description": "Name for the interface", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 32, "type": "string"}
    :param trap_source: {"description": "The trap source", "partition-visibility": "shared", "default": 0, "type": "number", "format": "flag", "optional": true}
    :param timer: {"description": "Timer to re-check the threshold under certain conditions (Time in seconds (Default: 10))", "format": "number", "default": 10, "optional": true, "maximum": 300, "minimum": 1, "type": "number"}
    :param mtu: {"platform-specific-range": 1, "platform-specific-default": 1, "description": "Interface mtu (Interface MTU, default 1500 (min MTU is 1280 for IPv6))", "format": "number", "optional": true, "type": "number"}
    :param ports_threshold: {"platform-specific-range": 1, "platform-specific-default": 1, "description": "Threshold for the minimum number of ports that need to be UP for the trunk to remain UP", "format": "number", "optional": true, "type": "number"}
    :param ifnum: {"optional": false, "type": "number", "description": "Trunk interface number", "format": "number"}
    :param do_auto_recovery: {"default": 0, "optional": true, "type": "number", "description": "(Only for LACP trunks) Attempt auto-recovery after ports-treshold is triggered", "format": "flag"}
    :param action: {"optional": true, "enum": ["enable", "disable"], "type": "string", "description": "'enable': Enable; 'disable': Disable; ", "format": "enum"}
    :param l3_vlan_fwd_disable: {"default": 0, "optional": true, "type": "number", "description": "Disable L3 forwarding between VLANs", "format": "flag"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/interface/trunk/{ifnum}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "ifnum"]

        self.b_key = "trunk"
        self.a10_url="/axapi/v3/interface/trunk/{ifnum}"
        self.DeviceProxy = ""
        self.icmp_rate_limit = {}
        self.isis = {}
        self.name = ""
        self.trap_source = ""
        self.bfd = {}
        self.ip = {}
        self.access_list = {}
        self.icmpv6_rate_limit = {}
        self.timer = ""
        self.mtu = ""
        self.ports_threshold = ""
        self.ifnum = ""
        self.lw_4o6 = {}
        self.do_auto_recovery = ""
        self.ipv6 = {}
        self.action = ""
        self.l3_vlan_fwd_disable = ""
        self.ddos = {}
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


