from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param bwl_drop: {"description": "BW Limit Drop", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "8"}
    :param pingofdeath_drop: {"description": "Anomaly PingDeath Drop", "format": "counter", "type": "number", "oid": "32", "optional": true, "size": "8"}
    :param l2_forward: {"description": "L2 Forward", "format": "counter", "type": "number", "oid": "12", "optional": true, "size": "8"}
    :param jumbo_frag_drop: {"description": "Jumbo Frag Drop", "format": "counter", "type": "number", "oid": "63", "optional": true, "size": "8"}
    :param ipv6frag_tcp_dropped: {"description": "IPv6 Frag TCP Dropped", "format": "counter", "type": "number", "oid": "47", "optional": true, "size": "8"}
    :param rx_arp_req: {"description": "ARP REQ Rcvd", "format": "counter", "type": "number", "oid": "5", "optional": true, "size": "8"}
    :param ipv4_frag_6rd_ok: {"description": "IPv4 Frag 6RD OK", "format": "counter", "type": "number", "oid": "42", "optional": true, "size": "8"}
    :param fwlb: {"description": "FWLB", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}
    :param ipfrag_tcp: {"description": "IP(TCP) Fragment Rcvd", "format": "counter", "type": "number", "oid": "23", "optional": true, "size": "8"}
    :param l2_def_vlan_drop: {"description": "L2 Default Vlan FWD Drop", "format": "counter", "type": "number", "oid": "8", "optional": true, "size": "8"}
    :param ipipv6_jumbo_frag_drop: {"description": "IPIPv6 Jumbo Frag Drop", "format": "counter", "type": "number", "oid": "65", "optional": true, "size": "8"}
    :param vlan_flood: {"description": "VLAN Flood", "format": "counter", "type": "number", "oid": "7", "optional": true, "size": "8"}
    :param ipv6frag_ipip_ok: {"description": "IPv6 Frag IPIP OKs", "format": "counter", "type": "number", "oid": "48", "optional": true, "size": "8"}
    :param max_arp_drop: {"description": "Max ARP Drop", "format": "counter", "type": "number", "oid": "56", "optional": true, "size": "8"}
    :param ipv4_frag_6rd_drop: {"description": "IPv4 Frag 6RD Dropped", "format": "counter", "type": "number", "oid": "43", "optional": true, "size": "8"}
    :param prot_down_drop: {"description": "Prot Down Drop", "format": "counter", "type": "number", "oid": "11", "optional": true, "size": "8"}
    :param ipfrag_reasmoks: {"description": "IP Fragment Reasm OKs", "format": "counter", "type": "number", "oid": "27", "optional": true, "size": "8"}
    :param rx_kernel: {"description": "Received kernel", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "8"}
    :param bpdu_rcvd: {"description": "BPDUs Received", "format": "counter", "type": "number", "oid": "38", "optional": true, "size": "8"}
    :param ttl_exceeded_drop: {"description": "TTL Exceeded Drop", "format": "counter", "type": "number", "oid": "17", "optional": true, "size": "8"}
    :param ipv6frag_ospf: {"description": "IPv6 Frag OSPF", "format": "counter", "type": "number", "oid": "59", "optional": true, "size": "8"}
    :param land_drop: {"description": "Anomaly Land Attack Drop", "format": "counter", "type": "number", "oid": "29", "optional": true, "size": "8"}
    :param ipv6frag_icmp: {"description": "IPv6 Frag ICMP", "format": "counter", "type": "number", "oid": "58", "optional": true, "size": "8"}
    :param ctrl_syn_rate_drop: {"description": "SYN rate exceeded Drop", "format": "counter", "type": "number", "oid": "40", "optional": true, "size": "8"}
    :param ipv6frag_udp_dropped: {"description": "IPv6 Frag UDP Dropped", "format": "counter", "type": "number", "oid": "46", "optional": true, "size": "8"}
    :param rx_arp_resp: {"description": "ARP RESP Rcvd", "format": "counter", "type": "number", "oid": "6", "optional": true, "size": "8"}
    :param allfrag_drop: {"description": "Anomaly All Frag Drop", "format": "counter", "type": "number", "oid": "33", "optional": true, "size": "8"}
    :param ip_defrag: {"description": "IP Defrag", "format": "counter", "type": "number", "oid": "21", "optional": true, "size": "8"}
    :param incorrect_len_drop: {"description": "Incorrect Length Drop", "format": "counter", "type": "number", "oid": "20", "optional": true, "size": "8"}
    :param ipv6_ndisc_mac_changes: {"description": "IPv6 DAD MAC Changed", "format": "counter", "type": "number", "oid": "68", "optional": true, "size": "8"}
    :param l4_process: {"description": "L4 Process", "format": "counter", "type": "number", "oid": "15", "optional": true, "size": "8"}
    :param linkdown_drop: {"description": "Link Down Drop", "format": "counter", "type": "number", "oid": "18", "optional": true, "size": "8"}
    :param ipv6frag_tcp: {"description": "IPv6 Frag TCP", "format": "counter", "type": "number", "oid": "57", "optional": true, "size": "8"}
    :param tcpnoflag_drop: {"description": "Anomaly TCP noFlag Drop", "format": "counter", "type": "number", "oid": "34", "optional": true, "size": "8"}
    :param ipoptions_drop: {"description": "Anomaly IP OPT Drops", "format": "counter", "type": "number", "oid": "30", "optional": true, "size": "8"}
    :param ip_defrag_invalid_len: {"description": "IP Invalid Length Frag", "format": "counter", "type": "number", "oid": "41", "optional": true, "size": "8"}
    :param ipv6_ndisc_out_of_memory: {"description": "IPv6 DAD Out-of-memory", "format": "counter", "type": "number", "oid": "69", "optional": true, "size": "8"}
    :param ipfrag_reasmfails: {"description": "IP Fragment Reasm Fails", "format": "counter", "type": "number", "oid": "28", "optional": true, "size": "8"}
    :param ipv6_jumbo_frag_drop: {"description": "IPv6 Jumbo Frag Drop", "format": "counter", "type": "number", "oid": "64", "optional": true, "size": "8"}
    :param ipv6_ndisc_dad_adverts: {"description": "IPv6 DAD on Adverts", "format": "counter", "type": "number", "oid": "67", "optional": true, "size": "8"}
    :param l4_in_ctrl_cpu: {"description": "L4 In Ctrl CPU", "format": "counter", "type": "number", "oid": "61", "optional": true, "size": "8"}
    :param fpga_error_pkt1: {"description": "FPGA Error PKT1", "format": "counter", "type": "number", "oid": "54", "optional": true, "size": "8"}
    :param fpga_error_pkt2: {"description": "FPGA Error PKT2", "format": "counter", "type": "number", "oid": "55", "optional": true, "size": "8"}
    :param tcpsynfrag_drop: {"description": "Anomaly SYN Frag Drop", "format": "counter", "type": "number", "oid": "35", "optional": true, "size": "8"}
    :param ipfrag_overload: {"description": "IP Frag Overload Drops", "format": "counter", "type": "number", "oid": "26", "optional": true, "size": "8"}
    :param ipv6frag_ipip_dropped: {"description": "IPv6 Frag IPIP Drop", "format": "counter", "type": "number", "oid": "49", "optional": true, "size": "8"}
    :param mgmt_svc_drop: {"description": "Management Service Drop", "format": "counter", "type": "number", "oid": "62", "optional": true, "size": "8"}
    :param ipv6_ndisc_dad_solicits: {"description": "IPv6 DAD on Solicits", "format": "counter", "type": "number", "oid": "66", "optional": true, "size": "8"}
    :param sport_drop: {"description": "SPORT Drop", "format": "counter", "type": "number", "oid": "19", "optional": true, "size": "8"}
    :param ipfrag_overlap: {"description": "IP Fragment Overlap", "format": "counter", "type": "number", "oid": "24", "optional": true, "size": "8"}
    :param ipv6_noroute_drop: {"description": "IPv6 No Route Drop", "format": "counter", "type": "number", "oid": "10", "optional": true, "size": "8"}
    :param no_ip_drop: {"description": "No IP Drop", "format": "counter", "type": "number", "oid": "44", "optional": true, "size": "8"}
    :param ipv4_noroute_drop: {"description": "IPv4 No Route Drop", "format": "counter", "type": "number", "oid": "9", "optional": true, "size": "8"}
    :param tcpsynfin_drop: {"description": "Anomaly TCP SYNFIN Drop", "format": "counter", "type": "number", "oid": "36", "optional": true, "size": "8"}
    :param ipsec_drop: {"description": "IPSec Drop", "format": "counter", "type": "number", "oid": "37", "optional": true, "size": "8"}
    :param bpdu_sent: {"description": "BPDUs Sent", "format": "counter", "type": "number", "oid": "39", "optional": true, "size": "8"}
    :param ipfrag_timeout: {"description": "IP Fragment Timeout", "format": "counter", "type": "number", "oid": "25", "optional": true, "size": "8"}
    :param l3_forward_ip: {"description": "L3 IP Forward", "format": "counter", "type": "number", "oid": "13", "optional": true, "size": "8"}
    :param ip_frag_too_many: {"description": "IP Fragment too many", "format": "counter", "type": "number", "oid": "51", "optional": true, "size": "8"}
    :param ipv6frag_esp: {"description": "IPv6 Frag ESP", "format": "counter", "type": "number", "oid": "60", "optional": true, "size": "8"}
    :param licexpire_drop: {"description": "License Expire Drop", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "8"}
    :param l3_forward_ipv6: {"description": "L3 IPv6 Forward", "format": "counter", "type": "number", "oid": "14", "optional": true, "size": "8"}
    :param acl_deny: {"description": "ACL Denys", "format": "counter", "type": "number", "oid": "22", "optional": true, "size": "8"}
    :param ip_frag_oversize: {"description": "IP Fragment oversize", "format": "counter", "type": "number", "oid": "50", "optional": true, "size": "8"}
    :param ipv6_novlanfwd_drop: {"description": "IPv6 No L3 VLAN FWD Drop", "format": "counter", "type": "number", "oid": "53", "optional": true, "size": "8"}
    :param unknown_prot_drop: {"description": "Unknown Prot Drop", "format": "counter", "type": "number", "oid": "16", "optional": true, "size": "8"}
    :param ipv4_novlanfwd_drop: {"description": "IPv4 No L3 VLAN FWD Drop", "format": "counter", "type": "number", "oid": "52", "optional": true, "size": "8"}
    :param badpkt_drop: {"description": "Bad Pkt Drop", "format": "counter", "type": "number", "oid": "31", "optional": true, "size": "8"}
    :param ipv6frag_udp: {"description": "IPv6 Frag UDP", "format": "counter", "type": "number", "oid": "45", "optional": true, "size": "8"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.bwl_drop = ""
        self.pingofdeath_drop = ""
        self.l2_forward = ""
        self.jumbo_frag_drop = ""
        self.ipv6frag_tcp_dropped = ""
        self.rx_arp_req = ""
        self.ipv4_frag_6rd_ok = ""
        self.fwlb = ""
        self.ipfrag_tcp = ""
        self.l2_def_vlan_drop = ""
        self.ipipv6_jumbo_frag_drop = ""
        self.vlan_flood = ""
        self.ipv6frag_ipip_ok = ""
        self.max_arp_drop = ""
        self.ipv4_frag_6rd_drop = ""
        self.prot_down_drop = ""
        self.ipfrag_reasmoks = ""
        self.rx_kernel = ""
        self.bpdu_rcvd = ""
        self.ttl_exceeded_drop = ""
        self.ipv6frag_ospf = ""
        self.land_drop = ""
        self.ipv6frag_icmp = ""
        self.ctrl_syn_rate_drop = ""
        self.ipv6frag_udp_dropped = ""
        self.rx_arp_resp = ""
        self.allfrag_drop = ""
        self.ip_defrag = ""
        self.incorrect_len_drop = ""
        self.ipv6_ndisc_mac_changes = ""
        self.l4_process = ""
        self.linkdown_drop = ""
        self.ipv6frag_tcp = ""
        self.tcpnoflag_drop = ""
        self.ipoptions_drop = ""
        self.ip_defrag_invalid_len = ""
        self.ipv6_ndisc_out_of_memory = ""
        self.ipfrag_reasmfails = ""
        self.ipv6_jumbo_frag_drop = ""
        self.ipv6_ndisc_dad_adverts = ""
        self.l4_in_ctrl_cpu = ""
        self.fpga_error_pkt1 = ""
        self.fpga_error_pkt2 = ""
        self.tcpsynfrag_drop = ""
        self.ipfrag_overload = ""
        self.ipv6frag_ipip_dropped = ""
        self.mgmt_svc_drop = ""
        self.ipv6_ndisc_dad_solicits = ""
        self.sport_drop = ""
        self.ipfrag_overlap = ""
        self.ipv6_noroute_drop = ""
        self.no_ip_drop = ""
        self.ipv4_noroute_drop = ""
        self.tcpsynfin_drop = ""
        self.ipsec_drop = ""
        self.bpdu_sent = ""
        self.ipfrag_timeout = ""
        self.l3_forward_ip = ""
        self.ip_frag_too_many = ""
        self.ipv6frag_esp = ""
        self.licexpire_drop = ""
        self.l3_forward_ipv6 = ""
        self.acl_deny = ""
        self.ip_frag_oversize = ""
        self.ipv6_novlanfwd_drop = ""
        self.unknown_prot_drop = ""
        self.ipv4_novlanfwd_drop = ""
        self.badpkt_drop = ""
        self.ipv6frag_udp = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Switch(A10BaseClass):
    
    """Class Description::
    Statistics for the object switch.

    Class switch supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/switch/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "switch"
        self.a10_url="/axapi/v3/slb/switch/stats"
        self.DeviceProxy = ""
        self.stats = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


