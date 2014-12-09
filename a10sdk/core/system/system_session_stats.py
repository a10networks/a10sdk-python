from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ssl_failed_ca_verification: {"description": "SSL Cert Auth Verification Errors", "format": "counter", "type": "number", "oid": "29", "optional": true, "size": "8"}
    :param server_ssl_count_total: {"description": "Total SSL Server Count", "format": "counter", "type": "number", "oid": "25", "optional": true, "size": "8"}
    :param tcp_est_counter: {"description": "TCP Established", "format": "counter", "type": "number", "oid": "10", "optional": true, "size": "8"}
    :param conn_smp_type_1_available: {"description": "Conn SMP Type 1 Available", "format": "counter", "type": "number", "oid": "41", "optional": true, "size": "8"}
    :param total_l4_packet_count: {"description": "Total L4 Packet Count", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "8"}
    :param total_l7_conn: {"description": "Total L7 Conn", "format": "counter", "type": "number", "oid": "7", "optional": true, "size": "8"}
    :param conn_smp_aged_counter: {"description": "Conn SMP Aged", "format": "counter", "type": "number", "oid": "21", "optional": true, "size": "8"}
    :param reverse_nat_tcp_ounter: {"description": "Reverse NAT TCP", "format": "counter", "type": "number", "oid": "16", "optional": true, "size": "8"}
    :param conn_type_1_available: {"description": "Conn Type 1 Available", "format": "counter", "type": "number", "oid": "36", "optional": true, "size": "8"}
    :param ssl_server_cert_error: {"description": "SSL Server Cert Errors", "format": "counter", "type": "number", "oid": "30", "optional": true, "size": "8"}
    :param ip_counter: {"description": "IP Count", "format": "counter", "type": "number", "oid": "14", "optional": true, "size": "8"}
    :param total_l2l3_conn: {"description": "Totl L2/L3 Connections", "format": "counter", "type": "number", "oid": "33", "optional": true, "size": "8"}
    :param ssl_failed_total: {"description": "Total SSL Failures", "format": "counter", "type": "number", "oid": "28", "optional": true, "size": "8"}
    :param conn_type_3_available: {"description": "Conn Type 3 Available", "format": "counter", "type": "number", "oid": "38", "optional": true, "size": "8"}
    :param conn_type_4_available: {"description": "Conn Type 4 Available", "format": "counter", "type": "number", "oid": "39", "optional": true, "size": "8"}
    :param conn_type_2_available: {"description": "Conn Type 2 Available", "format": "counter", "type": "number", "oid": "37", "optional": true, "size": "8"}
    :param conn_smp_type_0_available: {"description": "Conn SMP Type 0 Available", "format": "counter", "type": "number", "oid": "40", "optional": true, "size": "8"}
    :param total_l7_packet_count: {"description": "Total L7 Packet Count", "format": "counter", "type": "number", "oid": "5", "optional": true, "size": "8"}
    :param total_tcp_conn: {"description": "Total TCP Conn", "format": "counter", "type": "number", "oid": "8", "optional": true, "size": "8"}
    :param tcp_half_open_counter: {"description": "TCP Half Open", "format": "counter", "type": "number", "oid": "11", "optional": true, "size": "8"}
    :param ssl_client_cert_auth_fail: {"description": "SSL Client Cert Auth Failures", "format": "counter", "type": "number", "oid": "31", "optional": true, "size": "8"}
    :param ssl_count_total: {"description": "Total SSL Count", "format": "counter", "type": "number", "oid": "23", "optional": true, "size": "8"}
    :param conn_freed_counter: {"description": "Conn Freed", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "8"}
    :param conn_type_0_available: {"description": "Conn Type 0 Available", "format": "counter", "type": "number", "oid": "35", "optional": true, "size": "8"}
    :param conn_smp_free_counter: {"description": "Conn SMP Free", "format": "counter", "type": "number", "oid": "20", "optional": true, "size": "8"}
    :param curr_free_conn: {"description": "Curr Free Conn", "format": "counter", "type": "number", "oid": "9", "optional": true, "size": "8"}
    :param client_ssl_reuse_total: {"description": "Total SSL Client Reuse", "format": "counter", "type": "number", "oid": "26", "optional": true, "size": "8"}
    :param udp_counter: {"description": "UDP Count", "format": "counter", "type": "number", "oid": "13", "optional": true, "size": "8"}
    :param conn_smp_type_2_available: {"description": "Conn SMP Type 2 Available", "format": "counter", "type": "number", "oid": "42", "optional": true, "size": "8"}
    :param reverse_nat_udp_ounter: {"description": "Reverse NAT UDP", "format": "counter", "type": "number", "oid": "17", "optional": true, "size": "8"}
    :param client_ssl_ctx_malloc_failure: {"description": "Client SSL Ctx malloc Failures", "format": "counter", "type": "number", "oid": "34", "optional": true, "size": "8"}
    :param tcp_syn_half_open_counter: {"description": "TCP SYN Half Open", "format": "counter", "type": "number", "oid": "18", "optional": true, "size": "8"}
    :param total_l4_conn_proxy: {"description": "Total L4 Conn Proxy Count", "format": "counter", "type": "number", "oid": "6", "optional": true, "size": "8"}
    :param conn_smp_type_3_available: {"description": "Conn SMP Type 3 Available", "format": "counter", "type": "number", "oid": "43", "optional": true, "size": "8"}
    :param conn_smp_alloc_counter: {"description": "Conn SMP Alloc", "format": "counter", "type": "number", "oid": "19", "optional": true, "size": "8"}
    :param conn_counter: {"description": "Conn Count", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "8"}
    :param other_counter: {"description": "Non TCP/UDP IP sessions", "format": "counter", "type": "number", "oid": "15", "optional": true, "size": "8"}
    :param server_ssl_count_curr: {"description": "Current SSL Server Count", "format": "counter", "type": "number", "oid": "24", "optional": true, "size": "8"}
    :param server_ssl_reuse_total: {"description": "Total SSL Server Reuse", "format": "counter", "type": "number", "oid": "27", "optional": true, "size": "8"}
    :param total_ip_nat_donn: {"description": "Total IP Nat Conn", "format": "counter", "type": "number", "oid": "32", "optional": true, "size": "8"}
    :param conn_smp_type_4_available: {"description": "Conn SMP Type 4 Available", "format": "counter", "type": "number", "oid": "44", "optional": true, "size": "8"}
    :param tcp_half_close_counter: {"description": "TCP Half Closed", "format": "counter", "type": "number", "oid": "12", "optional": true, "size": "8"}
    :param total_l4_conn: {"description": "Total L4 Count", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}
    :param ssl_count_curr: {"description": "Curr SSL Count", "format": "counter", "type": "number", "oid": "22", "optional": true, "size": "8"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.ssl_failed_ca_verification = ""
        self.server_ssl_count_total = ""
        self.tcp_est_counter = ""
        self.conn_smp_type_1_available = ""
        self.total_l4_packet_count = ""
        self.total_l7_conn = ""
        self.conn_smp_aged_counter = ""
        self.reverse_nat_tcp_ounter = ""
        self.conn_type_1_available = ""
        self.ssl_server_cert_error = ""
        self.ip_counter = ""
        self.total_l2l3_conn = ""
        self.ssl_failed_total = ""
        self.conn_type_3_available = ""
        self.conn_type_4_available = ""
        self.conn_type_2_available = ""
        self.conn_smp_type_0_available = ""
        self.total_l7_packet_count = ""
        self.total_tcp_conn = ""
        self.tcp_half_open_counter = ""
        self.ssl_client_cert_auth_fail = ""
        self.ssl_count_total = ""
        self.conn_freed_counter = ""
        self.conn_type_0_available = ""
        self.conn_smp_free_counter = ""
        self.curr_free_conn = ""
        self.client_ssl_reuse_total = ""
        self.udp_counter = ""
        self.conn_smp_type_2_available = ""
        self.reverse_nat_udp_ounter = ""
        self.client_ssl_ctx_malloc_failure = ""
        self.tcp_syn_half_open_counter = ""
        self.total_l4_conn_proxy = ""
        self.conn_smp_type_3_available = ""
        self.conn_smp_alloc_counter = ""
        self.conn_counter = ""
        self.other_counter = ""
        self.server_ssl_count_curr = ""
        self.server_ssl_reuse_total = ""
        self.total_ip_nat_donn = ""
        self.conn_smp_type_4_available = ""
        self.tcp_half_close_counter = ""
        self.total_l4_conn = ""
        self.ssl_count_curr = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Session(A10BaseClass):
    
    """Class Description::
    Statistics for the object session.

    Class session supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/system/session/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "session"
        self.a10_url="/axapi/v3/system/session/stats"
        self.DeviceProxy = ""
        self.stats = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


