from a10sdk.common.A10BaseClass import A10BaseClass


class Dns64Virtualserver(A10BaseClass):
    
    """Class Description::
    Create a DNS64 Virtual Server.

    Class dns64-virtualserver supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param use_if_ip: {"description": "Use Interface IP", "format": "flag", "default": 0, "optional": true, "plat-pos-list": ["soft-ax"], "not-list": ["ipv6-address", "ip-address"], "type": "number"}
    :param port_list: {"minItems": 1, "items": {"type": "port"}, "uniqueItems": true, "array": [{"required": ["port-number", "protocol"], "properties": {"protocol": {"optional": false, "enum": ["dns-udp"], "type": "string", "description": "'dns-udp': DNS service over UDP; ", "format": "enum"}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}, "precedence": {"default": 0, "optional": true, "type": "number", "description": "Set auto NAT pool as higher precedence for source NAT", "format": "flag"}, "auto": {"default": 0, "optional": true, "type": "number", "description": "Configure auto NAT for the vport", "format": "flag"}, "template-policy": {"description": "Policy Template (Policy template name)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/cgnv6/template/policy"}, "sampling-enable": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "curr_conn", "total_l4_conn", "total_l7_conn", "toatal_tcp_conn", "total_conn", "total_fwd_bytes", "total_fwd_pkts", "total_rev_bytes", "total_rev_pkts", "total_dns_pkts", "total_mf_dns_pkts", "es_total_failure_actions", "compression_bytes_before", "compression_bytes_after", "compression_hit", "compression_miss", "compression_miss_no_client", "compression_miss_template_exclusion", "curr_req", "total_req", "total_req_succ", "peak_conn", "curr_conn_rate", "last_rsp_time", "fastest_rsp_time", "slowest_rsp_time"], "type": "string", "description": "'all': all; 'curr_conn': curr_conn; 'total_l4_conn': total_l4_conn; 'total_l7_conn': total_l7_conn; 'toatal_tcp_conn': toatal_tcp_conn; 'total_conn': total_conn; 'total_fwd_bytes': total_fwd_bytes; 'total_fwd_pkts': total_fwd_pkts; 'total_rev_bytes': total_rev_bytes; 'total_rev_pkts': total_rev_pkts; 'total_dns_pkts': total_dns_pkts; 'total_mf_dns_pkts': total_mf_dns_pkts; 'es_total_failure_actions': es_total_failure_actions; 'compression_bytes_before': compression_bytes_before; 'compression_bytes_after': compression_bytes_after; 'compression_hit': compression_hit; 'compression_miss': compression_miss; 'compression_miss_no_client': compression_miss_no_client; 'compression_miss_template_exclusion': compression_miss_template_exclusion; 'curr_req': curr_req; 'total_req': total_req; 'total_req_succ': total_req_succ; 'peak_conn': peak_conn; 'curr_conn_rate': curr_conn_rate; 'last_rsp_time': last_rsp_time; 'fastest_rsp_time': fastest_rsp_time; 'slowest_rsp_time': slowest_rsp_time; ", "format": "enum"}}}]}, "port-number": {"description": "Port", "format": "number", "type": "number", "maximum": 65534, "minimum": 0, "optional": false}, "template-dns": {"description": "DNS template (DNS template name)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/cgnv6/template/dns"}, "service-group": {"description": "Bind a Service Group to this Virtual Server (Service Group Name)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 128, "type": "string", "$ref": "/axapi/v3/cgnv6/service-group"}, "action": {"description": "'enable': Enable; 'disable': Disable; ", "format": "enum", "default": "enable", "type": "string", "enum": ["enable", "disable"], "optional": true}, "pool": {"description": "Specify NAT pool or pool group", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 128, "type": "string", "$ref": "/axapi/v3/ip/nat/pool"}}}], "type": "array", "$ref": "/axapi/v3/cgnv6/dns64-virtualserver/{name}/port/{port-number}+{protocol}"}
    :param name: {"description": "CGNV6 Virtual Server Name", "format": "string-rlx", "minLength": 1, "optional": false, "maxLength": 127, "type": "string"}
    :param template_policy: {"description": "Policy template name", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/cgnv6/template/policy"}
    :param vrid: {"description": "Join a vrrp group (Specify ha VRRP-A vrid)", "format": "number", "type": "number", "maximum": 31, "minimum": 1, "optional": true}
    :param enable_disable_action: {"description": "'enable': Enable Virtual Server (default); 'disable': Disable Virtual Server; ", "format": "enum", "default": "enable", "type": "string", "enum": ["enable", "disable"], "optional": true}
    :param policy: {"default": 0, "optional": true, "type": "number", "description": "Policy template", "format": "flag"}
    :param netmask: {"optional": true, "modify-not-allowed": 1, "type": "string", "description": "IP subnet mask", "format": "ipv4-netmask-brief"}
    :param ip_address: {"description": "IP Address", "format": "ipv4-address", "optional": true, "not-list": ["ipv6-address", "use-if-ip"], "modify-not-allowed": 1, "type": "string"}
    :param ipv6_address: {"description": "IPV6 address", "format": "ipv6-address", "optional": true, "not-list": ["ip-address", "use-if-ip"], "modify-not-allowed": 1, "type": "string"}
    :param ethernet: {"optional": true, "plat-pos-list": ["soft-ax"], "type": "number", "description": "Ethernet interface", "format": "interface"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/dns64-virtualserver/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "dns64-virtualserver"
        self.a10_url="/axapi/v3/cgnv6/dns64-virtualserver/{name}"
        self.DeviceProxy = ""
        self.use_if_ip = ""
        self.port_list = []
        self.name = ""
        self.template_policy = ""
        self.vrid = ""
        self.enable_disable_action = ""
        self.policy = ""
        self.netmask = ""
        self.ip_address = ""
        self.ipv6_address = ""
        self.ethernet = ""
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


