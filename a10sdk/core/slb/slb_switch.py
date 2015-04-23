from a10sdk.common.A10BaseClass import A10BaseClass


class SamplingEnable(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param counters1: {"enum": ["all", "fwlb", "licexpire_drop", "bwl_drop", "rx_kernel", "rx_arp_req", "rx_arp_resp", "vlan_flood", "l2_def_vlan_drop", "ipv4_noroute_drop", "ipv6_noroute_drop", "prot_down_drop", "l2_forward", "l3_forward_ip", "l3_forward_ipv6", "l4_process", "unknown_prot_drop", "ttl_exceeded_drop", "linkdown_drop", "sport_drop", "incorrect_len_drop", "ip_defrag", "acl_deny", "ipfrag_tcp", "ipfrag_overlap", "ipfrag_timeout", "ipfrag_overload", "ipfrag_reasmoks", "ipfrag_reasmfails", "land_drop", "ipoptions_drop", "badpkt_drop", "pingofdeath_drop", "allfrag_drop", "tcpnoflag_drop", "tcpsynfrag_drop", "tcpsynfin_drop", "ipsec_drop", "bpdu_rcvd", "bpdu_sent", "ctrl_syn_rate_drop", "ip_defrag_invalid_len", "ipv4_frag_6rd_ok", "ipv4_frag_6rd_drop", "no_ip_drop", "ipv6frag_udp", "ipv6frag_udp_dropped", "ipv6frag_tcp_dropped", "ipv6frag_ipip_ok", "ipv6frag_ipip_dropped", "ip_frag_oversize", "ip_frag_too_many", "ipv4_novlanfwd_drop", "ipv6_novlanfwd_drop", "fpga_error_pkt1", "fpga_error_pkt2", "max_arp_drop", "ipv6frag_tcp", "ipv6frag_icmp", "ipv6frag_ospf", "ipv6frag_esp", "l4_in_ctrl_cpu", "mgmt_svc_drop", "jumbo_frag_drop", "ipv6_jumbo_frag_drop", "ipipv6_jumbo_frag_drop", "ipv6_ndisc_dad_solicits", "ipv6_ndisc_dad_adverts", "ipv6_ndisc_mac_changes", "ipv6_ndisc_out_of_memory", "sp_non_ctrl_pkt_drop"], "type": "string", "description": "'all': all; 'fwlb': FWLB; 'licexpire_drop': License Expire Drop; 'bwl_drop': BW Limit Drop; 'rx_kernel': Received kernel; 'rx_arp_req': ARP REQ Rcvd; 'rx_arp_resp': ARP RESP Rcvd; 'vlan_flood': VLAN Flood; 'l2_def_vlan_drop': L2 Default Vlan FWD Drop; 'ipv4_noroute_drop': IPv4 No Route Drop; 'ipv6_noroute_drop': IPv6 No Route Drop; 'prot_down_drop': Prot Down Drop; 'l2_forward': L2 Forward; 'l3_forward_ip': L3 IP Forward; 'l3_forward_ipv6': L3 IPv6 Forward; 'l4_process': L4 Process; 'unknown_prot_drop': Unknown Prot Drop; 'ttl_exceeded_drop': TTL Exceeded Drop; 'linkdown_drop': Link Down Drop; 'sport_drop': SPORT Drop; 'incorrect_len_drop': Incorrect Length Drop; 'ip_defrag': IP Defrag; 'acl_deny': ACL Denys; 'ipfrag_tcp': IP(TCP) Fragment Rcvd; 'ipfrag_overlap': IP Fragment Overlap; 'ipfrag_timeout': IP Fragment Timeout; 'ipfrag_overload': IP Frag Overload Drops; 'ipfrag_reasmoks': IP Fragment Reasm OKs; 'ipfrag_reasmfails': IP Fragment Reasm Fails; 'land_drop': Anomaly Land Attack Drop; 'ipoptions_drop': Anomaly IP OPT Drops; 'badpkt_drop': Bad Pkt Drop; 'pingofdeath_drop': Anomaly PingDeath Drop; 'allfrag_drop': Anomaly All Frag Drop; 'tcpnoflag_drop': Anomaly TCP noFlag Drop; 'tcpsynfrag_drop': Anomaly SYN Frag Drop; 'tcpsynfin_drop': Anomaly TCP SYNFIN Drop; 'ipsec_drop': IPSec Drop; 'bpdu_rcvd': BPDUs Received; 'bpdu_sent': BPDUs Sent; 'ctrl_syn_rate_drop': SYN rate exceeded Drop; 'ip_defrag_invalid_len': IP Invalid Length Frag; 'ipv4_frag_6rd_ok': IPv4 Frag 6RD OK; 'ipv4_frag_6rd_drop': IPv4 Frag 6RD Dropped; 'no_ip_drop': No IP Drop; 'ipv6frag_udp': IPv6 Frag UDP; 'ipv6frag_udp_dropped': IPv6 Frag UDP Dropped; 'ipv6frag_tcp_dropped': IPv6 Frag TCP Dropped; 'ipv6frag_ipip_ok': IPv6 Frag IPIP OKs; 'ipv6frag_ipip_dropped': IPv6 Frag IPIP Drop; 'ip_frag_oversize': IP Fragment oversize; 'ip_frag_too_many': IP Fragment too many; 'ipv4_novlanfwd_drop': IPv4 No L3 VLAN FWD Drop; 'ipv6_novlanfwd_drop': IPv6 No L3 VLAN FWD Drop; 'fpga_error_pkt1': FPGA Error PKT1; 'fpga_error_pkt2': FPGA Error PKT2; 'max_arp_drop': Max ARP Drop; 'ipv6frag_tcp': IPv6 Frag TCP; 'ipv6frag_icmp': IPv6 Frag ICMP; 'ipv6frag_ospf': IPv6 Frag OSPF; 'ipv6frag_esp': IPv6 Frag ESP; 'l4_in_ctrl_cpu': L4 In Ctrl CPU; 'mgmt_svc_drop': Management Service Drop; 'jumbo_frag_drop': Jumbo Frag Drop; 'ipv6_jumbo_frag_drop': IPv6 Jumbo Frag Drop; 'ipipv6_jumbo_frag_drop': IPIPv6 Jumbo Frag Drop; 'ipv6_ndisc_dad_solicits': IPv6 DAD on Solicits; 'ipv6_ndisc_dad_adverts': IPv6 DAD on Adverts; 'ipv6_ndisc_mac_changes': IPv6 DAD MAC Changed; 'ipv6_ndisc_out_of_memory': IPv6 DAD Out-of-memory; 'sp_non_ctrl_pkt_drop': Shared IP mode non ctrl packet to linux drop; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "sampling-enable"
        self.DeviceProxy = ""
        self.counters1 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Switch(A10BaseClass):
    
    """    :param sampling_enable: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "fwlb", "licexpire_drop", "bwl_drop", "rx_kernel", "rx_arp_req", "rx_arp_resp", "vlan_flood", "l2_def_vlan_drop", "ipv4_noroute_drop", "ipv6_noroute_drop", "prot_down_drop", "l2_forward", "l3_forward_ip", "l3_forward_ipv6", "l4_process", "unknown_prot_drop", "ttl_exceeded_drop", "linkdown_drop", "sport_drop", "incorrect_len_drop", "ip_defrag", "acl_deny", "ipfrag_tcp", "ipfrag_overlap", "ipfrag_timeout", "ipfrag_overload", "ipfrag_reasmoks", "ipfrag_reasmfails", "land_drop", "ipoptions_drop", "badpkt_drop", "pingofdeath_drop", "allfrag_drop", "tcpnoflag_drop", "tcpsynfrag_drop", "tcpsynfin_drop", "ipsec_drop", "bpdu_rcvd", "bpdu_sent", "ctrl_syn_rate_drop", "ip_defrag_invalid_len", "ipv4_frag_6rd_ok", "ipv4_frag_6rd_drop", "no_ip_drop", "ipv6frag_udp", "ipv6frag_udp_dropped", "ipv6frag_tcp_dropped", "ipv6frag_ipip_ok", "ipv6frag_ipip_dropped", "ip_frag_oversize", "ip_frag_too_many", "ipv4_novlanfwd_drop", "ipv6_novlanfwd_drop", "fpga_error_pkt1", "fpga_error_pkt2", "max_arp_drop", "ipv6frag_tcp", "ipv6frag_icmp", "ipv6frag_ospf", "ipv6frag_esp", "l4_in_ctrl_cpu", "mgmt_svc_drop", "jumbo_frag_drop", "ipv6_jumbo_frag_drop", "ipipv6_jumbo_frag_drop", "ipv6_ndisc_dad_solicits", "ipv6_ndisc_dad_adverts", "ipv6_ndisc_mac_changes", "ipv6_ndisc_out_of_memory", "sp_non_ctrl_pkt_drop"], "type": "string", "description": "'all': all; 'fwlb': FWLB; 'licexpire_drop': License Expire Drop; 'bwl_drop': BW Limit Drop; 'rx_kernel': Received kernel; 'rx_arp_req': ARP REQ Rcvd; 'rx_arp_resp': ARP RESP Rcvd; 'vlan_flood': VLAN Flood; 'l2_def_vlan_drop': L2 Default Vlan FWD Drop; 'ipv4_noroute_drop': IPv4 No Route Drop; 'ipv6_noroute_drop': IPv6 No Route Drop; 'prot_down_drop': Prot Down Drop; 'l2_forward': L2 Forward; 'l3_forward_ip': L3 IP Forward; 'l3_forward_ipv6': L3 IPv6 Forward; 'l4_process': L4 Process; 'unknown_prot_drop': Unknown Prot Drop; 'ttl_exceeded_drop': TTL Exceeded Drop; 'linkdown_drop': Link Down Drop; 'sport_drop': SPORT Drop; 'incorrect_len_drop': Incorrect Length Drop; 'ip_defrag': IP Defrag; 'acl_deny': ACL Denys; 'ipfrag_tcp': IP(TCP) Fragment Rcvd; 'ipfrag_overlap': IP Fragment Overlap; 'ipfrag_timeout': IP Fragment Timeout; 'ipfrag_overload': IP Frag Overload Drops; 'ipfrag_reasmoks': IP Fragment Reasm OKs; 'ipfrag_reasmfails': IP Fragment Reasm Fails; 'land_drop': Anomaly Land Attack Drop; 'ipoptions_drop': Anomaly IP OPT Drops; 'badpkt_drop': Bad Pkt Drop; 'pingofdeath_drop': Anomaly PingDeath Drop; 'allfrag_drop': Anomaly All Frag Drop; 'tcpnoflag_drop': Anomaly TCP noFlag Drop; 'tcpsynfrag_drop': Anomaly SYN Frag Drop; 'tcpsynfin_drop': Anomaly TCP SYNFIN Drop; 'ipsec_drop': IPSec Drop; 'bpdu_rcvd': BPDUs Received; 'bpdu_sent': BPDUs Sent; 'ctrl_syn_rate_drop': SYN rate exceeded Drop; 'ip_defrag_invalid_len': IP Invalid Length Frag; 'ipv4_frag_6rd_ok': IPv4 Frag 6RD OK; 'ipv4_frag_6rd_drop': IPv4 Frag 6RD Dropped; 'no_ip_drop': No IP Drop; 'ipv6frag_udp': IPv6 Frag UDP; 'ipv6frag_udp_dropped': IPv6 Frag UDP Dropped; 'ipv6frag_tcp_dropped': IPv6 Frag TCP Dropped; 'ipv6frag_ipip_ok': IPv6 Frag IPIP OKs; 'ipv6frag_ipip_dropped': IPv6 Frag IPIP Drop; 'ip_frag_oversize': IP Fragment oversize; 'ip_frag_too_many': IP Fragment too many; 'ipv4_novlanfwd_drop': IPv4 No L3 VLAN FWD Drop; 'ipv6_novlanfwd_drop': IPv6 No L3 VLAN FWD Drop; 'fpga_error_pkt1': FPGA Error PKT1; 'fpga_error_pkt2': FPGA Error PKT2; 'max_arp_drop': Max ARP Drop; 'ipv6frag_tcp': IPv6 Frag TCP; 'ipv6frag_icmp': IPv6 Frag ICMP; 'ipv6frag_ospf': IPv6 Frag OSPF; 'ipv6frag_esp': IPv6 Frag ESP; 'l4_in_ctrl_cpu': L4 In Ctrl CPU; 'mgmt_svc_drop': Management Service Drop; 'jumbo_frag_drop': Jumbo Frag Drop; 'ipv6_jumbo_frag_drop': IPv6 Jumbo Frag Drop; 'ipipv6_jumbo_frag_drop': IPIPv6 Jumbo Frag Drop; 'ipv6_ndisc_dad_solicits': IPv6 DAD on Solicits; 'ipv6_ndisc_dad_adverts': IPv6 DAD on Adverts; 'ipv6_ndisc_mac_changes': IPv6 DAD MAC Changed; 'ipv6_ndisc_out_of_memory': IPv6 DAD Out-of-memory; 'sp_non_ctrl_pkt_drop': Shared IP mode non ctrl packet to linux drop; ", "format": "enum"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Show slb switch statistics.

    Class switch supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/switch`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "switch"
        self.a10_url="/axapi/v3/slb/switch"
        self.DeviceProxy = ""
        self.sampling_enable = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


