from a10sdk.common.A10BaseClass import A10BaseClass


class SamplingEnable(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param counters1: {"enum": ["all", "no-fwd-route", "no-rev-route", "out-of-session-memory", "tcp-rst-sent", "ipip-icmp-reply-sent", "icmp-filtered-sent", "icmp-host-unreachable-sent", "icmp-reply-no-session-drop", "ipip-truncated", "ip-src-invalid-unicast", "ip-dst-invalid-unicast", "ipv6-src-invalid-unicast", "ipv6-dst-invalid-unicast", "bad-l3-protocol", "special-ipv4-no-route", "special-ipv6-no-route", "icmp-reply-sent", "icmpv6-reply-sent", "out-of-state-dropped", "ttl-exceeded-sent", "cross-cpu-alg-gre-no-match", "cross-cpu-alg-gre-preprocess-err", "lsn-fast-setup", "lsn-fast-setup-err", "lsn-fast-setup-delayed-err", "lsn-fast-setup-mtu-too-small", "dst-nat-needed-drop", "invalid-nat64-translated-addr", "tcp-rst-loop-drop", "static-nat-alloc", "static-nat-free", "process-l4", "preprocess-error", "process-special", "process-continue", "process-error", "ip-unknown-process", "src-nat-pool-not-found", "dst-nat-pool-not-found", "l3-ip-src-invalid-unicast", "l3-ip-dst-invalid-unicast", "l3-ipv6-src-invalid-unicast", "l3-ipv6-dst-invalid-unicast"], "type": "string", "description": "'all': all; 'no-fwd-route': No Forward Route for Session; 'no-rev-route': No Reverse Route for Session; 'out-of-session-memory': Out of Session Memory; 'tcp-rst-sent': TCP RST Sent; 'ipip-icmp-reply-sent': IPIP ICMP Echo Reply Sent; 'icmp-filtered-sent': ICMP Administratively Filtered Sent; 'icmp-host-unreachable-sent': ICMP Host Unreachable Sent; 'icmp-reply-no-session-drop': ICMP Reply No Session Drop; 'ipip-truncated': IPIP Truncated Packet; 'ip-src-invalid-unicast': IPv4 Source Not Valid Unicast; 'ip-dst-invalid-unicast': IPv4 Destination Not Valid Unicast; 'ipv6-src-invalid-unicast': IPv6 Source Not Valid Unicast; 'ipv6-dst-invalid-unicast': IPv6 Destination Not Valid Unicast; 'bad-l3-protocol': Bad Layer 3 Protocol; 'special-ipv4-no-route': Stateless IPv4 No Forward Route; 'special-ipv6-no-route': Stateless IPv6 No Forward Route; 'icmp-reply-sent': ICMP Echo Reply Sent; 'icmpv6-reply-sent': ICMPv6 Echo Reply Sent; 'out-of-state-dropped': L4 Out of State packets; 'ttl-exceeded-sent': ICMP TTL Exceeded Sent; 'cross-cpu-alg-gre-no-match': ALG GRE Cross CPU No Matching Session; 'cross-cpu-alg-gre-preprocess-err': ALG GRE Cross CPU Preprocess Error; 'lsn-fast-setup': LSN Fast Setup Attempt; 'lsn-fast-setup-err': LSN Fast Setup Error; 'lsn-fast-setup-delayed-err': LSN Fast Setup Delayed Error; 'lsn-fast-setup-mtu-too-small': LSN Fast Setup MTU Too Small; 'dst-nat-needed-drop': Destination NAT Needed Drop; 'invalid-nat64-translated-addr': Invalid NAT64 Translated IPv4 Address; 'tcp-rst-loop-drop': RST Loop Drop; 'static-nat-alloc': Static NAT Alloc; 'static-nat-free': Static NAT Free; 'process-l4': Process L4; 'preprocess-error': Preprocess Error; 'process-special': Process Special; 'process-continue': Process Continue; 'process-error': Process Error; 'ip-unknown-process': Process IP Unknown; 'src-nat-pool-not-found': Src NAT Pool Not Found; 'dst-nat-pool-not-found': Dst NAT Pool Not Found; 'l3-ip-src-invalid-unicast': IPv4 L3 Source Invalid Unicast; 'l3-ip-dst-invalid-unicast': IPv4 L3 Destination Invalid Unicast; 'l3-ipv6-src-invalid-unicast': IPv6 L3 Source Invalid Unicast; 'l3-ipv6-dst-invalid-unicast': IPv6 L3 Destination Invalid Unicast; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "sampling-enable"
        self.DeviceProxy = ""
        self.counters1 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class L4(A10BaseClass):
    
    """    :param sampling_enable: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "no-fwd-route", "no-rev-route", "out-of-session-memory", "tcp-rst-sent", "ipip-icmp-reply-sent", "icmp-filtered-sent", "icmp-host-unreachable-sent", "icmp-reply-no-session-drop", "ipip-truncated", "ip-src-invalid-unicast", "ip-dst-invalid-unicast", "ipv6-src-invalid-unicast", "ipv6-dst-invalid-unicast", "bad-l3-protocol", "special-ipv4-no-route", "special-ipv6-no-route", "icmp-reply-sent", "icmpv6-reply-sent", "out-of-state-dropped", "ttl-exceeded-sent", "cross-cpu-alg-gre-no-match", "cross-cpu-alg-gre-preprocess-err", "lsn-fast-setup", "lsn-fast-setup-err", "lsn-fast-setup-delayed-err", "lsn-fast-setup-mtu-too-small", "dst-nat-needed-drop", "invalid-nat64-translated-addr", "tcp-rst-loop-drop", "static-nat-alloc", "static-nat-free", "process-l4", "preprocess-error", "process-special", "process-continue", "process-error", "ip-unknown-process", "src-nat-pool-not-found", "dst-nat-pool-not-found", "l3-ip-src-invalid-unicast", "l3-ip-dst-invalid-unicast", "l3-ipv6-src-invalid-unicast", "l3-ipv6-dst-invalid-unicast"], "type": "string", "description": "'all': all; 'no-fwd-route': No Forward Route for Session; 'no-rev-route': No Reverse Route for Session; 'out-of-session-memory': Out of Session Memory; 'tcp-rst-sent': TCP RST Sent; 'ipip-icmp-reply-sent': IPIP ICMP Echo Reply Sent; 'icmp-filtered-sent': ICMP Administratively Filtered Sent; 'icmp-host-unreachable-sent': ICMP Host Unreachable Sent; 'icmp-reply-no-session-drop': ICMP Reply No Session Drop; 'ipip-truncated': IPIP Truncated Packet; 'ip-src-invalid-unicast': IPv4 Source Not Valid Unicast; 'ip-dst-invalid-unicast': IPv4 Destination Not Valid Unicast; 'ipv6-src-invalid-unicast': IPv6 Source Not Valid Unicast; 'ipv6-dst-invalid-unicast': IPv6 Destination Not Valid Unicast; 'bad-l3-protocol': Bad Layer 3 Protocol; 'special-ipv4-no-route': Stateless IPv4 No Forward Route; 'special-ipv6-no-route': Stateless IPv6 No Forward Route; 'icmp-reply-sent': ICMP Echo Reply Sent; 'icmpv6-reply-sent': ICMPv6 Echo Reply Sent; 'out-of-state-dropped': L4 Out of State packets; 'ttl-exceeded-sent': ICMP TTL Exceeded Sent; 'cross-cpu-alg-gre-no-match': ALG GRE Cross CPU No Matching Session; 'cross-cpu-alg-gre-preprocess-err': ALG GRE Cross CPU Preprocess Error; 'lsn-fast-setup': LSN Fast Setup Attempt; 'lsn-fast-setup-err': LSN Fast Setup Error; 'lsn-fast-setup-delayed-err': LSN Fast Setup Delayed Error; 'lsn-fast-setup-mtu-too-small': LSN Fast Setup MTU Too Small; 'dst-nat-needed-drop': Destination NAT Needed Drop; 'invalid-nat64-translated-addr': Invalid NAT64 Translated IPv4 Address; 'tcp-rst-loop-drop': RST Loop Drop; 'static-nat-alloc': Static NAT Alloc; 'static-nat-free': Static NAT Free; 'process-l4': Process L4; 'preprocess-error': Preprocess Error; 'process-special': Process Special; 'process-continue': Process Continue; 'process-error': Process Error; 'ip-unknown-process': Process IP Unknown; 'src-nat-pool-not-found': Src NAT Pool Not Found; 'dst-nat-pool-not-found': Dst NAT Pool Not Found; 'l3-ip-src-invalid-unicast': IPv4 L3 Source Invalid Unicast; 'l3-ip-dst-invalid-unicast': IPv4 L3 Destination Invalid Unicast; 'l3-ipv6-src-invalid-unicast': IPv6 L3 Source Invalid Unicast; 'l3-ipv6-dst-invalid-unicast': IPv6 L3 Destination Invalid Unicast; ", "format": "enum"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    CGNV6 L4 Statistics.

    Class l4 supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/l4`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "l4"
        self.a10_url="/axapi/v3/cgnv6/l4"
        self.DeviceProxy = ""
        self.sampling_enable = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


