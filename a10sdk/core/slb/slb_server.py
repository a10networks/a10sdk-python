from a10sdk.common.A10BaseClass import A10BaseClass


class AlternateServer(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param alternate_name: {"minLength": 1, "maxLength": 127, "type": "string", "description": "Alternate Name", "format": "string-rlx"}
    :param alternate: {"description": "Alternate Server (Alternate Server Number)", "minimum": 1, "type": "number", "maximum": 16, "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "alternate-server"
        self.DeviceProxy = ""
        self.alternate_name = ""
        self.alternate = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class SamplingEnable(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param counters1: {"enum": ["all", "curr-conn", "total-conn", "fwd-pkt", "rev-pkt", "peak-conn"], "type": "string", "description": "'all': all; 'curr-conn': Current connections; 'total-conn': Total connections; 'fwd-pkt': Forward packets; 'rev-pkt': Reverse packets; 'peak-conn': Peak connections; ", "format": "enum"}
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
    Server.

    Class server supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param health_check_disable: {"description": "Disable configured health check configuration", "format": "flag", "default": 0, "optional": true, "not": "health-check", "type": "number"}
    :param port_list: {"minItems": 1, "items": {"type": "port"}, "uniqueItems": true, "array": [{"required": ["port-number", "protocol"], "properties": {"conn-limit": {"description": "Connection Limit", "format": "number", "default": 8000000, "optional": true, "maximum": 8000000, "minimum": 1, "type": "number"}, "health-check-disable": {"description": "Disable health check", "format": "flag", "default": 0, "optional": true, "not-list": ["health-check", "health-check-follow-port"], "type": "number"}, "extended-stats": {"default": 0, "optional": true, "type": "number", "description": "Enable extended statistics on real server port", "format": "flag"}, "template-server-ssl": {"description": "Server side SSL template (Server side SSL Name)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/slb/template/server-ssl"}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}, "weight": {"description": "Port Weight (Connection Weight)", "format": "number", "default": 1, "optional": true, "maximum": 100, "minimum": 1, "type": "number"}, "conn-resume": {"description": "Connection Resume", "format": "number", "type": "number", "maximum": 1000000, "minimum": 1, "optional": true}, "alternate-port": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"alternate-name": {"minLength": 1, "maxLength": 127, "type": "string", "description": "Alternate Name", "format": "string-rlx"}, "alternate-server-port": {"description": "Port (Alternate Server Port Value)", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}, "alternate": {"description": "Alternate Server Number", "minimum": 1, "type": "number", "maximum": 16, "format": "number"}, "optional": true}}]}, "no-logging": {"default": 0, "optional": true, "type": "number", "description": "Do not log connection over limit event", "format": "flag"}, "stats-data-action": {"description": "'stats-data-enable': Enable statistical data collection for real server port; 'stats-data-disable': Disable statistical data collection for real server port; ", "format": "enum", "default": "stats-data-enable", "type": "string", "enum": ["stats-data-enable", "stats-data-disable"], "optional": true}, "follow-port-protocol": {"optional": true, "enum": ["tcp", "udp"], "type": "string", "description": "'tcp': TCP Port; 'udp': UDP Port; ", "format": "enum"}, "port-number": {"description": "Port Number", "format": "number", "type": "number", "maximum": 65534, "minimum": 0, "optional": false}, "range": {"description": "Port range (Port range value - used for vip-to-rport-mapping)", "format": "number", "default": 0, "optional": true, "maximum": 254, "minimum": 0, "type": "number"}, "sampling-enable": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "curr_conn", "curr_req", "total_req", "total_req_succ", "total_fwd_bytes", "total_fwd_pkts", "total_rev_bytes", "total_rev_pkts", "total_conn", "last_total_conn", "peak_conn", "es_resp_200", "es_resp_300", "es_resp_400", "es_resp_500", "es_resp_other", "es_req_count", "es_resp_count", "es_resp_invalid_http", "total_rev_pkts_inspected", "total_rev_pkts_inspected_good_status_code", "response_time", "fastest_rsp_time", "slowest_rsp_time"], "type": "string", "description": "'all': all; 'curr_conn': Current connections; 'curr_req': Current requests; 'total_req': Total Requests; 'total_req_succ': Total requests succ; 'total_fwd_bytes': Forward bytes; 'total_fwd_pkts': Forward packets; 'total_rev_bytes': Reverse bytes; 'total_rev_pkts': Reverse packets; 'total_conn': Total connections; 'last_total_conn': Last total connections; 'peak_conn': Peak connections; 'es_resp_200': Response status 200; 'es_resp_300': Response status 300; 'es_resp_400': Response status 400; 'es_resp_500': Response status 500; 'es_resp_other': Response status other; 'es_req_count': Total proxy request; 'es_resp_count': Total proxy response; 'es_resp_invalid_http': Total non-http response; 'total_rev_pkts_inspected': Total reverse packets inspected; 'total_rev_pkts_inspected_good_status_code': Total reverse packets with good status code inspected; 'response_time': Response time; 'fastest_rsp_time': Fastest response time; 'slowest_rsp_time': Slowest response time; ", "format": "enum"}}}]}, "no-ssl": {"default": 0, "optional": true, "type": "number", "description": "No SSL", "format": "flag"}, "auth-cfg": {"type": "object", "properties": {"service-principal-name": {"minLength": 1, "maxLength": 128, "type": "string", "description": "Service Principal Name (Kerberos principal name)", "format": "string-rlx"}}}, "action": {"description": "'enable': enable; 'disable': disable; 'disable-with-health-check': disable port, but health check work; ", "format": "enum", "default": "enable", "type": "string", "enum": ["enable", "disable", "disable-with-health-check"], "optional": true}, "protocol": {"optional": false, "enum": ["tcp", "udp"], "type": "string", "description": "'tcp': TCP Port; 'udp': UDP Port; ", "format": "enum"}, "health-check-follow-port": {"description": "Specify which port to follow for health status (Port Number)", "format": "number", "optional": true, "not-list": ["health-check", "health-check-disable"], "maximum": 65534, "minimum": 1, "type": "number"}, "health-check": {"description": "Health Check (Monitor Name)", "format": "string", "minLength": 1, "not-list": ["health-check-follow-port", "health-check-disable"], "optional": true, "maxLength": 31, "type": "string", "$ref": "/axapi/v3/health/monitor"}, "template-port": {"description": "Port template (Port template name)", "format": "string-rlx", "default": "default", "minLength": 1, "optional": true, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/slb/template/port"}}}], "type": "array", "$ref": "/axapi/v3/slb/server/{name}/port/{port-number}+{protocol}"}
    :param stats_data_action: {"description": "'stats-data-enable': Enable statistical data collection for real server; 'stats-data-disable': Disable statistical data collection for real server; ", "format": "enum", "default": "stats-data-enable", "type": "string", "enum": ["stats-data-enable", "stats-data-disable"], "optional": true}
    :param slow_start: {"default": 0, "optional": true, "type": "number", "description": "Slowly ramp up the connection number after server is up (start from 128, then double every 10 sec till 4096)", "format": "flag"}
    :param weight: {"description": "Weight for this Real Server (Connection Weight)", "format": "number", "default": 1, "optional": true, "maximum": 100, "minimum": 1, "type": "number"}
    :param spoofing_cache: {"default": 0, "optional": true, "type": "number", "description": "This server is a spoofing cache", "format": "flag"}
    :param conn_limit: {"description": "Connection Limit", "format": "number", "default": 8000000, "optional": true, "maximum": 8000000, "minimum": 1, "type": "number"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param fqdn_name: {"description": "Server hostname", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param external_ip: {"optional": true, "type": "string", "description": "External IP address for NAT of GSLB", "format": "ipv4-address"}
    :param ipv6: {"optional": true, "type": "string", "description": "IPv6 address Mapping of GSLB", "format": "ipv6-address"}
    :param template_server: {"description": "Server template (Server template name)", "format": "string-rlx", "default": "default", "minLength": 1, "optional": true, "maxLength": 32, "type": "string", "$ref": "/axapi/v3/slb/template/server"}
    :param server_ipv6_addr: {"optional": true, "modify-not-allowed": 1, "type": "string", "description": "IPV6 address", "format": "ipv6-address"}
    :param alternate_server: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"alternate-name": {"minLength": 1, "maxLength": 127, "type": "string", "description": "Alternate Name", "format": "string-rlx"}, "alternate": {"description": "Alternate Server (Alternate Server Number)", "minimum": 1, "type": "number", "maximum": 16, "format": "number"}, "optional": true}}]}
    :param host: {"optional": true, "modify-not-allowed": 1, "type": "string", "description": "IP Address", "format": "ipv4-address"}
    :param extended_stats: {"default": 0, "optional": true, "type": "number", "description": "Enable extended statistics on real server", "format": "flag"}
    :param conn_resume: {"description": "Connection Resume (Connection Resume (min active conn before resume taking new conn))", "format": "number", "type": "number", "maximum": 1000000, "minimum": 1, "optional": true}
    :param name: {"description": "Server Name", "format": "string-rlx", "minLength": 1, "optional": false, "maxLength": 127, "type": "string"}
    :param sampling_enable: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "curr-conn", "total-conn", "fwd-pkt", "rev-pkt", "peak-conn"], "type": "string", "description": "'all': all; 'curr-conn': Current connections; 'total-conn': Total connections; 'fwd-pkt': Forward packets; 'rev-pkt': Reverse packets; 'peak-conn': Peak connections; ", "format": "enum"}}}]}
    :param action: {"description": "'enable': Enable this Real Server; 'disable': Disable this Real Server; 'disable-with-health-check': disable real server, but health check work; ", "format": "enum", "default": "enable", "type": "string", "enum": ["enable", "disable", "disable-with-health-check"], "optional": true}
    :param health_check: {"description": "Health Check Monitor (Health monitor name)", "format": "string", "minLength": 1, "optional": true, "maxLength": 31, "not": "health-check-disable", "type": "string", "$ref": "/axapi/v3/health/monitor"}
    :param no_logging: {"default": 0, "optional": true, "type": "number", "description": "Do not log connection over limit event", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/server/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "server"
        self.a10_url="/axapi/v3/slb/server/{name}"
        self.DeviceProxy = ""
        self.health_check_disable = ""
        self.port_list = []
        self.stats_data_action = ""
        self.slow_start = ""
        self.weight = ""
        self.spoofing_cache = ""
        self.conn_limit = ""
        self.uuid = ""
        self.fqdn_name = ""
        self.external_ip = ""
        self.ipv6 = ""
        self.template_server = ""
        self.server_ipv6_addr = ""
        self.alternate_server = []
        self.host = ""
        self.extended_stats = ""
        self.conn_resume = ""
        self.name = ""
        self.sampling_enable = []
        self.action = ""
        self.health_check = ""
        self.no_logging = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


