from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param tcp_frg_hdr: {"optional": true, "size": "8", "type": "number", "oid": "24", "format": "counter"}
    :param tcp_null_frg: {"optional": true, "size": "8", "type": "number", "oid": "18", "format": "counter"}
    :param over_ip_payload: {"optional": true, "size": "8", "type": "number", "oid": "10", "format": "counter"}
    :param udp_bad_csum: {"optional": true, "size": "8", "type": "number", "oid": "30", "format": "counter"}
    :param nvgre_err: {"optional": true, "size": "8", "type": "number", "oid": "37", "format": "counter"}
    :param tcp_syn_fin: {"optional": true, "size": "8", "type": "number", "oid": "20", "format": "counter"}
    :param udp_kerb_frg: {"optional": true, "size": "8", "type": "number", "oid": "28", "format": "counter"}
    :param tcp_syn_frg: {"optional": true, "size": "8", "type": "number", "oid": "23", "format": "counter"}
    :param tcp_bad_iplen: {"optional": true, "size": "8", "type": "number", "oid": "17", "format": "counter"}
    :param ipip_tnl_err: {"optional": true, "size": "8", "type": "number", "oid": "35", "format": "counter"}
    :param csum: {"optional": true, "size": "8", "type": "number", "oid": "13", "format": "counter"}
    :param tcp_xmas: {"optional": true, "size": "8", "type": "number", "oid": "21", "format": "counter"}
    :param pod: {"optional": true, "size": "8", "type": "number", "oid": "14", "format": "counter"}
    :param tcp_bad_csum: {"optional": true, "size": "8", "type": "number", "oid": "25", "format": "counter"}
    :param emp_frg: {"optional": true, "size": "8", "type": "number", "oid": "2", "format": "counter"}
    :param frg: {"optional": true, "size": "8", "type": "number", "oid": "5", "format": "counter"}
    :param bad_ip_ttl: {"optional": true, "size": "8", "type": "number", "oid": "8", "format": "counter"}
    :param bad_ip_frg_offset: {"optional": true, "size": "8", "type": "number", "oid": "12", "format": "counter"}
    :param tcp_sht_hdr: {"optional": true, "size": "8", "type": "number", "oid": "16", "format": "counter"}
    :param tcp_xmas_scan: {"optional": true, "size": "8", "type": "number", "oid": "22", "format": "counter"}
    :param no_ip_payload: {"optional": true, "size": "8", "type": "number", "oid": "9", "format": "counter"}
    :param udp_bad_len: {"optional": true, "size": "8", "type": "number", "oid": "27", "format": "counter"}
    :param opt: {"optional": true, "size": "8", "type": "number", "oid": "4", "format": "counter"}
    :param vxlan_err: {"optional": true, "size": "8", "type": "number", "oid": "36", "format": "counter"}
    :param bad_ip_payload_len: {"optional": true, "size": "8", "type": "number", "oid": "11", "format": "counter"}
    :param runt_ip_hdr: {"optional": true, "size": "8", "type": "number", "oid": "31", "format": "counter"}
    :param runt_tcp_udp_hdr: {"optional": true, "size": "8", "type": "number", "oid": "32", "format": "counter"}
    :param emp_mic_frg: {"optional": true, "size": "8", "type": "number", "oid": "3", "format": "counter"}
    :param bad_ip_hdrlen: {"optional": true, "size": "8", "type": "number", "oid": "6", "format": "counter"}
    :param tcp_null_scan: {"optional": true, "size": "8", "type": "number", "oid": "19", "format": "counter"}
    :param land: {"optional": true, "size": "8", "type": "number", "oid": "1", "format": "counter"}
    :param tcp_opt_err: {"optional": true, "size": "8", "type": "number", "oid": "34", "format": "counter"}
    :param bad_ip_flg: {"optional": true, "size": "8", "type": "number", "oid": "7", "format": "counter"}
    :param udp_srt_hdr: {"optional": true, "size": "8", "type": "number", "oid": "26", "format": "counter"}
    :param udp_port_lb: {"optional": true, "size": "8", "type": "number", "oid": "29", "format": "counter"}
    :param bad_tcp_urg_offset: {"optional": true, "size": "8", "type": "number", "oid": "15", "format": "counter"}
    :param ipip_tnl_msmtch: {"optional": true, "size": "8", "type": "number", "oid": "33", "format": "counter"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.tcp_frg_hdr = ""
        self.tcp_null_frg = ""
        self.over_ip_payload = ""
        self.udp_bad_csum = ""
        self.nvgre_err = ""
        self.tcp_syn_fin = ""
        self.udp_kerb_frg = ""
        self.tcp_syn_frg = ""
        self.tcp_bad_iplen = ""
        self.ipip_tnl_err = ""
        self.csum = ""
        self.tcp_xmas = ""
        self.pod = ""
        self.tcp_bad_csum = ""
        self.emp_frg = ""
        self.frg = ""
        self.bad_ip_ttl = ""
        self.bad_ip_frg_offset = ""
        self.tcp_sht_hdr = ""
        self.tcp_xmas_scan = ""
        self.no_ip_payload = ""
        self.udp_bad_len = ""
        self.opt = ""
        self.vxlan_err = ""
        self.bad_ip_payload_len = ""
        self.runt_ip_hdr = ""
        self.runt_tcp_udp_hdr = ""
        self.emp_mic_frg = ""
        self.bad_ip_hdrlen = ""
        self.tcp_null_scan = ""
        self.land = ""
        self.tcp_opt_err = ""
        self.bad_ip_flg = ""
        self.udp_srt_hdr = ""
        self.udp_port_lb = ""
        self.bad_tcp_urg_offset = ""
        self.ipip_tnl_msmtch = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class AnomalyDrop(A10BaseClass):
    
    """Class Description::
    Statistics for the object anomaly-drop.

    Class anomaly-drop supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/ip/anomaly-drop/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "anomaly-drop"
        self.a10_url="/axapi/v3/ip/anomaly-drop/stats"
        self.DeviceProxy = ""
        self.stats = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


