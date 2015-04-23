from a10sdk.common.A10BaseClass import A10BaseClass


class SamplingEnable(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param counters1: {"enum": ["all", "session-inserted", "session-expired", "icmp-rcv", "icmpv6-rcv", "udp-rcv", "tcp-rcv", "ipip-rcv", "ipv6ip-rcv", "other-rcv", "icmp-dropped", "icmpv6-dropped", "udp-dropped", "tcp-dropped", "ipip-dropped", "ipv6ip-dropped", "other-dropped", "overlap-error", "bad-ip-len", "too-small", "first-tcp-too-small", "first-l4-too-small", "total-sessions-exceeded", "no-session-memory", "fast-aging-set", "fast-aging-unset", "fragment-queue-success", "unaligned-len", "exceeded-len", "duplicate-first-frag", "duplicate-last-frag", "total-fragments-exceeded", "fragment-queue-failure", "reassembly-success", "max-len-exceeded", "reassembly-failure", "policy-drop", "error-drop", "max-packets-exceeded", "session-packets-exceeded", "frag-session-count", "high-cpu-threshold", "low-cpu-threshold", "cpu-threshold-drop", "ipd-entry-drop"], "type": "string", "description": "'all': all; 'session-inserted': Session Inserted; 'session-expired': Session Expired; 'icmp-rcv': ICMP Received; 'icmpv6-rcv': ICMPv6 Received; 'udp-rcv': UDP Received; 'tcp-rcv': TCP Received; 'ipip-rcv': IP-in-IP Received; 'ipv6ip-rcv': IPv6-in-IP Received; 'other-rcv': Other Received; 'icmp-dropped': ICMP Dropped; 'icmpv6-dropped': ICMPv6 Dropped; 'udp-dropped': UDP Dropped; 'tcp-dropped': TCP Dropped; 'ipip-dropped': IP-in-IP Dropped; 'ipv6ip-dropped': IPv6-in-IP Dropped; 'other-dropped': Other Dropped; 'overlap-error': Overlapping Fragment Dropped; 'bad-ip-len': Bad IP Length; 'too-small': Fragment Too Small Drop; 'first-tcp-too-small': First TCP Fragment Too Small Drop; 'first-l4-too-small': First L4 Fragment Too Small Drop; 'total-sessions-exceeded': Total Sessions Exceeded Drop; 'no-session-memory': Out of Session Memory; 'fast-aging-set': Fragmentation Fast Aging Set; 'fast-aging-unset': Fragmentation Fast Aging Unset; 'fragment-queue-success': Fragment Queue Success; 'unaligned-len': Payload Length Unaligned; 'exceeded-len': Payload Length Out of Bounds; 'duplicate-first-frag': Duplicate First Fragment; 'duplicate-last-frag': Duplicate Last Fragment; 'total-fragments-exceeded': Total Queued Fragments Exceeded; 'fragment-queue-failure': Fragment Queue Failure; 'reassembly-success': Fragment Reassembly Success; 'max-len-exceeded': Fragment Max Data Length Exceeded; 'reassembly-failure': Fragment Reassembly Failure; 'policy-drop': MTU Exceeded Policy Drop; 'error-drop': Fragment Processing Drop; 'max-packets-exceeded': Too Many Packets Per Reassembly Drop; 'session-packets-exceeded': Session Max Packets Exceeded; 'frag-session-count': Fragmentation Session Count; 'high-cpu-threshold': High CPU Threshold Reached; 'low-cpu-threshold': Low CPU Threshold Reached; 'cpu-threshold-drop': High CPU Drop; 'ipd-entry-drop': DDoS Protection Drop; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "sampling-enable"
        self.DeviceProxy = ""
        self.counters1 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Frag(A10BaseClass):
    
    """    :param sampling_enable: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "session-inserted", "session-expired", "icmp-rcv", "icmpv6-rcv", "udp-rcv", "tcp-rcv", "ipip-rcv", "ipv6ip-rcv", "other-rcv", "icmp-dropped", "icmpv6-dropped", "udp-dropped", "tcp-dropped", "ipip-dropped", "ipv6ip-dropped", "other-dropped", "overlap-error", "bad-ip-len", "too-small", "first-tcp-too-small", "first-l4-too-small", "total-sessions-exceeded", "no-session-memory", "fast-aging-set", "fast-aging-unset", "fragment-queue-success", "unaligned-len", "exceeded-len", "duplicate-first-frag", "duplicate-last-frag", "total-fragments-exceeded", "fragment-queue-failure", "reassembly-success", "max-len-exceeded", "reassembly-failure", "policy-drop", "error-drop", "max-packets-exceeded", "session-packets-exceeded", "frag-session-count", "high-cpu-threshold", "low-cpu-threshold", "cpu-threshold-drop", "ipd-entry-drop"], "type": "string", "description": "'all': all; 'session-inserted': Session Inserted; 'session-expired': Session Expired; 'icmp-rcv': ICMP Received; 'icmpv6-rcv': ICMPv6 Received; 'udp-rcv': UDP Received; 'tcp-rcv': TCP Received; 'ipip-rcv': IP-in-IP Received; 'ipv6ip-rcv': IPv6-in-IP Received; 'other-rcv': Other Received; 'icmp-dropped': ICMP Dropped; 'icmpv6-dropped': ICMPv6 Dropped; 'udp-dropped': UDP Dropped; 'tcp-dropped': TCP Dropped; 'ipip-dropped': IP-in-IP Dropped; 'ipv6ip-dropped': IPv6-in-IP Dropped; 'other-dropped': Other Dropped; 'overlap-error': Overlapping Fragment Dropped; 'bad-ip-len': Bad IP Length; 'too-small': Fragment Too Small Drop; 'first-tcp-too-small': First TCP Fragment Too Small Drop; 'first-l4-too-small': First L4 Fragment Too Small Drop; 'total-sessions-exceeded': Total Sessions Exceeded Drop; 'no-session-memory': Out of Session Memory; 'fast-aging-set': Fragmentation Fast Aging Set; 'fast-aging-unset': Fragmentation Fast Aging Unset; 'fragment-queue-success': Fragment Queue Success; 'unaligned-len': Payload Length Unaligned; 'exceeded-len': Payload Length Out of Bounds; 'duplicate-first-frag': Duplicate First Fragment; 'duplicate-last-frag': Duplicate Last Fragment; 'total-fragments-exceeded': Total Queued Fragments Exceeded; 'fragment-queue-failure': Fragment Queue Failure; 'reassembly-success': Fragment Reassembly Success; 'max-len-exceeded': Fragment Max Data Length Exceeded; 'reassembly-failure': Fragment Reassembly Failure; 'policy-drop': MTU Exceeded Policy Drop; 'error-drop': Fragment Processing Drop; 'max-packets-exceeded': Too Many Packets Per Reassembly Drop; 'session-packets-exceeded': Session Max Packets Exceeded; 'frag-session-count': Fragmentation Session Count; 'high-cpu-threshold': High CPU Threshold Reached; 'low-cpu-threshold': Low CPU Threshold Reached; 'cpu-threshold-drop': High CPU Drop; 'ipd-entry-drop': DDoS Protection Drop; ", "format": "enum"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    IPv4-in-IPv6 fragmentation parameters.

    Class frag supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/ipv4-in-ipv6/frag`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "frag"
        self.a10_url="/axapi/v3/ipv4-in-ipv6/frag"
        self.DeviceProxy = ""
        self.sampling_enable = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


