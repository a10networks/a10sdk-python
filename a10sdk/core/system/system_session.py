from a10sdk.common.A10BaseClass import A10BaseClass


class SamplingEnable(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param counters1: {"enum": ["all", "total_l4_conn", "conn_counter", "conn_freed_counter", "total_l4_packet_count", "total_l7_packet_count", "total_l4_conn_proxy", "total_l7_conn", "total_tcp_conn", "curr_free_conn", "tcp_est_counter", "tcp_half_open_counter", "tcp_half_close_counter", "udp_counter", "ip_counter", "other_counter", "reverse_nat_tcp_ounter", "reverse_nat_udp_ounter", "tcp_syn_half_open_counter", "conn_smp_alloc_counter", "conn_smp_free_counter", "conn_smp_aged_counter", "ssl_count_curr", "ssl_count_total", "server_ssl_count_curr", "server_ssl_count_total", "client_ssl_reuse_total", "server_ssl_reuse_total", "ssl_failed_total", "ssl_failed_ca_verification", "ssl_server_cert_error", "ssl_client_cert_auth_fail", "total_ip_nat_donn", "total_l2l3_conn", "client_ssl_ctx_malloc_failure", "conn_type_0_available", "conn_type_1_available", "conn_type_2_available", "conn_type_3_available", "conn_type_4_available", "conn_smp_type_0_available", "conn_smp_type_1_available", "conn_smp_type_2_available", "conn_smp_type_3_available", "conn_smp_type_4_available"], "type": "string", "description": "'all': all; 'total_l4_conn': Total L4 Count; 'conn_counter': Conn Count; 'conn_freed_counter': Conn Freed; 'total_l4_packet_count': Total L4 Packet Count; 'total_l7_packet_count': Total L7 Packet Count; 'total_l4_conn_proxy': Total L4 Conn Proxy Count; 'total_l7_conn': Total L7 Conn; 'total_tcp_conn': Total TCP Conn; 'curr_free_conn': Curr Free Conn; 'tcp_est_counter': TCP Established; 'tcp_half_open_counter': TCP Half Open; 'tcp_half_close_counter': TCP Half Closed; 'udp_counter': UDP Count; 'ip_counter': IP Count; 'other_counter': Non TCP/UDP IP sessions; 'reverse_nat_tcp_ounter': Reverse NAT TCP; 'reverse_nat_udp_ounter': Reverse NAT UDP; 'tcp_syn_half_open_counter': TCP SYN Half Open; 'conn_smp_alloc_counter': Conn SMP Alloc; 'conn_smp_free_counter': Conn SMP Free; 'conn_smp_aged_counter': Conn SMP Aged; 'ssl_count_curr': Curr SSL Count; 'ssl_count_total': Total SSL Count; 'server_ssl_count_curr': Current SSL Server Count; 'server_ssl_count_total': Total SSL Server Count; 'client_ssl_reuse_total': Total SSL Client Reuse; 'server_ssl_reuse_total': Total SSL Server Reuse; 'ssl_failed_total': Total SSL Failures; 'ssl_failed_ca_verification': SSL Cert Auth Verification Errors; 'ssl_server_cert_error': SSL Server Cert Errors; 'ssl_client_cert_auth_fail': SSL Client Cert Auth Failures; 'total_ip_nat_donn': Total IP Nat Conn; 'total_l2l3_conn': Totl L2/L3 Connections; 'client_ssl_ctx_malloc_failure': Client SSL Ctx malloc Failures; 'conn_type_0_available': Conn Type 0 Available; 'conn_type_1_available': Conn Type 1 Available; 'conn_type_2_available': Conn Type 2 Available; 'conn_type_3_available': Conn Type 3 Available; 'conn_type_4_available': Conn Type 4 Available; 'conn_smp_type_0_available': Conn SMP Type 0 Available; 'conn_smp_type_1_available': Conn SMP Type 1 Available; 'conn_smp_type_2_available': Conn SMP Type 2 Available; 'conn_smp_type_3_available': Conn SMP Type 3 Available; 'conn_smp_type_4_available': Conn SMP Type 4 Available; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "sampling-enable"
        self.DeviceProxy = ""
        self.counters1 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Session(A10BaseClass):
    
    """    :param sampling_enable: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "total_l4_conn", "conn_counter", "conn_freed_counter", "total_l4_packet_count", "total_l7_packet_count", "total_l4_conn_proxy", "total_l7_conn", "total_tcp_conn", "curr_free_conn", "tcp_est_counter", "tcp_half_open_counter", "tcp_half_close_counter", "udp_counter", "ip_counter", "other_counter", "reverse_nat_tcp_ounter", "reverse_nat_udp_ounter", "tcp_syn_half_open_counter", "conn_smp_alloc_counter", "conn_smp_free_counter", "conn_smp_aged_counter", "ssl_count_curr", "ssl_count_total", "server_ssl_count_curr", "server_ssl_count_total", "client_ssl_reuse_total", "server_ssl_reuse_total", "ssl_failed_total", "ssl_failed_ca_verification", "ssl_server_cert_error", "ssl_client_cert_auth_fail", "total_ip_nat_donn", "total_l2l3_conn", "client_ssl_ctx_malloc_failure", "conn_type_0_available", "conn_type_1_available", "conn_type_2_available", "conn_type_3_available", "conn_type_4_available", "conn_smp_type_0_available", "conn_smp_type_1_available", "conn_smp_type_2_available", "conn_smp_type_3_available", "conn_smp_type_4_available"], "type": "string", "description": "'all': all; 'total_l4_conn': Total L4 Count; 'conn_counter': Conn Count; 'conn_freed_counter': Conn Freed; 'total_l4_packet_count': Total L4 Packet Count; 'total_l7_packet_count': Total L7 Packet Count; 'total_l4_conn_proxy': Total L4 Conn Proxy Count; 'total_l7_conn': Total L7 Conn; 'total_tcp_conn': Total TCP Conn; 'curr_free_conn': Curr Free Conn; 'tcp_est_counter': TCP Established; 'tcp_half_open_counter': TCP Half Open; 'tcp_half_close_counter': TCP Half Closed; 'udp_counter': UDP Count; 'ip_counter': IP Count; 'other_counter': Non TCP/UDP IP sessions; 'reverse_nat_tcp_ounter': Reverse NAT TCP; 'reverse_nat_udp_ounter': Reverse NAT UDP; 'tcp_syn_half_open_counter': TCP SYN Half Open; 'conn_smp_alloc_counter': Conn SMP Alloc; 'conn_smp_free_counter': Conn SMP Free; 'conn_smp_aged_counter': Conn SMP Aged; 'ssl_count_curr': Curr SSL Count; 'ssl_count_total': Total SSL Count; 'server_ssl_count_curr': Current SSL Server Count; 'server_ssl_count_total': Total SSL Server Count; 'client_ssl_reuse_total': Total SSL Client Reuse; 'server_ssl_reuse_total': Total SSL Server Reuse; 'ssl_failed_total': Total SSL Failures; 'ssl_failed_ca_verification': SSL Cert Auth Verification Errors; 'ssl_server_cert_error': SSL Server Cert Errors; 'ssl_client_cert_auth_fail': SSL Client Cert Auth Failures; 'total_ip_nat_donn': Total IP Nat Conn; 'total_l2l3_conn': Totl L2/L3 Connections; 'client_ssl_ctx_malloc_failure': Client SSL Ctx malloc Failures; 'conn_type_0_available': Conn Type 0 Available; 'conn_type_1_available': Conn Type 1 Available; 'conn_type_2_available': Conn Type 2 Available; 'conn_type_3_available': Conn Type 3 Available; 'conn_type_4_available': Conn Type 4 Available; 'conn_smp_type_0_available': Conn SMP Type 0 Available; 'conn_smp_type_1_available': Conn SMP Type 1 Available; 'conn_smp_type_2_available': Conn SMP Type 2 Available; 'conn_smp_type_3_available': Conn SMP Type 3 Available; 'conn_smp_type_4_available': Conn SMP Type 4 Available; ", "format": "enum"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Session Entries.

    Class session supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/system/session`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "session"
        self.a10_url="/axapi/v3/system/session"
        self.DeviceProxy = ""
        self.sampling_enable = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


