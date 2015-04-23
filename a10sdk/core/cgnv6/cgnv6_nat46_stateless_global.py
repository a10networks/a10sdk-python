from a10sdk.common.A10BaseClass import A10BaseClass


class SamplingEnable(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param counters1: {"enum": ["all", "outbound_ipv4_received", "outbound_ipv4_drop", "outbound_ipv4_fragment_received", "outbound_ipv6_unreachable", "outbound_ipv6_fragmented", "inbound_ipv6_received", "inbound_ipv6_drop", "inbound_ipv6_fragment_received", "inbound_ipv4_unreachable", "inbound_ipv4_fragmented", "packet_too_big", "fragment_error", "icmpv6_to_icmp", "icmpv6_to_icmp_error", "icmp_to_icmpv6", "icmp_to_icmpv6_error", "ha_standby", "other_error"], "type": "string", "description": "'all': all; 'outbound_ipv4_received': Outbound IPv4 packets received; 'outbound_ipv4_drop': Outbound IPv4 packets dropped; 'outbound_ipv4_fragment_received': Outbound IPv4 fragment packets received; 'outbound_ipv6_unreachable': Outbound IPv6 destination unreachable; 'outbound_ipv6_fragmented': Outbound IPv6 packets fragmented; 'inbound_ipv6_received': Inbound IPv6 packets received; 'inbound_ipv6_drop': Inbound IPv6 packets dropped; 'inbound_ipv6_fragment_received': Inbound IPv6 fragment packets received; 'inbound_ipv4_unreachable': Inbound IPv4 destination unreachable; 'inbound_ipv4_fragmented': Inbound IPv4 packets fragmented; 'packet_too_big': Packet too big; 'fragment_error': Fragment processing errors; 'icmpv6_to_icmp': ICMPv6 to ICMP; 'icmpv6_to_icmp_error': ICMPv6 to ICMP errors; 'icmp_to_icmpv6': ICMP to ICMPv6; 'icmp_to_icmpv6_error': ICMP to ICMPv6 errors; 'ha_standby': HA is standby; 'other_error': Other errors; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "sampling-enable"
        self.DeviceProxy = ""
        self.counters1 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Global(A10BaseClass):
    
    """    :param sampling_enable: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "outbound_ipv4_received", "outbound_ipv4_drop", "outbound_ipv4_fragment_received", "outbound_ipv6_unreachable", "outbound_ipv6_fragmented", "inbound_ipv6_received", "inbound_ipv6_drop", "inbound_ipv6_fragment_received", "inbound_ipv4_unreachable", "inbound_ipv4_fragmented", "packet_too_big", "fragment_error", "icmpv6_to_icmp", "icmpv6_to_icmp_error", "icmp_to_icmpv6", "icmp_to_icmpv6_error", "ha_standby", "other_error"], "type": "string", "description": "'all': all; 'outbound_ipv4_received': Outbound IPv4 packets received; 'outbound_ipv4_drop': Outbound IPv4 packets dropped; 'outbound_ipv4_fragment_received': Outbound IPv4 fragment packets received; 'outbound_ipv6_unreachable': Outbound IPv6 destination unreachable; 'outbound_ipv6_fragmented': Outbound IPv6 packets fragmented; 'inbound_ipv6_received': Inbound IPv6 packets received; 'inbound_ipv6_drop': Inbound IPv6 packets dropped; 'inbound_ipv6_fragment_received': Inbound IPv6 fragment packets received; 'inbound_ipv4_unreachable': Inbound IPv4 destination unreachable; 'inbound_ipv4_fragmented': Inbound IPv4 packets fragmented; 'packet_too_big': Packet too big; 'fragment_error': Fragment processing errors; 'icmpv6_to_icmp': ICMPv6 to ICMP; 'icmpv6_to_icmp_error': ICMPv6 to ICMP errors; 'icmp_to_icmpv6': ICMP to ICMPv6; 'icmp_to_icmpv6_error': ICMP to ICMPv6 errors; 'ha_standby': HA is standby; 'other_error': Other errors; ", "format": "enum"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Stateless NAT46 Statistics.

    Class global supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/nat46-stateless/global`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "global"
        self.a10_url="/axapi/v3/cgnv6/nat46-stateless/global"
        self.DeviceProxy = ""
        self.sampling_enable = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


