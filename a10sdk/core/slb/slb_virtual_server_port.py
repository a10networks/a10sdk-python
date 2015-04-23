from a10sdk.common.A10BaseClass import A10BaseClass


class AclNameList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param acl_name: {"description": "Apply an access list name (Named Access List)", "format": "string", "minLength": 1, "maxLength": 16, "type": "string", "$ref": "/axapi/v3/ip/access-list"}
    :param acl_name_src_nat_pool: {"description": "Policy based Source NAT (NAT Pool or Pool Group)", "format": "string", "minLength": 1, "maxLength": 128, "type": "string", "$ref": "/axapi/v3/ip/nat/pool"}
    :param acl_name_seq_num: {"description": "Specify ACL precedence (sequence-number)", "minimum": 1, "type": "number", "maximum": 32, "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "acl-name-list"
        self.DeviceProxy = ""
        self.acl_name = ""
        self.acl_name_src_nat_pool = ""
        self.acl_name_seq_num = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class SamplingEnable(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param counters1: {"enum": ["all", "curr_conn", "total_l4_conn", "total_l7_conn", "total_tcp_conn", "total_conn", "total_fwd_bytes", "total_fwd_pkts", "total_rev_bytes", "total_rev_pkts", "total_dns_pkts", "total_mf_dns_pkts", "es_total_failure_actions", "compression_bytes_before", "compression_bytes_after", "compression_hit", "compression_miss", "compression_miss_no_client", "compression_miss_template_exclusion", "curr_req", "total_req", "total_req_succ", "peak_conn", "curr_conn_rate", "last_rsp_time", "fastest_rsp_time", "slowest_rsp_time"], "type": "string", "description": "'all': all; 'curr_conn': Current connections; 'total_l4_conn': Total L4 connections; 'total_l7_conn': Total L7 connections; 'total_tcp_conn': Total TCP connections; 'total_conn': Total connections; 'total_fwd_bytes': Total forward bytes; 'total_fwd_pkts': Total forward packets; 'total_rev_bytes': Total reverse bytes; 'total_rev_pkts': Total reverse packets; 'total_dns_pkts': Total DNS packets; 'total_mf_dns_pkts': Total MF DNS packets; 'es_total_failure_actions': Total failure actions; 'compression_bytes_before': Data into compression engine; 'compression_bytes_after': Data out of compression engine; 'compression_hit': Number of requests compressed; 'compression_miss': Number of requests NOT compressed; 'compression_miss_no_client': Compression miss no client; 'compression_miss_template_exclusion': Compression miss template exclusion; 'curr_req': Current requests; 'total_req': Total requests; 'total_req_succ': Total successful requests; 'peak_conn': Peak connections; 'curr_conn_rate': Current connection rate; 'last_rsp_time': Last response time; 'fastest_rsp_time': Fastest response time; 'slowest_rsp_time': Slowest response time; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "sampling-enable"
        self.DeviceProxy = ""
        self.counters1 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class AflexScripts(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param aflex: {"minLength": 1, "maxLength": 63, "type": "string", "description": "Bind aFleX Script to the Virtual Port (aFleX Script Name)", "format": "string-rlx"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "aflex-scripts"
        self.DeviceProxy = ""
        self.aflex = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class AclIdList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param acl_id_seq_num: {"description": "Specify ACL precedence (sequence-number)", "minimum": 1, "type": "number", "maximum": 32, "format": "number"}
    :param acl_id: {"description": "ACL id VPORT", "format": "number", "maximum": 199, "minimum": 1, "type": "number", "$ref": "/axapi/v3/access-list/standard"}
    :param acl_id_src_nat_pool: {"description": "Policy based Source NAT (NAT Pool or Pool Group)", "format": "string", "minLength": 1, "maxLength": 128, "type": "string", "$ref": "/axapi/v3/ip/nat/pool"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "acl-id-list"
        self.DeviceProxy = ""
        self.acl_id_seq_num = ""
        self.acl_id = ""
        self.acl_id_src_nat_pool = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class AuthCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param aaa_policy: {"minLength": 1, "maxLength": 63, "type": "string", "description": "Specify AAA policy name to bind to the virtual port", "format": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "auth-cfg"
        self.DeviceProxy = ""
        self.aaa_policy = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Port(A10BaseClass):
    
    """Class Description::
    Virtual Port.

    Class port supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param reset_on_server_selection_fail: {"default": 0, "optional": true, "type": "number", "description": "Send client reset when server selection fails", "format": "flag"}
    :param ha_conn_mirror: {"default": 0, "optional": true, "type": "number", "description": "Enable for HA Conn sync", "format": "flag"}
    :param template_ftp: {"description": "FTP port template (Ftp template name)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 31, "type": "string", "$ref": "/axapi/v3/slb/template/ftp"}
    :param protocol: {"optional": false, "enum": ["tcp", "udp", "others", "diameter", "dns-tcp", "dns-udp", "fast-http", "fix", "ftp", "ftp-proxy", "http", "https", "mlb", "mms", "mysql", "mssql", "radius", "rtsp", "sip", "sip-tcp", "sips", "smpp-tcp", "spdy", "spdys", "smtp", "ssl-proxy", "tcp-proxy", "tftp"], "type": "string", "description": "'tcp': TCP LB service; 'udp': UDP Port; 'others': for no tcp/udp protocol, do IP load balancing; 'diameter': diameter port; 'dns-tcp': DNS service over TCP; 'dns-udp': DNS service over UDP; 'fast-http': Fast HTTP Port; 'fix': FIX Port; 'ftp': File Transfer Protocol Port; 'ftp-proxy': ftp proxy port; 'http': HTTP Port; 'https': HTTPS port; 'mlb': Message based load balancing; 'mms': Microsoft Multimedia Service Port; 'mysql': mssql port; 'mssql': mssql; 'radius': RADIUS Port; 'rtsp': Real Time Streaming Protocol Port; 'sip': Session initiation protocol over UDP; 'sip-tcp': Session initiation protocol over TCP; 'sips': Session initiation protocol over TLS; 'smpp-tcp': SMPP service over TCP; 'spdy': spdy port; 'spdys': spdys port; 'smtp': SMTP Port; 'ssl-proxy': Generic SSL proxy; 'tcp-proxy': Generic TCP proxy; 'tftp': TFTP Port; ", "format": "enum"}
    :param force_routing_mode: {"default": 0, "optional": true, "type": "number", "description": "Force routing mode", "format": "flag"}
    :param waf_template: {"description": "WAF template (WAF Template Name)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/waf/template"}
    :param l7_hardware_assist: {"description": "FPGA assist L7 packet parsing", "format": "flag", "default": 0, "type": "number", "optional": true, "plat-neg-list": ["non-fpga", "soft-ax"]}
    :param template_persist_ssl_sid: {"description": "SSL session ID persistence (Source IP Persistence Config name)", "format": "string", "minLength": 1, "optional": true, "maxLength": 128, "type": "string", "$ref": "/axapi/v3/slb/template/persist/ssl-sid"}
    :param no_auto_up_on_aflex: {"default": 0, "optional": true, "type": "number", "description": "Don't automatically mark vport up when aFleX is bound", "format": "flag"}
    :param template_dns: {"description": "DNS template (DNS template name)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/slb/template/dns"}
    :param template_http_policy: {"description": "http-policy template (http-policy template name)", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/slb/template/http-policy"}
    :param gslb_enable: {"default": 0, "optional": true, "type": "number", "description": "Enable Global Server Load Balancing", "format": "flag"}
    :param template_policy: {"description": "Policy Template (Policy template name)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/slb/template/policy"}
    :param use_alternate_port: {"default": 0, "optional": true, "type": "number", "description": "Use alternate virtual port", "format": "flag"}
    :param ipinip: {"default": 0, "optional": true, "type": "number", "description": "Enable IP in IP", "format": "flag"}
    :param acl_name_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"acl-name": {"description": "Apply an access list name (Named Access List)", "format": "string", "minLength": 1, "maxLength": 16, "type": "string", "$ref": "/axapi/v3/ip/access-list"}, "acl-name-src-nat-pool": {"description": "Policy based Source NAT (NAT Pool or Pool Group)", "format": "string", "minLength": 1, "maxLength": 128, "type": "string", "$ref": "/axapi/v3/ip/nat/pool"}, "optional": true, "acl-name-seq-num": {"description": "Specify ACL precedence (sequence-number)", "minimum": 1, "type": "number", "maximum": 32, "format": "number"}}}]}
    :param stats_data_action: {"description": "'stats-data-enable': Enable statistical data collection for virtual port; 'stats-data-disable': Disable statistical data collection for virtual port; ", "format": "enum", "default": "stats-data-enable", "type": "string", "enum": ["stats-data-enable", "stats-data-disable"], "optional": true}
    :param template_persist_destination_ip: {"description": "Destination IP persistence (Destination IP persistence template name)", "format": "string", "minLength": 1, "optional": true, "maxLength": 128, "type": "string", "$ref": "/axapi/v3/slb/template/persist/destination-ip"}
    :param template_tcp_proxy_server: {"description": "TCP Proxy Config Server (TCP Proxy Config name)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/slb/template/tcp-proxy"}
    :param template_sip: {"description": "SIP template", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/slb/template/sip"}
    :param template_virtual_port: {"description": "Virtual port template (Virtual port template name)", "format": "string-rlx", "default": "default", "minLength": 1, "optional": true, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/slb/template/virtual-port"}
    :param conn_limit: {"description": "Connection Limit", "format": "number", "default": 8000000, "optional": true, "maximum": 8000000, "minimum": 1, "type": "number"}
    :param scaleout_device_group: {"description": "Device group id", "format": "number", "type": "number", "maximum": 16, "minimum": 1, "optional": true}
    :param template_client_ssl: {"description": "Client SSL Template (Client SSL Config Name)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/slb/template/client-ssl"}
    :param template_persist_cookie: {"description": "Cookie persistence (Cookie persistence template name)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 128, "type": "string", "$ref": "/axapi/v3/slb/template/persist/cookie"}
    :param template_tcp: {"description": "L4 TCP Template (TCP Config Name)", "format": "string-rlx", "default": "default", "minLength": 1, "optional": true, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/slb/template/tcp"}
    :param sampling_enable: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "curr_conn", "total_l4_conn", "total_l7_conn", "total_tcp_conn", "total_conn", "total_fwd_bytes", "total_fwd_pkts", "total_rev_bytes", "total_rev_pkts", "total_dns_pkts", "total_mf_dns_pkts", "es_total_failure_actions", "compression_bytes_before", "compression_bytes_after", "compression_hit", "compression_miss", "compression_miss_no_client", "compression_miss_template_exclusion", "curr_req", "total_req", "total_req_succ", "peak_conn", "curr_conn_rate", "last_rsp_time", "fastest_rsp_time", "slowest_rsp_time"], "type": "string", "description": "'all': all; 'curr_conn': Current connections; 'total_l4_conn': Total L4 connections; 'total_l7_conn': Total L7 connections; 'total_tcp_conn': Total TCP connections; 'total_conn': Total connections; 'total_fwd_bytes': Total forward bytes; 'total_fwd_pkts': Total forward packets; 'total_rev_bytes': Total reverse bytes; 'total_rev_pkts': Total reverse packets; 'total_dns_pkts': Total DNS packets; 'total_mf_dns_pkts': Total MF DNS packets; 'es_total_failure_actions': Total failure actions; 'compression_bytes_before': Data into compression engine; 'compression_bytes_after': Data out of compression engine; 'compression_hit': Number of requests compressed; 'compression_miss': Number of requests NOT compressed; 'compression_miss_no_client': Compression miss no client; 'compression_miss_template_exclusion': Compression miss template exclusion; 'curr_req': Current requests; 'total_req': Total requests; 'total_req_succ': Total successful requests; 'peak_conn': Peak connections; 'curr_conn_rate': Current connection rate; 'last_rsp_time': Last response time; 'fastest_rsp_time': Fastest response time; 'slowest_rsp_time': Slowest response time; ", "format": "enum"}}}]}
    :param template_connection_reuse: {"description": "Connection Reuse Template (Connection Reuse Template Name)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 128, "type": "string", "$ref": "/axapi/v3/slb/template/connection-reuse"}
    :param service_group: {"description": "Bind a Service Group to this Virtual Server (Service Group Name)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 128, "type": "string", "$ref": "/axapi/v3/slb/service-group"}
    :param pool: {"description": "Specify NAT pool or pool group", "format": "string", "minLength": 1, "optional": true, "maxLength": 128, "type": "string", "$ref": "/axapi/v3/ip/nat/pool"}
    :param persist_type: {"optional": true, "enum": ["src-dst-ip-swap-persist", "use-src-ip-for-dst-persist", "use-dst-ip-for-src-persist"], "type": "string", "description": "'src-dst-ip-swap-persist': Create persist session after source IP and destination IP swap; 'use-src-ip-for-dst-persist': Use the source IP to create a destination persist session; 'use-dst-ip-for-src-persist': Use the destination IP to create source IP persist session; ", "format": "enum"}
    :param template_fix: {"description": "FIX template (FIX Template Name)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/slb/template/fix"}
    :param snat_on_vip: {"default": 0, "optional": true, "type": "number", "description": "Enable source NAT traffic against VIP", "format": "flag"}
    :param use_default_if_no_server: {"default": 0, "optional": true, "type": "number", "description": "Use default forwarding if server selection failed", "format": "flag"}
    :param syn_cookie: {"default": 0, "optional": true, "type": "number", "description": "Enable syn-cookie", "format": "flag"}
    :param when_down: {"default": 0, "optional": true, "type": "number", "description": "Use alternate virtual port when down", "format": "flag"}
    :param template_udp: {"description": "L4 UDP Template (UDP Config Name)", "format": "string-rlx", "default": "default", "minLength": 1, "optional": true, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/slb/template/udp"}
    :param aflex_scripts: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"aflex": {"minLength": 1, "maxLength": 63, "type": "string", "description": "Bind aFleX Script to the Virtual Port (aFleX Script Name)", "format": "string-rlx"}, "optional": true}}]}
    :param acl_id_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"acl-id-seq-num": {"description": "Specify ACL precedence (sequence-number)", "minimum": 1, "type": "number", "maximum": 32, "format": "number"}, "acl-id": {"description": "ACL id VPORT", "format": "number", "maximum": 199, "minimum": 1, "type": "number", "$ref": "/axapi/v3/access-list/standard"}, "optional": true, "acl-id-src-nat-pool": {"description": "Policy based Source NAT (NAT Pool or Pool Group)", "format": "string", "minLength": 1, "maxLength": 128, "type": "string", "$ref": "/axapi/v3/ip/nat/pool"}}}]}
    :param rtp_sip_call_id_match: {"default": 0, "optional": true, "type": "number", "description": "rtp traffic try to match the real server of sip smp call-id session", "format": "flag"}
    :param alternate_port: {"description": "Alternate Virtual Port", "format": "flag", "default": 0, "optional": true, "modify-not-allowed": 1, "not": "range", "type": "number"}
    :param auto: {"default": 0, "optional": true, "type": "number", "description": "Configure auto NAT for the vport", "format": "flag"}
    :param view: {"description": "Specify a GSLB View (ID)", "format": "number", "type": "number", "maximum": 31, "minimum": 1, "optional": true}
    :param alternate_port_number: {"description": "Virtual Port", "format": "number", "type": "number", "maximum": 65534, "minimum": 0, "optional": true}
    :param port_number: {"description": "Port", "format": "number", "type": "number", "maximum": 65534, "minimum": 0, "optional": false}
    :param template_tcp_proxy_client: {"description": "TCP Proxy Config Client (TCP Proxy Config name)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/slb/template/tcp-proxy"}
    :param use_rcv_hop_for_resp: {"default": 0, "optional": true, "type": "number", "description": "Use receive hop for response to client", "format": "flag"}
    :param no_dest_nat: {"default": 0, "optional": true, "type": "number", "description": "Disable destination NAT", "format": "flag"}
    :param template_external_service: {"description": "External service template (external-service template name)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/slb/template/external-service"}
    :param scaleout_bucket_count: {"description": "Number of traffic buckets", "format": "number", "default": 32, "optional": true, "maximum": 256, "minimum": 1, "type": "number"}
    :param template_cache: {"description": "RAM caching template (Cache Template Name)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/slb/template/cache"}
    :param extended_stats: {"default": 0, "optional": true, "type": "number", "description": "Enable extended statistics on virtual port", "format": "flag"}
    :param expand: {"default": 0, "optional": true, "type": "number", "description": "expand syn-cookie with timestamp and wscale", "format": "flag"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param reset: {"default": 0, "optional": true, "type": "number", "description": "Send client reset when connection number over limit", "format": "flag"}
    :param req_fail: {"default": 0, "optional": true, "type": "number", "description": "Use alternate virtual port when L7 request fail", "format": "flag"}
    :param template_dblb: {"description": "DBLB Template (DBLB template name)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/slb/template/dblb"}
    :param skip_rev_hash: {"default": 0, "optional": true, "type": "number", "description": "Skip rev tuple hash insertion", "format": "flag"}
    :param name: {"description": "SLB Virtual Service Name", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 127, "type": "string"}
    :param template_smpp: {"description": "SMPP template", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/slb/template/smpp"}
    :param port_translation: {"default": 0, "optional": true, "type": "number", "description": "Enable port translation under no-dest-nat", "format": "flag"}
    :param precedence: {"default": 0, "optional": true, "type": "number", "description": "Set auto NAT pool as higher precedence for source NAT", "format": "flag"}
    :param clientip_sticky_nat: {"default": 0, "optional": true, "type": "number", "description": "Prefer to use same source NAT address for a client", "format": "flag"}
    :param template_persist_source_ip: {"description": "Source IP persistence (Source IP persistence template name)", "format": "string", "minLength": 1, "optional": true, "maxLength": 128, "type": "string", "$ref": "/axapi/v3/slb/template/persist/source-ip"}
    :param serv_sel_fail: {"default": 0, "optional": true, "type": "number", "description": "Use alternate virtual port when server selection failure", "format": "flag"}
    :param template_diameter: {"description": "Diameter Template (diameter template name)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/slb/template/diameter"}
    :param template_scaleout: {"description": "Scaleout template (Scaleout template name)", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param range: {"description": "Virtual Port range (Virtual Port range value)", "format": "number", "default": 0, "optional": true, "maximum": 254, "minimum": 0, "modify-not-allowed": 1, "not": "alternate-port", "type": "number"}
    :param when_down_protocol2: {"default": 0, "optional": true, "type": "number", "description": "Use alternate virtual port when down", "format": "flag"}
    :param def_selection_if_pref_failed: {"description": "'def-selection-if-pref-failed': Use default server selection method if prefer method failed; 'def-selection-if-pref-failed-disable': Stop using default server selection method if prefer method failed; ", "format": "enum", "default": "def-selection-if-pref-failed", "type": "string", "enum": ["def-selection-if-pref-failed", "def-selection-if-pref-failed-disable"], "optional": true}
    :param template_tcp_proxy: {"description": "TCP Proxy Template Name", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/slb/template/tcp-proxy"}
    :param template_smtp: {"description": "SMTP Template (SMTP Config Name)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/slb/template/smtp"}
    :param redirect_to_https: {"default": 0, "optional": true, "type": "number", "description": "Redirect HTTP to HTTPS", "format": "flag"}
    :param action: {"description": "'enable': Enable; 'disable': Disable; ", "format": "enum", "default": "enable", "type": "string", "enum": ["enable", "disable"], "optional": true}
    :param template_http: {"description": "HTTP Template (HTTP Config Name)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/slb/template/http"}
    :param no_logging: {"default": 0, "optional": true, "type": "number", "description": "Do not log connection over limit event", "format": "flag"}
    :param template_server_ssl: {"description": "Server Side SSL Template (Server SSL Name)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/slb/template/server-ssl"}
    :param alt_protocol2: {"optional": true, "enum": ["tcp"], "type": "string", "description": "'tcp': TCP LB service; ", "format": "enum"}
    :param alt_protocol1: {"optional": true, "enum": ["http"], "type": "string", "description": "'http': HTTP Port; ", "format": "enum"}
    :param message_switching: {"default": 0, "optional": true, "type": "number", "description": "Message switching", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/virtual-server/{name}/port/{port_number}+{protocol}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "port_number","protocol"]

        self.b_key = "port"
        self.a10_url="/axapi/v3/slb/virtual-server/{name}/port/{port_number}+{protocol}"
        self.DeviceProxy = ""
        self.reset_on_server_selection_fail = ""
        self.ha_conn_mirror = ""
        self.template_ftp = ""
        self.protocol = ""
        self.force_routing_mode = ""
        self.waf_template = ""
        self.l7_hardware_assist = ""
        self.template_persist_ssl_sid = ""
        self.no_auto_up_on_aflex = ""
        self.template_dns = ""
        self.template_http_policy = ""
        self.gslb_enable = ""
        self.template_policy = ""
        self.use_alternate_port = ""
        self.ipinip = ""
        self.acl_name_list = []
        self.stats_data_action = ""
        self.template_persist_destination_ip = ""
        self.template_tcp_proxy_server = ""
        self.template_sip = ""
        self.template_virtual_port = ""
        self.conn_limit = ""
        self.scaleout_device_group = ""
        self.template_client_ssl = ""
        self.template_persist_cookie = ""
        self.template_tcp = ""
        self.sampling_enable = []
        self.template_connection_reuse = ""
        self.service_group = ""
        self.pool = ""
        self.persist_type = ""
        self.template_fix = ""
        self.snat_on_vip = ""
        self.use_default_if_no_server = ""
        self.syn_cookie = ""
        self.when_down = ""
        self.template_udp = ""
        self.aflex_scripts = []
        self.acl_id_list = []
        self.auth_cfg = {}
        self.rtp_sip_call_id_match = ""
        self.alternate_port = ""
        self.auto = ""
        self.view = ""
        self.alternate_port_number = ""
        self.port_number = ""
        self.template_tcp_proxy_client = ""
        self.use_rcv_hop_for_resp = ""
        self.no_dest_nat = ""
        self.template_external_service = ""
        self.scaleout_bucket_count = ""
        self.template_cache = ""
        self.extended_stats = ""
        self.expand = ""
        self.uuid = ""
        self.reset = ""
        self.req_fail = ""
        self.template_dblb = ""
        self.skip_rev_hash = ""
        self.name = ""
        self.template_smpp = ""
        self.port_translation = ""
        self.precedence = ""
        self.clientip_sticky_nat = ""
        self.template_persist_source_ip = ""
        self.serv_sel_fail = ""
        self.template_diameter = ""
        self.template_scaleout = ""
        self.A10WW_range = ""
        self.when_down_protocol2 = ""
        self.def_selection_if_pref_failed = ""
        self.template_tcp_proxy = ""
        self.template_smtp = ""
        self.redirect_to_https = ""
        self.action = ""
        self.template_http = ""
        self.no_logging = ""
        self.template_server_ssl = ""
        self.alt_protocol2 = ""
        self.alt_protocol1 = ""
        self.message_switching = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


