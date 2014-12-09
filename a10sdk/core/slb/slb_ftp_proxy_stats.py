from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ser_connecting_err: {"description": "Serv CTNG state error", "format": "counter", "type": "number", "oid": "42", "optional": true, "size": "8"}
    :param svrsel_fail: {"description": "Server selection failure", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "8"}
    :param curr: {"description": "Current proxy conns", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "8"}
    :param unsupported_prot_value: {"description": "Unsupported PROT", "format": "counter", "type": "number", "oid": "32", "optional": true, "size": "8"}
    :param cc: {"description": "clear ctrl port packet", "format": "counter", "type": "number", "oid": "8", "optional": true, "size": "8"}
    :param request: {"description": "Total FTP Request", "format": "counter", "type": "number", "oid": "48", "optional": true, "size": "8"}
    :param server_response_err: {"description": "Serv RESP state error", "format": "counter", "type": "number", "oid": "43", "optional": true, "size": "8"}
    :param unsupported_pbsz_value: {"description": "Unsupported PBSZ", "format": "counter", "type": "number", "oid": "31", "optional": true, "size": "8"}
    :param cant_find_pasv: {"description": "cant find pasv", "format": "counter", "type": "number", "oid": "20", "optional": true, "size": "8"}
    :param pbsz: {"description": "pbsz cmd", "format": "counter", "type": "number", "oid": "15", "optional": true, "size": "8"}
    :param pasv: {"description": "pasv cmd", "format": "counter", "type": "number", "oid": "16", "optional": true, "size": "8"}
    :param smp_v4_fail: {"description": "Serv Sel SMPv4 fail", "format": "counter", "type": "number", "oid": "39", "optional": true, "size": "8"}
    :param no_route: {"description": "no route failure", "format": "counter", "type": "number", "oid": "5", "optional": true, "size": "8"}
    :param total: {"description": "Total proxy conns", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "8"}
    :param feat: {"description": "feat packet", "format": "counter", "type": "number", "oid": "7", "optional": true, "size": "8"}
    :param port: {"description": "port cmd", "format": "counter", "type": "number", "oid": "17", "optional": true, "size": "8"}
    :param data_total: {"description": "Total Data Proxy", "format": "counter", "type": "number", "oid": "28", "optional": true, "size": "8"}
    :param auth_tls: {"description": "auth tls cmd", "format": "counter", "type": "number", "oid": "13", "optional": true, "size": "8"}
    :param request_dont_care: {"description": "other cmd", "format": "counter", "type": "number", "oid": "18", "optional": true, "size": "8"}
    :param cl_est_err: {"description": "Client EST state erro", "format": "counter", "type": "number", "oid": "41", "optional": true, "size": "8"}
    :param cl_request_err: {"description": "Client RQ state error", "format": "counter", "type": "number", "oid": "44", "optional": true, "size": "8"}
    :param prot: {"description": "prot cmd", "format": "counter", "type": "number", "oid": "14", "optional": true, "size": "8"}
    :param insert_tuple_fail: {"description": "Serv Sel insert tuple fail", "format": "counter", "type": "number", "oid": "40", "optional": true, "size": "8"}
    :param line_mem_freed: {"description": "request line freed", "format": "counter", "type": "number", "oid": "11", "optional": true, "size": "8"}
    :param invalid_start_line: {"description": "invalid start line", "format": "counter", "type": "number", "oid": "12", "optional": true, "size": "8"}
    :param epsv: {"description": "epsv command", "format": "counter", "type": "number", "oid": "25", "optional": true, "size": "8"}
    :param rsv_persist_conn_fail: {"description": "Serv Sel Persist fail", "format": "counter", "type": "number", "oid": "37", "optional": true, "size": "8"}
    :param control_to_ssl: {"description": "Control chn ssl", "format": "counter", "type": "number", "oid": "35", "optional": true, "size": "8"}
    :param cant_find_epsv: {"description": "cant find epsv", "format": "counter", "type": "number", "oid": "26", "optional": true, "size": "8"}
    :param smp_v6_fail: {"description": "Serv Sel SMPv6 fail", "format": "counter", "type": "number", "oid": "38", "optional": true, "size": "8"}
    :param data_curr: {"description": "Current Data Proxy", "format": "counter", "type": "number", "oid": "27", "optional": true, "size": "8"}
    :param snat_fail: {"description": "source nat failure", "format": "counter", "type": "number", "oid": "6", "optional": true, "size": "8"}
    :param data_ssl: {"description": "data ssl force", "format": "counter", "type": "number", "oid": "9", "optional": true, "size": "8"}
    :param data_serv_connecting_err: {"description": "Data Serv CTNG error", "format": "counter", "type": "number", "oid": "46", "optional": true, "size": "8"}
    :param auth_unsupported: {"description": "Unsupported auth", "format": "counter", "type": "number", "oid": "29", "optional": true, "size": "8"}
    :param pasv_addr_ne_server: {"description": "psv addr not equal to svr", "format": "counter", "type": "number", "oid": "21", "optional": true, "size": "8"}
    :param smp_create_fail: {"description": "smp create fail", "format": "counter", "type": "number", "oid": "22", "optional": true, "size": "8"}
    :param control_to_clear: {"description": "Control chn clear txt", "format": "counter", "type": "number", "oid": "34", "optional": true, "size": "8"}
    :param line_too_long: {"description": "line too long", "format": "counter", "type": "number", "oid": "10", "optional": true, "size": "8"}
    :param data_serv_connected_err: {"description": "Data Serv CTED error", "format": "counter", "type": "number", "oid": "47", "optional": true, "size": "8"}
    :param client_auth_tls: {"description": "client auth tls", "format": "counter", "type": "number", "oid": "19", "optional": true, "size": "8"}
    :param adat: {"description": "adat cmd", "format": "counter", "type": "number", "oid": "30", "optional": true, "size": "8"}
    :param bad_sequence: {"description": "Bad Sequence", "format": "counter", "type": "number", "oid": "36", "optional": true, "size": "8"}
    :param unsupported_command: {"description": "Unsupported cmd", "format": "counter", "type": "number", "oid": "33", "optional": true, "size": "8"}
    :param data_send_fail: {"description": "data send fail", "format": "counter", "type": "number", "oid": "24", "optional": true, "size": "8"}
    :param data_conn_start_err: {"description": "Data Start state error", "format": "counter", "type": "number", "oid": "45", "optional": true, "size": "8"}
    :param data_server_conn_fail: {"description": "data svr conn fail", "format": "counter", "type": "number", "oid": "23", "optional": true, "size": "8"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.ser_connecting_err = ""
        self.svrsel_fail = ""
        self.curr = ""
        self.unsupported_prot_value = ""
        self.cc = ""
        self.request = ""
        self.server_response_err = ""
        self.unsupported_pbsz_value = ""
        self.cant_find_pasv = ""
        self.pbsz = ""
        self.pasv = ""
        self.smp_v4_fail = ""
        self.no_route = ""
        self.total = ""
        self.feat = ""
        self.port = ""
        self.data_total = ""
        self.auth_tls = ""
        self.request_dont_care = ""
        self.cl_est_err = ""
        self.cl_request_err = ""
        self.prot = ""
        self.insert_tuple_fail = ""
        self.line_mem_freed = ""
        self.invalid_start_line = ""
        self.epsv = ""
        self.rsv_persist_conn_fail = ""
        self.control_to_ssl = ""
        self.cant_find_epsv = ""
        self.smp_v6_fail = ""
        self.data_curr = ""
        self.snat_fail = ""
        self.data_ssl = ""
        self.data_serv_connecting_err = ""
        self.auth_unsupported = ""
        self.pasv_addr_ne_server = ""
        self.smp_create_fail = ""
        self.control_to_clear = ""
        self.line_too_long = ""
        self.data_serv_connected_err = ""
        self.client_auth_tls = ""
        self.adat = ""
        self.bad_sequence = ""
        self.unsupported_command = ""
        self.data_send_fail = ""
        self.data_conn_start_err = ""
        self.data_server_conn_fail = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class FtpProxy(A10BaseClass):
    
    """Class Description::
    Statistics for the object ftp-proxy.

    Class ftp-proxy supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/ftp-proxy/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "ftp-proxy"
        self.a10_url="/axapi/v3/slb/ftp-proxy/stats"
        self.DeviceProxy = ""
        self.stats = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


