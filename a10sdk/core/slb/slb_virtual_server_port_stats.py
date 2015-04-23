from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param curr_req: {"description": "Current requests", "format": "counter", "type": "number", "oid": "19", "optional": true, "size": "8"}
    :param total_fwd_bytes: {"description": "Total forward bytes", "format": "counter", "type": "number", "oid": "6", "optional": true, "size": "8"}
    :param compression_miss: {"description": "Number of requests NOT compressed", "format": "counter", "type": "number", "oid": "16", "optional": true, "size": "2"}
    :param fastest_rsp_time: {"description": "Fastest response time", "format": "counter", "type": "number", "oid": "25", "optional": true, "size": "8"}
    :param total_fwd_pkts: {"description": "Total forward packets", "format": "counter", "type": "number", "oid": "7", "optional": true, "size": "8"}
    :param total_tcp_conn: {"description": "Total TCP connections", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "8"}
    :param total_mf_dns_pkts: {"description": "Total MF DNS packets", "format": "counter", "type": "number", "oid": "11", "optional": true, "size": "2"}
    :param compression_miss_template_exclusion: {"description": "Compression miss template exclusion", "format": "counter", "type": "number", "oid": "18", "optional": true, "size": "2"}
    :param total_dns_pkts: {"description": "Total DNS packets", "format": "counter", "type": "number", "oid": "10", "optional": true, "size": "2"}
    :param peak_conn: {"description": "Peak connections", "format": "counter", "type": "number", "oid": "22", "optional": true, "size": "8"}
    :param compression_bytes_after: {"description": "Data out of compression engine", "format": "counter", "type": "number", "oid": "14", "optional": true, "size": "2"}
    :param total_req: {"description": "Total requests", "format": "counter", "type": "number", "oid": "20", "optional": true, "size": "8"}
    :param compression_bytes_before: {"description": "Data into compression engine", "format": "counter", "type": "number", "oid": "13", "optional": true, "size": "2"}
    :param last_rsp_time: {"description": "Last response time", "format": "counter", "type": "number", "oid": "24", "optional": true, "size": "8"}
    :param curr_conn: {"description": "Current connections", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}
    :param total_rev_bytes: {"description": "Total reverse bytes", "format": "counter", "type": "number", "oid": "8", "optional": true, "size": "8"}
    :param curr_conn_rate: {"description": "Current connection rate", "format": "counter", "type": "number", "oid": "23", "optional": true, "size": "8"}
    :param compression_miss_no_client: {"description": "Compression miss no client", "format": "counter", "type": "number", "oid": "17", "optional": true, "size": "2"}
    :param es_total_failure_actions: {"description": "Total failure actions", "format": "counter", "type": "number", "oid": "12", "optional": true, "size": "2"}
    :param total_conn: {"description": "Total connections", "format": "counter", "type": "number", "oid": "5", "optional": true, "size": "8"}
    :param total_rev_pkts: {"description": "Total reverse packets", "format": "counter", "type": "number", "oid": "9", "optional": true, "size": "8"}
    :param total_l7_conn: {"description": "Total L7 connections", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "8"}
    :param total_req_succ: {"description": "Total successful requests", "format": "counter", "type": "number", "oid": "21", "optional": true, "size": "8"}
    :param total_l4_conn: {"description": "Total L4 connections", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "8"}
    :param slowest_rsp_time: {"description": "Slowest response time", "format": "counter", "type": "number", "oid": "26", "optional": true, "size": "8"}
    :param compression_hit: {"description": "Number of requests compressed", "format": "counter", "type": "number", "oid": "15", "optional": true, "size": "2"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.curr_req = ""
        self.total_fwd_bytes = ""
        self.compression_miss = ""
        self.fastest_rsp_time = ""
        self.total_fwd_pkts = ""
        self.total_tcp_conn = ""
        self.total_mf_dns_pkts = ""
        self.compression_miss_template_exclusion = ""
        self.total_dns_pkts = ""
        self.peak_conn = ""
        self.compression_bytes_after = ""
        self.total_req = ""
        self.compression_bytes_before = ""
        self.last_rsp_time = ""
        self.curr_conn = ""
        self.total_rev_bytes = ""
        self.curr_conn_rate = ""
        self.compression_miss_no_client = ""
        self.es_total_failure_actions = ""
        self.total_conn = ""
        self.total_rev_pkts = ""
        self.total_l7_conn = ""
        self.total_req_succ = ""
        self.total_l4_conn = ""
        self.slowest_rsp_time = ""
        self.compression_hit = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Port(A10BaseClass):
    
    """Class Description::
    Statistics for the object port.

    Class port supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param protocol: {"enum": ["tcp", "udp", "others", "diameter", "dns-tcp", "dns-udp", "fast-http", "fix", "ftp", "ftp-proxy", "http", "https", "mlb", "mms", "mysql", "mssql", "radius", "rtsp", "sip", "sip-tcp", "sips", "smpp-tcp", "spdy", "spdys", "smtp", "ssl-proxy", "tcp-proxy", "tftp"], "description": "'tcp': TCP LB service; 'udp': UDP Port; 'others': for no tcp/udp protocol, do IP load balancing; 'diameter': diameter port; 'dns-tcp': DNS service over TCP; 'dns-udp': DNS service over UDP; 'fast-http': Fast HTTP Port; 'fix': FIX Port; 'ftp': File Transfer Protocol Port; 'ftp-proxy': ftp proxy port; 'http': HTTP Port; 'https': HTTPS port; 'mlb': Message based load balancing; 'mms': Microsoft Multimedia Service Port; 'mysql': mssql port; 'mssql': mssql; 'radius': RADIUS Port; 'rtsp': Real Time Streaming Protocol Port; 'sip': Session initiation protocol over UDP; 'sip-tcp': Session initiation protocol over TCP; 'sips': Session initiation protocol over TLS; 'smpp-tcp': SMPP service over TCP; 'spdy': spdy port; 'spdys': spdys port; 'smtp': SMTP Port; 'ssl-proxy': Generic SSL proxy; 'tcp-proxy': Generic TCP proxy; 'tftp': TFTP Port; ", "format": "enum", "type": "string", "oid": "1002", "optional": false}
    :param port_number: {"description": "Port", "format": "number", "optional": false, "oid": "1001", "maximum": 65534, "minimum": 0, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/virtual-server/{name}/port/{port_number}+{protocol}/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "port_number","protocol"]

        self.b_key = "port"
        self.a10_url="/axapi/v3/slb/virtual-server/{name}/port/{port_number}+{protocol}/stats"
        self.DeviceProxy = ""
        self.stats = {}
        self.protocol = ""
        self.port_number = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


