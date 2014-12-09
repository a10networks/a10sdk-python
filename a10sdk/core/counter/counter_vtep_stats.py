from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param rx_bad_inner_ipv4_len_pkts: {"description": "Packets received with Bad Inner IPv4 Payload length", "format": "counter", "type": "number", "oid": "34", "optional": true, "size": "2"}
    :param rx_pkts: {"description": "In Total Packets", "format": "counter", "type": "number", "oid": "15", "optional": true, "size": "8"}
    :param tx_encap_missing_pkts: {"description": "Remote Vtep unreachable: Drop Tx", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "2"}
    :param rx_mcast_pkts: {"description": "Out Multicast Packets", "format": "counter", "type": "number", "oid": "19", "optional": true, "size": "2"}
    :param cfg_vtep_error: {"description": "Config Error: Drop Packet", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "2"}
    :param rx_reassembled_pkts: {"description": "Reassembled Packets", "format": "counter", "type": "number", "oid": "33", "optional": true, "size": "2"}
    :param rx_ucast_pkts: {"description": "In Unicast Packets", "format": "counter", "type": "number", "oid": "17", "optional": true, "size": "8"}
    :param rx_lif_uninit: {"description": "Lif not UP: Drop Rx", "format": "counter", "type": "number", "oid": "36", "optional": true, "size": "2"}
    :param rx_lif_invalid: {"description": "Invalid Lif: Drop Rx", "format": "counter", "type": "number", "oid": "9", "optional": true, "size": "2"}
    :param rx_dot1q_ptks: {"description": "Dot1q Packet: Drop Rx", "format": "counter", "type": "number", "oid": "31", "optional": true, "size": "2"}
    :param rx_bad_checksum_pkts: {"description": "Packet reveived with Bad Inner checksum", "format": "counter", "type": "number", "oid": "22", "optional": true, "size": "2"}
    :param tx_bcast_pkts: {"description": "Out Broadcast Packets", "format": "counter", "type": "number", "oid": "27", "optional": true, "size": "8"}
    :param tx_fragmented_pkts: {"description": "Fragmented Packets", "format": "counter", "type": "number", "oid": "32", "optional": true, "size": "2"}
    :param rx_host_learned: {"description": "Number of Host =", "format": "counter", "type": "number", "oid": "7", "optional": true, "size": "2"}
    :param rx_unhandled_pkts: {"description": "Unhandled Packets: Drop Rx", "format": "counter", "type": "number", "oid": "13", "optional": true, "size": "2"}
    :param tx_arp_req_sent_pkts: {"description": "Number of Arp Requests Sent", "format": "counter", "type": "number", "oid": "6", "optional": true, "size": "2"}
    :param rx_host_learn_error: {"description": "Number of Host =", "format": "counter", "type": "number", "oid": "8", "optional": true, "size": "2"}
    :param rx_encap_miss_pkts: {"description": "Remote Vtep unreachable: Drop Tx", "format": "counter", "type": "number", "oid": "21", "optional": true, "size": "2"}
    :param rx_requeued_pkts: {"description": "Packets requeued to another CPU", "format": "counter", "type": "number", "oid": "23", "optional": true, "size": "2"}
    :param tx_lif_invalid: {"description": "Invalid Lif: Drop Tx", "format": "counter", "type": "number", "oid": "10", "optional": true, "size": "2"}
    :param rx_vtep_unknown: {"description": "Vtep unknown: Drop Rx", "format": "counter", "type": "number", "oid": "12", "optional": true, "size": "2"}
    :param rx_dropped_pkts: {"description": "In Dropped Packets", "format": "counter", "type": "number", "oid": "20", "optional": true, "size": "2"}
    :param tx_flood_pkts: {"description": "Out Flooded Packets", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "8"}
    :param rx_bad_inner_ipv6_len_pkts: {"description": "Packets received with Bad Inner IPv6 Payload length", "format": "counter", "type": "number", "oid": "35", "optional": true, "size": "2"}
    :param rx_pkts_too_large: {"description": "Packet too large: Drop Rx", "format": "counter", "type": "number", "oid": "30", "optional": true, "size": "2"}
    :param tx_bytes: {"description": "Out Total Octets", "format": "counter", "type": "number", "oid": "25", "optional": true, "size": "8"}
    :param tx_mcast_pkts: {"description": "Out Multicast Packets", "format": "counter", "type": "number", "oid": "28", "optional": true, "size": "2"}
    :param tx_vtep_unknown: {"description": "Vtep unknown: Drop Tx", "format": "counter", "type": "number", "oid": "11", "optional": true, "size": "2"}
    :param tx_encap_unresolved_pkts: {"description": "Remote Vtep unreachable: Drop Tx", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "2"}
    :param tx_encap_bad_pkts: {"description": "Remote Vtep unreachable: Drop Tx", "format": "counter", "type": "number", "oid": "5", "optional": true, "size": "2"}
    :param rx_bcast_pkts: {"description": "In Broadcast Packets", "format": "counter", "type": "number", "oid": "18", "optional": true, "size": "8"}
    :param tx_unhandled_pkts: {"description": "Unhandled Packets: Drop Tx", "format": "counter", "type": "number", "oid": "14", "optional": true, "size": "2"}
    :param tx_dropped_pkts: {"description": "Out Dropped Packets", "format": "counter", "type": "number", "oid": "29", "optional": true, "size": "2"}
    :param tx_ucast_pkts: {"description": "Out Unicast Packets", "format": "counter", "type": "number", "oid": "26", "optional": true, "size": "8"}
    :param tx_pkts: {"description": "Out Total Packets", "format": "counter", "type": "number", "oid": "24", "optional": true, "size": "8"}
    :param rx_bytes: {"description": "In Total Octets", "format": "counter", "type": "number", "oid": "16", "optional": true, "size": "8"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.rx_bad_inner_ipv4_len_pkts = ""
        self.rx_pkts = ""
        self.tx_encap_missing_pkts = ""
        self.rx_mcast_pkts = ""
        self.cfg_vtep_error = ""
        self.rx_reassembled_pkts = ""
        self.rx_ucast_pkts = ""
        self.rx_lif_uninit = ""
        self.rx_lif_invalid = ""
        self.rx_dot1q_ptks = ""
        self.rx_bad_checksum_pkts = ""
        self.tx_bcast_pkts = ""
        self.tx_fragmented_pkts = ""
        self.rx_host_learned = ""
        self.rx_unhandled_pkts = ""
        self.tx_arp_req_sent_pkts = ""
        self.rx_host_learn_error = ""
        self.rx_encap_miss_pkts = ""
        self.rx_requeued_pkts = ""
        self.tx_lif_invalid = ""
        self.rx_vtep_unknown = ""
        self.rx_dropped_pkts = ""
        self.tx_flood_pkts = ""
        self.rx_bad_inner_ipv6_len_pkts = ""
        self.rx_pkts_too_large = ""
        self.tx_bytes = ""
        self.tx_mcast_pkts = ""
        self.tx_vtep_unknown = ""
        self.tx_encap_unresolved_pkts = ""
        self.tx_encap_bad_pkts = ""
        self.rx_bcast_pkts = ""
        self.tx_unhandled_pkts = ""
        self.tx_dropped_pkts = ""
        self.tx_ucast_pkts = ""
        self.tx_pkts = ""
        self.rx_bytes = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Vtep(A10BaseClass):
    
    """Class Description::
    Statistics for the object vtep.

    Class vtep supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/counter/vtep/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "vtep"
        self.a10_url="/axapi/v3/counter/vtep/stats"
        self.DeviceProxy = ""
        self.stats = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


