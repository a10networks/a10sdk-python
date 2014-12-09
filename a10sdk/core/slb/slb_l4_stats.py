from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param conn_rate_limit_drop: {"description": "Conn rate limit drops", "format": "counter", "type": "number", "oid": "37", "optional": true, "size": "8"}
    :param outrst_stale_sess: {"description": "TCP out RST stale sess", "format": "counter", "type": "number", "oid": "17", "optional": true, "size": "8"}
    :param connlimit_reset: {"description": "Conn Limit resets", "format": "counter", "type": "number", "oid": "36", "optional": true, "size": "8"}
    :param tcp_sess_aged_out: {"description": "TCP Session aged out", "format": "counter", "type": "number", "oid": "42", "optional": true, "size": "8"}
    :param bw_rate_limit_exceed: {"description": "BW-Limit Exceed drop", "format": "counter", "type": "number", "oid": "70", "optional": true, "size": "8"}
    :param no_vport_drop: {"description": "vport not matching drops", "format": "counter", "type": "number", "oid": "30", "optional": true, "size": "8"}
    :param snat_icmp_error_process: {"description": "Source NAT ICMP Process", "format": "counter", "type": "number", "oid": "25", "optional": true, "size": "8"}
    :param port_preserve_attempt: {"description": "NAT Port Preserve Try", "format": "counter", "type": "number", "oid": "66", "optional": true, "size": "8"}
    :param anomaly_pbslb_drop: {"description": "Anomaly pbslb drop", "format": "counter", "type": "number", "oid": "59", "optional": true, "size": "8"}
    :param proxy_nosock_drop: {"description": "Proxy no sock drops", "format": "counter", "type": "number", "oid": "39", "optional": true, "size": "8"}
    :param svr_syn_handshake_fail: {"description": "L4 server handshake fail", "format": "counter", "type": "number", "oid": "79", "optional": true, "size": "8"}
    :param snat_icmp_no_match: {"description": "Source NAT ICMP No Match", "format": "counter", "type": "number", "oid": "26", "optional": true, "size": "8"}
    :param drop_gslb: {"description": "Drop GSLB", "format": "counter", "type": "number", "oid": "48", "optional": true, "size": "8"}
    :param outrst_aflex: {"description": "TCP out RST aFleX", "format": "counter", "type": "number", "oid": "16", "optional": true, "size": "8"}
    :param anomaly_zero_win: {"description": "Anomaly zero window", "format": "counter", "type": "number", "oid": "57", "optional": true, "size": "8"}
    :param concurrent_conn_exceed: {"description": "L3V Conn Limit Drop", "format": "counter", "type": "number", "oid": "78", "optional": true, "size": "8"}
    :param reset_l7_on_failover: {"description": "RST L7 on failover", "format": "counter", "type": "number", "oid": "62", "optional": true, "size": "8"}
    :param nosyn_drop_rst: {"description": "No SYN pkt drops - RST", "format": "counter", "type": "number", "oid": "33", "optional": true, "size": "8"}
    :param anomaly_bad_content: {"description": "Anomaly bad content", "format": "counter", "type": "number", "oid": "58", "optional": true, "size": "8"}
    :param ignore_msl: {"description": "ignore msl", "format": "counter", "type": "number", "oid": "63", "optional": true, "size": "8"}
    :param tcpsyndata_drop: {"description": "TCP SYN With Data Drop", "format": "counter", "type": "number", "oid": "68", "optional": true, "size": "8"}
    :param nosyn_drop_fin: {"description": "No SYN pkt drops - FIN", "format": "counter", "type": "number", "oid": "32", "optional": true, "size": "8"}
    :param anomaly_out_seq: {"description": "Anomaly out of sequence", "format": "counter", "type": "number", "oid": "56", "optional": true, "size": "8"}
    :param tcp_rev_ackfin: {"description": "L4 rcv rev FIN|ACK", "format": "counter", "type": "number", "oid": "93", "optional": true, "size": "8"}
    :param tcp_rev_fin: {"description": "L4 rcv rev FIN", "format": "counter", "type": "number", "oid": "5", "optional": true, "size": "8"}
    :param conn_rate_limit_reset: {"description": "Conn rate limit resets", "format": "counter", "type": "number", "oid": "38", "optional": true, "size": "8"}
    :param out_seq_ack_drop: {"description": "Out of sequence ACK drop", "format": "counter", "type": "number", "oid": "103", "optional": true, "size": "8"}
    :param bw_watermark_drop: {"description": "BW-Watermark drop", "format": "counter", "type": "number", "oid": "71", "optional": true, "size": "8"}
    :param sess_aged_out: {"description": "Session aged out", "format": "counter", "type": "number", "oid": "41", "optional": true, "size": "8"}
    :param tcp_invalid_drop: {"description": "TCP invalid drop", "format": "counter", "type": "number", "oid": "55", "optional": true, "size": "8"}
    :param syn_stale_sess: {"description": "SYN stale sess drop", "format": "counter", "type": "number", "oid": "18", "optional": true, "size": "8"}
    :param syncookie_buff_drop: {"description": "TCP SYN cookie buff drop", "format": "counter", "type": "number", "oid": "107", "optional": true, "size": "8"}
    :param inudp: {"description": "UDP received", "format": "counter", "type": "number", "oid": "8", "optional": true, "size": "8"}
    :param tcpotherflags_drop: {"description": "TCP SYN Other Flags Drop", "format": "counter", "type": "number", "oid": "69", "optional": true, "size": "8"}
    :param udp_sess_aged_out: {"description": "UDP Session aged out", "format": "counter", "type": "number", "oid": "43", "optional": true, "size": "8"}
    :param auto_reassign: {"description": "Auto-reselect server", "format": "counter", "type": "number", "oid": "51", "optional": true, "size": "8"}
    :param dns_id_switch: {"description": "DNS query id switch", "format": "counter", "type": "number", "oid": "111", "optional": true, "size": "8"}
    :param fast_aging_set: {"description": "Fast aging set", "format": "counter", "type": "number", "oid": "52", "optional": true, "size": "8"}
    :param outrst_ack_attack: {"description": "TCP out RST ACK attack", "format": "counter", "type": "number", "oid": "15", "optional": true, "size": "8"}
    :param connlimit_drop: {"description": "Conn Limit drops", "format": "counter", "type": "number", "oid": "35", "optional": true, "size": "8"}
    :param udp_req_one_oneplus_resp: {"description": "L4 UDP req rsps", "format": "counter", "type": "number", "oid": "97", "optional": true, "size": "8"}
    :param tcp_syn_rcv_rst: {"description": "L4 rcv RST on SYN", "format": "counter", "type": "number", "oid": "83", "optional": true, "size": "8"}
    :param ssl_cps_exceed: {"description": "SSL CPS exceed drop", "format": "counter", "type": "number", "oid": "75", "optional": true, "size": "8"}
    :param syncookiessentfailed: {"description": "TCP SYN cookie snt fail", "format": "counter", "type": "number", "oid": "11", "optional": true, "size": "8"}
    :param ssl_tpt_exceed: {"description": "SSL TPT exceed drop", "format": "counter", "type": "number", "oid": "76", "optional": true, "size": "8"}
    :param smart_nat_id_mismatch: {"description": "Auto NAT id mismatch", "format": "counter", "type": "number", "oid": "27", "optional": true, "size": "8"}
    :param tcp_fwd_ackfin: {"description": "L4 rcv fwd FIN|ACK", "format": "counter", "type": "number", "oid": "7", "optional": true, "size": "8"}
    :param ssl_watermark_drop: {"description": "SSL TPT-Watermark drop", "format": "counter", "type": "number", "oid": "77", "optional": true, "size": "8"}
    :param tcp_rexmit_synack_delq: {"description": "L4 rcv rexmit SYN|ACK DQ", "format": "counter", "type": "number", "oid": "90", "optional": true, "size": "8"}
    :param tcp_fwd_fin: {"description": "L4 rcv fwd FIN", "format": "counter", "type": "number", "oid": "6", "optional": true, "size": "8"}
    :param tcp_fwd_fin_dup: {"description": "L4 rcv fwd FIN dup", "format": "counter", "type": "number", "oid": "91", "optional": true, "size": "8"}
    :param nosyn_drop_ack: {"description": "No SYN pkt drops - ACK", "format": "counter", "type": "number", "oid": "34", "optional": true, "size": "8"}
    :param tcp_rexmit_synack: {"description": "L4 rcv rexmit SYN|ACK", "format": "counter", "type": "number", "oid": "89", "optional": true, "size": "8"}
    :param skip_insert_client_ip: {"description": "Skip Insert-client-ip", "format": "counter", "type": "number", "oid": "109", "optional": true, "size": "8"}
    :param l3_dsr: {"description": "L3 DSR received", "format": "counter", "type": "number", "oid": "65", "optional": true, "size": "8"}
    :param tcp_sess_noest_aged_out: {"description": "TCP no-Est Sess aged out", "format": "counter", "type": "number", "oid": "84", "optional": true, "size": "8"}
    :param syn_rate: {"description": "TCP SYN rate per sec", "format": "counter", "type": "number", "oid": "106", "optional": true, "size": "8"}
    :param l7_cps_exceed: {"description": "L7 CPS exceed drop", "format": "counter", "type": "number", "oid": "74", "optional": true, "size": "8"}
    :param synattack: {"description": "L4 SYN attack", "format": "counter", "type": "number", "oid": "105", "optional": true, "size": "8"}
    :param drop_aflex: {"description": "aFleX drops", "format": "counter", "type": "number", "oid": "40", "optional": true, "size": "8"}
    :param tcp_est: {"description": "L4 TCP Established", "format": "counter", "type": "number", "oid": "104", "optional": true, "size": "8"}
    :param svrselfail: {"description": "Server sel failure", "format": "counter", "type": "number", "oid": "20", "optional": true, "size": "8"}
    :param outrst_broker: {"description": "TCP out RST L4 proxy", "format": "counter", "type": "number", "oid": "14", "optional": true, "size": "8"}
    :param tcp_sess_noest_csyn_rcv_aged_out: {"description": "no-Est CSYN rcv aged out", "format": "counter", "type": "number", "oid": "85", "optional": true, "size": "8"}
    :param novport_drop: {"description": "NAT no session drops", "format": "counter", "type": "number", "oid": "29", "optional": true, "size": "8"}
    :param udp_req_oneplus_no_resp: {"description": "L4 UDP reqs no rsp", "format": "counter", "type": "number", "oid": "96", "optional": true, "size": "8"}
    :param fast_aging_reset: {"description": "Fast aging reset", "format": "counter", "type": "number", "oid": "53", "optional": true, "size": "8"}
    :param syncookiessent: {"description": "TCP SYN cookie snt", "format": "counter", "type": "number", "oid": "9", "optional": true, "size": "8"}
    :param tcp_rexmit_syn: {"description": "L4 rcv rexmit SYN", "format": "counter", "type": "number", "oid": "87", "optional": true, "size": "8"}
    :param outrst: {"description": "TCP out RST", "format": "counter", "type": "number", "oid": "12", "optional": true, "size": "8"}
    :param tcp_ax_rexmit_syn: {"description": "L4 AX re-xmit SYN", "format": "counter", "type": "number", "oid": "81", "optional": true, "size": "8"}
    :param tcp_sess_noest_ssyn_xmit_aged_out: {"description": "no-Est SSYN snt aged out", "format": "counter", "type": "number", "oid": "86", "optional": true, "size": "8"}
    :param syncookie_buff_queue: {"description": "TCP SYN cookie buff queue", "format": "counter", "type": "number", "oid": "108", "optional": true, "size": "8"}
    :param dns_policy_drop: {"description": "DNS Policy Drop", "format": "counter", "type": "number", "oid": "54", "optional": true, "size": "8"}
    :param throttle_syn: {"description": "SYN Throttle", "format": "counter", "type": "number", "oid": "47", "optional": true, "size": "8"}
    :param nosyn_drop: {"description": "No SYN pkt drops", "format": "counter", "type": "number", "oid": "31", "optional": true, "size": "8"}
    :param l4_cps_exceed: {"description": "L4 CPS exceed drop", "format": "counter", "type": "number", "oid": "72", "optional": true, "size": "8"}
    :param tcp_syn_rcv_ack: {"description": "L4 rcv ACK on SYN", "format": "counter", "type": "number", "oid": "82", "optional": true, "size": "8"}
    :param snat_fail: {"description": "Source NAT failure", "format": "counter", "type": "number", "oid": "22", "optional": true, "size": "8"}
    :param no_resourse_drop: {"description": "No resource drop", "format": "counter", "type": "number", "oid": "60", "optional": true, "size": "8"}
    :param inband_hm_retry: {"description": "Inband HM retry", "format": "counter", "type": "number", "oid": "49", "optional": true, "size": "8"}
    :param synreceived: {"description": "TCP SYN received", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "8"}
    :param reset_unknown_conn: {"description": "Reset unknown conn", "format": "counter", "type": "number", "oid": "61", "optional": true, "size": "8"}
    :param l2_dsr: {"description": "L2 DSR received", "format": "counter", "type": "number", "oid": "64", "optional": true, "size": "8"}
    :param outrst_nosyn: {"description": "TCP out RST no SYN", "format": "counter", "type": "number", "oid": "13", "optional": true, "size": "8"}
    :param udp_req_more_resp: {"description": "L4 UDP req greater than rsps", "format": "counter", "type": "number", "oid": "99", "optional": true, "size": "8"}
    :param other_sess_aged_out: {"description": "Other Session aged out", "format": "counter", "type": "number", "oid": "44", "optional": true, "size": "8"}
    :param snat_no_rev_route: {"description": "Source NAT no rev route", "format": "counter", "type": "number", "oid": "24", "optional": true, "size": "8"}
    :param tcp_fwd_rst: {"description": "L4 rcv fwd RST", "format": "counter", "type": "number", "oid": "94", "optional": true, "size": "8"}
    :param tcp_no_slb: {"description": "TCP no SLB", "format": "counter", "type": "number", "oid": "45", "optional": true, "size": "8"}
    :param nat_cps_exceed: {"description": "NAT CPS exceed drop", "format": "counter", "type": "number", "oid": "73", "optional": true, "size": "8"}
    :param udp_resp_oneplus: {"description": "L4 UDP rsps", "format": "counter", "type": "number", "oid": "102", "optional": true, "size": "8"}
    :param outrst_tcpproxy: {"description": "TCP out RST TCP proxy", "format": "counter", "type": "number", "oid": "19", "optional": true, "size": "8"}
    :param tcp_rev_fin_dup: {"description": "L4 rcv rev FIN dup", "format": "counter", "type": "number", "oid": "92", "optional": true, "size": "8"}
    :param udp_req_resp_notmatch: {"description": "L4 UDP req/rsp not match", "format": "counter", "type": "number", "oid": "98", "optional": true, "size": "8"}
    :param udp_no_slb: {"description": "UDP no SLB", "format": "counter", "type": "number", "oid": "46", "optional": true, "size": "8"}
    :param port_preserve_succ: {"description": "NAT Port Preserve Succ", "format": "counter", "type": "number", "oid": "67", "optional": true, "size": "8"}
    :param udp_resp_more_req: {"description": "L4 UDP rsps greater than reqs", "format": "counter", "type": "number", "oid": "100", "optional": true, "size": "8"}
    :param intcp: {"description": "TCP received", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}
    :param tcp_fwd_last_ack: {"description": "L4 rcv fwd last ACK", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "8"}
    :param syncookiescheckfailed: {"description": "TCP SYN cookie failed", "format": "counter", "type": "number", "oid": "28", "optional": true, "size": "8"}
    :param tcp_rexmit_syn_delq: {"description": "L4 rcv rexmit SYN (delq)", "format": "counter", "type": "number", "oid": "88", "optional": true, "size": "8"}
    :param stateless_conn_timeout: {"description": "L4 stateless Conn TO", "format": "counter", "type": "number", "oid": "80", "optional": true, "size": "8"}
    :param tcp_rev_last_ack: {"description": "L4 rcv rev last ACK", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "8"}
    :param tcp_rev_rst: {"description": "L4 rcv rev RST", "format": "counter", "type": "number", "oid": "95", "optional": true, "size": "8"}
    :param noroute: {"description": "IP out noroute", "format": "counter", "type": "number", "oid": "21", "optional": true, "size": "8"}
    :param udp_req_oneplus: {"description": "L4 UDP reqs", "format": "counter", "type": "number", "oid": "101", "optional": true, "size": "8"}
    :param syncookiessent_ts: {"description": "TCP SYN cookie snt ts", "format": "counter", "type": "number", "oid": "10", "optional": true, "size": "8"}
    :param snat_no_fwd_route: {"description": "Source NAT no fwd route", "format": "counter", "type": "number", "oid": "23", "optional": true, "size": "8"}
    :param synreceived_hw: {"description": "TCP SYN (HW SYN cookie)", "format": "counter", "type": "number", "oid": "110", "optional": true, "size": "8"}
    :param inband_hm_reassign: {"description": "Inband HM reassign", "format": "counter", "type": "number", "oid": "50", "optional": true, "size": "8"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.conn_rate_limit_drop = ""
        self.outrst_stale_sess = ""
        self.connlimit_reset = ""
        self.tcp_sess_aged_out = ""
        self.bw_rate_limit_exceed = ""
        self.no_vport_drop = ""
        self.snat_icmp_error_process = ""
        self.port_preserve_attempt = ""
        self.anomaly_pbslb_drop = ""
        self.proxy_nosock_drop = ""
        self.svr_syn_handshake_fail = ""
        self.snat_icmp_no_match = ""
        self.drop_gslb = ""
        self.outrst_aflex = ""
        self.anomaly_zero_win = ""
        self.concurrent_conn_exceed = ""
        self.reset_l7_on_failover = ""
        self.nosyn_drop_rst = ""
        self.anomaly_bad_content = ""
        self.ignore_msl = ""
        self.tcpsyndata_drop = ""
        self.nosyn_drop_fin = ""
        self.anomaly_out_seq = ""
        self.tcp_rev_ackfin = ""
        self.tcp_rev_fin = ""
        self.conn_rate_limit_reset = ""
        self.out_seq_ack_drop = ""
        self.bw_watermark_drop = ""
        self.sess_aged_out = ""
        self.tcp_invalid_drop = ""
        self.syn_stale_sess = ""
        self.syncookie_buff_drop = ""
        self.inudp = ""
        self.tcpotherflags_drop = ""
        self.udp_sess_aged_out = ""
        self.auto_reassign = ""
        self.dns_id_switch = ""
        self.fast_aging_set = ""
        self.outrst_ack_attack = ""
        self.connlimit_drop = ""
        self.udp_req_one_oneplus_resp = ""
        self.tcp_syn_rcv_rst = ""
        self.ssl_cps_exceed = ""
        self.syncookiessentfailed = ""
        self.ssl_tpt_exceed = ""
        self.smart_nat_id_mismatch = ""
        self.tcp_fwd_ackfin = ""
        self.ssl_watermark_drop = ""
        self.tcp_rexmit_synack_delq = ""
        self.tcp_fwd_fin = ""
        self.tcp_fwd_fin_dup = ""
        self.nosyn_drop_ack = ""
        self.tcp_rexmit_synack = ""
        self.skip_insert_client_ip = ""
        self.l3_dsr = ""
        self.tcp_sess_noest_aged_out = ""
        self.syn_rate = ""
        self.l7_cps_exceed = ""
        self.synattack = ""
        self.drop_aflex = ""
        self.tcp_est = ""
        self.svrselfail = ""
        self.outrst_broker = ""
        self.tcp_sess_noest_csyn_rcv_aged_out = ""
        self.novport_drop = ""
        self.udp_req_oneplus_no_resp = ""
        self.fast_aging_reset = ""
        self.syncookiessent = ""
        self.tcp_rexmit_syn = ""
        self.outrst = ""
        self.tcp_ax_rexmit_syn = ""
        self.tcp_sess_noest_ssyn_xmit_aged_out = ""
        self.syncookie_buff_queue = ""
        self.dns_policy_drop = ""
        self.throttle_syn = ""
        self.nosyn_drop = ""
        self.l4_cps_exceed = ""
        self.tcp_syn_rcv_ack = ""
        self.snat_fail = ""
        self.no_resourse_drop = ""
        self.inband_hm_retry = ""
        self.synreceived = ""
        self.reset_unknown_conn = ""
        self.l2_dsr = ""
        self.outrst_nosyn = ""
        self.udp_req_more_resp = ""
        self.other_sess_aged_out = ""
        self.snat_no_rev_route = ""
        self.tcp_fwd_rst = ""
        self.tcp_no_slb = ""
        self.nat_cps_exceed = ""
        self.udp_resp_oneplus = ""
        self.outrst_tcpproxy = ""
        self.tcp_rev_fin_dup = ""
        self.udp_req_resp_notmatch = ""
        self.udp_no_slb = ""
        self.port_preserve_succ = ""
        self.udp_resp_more_req = ""
        self.intcp = ""
        self.tcp_fwd_last_ack = ""
        self.syncookiescheckfailed = ""
        self.tcp_rexmit_syn_delq = ""
        self.stateless_conn_timeout = ""
        self.tcp_rev_last_ack = ""
        self.tcp_rev_rst = ""
        self.noroute = ""
        self.udp_req_oneplus = ""
        self.syncookiessent_ts = ""
        self.snat_no_fwd_route = ""
        self.synreceived_hw = ""
        self.inband_hm_reassign = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class L4(A10BaseClass):
    
    """Class Description::
    Statistics for the object l4.

    Class l4 supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/l4/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "l4"
        self.a10_url="/axapi/v3/slb/l4/stats"
        self.DeviceProxy = ""
        self.stats = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


