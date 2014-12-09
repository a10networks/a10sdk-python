from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param icmpv6_rcv: {"description": "ICMPv6 Received", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "8"}
    :param tcp_rcv: {"description": "TCP Received", "format": "counter", "type": "number", "oid": "6", "optional": true, "size": "8"}
    :param other_rcv: {"description": "Other Received", "format": "counter", "type": "number", "oid": "9", "optional": true, "size": "8"}
    :param udp_dropped: {"description": "UDP Dropped", "format": "counter", "type": "number", "oid": "12", "optional": true, "size": "8"}
    :param bad_ip_len: {"description": "Bad IP Length", "format": "counter", "type": "number", "oid": "18", "optional": true, "size": "8"}
    :param first_l4_too_small: {"description": "First L4 Fragment Too Small Drop", "format": "counter", "type": "number", "oid": "21", "optional": true, "size": "8"}
    :param no_session_memory: {"description": "Out of Session Memory", "format": "counter", "type": "number", "oid": "23", "optional": true, "size": "8"}
    :param unaligned_len: {"description": "Payload Length Unaligned", "format": "counter", "type": "number", "oid": "27", "optional": true, "size": "8"}
    :param icmp_dropped: {"description": "ICMP Dropped", "format": "counter", "type": "number", "oid": "10", "optional": true, "size": "8"}
    :param udp_rcv: {"description": "UDP Received", "format": "counter", "type": "number", "oid": "5", "optional": true, "size": "8"}
    :param exceeded_len: {"description": "Payload Length Out of Bounds", "format": "counter", "type": "number", "oid": "28", "optional": true, "size": "8"}
    :param fragment_queue_success: {"description": "Fragment Queue Success", "format": "counter", "type": "number", "oid": "26", "optional": true, "size": "8"}
    :param fragment_queue_failure: {"description": "Fragment Queue Failure", "format": "counter", "type": "number", "oid": "32", "optional": true, "size": "8"}
    :param total_fragments_exceeded: {"description": "Total Queued Fragments Exceeded", "format": "counter", "type": "number", "oid": "31", "optional": true, "size": "8"}
    :param tcp_dropped: {"description": "TCP Dropped", "format": "counter", "type": "number", "oid": "13", "optional": true, "size": "8"}
    :param ipip_dropped: {"description": "IP-in-IP Dropped", "format": "counter", "type": "number", "oid": "14", "optional": true, "size": "8"}
    :param total_sessions_exceeded: {"description": "Total Sessions Exceeded Drop", "format": "counter", "type": "number", "oid": "22", "optional": true, "size": "8"}
    :param error_drop: {"description": "Fragment Processing Drop", "format": "counter", "type": "number", "oid": "37", "optional": true, "size": "8"}
    :param overlap_error: {"description": "Overlapping Fragment Dropped", "format": "counter", "type": "number", "oid": "17", "optional": true, "size": "8"}
    :param ipv6ip_rcv: {"description": "IPv6-in-IP Received", "format": "counter", "type": "number", "oid": "8", "optional": true, "size": "8"}
    :param session_expired: {"description": "Session Expired", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "8"}
    :param policy_drop: {"description": "MTU Exceeded Policy Drop", "format": "counter", "type": "number", "oid": "36", "optional": true, "size": "8"}
    :param icmp_rcv: {"description": "ICMP Received", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "8"}
    :param session_packets_exceeded: {"description": "Session Max Packets Exceeded", "format": "counter", "type": "number", "oid": "39", "optional": true, "size": "8"}
    :param duplicate_first_frag: {"description": "Duplicate First Fragment", "format": "counter", "type": "number", "oid": "29", "optional": true, "size": "8"}
    :param reassembly_success: {"description": "Fragment Reassembly Success", "format": "counter", "type": "number", "oid": "33", "optional": true, "size": "8"}
    :param too_small: {"description": "Fragment Too Small Drop", "format": "counter", "type": "number", "oid": "19", "optional": true, "size": "8"}
    :param ipv6ip_dropped: {"description": "IPv6-in-IP Dropped", "format": "counter", "type": "number", "oid": "15", "optional": true, "size": "8"}
    :param session_inserted: {"description": "Session Inserted", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}
    :param max_len_exceeded: {"description": "Fragment Max Data Length Exceeded", "format": "counter", "type": "number", "oid": "34", "optional": true, "size": "8"}
    :param max_packets_exceeded: {"description": "Too Many Packets Per Reassembly Drop", "format": "counter", "type": "number", "oid": "38", "optional": true, "size": "8"}
    :param other_dropped: {"description": "Other Dropped", "format": "counter", "type": "number", "oid": "16", "optional": true, "size": "8"}
    :param first_tcp_too_small: {"description": "First TCP Fragment Too Small Drop", "format": "counter", "type": "number", "oid": "20", "optional": true, "size": "8"}
    :param fast_aging_set: {"description": "Fragmentation Fast Aging Set", "format": "counter", "type": "number", "oid": "24", "optional": true, "size": "8"}
    :param ipip_rcv: {"description": "IP-in-IP Received", "format": "counter", "type": "number", "oid": "7", "optional": true, "size": "8"}
    :param icmpv6_dropped: {"description": "ICMPv6 Dropped", "format": "counter", "type": "number", "oid": "11", "optional": true, "size": "8"}
    :param fast_aging_unset: {"description": "Fragmentation Fast Aging Unset", "format": "counter", "type": "number", "oid": "25", "optional": true, "size": "8"}
    :param reassembly_failure: {"description": "Fragment Reassembly Failure", "format": "counter", "type": "number", "oid": "35", "optional": true, "size": "8"}
    :param duplicate_last_frag: {"description": "Duplicate Last Fragment", "format": "counter", "type": "number", "oid": "30", "optional": true, "size": "8"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.icmpv6_rcv = ""
        self.tcp_rcv = ""
        self.other_rcv = ""
        self.udp_dropped = ""
        self.bad_ip_len = ""
        self.first_l4_too_small = ""
        self.no_session_memory = ""
        self.unaligned_len = ""
        self.icmp_dropped = ""
        self.udp_rcv = ""
        self.exceeded_len = ""
        self.fragment_queue_success = ""
        self.fragment_queue_failure = ""
        self.total_fragments_exceeded = ""
        self.tcp_dropped = ""
        self.ipip_dropped = ""
        self.total_sessions_exceeded = ""
        self.error_drop = ""
        self.overlap_error = ""
        self.ipv6ip_rcv = ""
        self.session_expired = ""
        self.policy_drop = ""
        self.icmp_rcv = ""
        self.session_packets_exceeded = ""
        self.duplicate_first_frag = ""
        self.reassembly_success = ""
        self.too_small = ""
        self.ipv6ip_dropped = ""
        self.session_inserted = ""
        self.max_len_exceeded = ""
        self.max_packets_exceeded = ""
        self.other_dropped = ""
        self.first_tcp_too_small = ""
        self.fast_aging_set = ""
        self.ipip_rcv = ""
        self.icmpv6_dropped = ""
        self.fast_aging_unset = ""
        self.reassembly_failure = ""
        self.duplicate_last_frag = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Frag(A10BaseClass):
    
    """Class Description::
    Statistics for the object frag.

    Class frag supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/ip/frag/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "frag"
        self.a10_url="/axapi/v3/ip/frag/stats"
        self.DeviceProxy = ""
        self.stats = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


