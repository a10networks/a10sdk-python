from a10sdk.common.A10BaseClass import A10BaseClass


class SecurityAttack(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param layer_3: {"default": 0, "type": "number", "description": "drop packets with layer 3 anomaly", "format": "flag"}
    :param layer_4: {"default": 0, "type": "number", "description": "drop packets with layer 4 anomaly", "format": "flag"}
    :param security_attack: {"default": 0, "type": "number", "description": "drop packets causing security attack", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "security-attack"
        self.DeviceProxy = ""
        self.layer_3 = ""
        self.layer_4 = ""
        self.security_attack = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class PacketDeformity(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param layer_4: {"default": 0, "type": "number", "description": "drop packets with layer 4 anomaly", "format": "flag"}
    :param layer_3: {"default": 0, "type": "number", "description": "drop packets with layer 3 anomaly", "format": "flag"}
    :param packet_deformity: {"default": 0, "type": "number", "description": "drop packets with deformity", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "packet-deformity"
        self.DeviceProxy = ""
        self.layer_4 = ""
        self.layer_3 = ""
        self.packet_deformity = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class SamplingEnable(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param counters1: {"enum": ["all", "land", "emp_frg", "emp_mic_frg", "opt", "frg", "bad_ip_hdrlen", "bad_ip_flg", "bad_ip_ttl", "no_ip_payload", "over_ip_payload", "bad_ip_payload_len", "bad_ip_frg_offset", "csum", "pod", "bad_tcp_urg_offset", "tcp_sht_hdr", "tcp_bad_iplen", "tcp_null_frg", "tcp_null_scan", "tcp_syn_fin", "tcp_xmas", "tcp_xmas_scan", "tcp_syn_frg", "tcp_frg_hdr", "tcp_bad_csum", "udp_srt_hdr", "udp_bad_len", "udp_kerb_frg", "udp_port_lb", "udp_bad_csum", "runt_ip_hdr", "runt_tcp_udp_hdr", "ipip_tnl_msmtch", "tcp_opt_err", "ipip_tnl_err", "vxlan_err", "nvgre_err"], "type": "string", "description": "'all': all; 'land': land; 'emp_frg': emp_frg; 'emp_mic_frg': emp_mic_frg; 'opt': opt; 'frg': frg; 'bad_ip_hdrlen': bad_ip_hdrlen; 'bad_ip_flg': bad_ip_flg; 'bad_ip_ttl': bad_ip_ttl; 'no_ip_payload': no_ip_payload; 'over_ip_payload': over_ip_payload; 'bad_ip_payload_len': bad_ip_payload_len; 'bad_ip_frg_offset': bad_ip_frg_offset; 'csum': csum; 'pod': pod; 'bad_tcp_urg_offset': bad_tcp_urg_offset; 'tcp_sht_hdr': tcp_sht_hdr; 'tcp_bad_iplen': tcp_bad_iplen; 'tcp_null_frg': tcp_null_frg; 'tcp_null_scan': tcp_null_scan; 'tcp_syn_fin': tcp_syn_fin; 'tcp_xmas': tcp_xmas; 'tcp_xmas_scan': tcp_xmas_scan; 'tcp_syn_frg': tcp_syn_frg; 'tcp_frg_hdr': tcp_frg_hdr; 'tcp_bad_csum': tcp_bad_csum; 'udp_srt_hdr': udp_srt_hdr; 'udp_bad_len': udp_bad_len; 'udp_kerb_frg': udp_kerb_frg; 'udp_port_lb': udp_port_lb; 'udp_bad_csum': udp_bad_csum; 'runt_ip_hdr': runt_ip_hdr; 'runt_tcp_udp_hdr': runt_tcp_udp_hdr; 'ipip_tnl_msmtch': ipip_tnl_msmtch; 'tcp_opt_err': tcp_opt_err; 'ipip_tnl_err': ipip_tnl_err; 'vxlan_err': vxlan_err; 'nvgre_err': nvgre_err; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "sampling-enable"
        self.DeviceProxy = ""
        self.counters1 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class AnomalyDrop(A10BaseClass):
    
    """    :param frag: {"default": 0, "optional": true, "type": "number", "description": "drop all fragmented packets", "format": "flag"}
    :param out_of_sequence: {"description": "out of sequence packet threshold (threshold value)", "format": "number", "type": "number", "maximum": 127, "minimum": 1, "optional": true}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param tcp_syn_fin: {"default": 0, "optional": true, "type": "number", "description": "drop TCP packets with both syn and fin flags set", "format": "flag"}
    :param drop_all: {"default": 0, "optional": true, "type": "number", "description": "drop all IP anomaly packets", "format": "flag"}
    :param ping_of_death: {"default": 0, "optional": true, "type": "number", "description": "drop oversize ICMP packets", "format": "flag"}
    :param tcp_no_flag: {"default": 0, "optional": true, "type": "number", "description": "drop TCP packets with no flag", "format": "flag"}
    :param zero_window: {"description": "zero window size threshold (threshold value)", "format": "number", "type": "number", "maximum": 127, "minimum": 1, "optional": true}
    :param sampling_enable: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "land", "emp_frg", "emp_mic_frg", "opt", "frg", "bad_ip_hdrlen", "bad_ip_flg", "bad_ip_ttl", "no_ip_payload", "over_ip_payload", "bad_ip_payload_len", "bad_ip_frg_offset", "csum", "pod", "bad_tcp_urg_offset", "tcp_sht_hdr", "tcp_bad_iplen", "tcp_null_frg", "tcp_null_scan", "tcp_syn_fin", "tcp_xmas", "tcp_xmas_scan", "tcp_syn_frg", "tcp_frg_hdr", "tcp_bad_csum", "udp_srt_hdr", "udp_bad_len", "udp_kerb_frg", "udp_port_lb", "udp_bad_csum", "runt_ip_hdr", "runt_tcp_udp_hdr", "ipip_tnl_msmtch", "tcp_opt_err", "ipip_tnl_err", "vxlan_err", "nvgre_err"], "type": "string", "description": "'all': all; 'land': land; 'emp_frg': emp_frg; 'emp_mic_frg': emp_mic_frg; 'opt': opt; 'frg': frg; 'bad_ip_hdrlen': bad_ip_hdrlen; 'bad_ip_flg': bad_ip_flg; 'bad_ip_ttl': bad_ip_ttl; 'no_ip_payload': no_ip_payload; 'over_ip_payload': over_ip_payload; 'bad_ip_payload_len': bad_ip_payload_len; 'bad_ip_frg_offset': bad_ip_frg_offset; 'csum': csum; 'pod': pod; 'bad_tcp_urg_offset': bad_tcp_urg_offset; 'tcp_sht_hdr': tcp_sht_hdr; 'tcp_bad_iplen': tcp_bad_iplen; 'tcp_null_frg': tcp_null_frg; 'tcp_null_scan': tcp_null_scan; 'tcp_syn_fin': tcp_syn_fin; 'tcp_xmas': tcp_xmas; 'tcp_xmas_scan': tcp_xmas_scan; 'tcp_syn_frg': tcp_syn_frg; 'tcp_frg_hdr': tcp_frg_hdr; 'tcp_bad_csum': tcp_bad_csum; 'udp_srt_hdr': udp_srt_hdr; 'udp_bad_len': udp_bad_len; 'udp_kerb_frg': udp_kerb_frg; 'udp_port_lb': udp_port_lb; 'udp_bad_csum': udp_bad_csum; 'runt_ip_hdr': runt_ip_hdr; 'runt_tcp_udp_hdr': runt_tcp_udp_hdr; 'ipip_tnl_msmtch': ipip_tnl_msmtch; 'tcp_opt_err': tcp_opt_err; 'ipip_tnl_err': ipip_tnl_err; 'vxlan_err': vxlan_err; 'nvgre_err': nvgre_err; ", "format": "enum"}}}]}
    :param ip_option: {"default": 0, "optional": true, "type": "number", "description": "drop packets with IP options", "format": "flag"}
    :param land_attack: {"default": 0, "optional": true, "type": "number", "description": "drop IP packets with the same source and destination addresses", "format": "flag"}
    :param tcp_syn_frag: {"default": 0, "optional": true, "type": "number", "description": "drop fragmented TCP packets with syn flag set", "format": "flag"}
    :param bad_content: {"description": "bad content threshold (threshold value)", "format": "number", "type": "number", "maximum": 127, "minimum": 1, "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Set IP anomaly drop policy.

    Class anomaly-drop supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/ip/anomaly-drop`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "anomaly-drop"
        self.a10_url="/axapi/v3/ip/anomaly-drop"
        self.DeviceProxy = ""
        self.frag = ""
        self.out_of_sequence = ""
        self.uuid = ""
        self.tcp_syn_fin = ""
        self.drop_all = ""
        self.ping_of_death = ""
        self.security_attack = {}
        self.tcp_no_flag = ""
        self.packet_deformity = {}
        self.zero_window = ""
        self.sampling_enable = []
        self.ip_option = ""
        self.land_attack = ""
        self.tcp_syn_frag = ""
        self.bad_content = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


