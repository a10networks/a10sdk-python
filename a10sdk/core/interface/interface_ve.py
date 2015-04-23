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


class AccessList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param acl_name: {"minLength": 1, "maxLength": 16, "type": "string", "description": "Named Access List", "format": "string"}
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


class SamplingEnable(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param counters1: {"enum": ["all", "num_pkts", "num_total_bytes", "num_unicast_pkts", "num_broadcast_pkts", "num_multicast_pkts", "num_tx_pkts", "num_total_tx_bytes", "num_unicast_tx_pkts", "num_broadcast_tx_pkts", "num_multicast_tx_pkts", "rate_pkt_sent", "rate_byte_sent", "rate_pkt_rcvd", "rate_byte_rcvd", "load_interval"], "type": "string", "description": "'all': all; 'num_pkts': Input packets; 'num_total_bytes': Input bytes; 'num_unicast_pkts': Received unicasts; 'num_broadcast_pkts': Received braodcasts; 'num_multicast_pkts': Received multicasts; 'num_tx_pkts': Transmitted packtes; 'num_total_tx_bytes': Transmitte bytes; 'num_unicast_tx_pkts': Trasnmitted unicasts; 'num_broadcast_tx_pkts': Transmitted broadcasts; 'num_multicast_tx_pkts': Transmitted multicasts; 'rate_pkt_sent': Packet sent rate packets/sec; 'rate_byte_sent': Byte sent rate bits/sec; 'rate_pkt_rcvd': Packet received rate packets/sec; 'rate_byte_rcvd': Byte received rate bits/sec; 'load_interval': Load Interval; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "sampling-enable"
        self.DeviceProxy = ""
        self.counters1 = ""

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


class Ve(A10BaseClass):
    
    """Class Description::
    Virtual ethernet interface.

    Class ve supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param name: {"description": "Name for the interface", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 32, "type": "string"}
    :param trap_source: {"description": "The trap source", "partition-visibility": "shared", "default": 0, "type": "number", "format": "flag", "optional": true}
    :param mtu: {"platform-specific-range": 1, "platform-specific-default": 1, "description": "Interface mtu (Interface MTU, default 1500 (min MTU is 1280 for IPv6))", "format": "number", "optional": true, "type": "number"}
    :param ifnum: {"optional": false, "$ref": "/axapi/v3/network/vlan", "type": "number", "description": "Virtual ethernet interface number", "format": "number"}
    :param sampling_enable: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "num_pkts", "num_total_bytes", "num_unicast_pkts", "num_broadcast_pkts", "num_multicast_pkts", "num_tx_pkts", "num_total_tx_bytes", "num_unicast_tx_pkts", "num_broadcast_tx_pkts", "num_multicast_tx_pkts", "rate_pkt_sent", "rate_byte_sent", "rate_pkt_rcvd", "rate_byte_rcvd", "load_interval"], "type": "string", "description": "'all': all; 'num_pkts': Input packets; 'num_total_bytes': Input bytes; 'num_unicast_pkts': Received unicasts; 'num_broadcast_pkts': Received braodcasts; 'num_multicast_pkts': Received multicasts; 'num_tx_pkts': Transmitted packtes; 'num_total_tx_bytes': Transmitte bytes; 'num_unicast_tx_pkts': Trasnmitted unicasts; 'num_broadcast_tx_pkts': Transmitted broadcasts; 'num_multicast_tx_pkts': Transmitted multicasts; 'rate_pkt_sent': Packet sent rate packets/sec; 'rate_byte_sent': Byte sent rate bits/sec; 'rate_pkt_rcvd': Packet received rate packets/sec; 'rate_byte_rcvd': Byte received rate bits/sec; 'load_interval': Load Interval; ", "format": "enum"}}}]}
    :param action: {"optional": true, "enum": ["enable", "disable"], "type": "string", "description": "'enable': Enable; 'disable': Disable; ", "format": "enum"}
    :param l3_vlan_fwd_disable: {"default": 0, "optional": true, "type": "number", "description": "Disable L3 forwarding between VLANs for incoming packets on this interface", "format": "flag"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/interface/ve/{ifnum}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "ifnum"]

        self.b_key = "ve"
        self.a10_url="/axapi/v3/interface/ve/{ifnum}"
        self.DeviceProxy = ""
        self.icmp_rate_limit = {}
        self.isis = {}
        self.name = ""
        self.trap_source = ""
        self.bfd = {}
        self.ip = {}
        self.icmpv6_rate_limit = {}
        self.mtu = ""
        self.access_list = {}
        self.ifnum = ""
        self.sampling_enable = []
        self.lw_4o6 = {}
        self.ipv6 = {}
        self.action = ""
        self.l3_vlan_fwd_disable = ""
        self.ddos = {}
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


