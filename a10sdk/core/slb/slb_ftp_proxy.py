from a10sdk.common.A10BaseClass import A10BaseClass


class SamplingEnable(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param counters1: {"enum": ["all", "num", "curr", "total", "svrsel_fail", "no_route", "snat_fail", "feat", "cc", "data_ssl", "line_too_long", "line_mem_freed", "invalid_start_line", "auth_tls", "prot", "pbsz", "pasv", "port", "request_dont_care", "client_auth_tls", "cant_find_pasv", "pasv_addr_ne_server", "smp_create_fail", "data_server_conn_fail", "data_send_fail", "epsv", "cant_find_epsv", "data_curr", "data_total", "auth_unsupported", "adat", "unsupported_pbsz_value", "unsupported_prot_value", "unsupported_command", "control_to_clear", "control_to_ssl", "bad_sequence", "rsv_persist_conn_fail", "smp_v6_fail", "smp_v4_fail", "insert_tuple_fail", "cl_est_err", "ser_connecting_err", "server_response_err", "cl_request_err", "data_conn_start_err", "data_serv_connecting_err", "data_serv_connected_err", "request"], "type": "string", "description": "'all': all; 'num': Num; 'curr': Current proxy conns; 'total': Total proxy conns; 'svrsel_fail': Server selection failure; 'no_route': no route failure; 'snat_fail': source nat failure; 'feat': feat packet; 'cc': clear ctrl port packet; 'data_ssl': data ssl force; 'line_too_long': line too long; 'line_mem_freed': request line freed; 'invalid_start_line': invalid start line; 'auth_tls': auth tls cmd; 'prot': prot cmd; 'pbsz': pbsz cmd; 'pasv': pasv cmd; 'port': port cmd; 'request_dont_care': other cmd; 'client_auth_tls': client auth tls; 'cant_find_pasv': cant find pasv; 'pasv_addr_ne_server': psv addr not equal to svr; 'smp_create_fail': smp create fail; 'data_server_conn_fail': data svr conn fail; 'data_send_fail': data send fail; 'epsv': epsv command; 'cant_find_epsv': cant find epsv; 'data_curr': Current Data Proxy; 'data_total': Total Data Proxy; 'auth_unsupported': Unsupported auth; 'adat': adat cmd; 'unsupported_pbsz_value': Unsupported PBSZ; 'unsupported_prot_value': Unsupported PROT; 'unsupported_command': Unsupported cmd; 'control_to_clear': Control chn clear txt; 'control_to_ssl': Control chn ssl; 'bad_sequence': Bad Sequence; 'rsv_persist_conn_fail': Serv Sel Persist fail; 'smp_v6_fail': Serv Sel SMPv6 fail; 'smp_v4_fail': Serv Sel SMPv4 fail; 'insert_tuple_fail': Serv Sel insert tuple fail; 'cl_est_err': Client EST state erro; 'ser_connecting_err': Serv CTNG state error; 'server_response_err': Serv RESP state error; 'cl_request_err': Client RQ state error; 'data_conn_start_err': Data Start state error; 'data_serv_connecting_err': Data Serv CTNG error; 'data_serv_connected_err': Data Serv CTED error; 'request': Total FTP Request; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "sampling-enable"
        self.DeviceProxy = ""
        self.counters1 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class FtpProxy(A10BaseClass):
    
    """    :param sampling_enable: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "num", "curr", "total", "svrsel_fail", "no_route", "snat_fail", "feat", "cc", "data_ssl", "line_too_long", "line_mem_freed", "invalid_start_line", "auth_tls", "prot", "pbsz", "pasv", "port", "request_dont_care", "client_auth_tls", "cant_find_pasv", "pasv_addr_ne_server", "smp_create_fail", "data_server_conn_fail", "data_send_fail", "epsv", "cant_find_epsv", "data_curr", "data_total", "auth_unsupported", "adat", "unsupported_pbsz_value", "unsupported_prot_value", "unsupported_command", "control_to_clear", "control_to_ssl", "bad_sequence", "rsv_persist_conn_fail", "smp_v6_fail", "smp_v4_fail", "insert_tuple_fail", "cl_est_err", "ser_connecting_err", "server_response_err", "cl_request_err", "data_conn_start_err", "data_serv_connecting_err", "data_serv_connected_err", "request"], "type": "string", "description": "'all': all; 'num': Num; 'curr': Current proxy conns; 'total': Total proxy conns; 'svrsel_fail': Server selection failure; 'no_route': no route failure; 'snat_fail': source nat failure; 'feat': feat packet; 'cc': clear ctrl port packet; 'data_ssl': data ssl force; 'line_too_long': line too long; 'line_mem_freed': request line freed; 'invalid_start_line': invalid start line; 'auth_tls': auth tls cmd; 'prot': prot cmd; 'pbsz': pbsz cmd; 'pasv': pasv cmd; 'port': port cmd; 'request_dont_care': other cmd; 'client_auth_tls': client auth tls; 'cant_find_pasv': cant find pasv; 'pasv_addr_ne_server': psv addr not equal to svr; 'smp_create_fail': smp create fail; 'data_server_conn_fail': data svr conn fail; 'data_send_fail': data send fail; 'epsv': epsv command; 'cant_find_epsv': cant find epsv; 'data_curr': Current Data Proxy; 'data_total': Total Data Proxy; 'auth_unsupported': Unsupported auth; 'adat': adat cmd; 'unsupported_pbsz_value': Unsupported PBSZ; 'unsupported_prot_value': Unsupported PROT; 'unsupported_command': Unsupported cmd; 'control_to_clear': Control chn clear txt; 'control_to_ssl': Control chn ssl; 'bad_sequence': Bad Sequence; 'rsv_persist_conn_fail': Serv Sel Persist fail; 'smp_v6_fail': Serv Sel SMPv6 fail; 'smp_v4_fail': Serv Sel SMPv4 fail; 'insert_tuple_fail': Serv Sel insert tuple fail; 'cl_est_err': Client EST state erro; 'ser_connecting_err': Serv CTNG state error; 'server_response_err': Serv RESP state error; 'cl_request_err': Client RQ state error; 'data_conn_start_err': Data Start state error; 'data_serv_connecting_err': Data Serv CTNG error; 'data_serv_connected_err': Data Serv CTED error; 'request': Total FTP Request; ", "format": "enum"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Show FTP Proxy global Statistics.

    Class ftp-proxy supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/ftp-proxy`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "ftp-proxy"
        self.a10_url="/axapi/v3/slb/ftp-proxy"
        self.DeviceProxy = ""
        self.sampling_enable = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


