from a10sdk.common.A10BaseClass import A10BaseClass


class SamplingEnable(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param counters1: {"enum": ["all", "curr-conn", "total-conn", "fwd-pkt", "rev-pkt", "peak-conn"], "type": "string", "description": "'all': all; 'curr-conn': curr-conn; 'total-conn': total-conn; 'fwd-pkt': fwd-pkt; 'rev-pkt': rev-pkt; 'peak-conn': peak-conn; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "sampling-enable"
        self.DeviceProxy = ""
        self.counters1 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Server(A10BaseClass):
    
    """Class Description::
    CGNV6 logging Server.

    Class server supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param health_check_disable: {"description": "Disable configured health check configuration", "format": "flag", "default": 0, "optional": true, "not": "health-check", "type": "number"}
    :param port_list: {"minItems": 1, "items": {"type": "port"}, "uniqueItems": true, "array": [{"required": ["port-number", "protocol"], "properties": {"health-check-disable": {"description": "Disable health check", "format": "flag", "default": 0, "optional": true, "not": "health-check", "type": "number"}, "protocol": {"optional": false, "enum": ["tcp", "udp"], "type": "string", "description": "'tcp': TCP Port; 'udp': UDP Port; ", "format": "enum"}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}, "port-number": {"description": "Port Number", "format": "number", "type": "number", "maximum": 65534, "minimum": 0, "optional": false}, "sampling-enable": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "curr_conn", "curr_req", "total_req", "total_req_succ", "total_fwd_bytes", "total_fwd_pkts", "total_rev_bytes", "total_rev_pkts", "total_conn", "last_total_conn", "peak_conn", "es_resp_200", "es_resp_300", "es_resp_400", "es_resp_500", "es_resp_other", "es_req_count", "es_resp_count", "es_resp_invalid_http", "total_rev_pkts_inspected", "total_rev_pkts_inspected_good_status_code", "response_time", "fastest_rsp_time", "slowest_rsp_time"], "type": "string", "description": "'all': all; 'curr_conn': curr_conn; 'curr_req': curr_req; 'total_req': total_req; 'total_req_succ': total_req_succ; 'total_fwd_bytes': total_fwd_bytes; 'total_fwd_pkts': total_fwd_pkts; 'total_rev_bytes': total_rev_bytes; 'total_rev_pkts': total_rev_pkts; 'total_conn': total_conn; 'last_total_conn': last_total_conn; 'peak_conn': peak_conn; 'es_resp_200': es_resp_200; 'es_resp_300': es_resp_300; 'es_resp_400': es_resp_400; 'es_resp_500': es_resp_500; 'es_resp_other': es_resp_other; 'es_req_count': es_req_count; 'es_resp_count': es_resp_count; 'es_resp_invalid_http': es_resp_invalid_http; 'total_rev_pkts_inspected': total_rev_pkts_inspected; 'total_rev_pkts_inspected_good_status_code': total_rev_pkts_inspected_good_status_code; 'response_time': response_time; 'fastest_rsp_time': fastest_rsp_time; 'slowest_rsp_time': slowest_rsp_time; ", "format": "enum"}}}]}, "action": {"description": "'enable': enable; 'disable': disable; ", "format": "enum", "default": "enable", "type": "string", "enum": ["enable", "disable"], "optional": true}, "health-check": {"description": "Health Check (Monitor Name)", "format": "string", "minLength": 1, "optional": true, "maxLength": 31, "not": "health-check-disable", "type": "string", "$ref": "/axapi/v3/health/monitor"}}}], "type": "array", "$ref": "/axapi/v3/cgnv6/server/{name}/port/{port-number}+{protocol}"}
    :param name: {"description": "Server Name", "format": "string-rlx", "minLength": 1, "optional": false, "maxLength": 127, "type": "string"}
    :param fqdn_name: {"description": "Server hostname", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param sampling_enable: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "curr-conn", "total-conn", "fwd-pkt", "rev-pkt", "peak-conn"], "type": "string", "description": "'all': all; 'curr-conn': curr-conn; 'total-conn': total-conn; 'fwd-pkt': fwd-pkt; 'rev-pkt': rev-pkt; 'peak-conn': peak-conn; ", "format": "enum"}}}]}
    :param host: {"optional": true, "modify-not-allowed": 1, "type": "string", "description": "IP Address", "format": "ipv4-address"}
    :param action: {"description": "'enable': Enable this Real Server; 'disable': Disable this Real Server; ", "format": "enum", "default": "enable", "type": "string", "enum": ["enable", "disable"], "optional": true}
    :param server_ipv6_addr: {"optional": true, "modify-not-allowed": 1, "type": "string", "description": "IPV6 address", "format": "ipv6-address"}
    :param health_check: {"description": "Health Check Monitor (Health monitor name)", "format": "string", "minLength": 1, "optional": true, "maxLength": 31, "not": "health-check-disable", "type": "string", "$ref": "/axapi/v3/health/monitor"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/server/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "server"
        self.a10_url="/axapi/v3/cgnv6/server/{name}"
        self.DeviceProxy = ""
        self.health_check_disable = ""
        self.port_list = []
        self.name = ""
        self.fqdn_name = ""
        self.sampling_enable = []
        self.host = ""
        self.action = ""
        self.server_ipv6_addr = ""
        self.health_check = ""
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


