from a10sdk.common.A10BaseClass import A10BaseClass


class SamplingEnable(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param counters1: {"enum": ["all", "icmp-unknown-type", "icmp-no-port-info", "icmp-no-session-drop", "icmpv6-unknown-type", "icmpv6-no-port-info", "icmpv6-no-session-drop", "icmp-to-icmp", "icmp-to-icmpv6", "icmpv6-to-icmp", "icmpv6-to-icmpv6", "icmp-bad-type", "icmpv6-bad-type", "64-known-drop", "64-unknown-drop", "64-midpoint-hop", "46-known-drop", "46-unknown-drop", "46-no-prefix-for-ipv4", "46-bad-encap-ip-header-len", "icmp-to-icmp-err", "icmp-to-icmpv6-err", "icmpv6-to-icmp-err", "icmpv6-to-icmpv6-err", "encap-cross-cpu-no-match", "encap-cross-cpu-preprocess-err", "icmp-to-icmp-unknown-l4", "icmp-to-icmpv6-unknown-l4", "icmpv6-to-icmp-unknown-l4", "icmpv6-to-icmpv6-unknown-l4", "static-nat", "echo-to-pool-reply", "echo-to-pool-drop", "error-to-pool-drop", "echo-to-pool-reply-v6", "echo-to-pool-drop-v6", "error-to-pool-drop-v6"], "type": "string", "description": "'all': all; 'icmp-unknown-type': ICMP Unknown Type; 'icmp-no-port-info': ICMP Port Info Not Included; 'icmp-no-session-drop': ICMP No Matching Session Drop; 'icmpv6-unknown-type': ICMPv6 Unknown Type; 'icmpv6-no-port-info': ICMPv6 Port Info Not Included; 'icmpv6-no-session-drop': ICMPv6 No Matching Session Drop; 'icmp-to-icmp': ICMP to ICMP Conversion; 'icmp-to-icmpv6': ICMP to ICMPv6 Conversion; 'icmpv6-to-icmp': ICMPv6 to ICMP Conversion; 'icmpv6-to-icmpv6': ICMPv6 to ICMPv6 Conversion; 'icmp-bad-type': Bad Embedded ICMP Type; 'icmpv6-bad-type': Bad Embedded ICMPv6 Type; '64-known-drop': NAT64 Forward Known ICMPv6 Drop; '64-unknown-drop': NAT64 Forward Unknown ICMPv6 Drop; '64-midpoint-hop': NAT64 Forward Unknown Source Drop; '46-known-drop': NAT64 Reverse Known ICMP Drop; '46-unknown-drop': NAT64 Reverse Known ICMPv6 Drop; '46-no-prefix-for-ipv4': NAT64 Reverse No Prefix Match for IPv4; '46-bad-encap-ip-header-len': 4to6 Bad Encapsulated IP Header Length; 'icmp-to-icmp-err': ICMP to ICMP Conversion Error; 'icmp-to-icmpv6-err': ICMP to ICMPv6 Conversion Error; 'icmpv6-to-icmp-err': ICMPv6 to ICMP Conversion Error; 'icmpv6-to-icmpv6-err': ICMPv6 to ICMPv6 Conversion Error; 'encap-cross-cpu-no-match': ICMP Embedded Cross CPU No Matching Session; 'encap-cross-cpu-preprocess-err': ICMP Embedded Cross CPU Preprocess Error; 'icmp-to-icmp-unknown-l4': ICMP Embedded Unknown L4 Protocol; 'icmp-to-icmpv6-unknown-l4': ICMP to ICMPv6 Embedded Unknown L4 Protocol; 'icmpv6-to-icmp-unknown-l4': ICMPv6 to ICMP Embedded Unknown L4 Protocol; 'icmpv6-to-icmpv6-unknown-l4': ICMPv6 to ICMPv6 Embedded Unknown L4 Protocol; 'static-nat': ICMP Static NAT; 'echo-to-pool-reply': Ping to Pool Reply; 'echo-to-pool-drop': Ping to Pool Drop; 'error-to-pool-drop': Error to Pool Drop; 'echo-to-pool-reply-v6': Ping6 to Pool Reply; 'echo-to-pool-drop-v6': Ping6 to Pool Drop; 'error-to-pool-drop-v6': Error to IPv6 Pool Drop; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "sampling-enable"
        self.DeviceProxy = ""
        self.counters1 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Icmp(A10BaseClass):
    
    """    :param sampling_enable: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "icmp-unknown-type", "icmp-no-port-info", "icmp-no-session-drop", "icmpv6-unknown-type", "icmpv6-no-port-info", "icmpv6-no-session-drop", "icmp-to-icmp", "icmp-to-icmpv6", "icmpv6-to-icmp", "icmpv6-to-icmpv6", "icmp-bad-type", "icmpv6-bad-type", "64-known-drop", "64-unknown-drop", "64-midpoint-hop", "46-known-drop", "46-unknown-drop", "46-no-prefix-for-ipv4", "46-bad-encap-ip-header-len", "icmp-to-icmp-err", "icmp-to-icmpv6-err", "icmpv6-to-icmp-err", "icmpv6-to-icmpv6-err", "encap-cross-cpu-no-match", "encap-cross-cpu-preprocess-err", "icmp-to-icmp-unknown-l4", "icmp-to-icmpv6-unknown-l4", "icmpv6-to-icmp-unknown-l4", "icmpv6-to-icmpv6-unknown-l4", "static-nat", "echo-to-pool-reply", "echo-to-pool-drop", "error-to-pool-drop", "echo-to-pool-reply-v6", "echo-to-pool-drop-v6", "error-to-pool-drop-v6"], "type": "string", "description": "'all': all; 'icmp-unknown-type': ICMP Unknown Type; 'icmp-no-port-info': ICMP Port Info Not Included; 'icmp-no-session-drop': ICMP No Matching Session Drop; 'icmpv6-unknown-type': ICMPv6 Unknown Type; 'icmpv6-no-port-info': ICMPv6 Port Info Not Included; 'icmpv6-no-session-drop': ICMPv6 No Matching Session Drop; 'icmp-to-icmp': ICMP to ICMP Conversion; 'icmp-to-icmpv6': ICMP to ICMPv6 Conversion; 'icmpv6-to-icmp': ICMPv6 to ICMP Conversion; 'icmpv6-to-icmpv6': ICMPv6 to ICMPv6 Conversion; 'icmp-bad-type': Bad Embedded ICMP Type; 'icmpv6-bad-type': Bad Embedded ICMPv6 Type; '64-known-drop': NAT64 Forward Known ICMPv6 Drop; '64-unknown-drop': NAT64 Forward Unknown ICMPv6 Drop; '64-midpoint-hop': NAT64 Forward Unknown Source Drop; '46-known-drop': NAT64 Reverse Known ICMP Drop; '46-unknown-drop': NAT64 Reverse Known ICMPv6 Drop; '46-no-prefix-for-ipv4': NAT64 Reverse No Prefix Match for IPv4; '46-bad-encap-ip-header-len': 4to6 Bad Encapsulated IP Header Length; 'icmp-to-icmp-err': ICMP to ICMP Conversion Error; 'icmp-to-icmpv6-err': ICMP to ICMPv6 Conversion Error; 'icmpv6-to-icmp-err': ICMPv6 to ICMP Conversion Error; 'icmpv6-to-icmpv6-err': ICMPv6 to ICMPv6 Conversion Error; 'encap-cross-cpu-no-match': ICMP Embedded Cross CPU No Matching Session; 'encap-cross-cpu-preprocess-err': ICMP Embedded Cross CPU Preprocess Error; 'icmp-to-icmp-unknown-l4': ICMP Embedded Unknown L4 Protocol; 'icmp-to-icmpv6-unknown-l4': ICMP to ICMPv6 Embedded Unknown L4 Protocol; 'icmpv6-to-icmp-unknown-l4': ICMPv6 to ICMP Embedded Unknown L4 Protocol; 'icmpv6-to-icmpv6-unknown-l4': ICMPv6 to ICMPv6 Embedded Unknown L4 Protocol; 'static-nat': ICMP Static NAT; 'echo-to-pool-reply': Ping to Pool Reply; 'echo-to-pool-drop': Ping to Pool Drop; 'error-to-pool-drop': Error to Pool Drop; 'echo-to-pool-reply-v6': Ping6 to Pool Reply; 'echo-to-pool-drop-v6': Ping6 to Pool Drop; 'error-to-pool-drop-v6': Error to IPv6 Pool Drop; ", "format": "enum"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    CGNV6 ICMP Statistics.

    Class icmp supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/icmp`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "icmp"
        self.a10_url="/axapi/v3/cgnv6/icmp"
        self.DeviceProxy = ""
        self.sampling_enable = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


