from a10sdk.common.A10BaseClass import A10BaseClass


class SamplingEnable(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param counters1: {"enum": ["all", "curr_conn", "total_l4_conn", "total_l7_conn", "toatal_tcp_conn", "total_conn", "total_fwd_bytes", "total_fwd_pkts", "total_rev_bytes", "total_rev_pkts", "total_dns_pkts", "total_mf_dns_pkts", "es_total_failure_actions", "compression_bytes_before", "compression_bytes_after", "compression_hit", "compression_miss", "compression_miss_no_client", "compression_miss_template_exclusion", "curr_req", "total_req", "total_req_succ", "peak_conn", "curr_conn_rate", "last_rsp_time", "fastest_rsp_time", "slowest_rsp_time"], "type": "string", "description": "'all': all; 'curr_conn': curr_conn; 'total_l4_conn': total_l4_conn; 'total_l7_conn': total_l7_conn; 'toatal_tcp_conn': toatal_tcp_conn; 'total_conn': total_conn; 'total_fwd_bytes': total_fwd_bytes; 'total_fwd_pkts': total_fwd_pkts; 'total_rev_bytes': total_rev_bytes; 'total_rev_pkts': total_rev_pkts; 'total_dns_pkts': total_dns_pkts; 'total_mf_dns_pkts': total_mf_dns_pkts; 'es_total_failure_actions': es_total_failure_actions; 'compression_bytes_before': compression_bytes_before; 'compression_bytes_after': compression_bytes_after; 'compression_hit': compression_hit; 'compression_miss': compression_miss; 'compression_miss_no_client': compression_miss_no_client; 'compression_miss_template_exclusion': compression_miss_template_exclusion; 'curr_req': curr_req; 'total_req': total_req; 'total_req_succ': total_req_succ; 'peak_conn': peak_conn; 'curr_conn_rate': curr_conn_rate; 'last_rsp_time': last_rsp_time; 'fastest_rsp_time': fastest_rsp_time; 'slowest_rsp_time': slowest_rsp_time; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "sampling-enable"
        self.DeviceProxy = ""
        self.counters1 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Port(A10BaseClass):
    
    """Class Description::
    Virtual Port.

    Class port supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param protocol: {"optional": false, "enum": ["dns-udp"], "type": "string", "description": "'dns-udp': DNS service over UDP; ", "format": "enum"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param precedence: {"default": 0, "optional": true, "type": "number", "description": "Set auto NAT pool as higher precedence for source NAT", "format": "flag"}
    :param auto: {"default": 0, "optional": true, "type": "number", "description": "Configure auto NAT for the vport", "format": "flag"}
    :param template_policy: {"description": "Policy Template (Policy template name)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/cgnv6/template/policy"}
    :param sampling_enable: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "curr_conn", "total_l4_conn", "total_l7_conn", "toatal_tcp_conn", "total_conn", "total_fwd_bytes", "total_fwd_pkts", "total_rev_bytes", "total_rev_pkts", "total_dns_pkts", "total_mf_dns_pkts", "es_total_failure_actions", "compression_bytes_before", "compression_bytes_after", "compression_hit", "compression_miss", "compression_miss_no_client", "compression_miss_template_exclusion", "curr_req", "total_req", "total_req_succ", "peak_conn", "curr_conn_rate", "last_rsp_time", "fastest_rsp_time", "slowest_rsp_time"], "type": "string", "description": "'all': all; 'curr_conn': curr_conn; 'total_l4_conn': total_l4_conn; 'total_l7_conn': total_l7_conn; 'toatal_tcp_conn': toatal_tcp_conn; 'total_conn': total_conn; 'total_fwd_bytes': total_fwd_bytes; 'total_fwd_pkts': total_fwd_pkts; 'total_rev_bytes': total_rev_bytes; 'total_rev_pkts': total_rev_pkts; 'total_dns_pkts': total_dns_pkts; 'total_mf_dns_pkts': total_mf_dns_pkts; 'es_total_failure_actions': es_total_failure_actions; 'compression_bytes_before': compression_bytes_before; 'compression_bytes_after': compression_bytes_after; 'compression_hit': compression_hit; 'compression_miss': compression_miss; 'compression_miss_no_client': compression_miss_no_client; 'compression_miss_template_exclusion': compression_miss_template_exclusion; 'curr_req': curr_req; 'total_req': total_req; 'total_req_succ': total_req_succ; 'peak_conn': peak_conn; 'curr_conn_rate': curr_conn_rate; 'last_rsp_time': last_rsp_time; 'fastest_rsp_time': fastest_rsp_time; 'slowest_rsp_time': slowest_rsp_time; ", "format": "enum"}}}]}
    :param port_number: {"description": "Port", "format": "number", "type": "number", "maximum": 65534, "minimum": 0, "optional": false}
    :param template_dns: {"description": "DNS template (DNS template name)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/cgnv6/template/dns"}
    :param service_group: {"description": "Bind a Service Group to this Virtual Server (Service Group Name)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 128, "type": "string", "$ref": "/axapi/v3/cgnv6/service-group"}
    :param action: {"description": "'enable': Enable; 'disable': Disable; ", "format": "enum", "default": "enable", "type": "string", "enum": ["enable", "disable"], "optional": true}
    :param pool: {"description": "Specify NAT pool or pool group", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 128, "type": "string", "$ref": "/axapi/v3/ip/nat/pool"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/dns64-virtualserver/{name}/port/{port_number}+{protocol}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "port_number","protocol"]

        self.b_key = "port"
        self.a10_url="/axapi/v3/cgnv6/dns64-virtualserver/{name}/port/{port_number}+{protocol}"
        self.DeviceProxy = ""
        self.protocol = ""
        self.uuid = ""
        self.precedence = ""
        self.auto = ""
        self.template_policy = ""
        self.sampling_enable = []
        self.port_number = ""
        self.template_dns = ""
        self.service_group = ""
        self.action = ""
        self.pool = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


