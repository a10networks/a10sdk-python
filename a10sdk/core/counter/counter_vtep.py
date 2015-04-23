from a10sdk.common.A10BaseClass import A10BaseClass


class SamplingEnable(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param counters1: {"enum": ["all", "cfg_vtep_error", "tx_flood_pkts", "tx_encap_unresolved_pkts", "tx_encap_missing_pkts", "tx_encap_bad_pkts", "tx_arp_req_sent_pkts", "rx_host_learned", "rx_host_learn_error", "rx_lif_invalid", "tx_lif_invalid", "tx_vtep_unknown", "rx_vtep_unknown", "rx_unhandled_pkts", "tx_unhandled_pkts", "rx_pkts", "rx_bytes", "rx_ucast_pkts", "rx_bcast_pkts", "rx_mcast_pkts", "rx_dropped_pkts", "rx_encap_miss_pkts", "rx_bad_checksum_pkts", "rx_requeued_pkts", "tx_pkts", "tx_bytes", "tx_ucast_pkts", "tx_bcast_pkts", "tx_mcast_pkts", "tx_dropped_pkts", "rx_pkts_too_large", "rx_dot1q_ptks", "tx_fragmented_pkts", "rx_reassembled_pkts", "rx_bad_inner_ipv4_len_pkts", "rx_bad_inner_ipv6_len_pkts", "rx_lif_uninit"], "type": "string", "description": "'all': all; 'cfg_vtep_error': Config Error: Drop Packet; 'tx_flood_pkts': Out Flooded Packets; 'tx_encap_unresolved_pkts': Remote Vtep unreachable: Drop Tx; 'tx_encap_missing_pkts': Remote Vtep unreachable: Drop Tx; 'tx_encap_bad_pkts': Remote Vtep unreachable: Drop Tx; 'tx_arp_req_sent_pkts': Number of Arp Requests Sent; 'rx_host_learned': Number of Host =; 'rx_host_learn_error': Number of Host =; 'rx_lif_invalid': Invalid Lif: Drop Rx; 'tx_lif_invalid': Invalid Lif: Drop Tx; 'tx_vtep_unknown': Vtep unknown: Drop Tx; 'rx_vtep_unknown': Vtep unknown: Drop Rx; 'rx_unhandled_pkts': Unhandled Packets: Drop Rx; 'tx_unhandled_pkts': Unhandled Packets: Drop Tx; 'rx_pkts': In Total Packets; 'rx_bytes': In Total Octets; 'rx_ucast_pkts': In Unicast Packets; 'rx_bcast_pkts': In Broadcast Packets; 'rx_mcast_pkts': Out Multicast Packets; 'rx_dropped_pkts': In Dropped Packets; 'rx_encap_miss_pkts': Remote Vtep unreachable: Drop Tx; 'rx_bad_checksum_pkts': Packet reveived with Bad Inner checksum; 'rx_requeued_pkts': Packets requeued to another CPU; 'tx_pkts': Out Total Packets; 'tx_bytes': Out Total Octets; 'tx_ucast_pkts': Out Unicast Packets; 'tx_bcast_pkts': Out Broadcast Packets; 'tx_mcast_pkts': Out Multicast Packets; 'tx_dropped_pkts': Out Dropped Packets; 'rx_pkts_too_large': Packet too large: Drop Rx; 'rx_dot1q_ptks': Dot1q Packet: Drop Rx; 'tx_fragmented_pkts': Fragmented Packets; 'rx_reassembled_pkts': Reassembled Packets; 'rx_bad_inner_ipv4_len_pkts': Packets received with Bad Inner IPv4 Payload length; 'rx_bad_inner_ipv6_len_pkts': Packets received with Bad Inner IPv6 Payload length; 'rx_lif_uninit': Lif not UP: Drop Rx; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "sampling-enable"
        self.DeviceProxy = ""
        self.counters1 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Vtep(A10BaseClass):
    
    """Class Description::
    Virtual Tunnel End Point.

    Class vtep supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param sampling_enable: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "cfg_vtep_error", "tx_flood_pkts", "tx_encap_unresolved_pkts", "tx_encap_missing_pkts", "tx_encap_bad_pkts", "tx_arp_req_sent_pkts", "rx_host_learned", "rx_host_learn_error", "rx_lif_invalid", "tx_lif_invalid", "tx_vtep_unknown", "rx_vtep_unknown", "rx_unhandled_pkts", "tx_unhandled_pkts", "rx_pkts", "rx_bytes", "rx_ucast_pkts", "rx_bcast_pkts", "rx_mcast_pkts", "rx_dropped_pkts", "rx_encap_miss_pkts", "rx_bad_checksum_pkts", "rx_requeued_pkts", "tx_pkts", "tx_bytes", "tx_ucast_pkts", "tx_bcast_pkts", "tx_mcast_pkts", "tx_dropped_pkts", "rx_pkts_too_large", "rx_dot1q_ptks", "tx_fragmented_pkts", "rx_reassembled_pkts", "rx_bad_inner_ipv4_len_pkts", "rx_bad_inner_ipv6_len_pkts", "rx_lif_uninit"], "type": "string", "description": "'all': all; 'cfg_vtep_error': Config Error: Drop Packet; 'tx_flood_pkts': Out Flooded Packets; 'tx_encap_unresolved_pkts': Remote Vtep unreachable: Drop Tx; 'tx_encap_missing_pkts': Remote Vtep unreachable: Drop Tx; 'tx_encap_bad_pkts': Remote Vtep unreachable: Drop Tx; 'tx_arp_req_sent_pkts': Number of Arp Requests Sent; 'rx_host_learned': Number of Host =; 'rx_host_learn_error': Number of Host =; 'rx_lif_invalid': Invalid Lif: Drop Rx; 'tx_lif_invalid': Invalid Lif: Drop Tx; 'tx_vtep_unknown': Vtep unknown: Drop Tx; 'rx_vtep_unknown': Vtep unknown: Drop Rx; 'rx_unhandled_pkts': Unhandled Packets: Drop Rx; 'tx_unhandled_pkts': Unhandled Packets: Drop Tx; 'rx_pkts': In Total Packets; 'rx_bytes': In Total Octets; 'rx_ucast_pkts': In Unicast Packets; 'rx_bcast_pkts': In Broadcast Packets; 'rx_mcast_pkts': Out Multicast Packets; 'rx_dropped_pkts': In Dropped Packets; 'rx_encap_miss_pkts': Remote Vtep unreachable: Drop Tx; 'rx_bad_checksum_pkts': Packet reveived with Bad Inner checksum; 'rx_requeued_pkts': Packets requeued to another CPU; 'tx_pkts': Out Total Packets; 'tx_bytes': Out Total Octets; 'tx_ucast_pkts': Out Unicast Packets; 'tx_bcast_pkts': Out Broadcast Packets; 'tx_mcast_pkts': Out Multicast Packets; 'tx_dropped_pkts': Out Dropped Packets; 'rx_pkts_too_large': Packet too large: Drop Rx; 'rx_dot1q_ptks': Dot1q Packet: Drop Rx; 'tx_fragmented_pkts': Fragmented Packets; 'rx_reassembled_pkts': Reassembled Packets; 'rx_bad_inner_ipv4_len_pkts': Packets received with Bad Inner IPv4 Payload length; 'rx_bad_inner_ipv6_len_pkts': Packets received with Bad Inner IPv6 Payload length; 'rx_lif_uninit': Lif not UP: Drop Rx; ", "format": "enum"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/counter/vtep/{sampling_enable}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "sampling_enable"]

        self.b_key = "vtep"
        self.a10_url="/axapi/v3/counter/vtep/{sampling_enable}"
        self.DeviceProxy = ""
        self.sampling_enable = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


