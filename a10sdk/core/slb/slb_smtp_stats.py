from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param recv_client_command_RCPT: {"description": "Recv client RCPT", "format": "counter", "type": "number", "oid": "23", "optional": true, "size": "8"}
    :param line_across_packet: {"description": "Line across packets", "format": "counter", "type": "number", "oid": "55", "optional": true, "size": "8"}
    :param forward_req_fail: {"description": "Forward request failure", "format": "counter", "type": "number", "oid": "11", "optional": true, "size": "8"}
    :param server_select_fail: {"description": "Server selection failure", "format": "counter", "type": "number", "oid": "10", "optional": true, "size": "8"}
    :param total_proxy: {"description": "Total proxy conns", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "8"}
    :param recv_server_unknow_reply_code: {"description": "Recv server unknown-code", "format": "counter", "type": "number", "oid": "34", "optional": true, "size": "8"}
    :param too_many_headers: {"description": "Too many headers", "format": "counter", "type": "number", "oid": "53", "optional": true, "size": "8"}
    :param recv_client_command_QUIT: {"description": "Recv client QUIT", "format": "counter", "type": "number", "oid": "30", "optional": true, "size": "8"}
    :param recv_client_command_NOOP: {"description": "Recv client NOOP", "format": "counter", "type": "number", "oid": "29", "optional": true, "size": "8"}
    :param new_server_conn: {"description": "Server connection made", "format": "counter", "type": "number", "oid": "17", "optional": true, "size": "8"}
    :param req_retran: {"description": "Request retransmit", "format": "counter", "type": "number", "oid": "13", "optional": true, "size": "8"}
    :param recv_client_command_MAIL: {"description": "Recv client MAIL", "format": "counter", "type": "number", "oid": "22", "optional": true, "size": "8"}
    :param client_domain_switch_ok: {"description": "Client domain sw (succ)", "format": "counter", "type": "number", "oid": "48", "optional": true, "size": "8"}
    :param recv_client_command_VRFY: {"description": "Recv client VRFY", "format": "counter", "type": "number", "oid": "26", "optional": true, "size": "8"}
    :param server_prem_close: {"description": "Server premature close", "format": "counter", "type": "number", "oid": "16", "optional": true, "size": "8"}
    :param Aflex_lb_reselect_ok: {"description": "aFleX lb reselect (succ)", "format": "counter", "type": "number", "oid": "65", "optional": true, "size": "8"}
    :param parse_resonse_line_fail: {"description": "Parse response line fail", "format": "counter", "type": "number", "oid": "63", "optional": true, "size": "8"}
    :param line_table_extend_fail: {"description": "Table extend fail", "format": "counter", "type": "number", "oid": "59", "optional": true, "size": "8"}
    :param send_client_close_connection: {"description": "Sent client close-conn", "format": "counter", "type": "number", "oid": "37", "optional": true, "size": "8"}
    :param forward_req_data_fail: {"description": "Forward REQ data failure", "format": "counter", "type": "number", "oid": "12", "optional": true, "size": "8"}
    :param recv_client_command_RSET: {"description": "Recv client RSET", "format": "counter", "type": "number", "oid": "25", "optional": true, "size": "8"}
    :param no_proxy: {"description": "No proxy error", "format": "counter", "type": "number", "oid": "5", "optional": true, "size": "8"}
    :param client_reset: {"description": "Client reset", "format": "counter", "type": "number", "oid": "6", "optional": true, "size": "8"}
    :param recv_client_command_DATA: {"description": "Recv client DATA", "format": "counter", "type": "number", "oid": "24", "optional": true, "size": "8"}
    :param recv_client_command_HELP: {"description": "Recv client HELP", "format": "counter", "type": "number", "oid": "28", "optional": true, "size": "8"}
    :param send_client_start_TLS_first: {"description": "Sent client STARTTLS-1st", "format": "counter", "type": "number", "oid": "39", "optional": true, "size": "8"}
    :param recv_client_command_HELO: {"description": "Recv client HELO", "format": "counter", "type": "number", "oid": "21", "optional": true, "size": "8"}
    :param recv_client_command_STARTTLS: {"description": "Recv client STARTTLS", "format": "counter", "type": "number", "oid": "31", "optional": true, "size": "8"}
    :param recv_client_command_others: {"description": "Recv client other cmds", "format": "counter", "type": "number", "oid": "32", "optional": true, "size": "8"}
    :param recv_client_command_EXPN: {"description": "Recv client EXPN", "format": "counter", "type": "number", "oid": "27", "optional": true, "size": "8"}
    :param LB_switch: {"description": "LB switching", "format": "counter", "type": "number", "oid": "49", "optional": true, "size": "8"}
    :param no_tuple: {"description": "No tuple error", "format": "counter", "type": "number", "oid": "8", "optional": true, "size": "8"}
    :param L4_switch: {"description": "L4 switching", "format": "counter", "type": "number", "oid": "44", "optional": true, "size": "8"}
    :param send_client_no_command: {"description": "Sent client no-such-cmd", "format": "counter", "type": "number", "oid": "41", "optional": true, "size": "8"}
    :param Aflex_switch_ok: {"description": "aFleX switching (succ)", "format": "counter", "type": "number", "oid": "46", "optional": true, "size": "8"}
    :param request_success: {"description": "SMTP requests (success)", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "8"}
    :param tcp_out_reset: {"description": "TCP out reset", "format": "counter", "type": "number", "oid": "19", "optional": true, "size": "8"}
    :param line_table_extend: {"description": "Table extend", "format": "counter", "type": "number", "oid": "58", "optional": true, "size": "8"}
    :param send_server_cmd_reset: {"description": "Sent server RSET", "format": "counter", "type": "number", "oid": "42", "optional": true, "size": "8"}
    :param line_extend_fail: {"description": "Line extend fail", "format": "counter", "type": "number", "oid": "57", "optional": true, "size": "8"}
    :param server_reselect: {"description": "Server reselection", "format": "counter", "type": "number", "oid": "15", "optional": true, "size": "8"}
    :param Aflex_lb_reselect: {"description": "aFleX lb reselect", "format": "counter", "type": "number", "oid": "64", "optional": true, "size": "8"}
    :param curr_proxy: {"description": "Current proxy conns", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}
    :param send_client_service_ready: {"description": "Sent client serv-rdy", "format": "counter", "type": "number", "oid": "35", "optional": true, "size": "8"}
    :param send_client_go_ahead: {"description": "Sent client go-ahead", "format": "counter", "type": "number", "oid": "38", "optional": true, "size": "8"}
    :param req_ofo: {"description": "Request pkt out-of-order", "format": "counter", "type": "number", "oid": "14", "optional": true, "size": "8"}
    :param client_domain_switch: {"description": "Client domain switching", "format": "counter", "type": "number", "oid": "47", "optional": true, "size": "8"}
    :param server_reset: {"description": "Server reset", "format": "counter", "type": "number", "oid": "7", "optional": true, "size": "8"}
    :param snat_fail: {"description": "Source NAT failure", "format": "counter", "type": "number", "oid": "18", "optional": true, "size": "8"}
    :param send_client_TLS_not_available: {"description": "Sent client TLS-not-aval", "format": "counter", "type": "number", "oid": "40", "optional": true, "size": "8"}
    :param parse_request_line_fail: {"description": "Parse request line fail", "format": "counter", "type": "number", "oid": "60", "optional": true, "size": "8"}
    :param remove_resonse_line_fail: {"description": "Del response line fail", "format": "counter", "type": "number", "oid": "62", "optional": true, "size": "8"}
    :param send_client_service_not_ready: {"description": "Sent client serv-not-rdy", "format": "counter", "type": "number", "oid": "36", "optional": true, "size": "8"}
    :param get_all_headers_fail: {"description": "Get all headers fail", "format": "counter", "type": "number", "oid": "52", "optional": true, "size": "8"}
    :param parse_req_fail: {"description": "Parse request failure", "format": "counter", "type": "number", "oid": "9", "optional": true, "size": "8"}
    :param LB_switch_ok: {"description": "LB switching (succ)", "format": "counter", "type": "number", "oid": "50", "optional": true, "size": "8"}
    :param Aflex_switch: {"description": "aFleX switching", "format": "counter", "type": "number", "oid": "45", "optional": true, "size": "8"}
    :param line_too_long: {"description": "Line too long", "format": "counter", "type": "number", "oid": "54", "optional": true, "size": "8"}
    :param insert_resonse_line_fail: {"description": "Ins response line fail", "format": "counter", "type": "number", "oid": "61", "optional": true, "size": "8"}
    :param request: {"description": "SMTP requests", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "8"}
    :param line_extend: {"description": "Line extend", "format": "counter", "type": "number", "oid": "56", "optional": true, "size": "8"}
    :param read_request_line_fail: {"description": "Read request line fail", "format": "counter", "type": "number", "oid": "51", "optional": true, "size": "8"}
    :param recv_client_command_EHLO: {"description": "Recv client EHLO", "format": "counter", "type": "number", "oid": "20", "optional": true, "size": "8"}
    :param recv_server_service_not_ready: {"description": "Recv server serv-not-rdy", "format": "counter", "type": "number", "oid": "33", "optional": true, "size": "8"}
    :param TLS_established: {"description": "SSL session established", "format": "counter", "type": "number", "oid": "43", "optional": true, "size": "8"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.recv_client_command_RCPT = ""
        self.line_across_packet = ""
        self.forward_req_fail = ""
        self.server_select_fail = ""
        self.total_proxy = ""
        self.recv_server_unknow_reply_code = ""
        self.too_many_headers = ""
        self.recv_client_command_QUIT = ""
        self.recv_client_command_NOOP = ""
        self.new_server_conn = ""
        self.req_retran = ""
        self.recv_client_command_MAIL = ""
        self.client_domain_switch_ok = ""
        self.recv_client_command_VRFY = ""
        self.server_prem_close = ""
        self.Aflex_lb_reselect_ok = ""
        self.parse_resonse_line_fail = ""
        self.line_table_extend_fail = ""
        self.send_client_close_connection = ""
        self.forward_req_data_fail = ""
        self.recv_client_command_RSET = ""
        self.no_proxy = ""
        self.client_reset = ""
        self.recv_client_command_DATA = ""
        self.recv_client_command_HELP = ""
        self.send_client_start_TLS_first = ""
        self.recv_client_command_HELO = ""
        self.recv_client_command_STARTTLS = ""
        self.recv_client_command_others = ""
        self.recv_client_command_EXPN = ""
        self.LB_switch = ""
        self.no_tuple = ""
        self.L4_switch = ""
        self.send_client_no_command = ""
        self.Aflex_switch_ok = ""
        self.request_success = ""
        self.tcp_out_reset = ""
        self.line_table_extend = ""
        self.send_server_cmd_reset = ""
        self.line_extend_fail = ""
        self.server_reselect = ""
        self.Aflex_lb_reselect = ""
        self.curr_proxy = ""
        self.send_client_service_ready = ""
        self.send_client_go_ahead = ""
        self.req_ofo = ""
        self.client_domain_switch = ""
        self.server_reset = ""
        self.snat_fail = ""
        self.send_client_TLS_not_available = ""
        self.parse_request_line_fail = ""
        self.remove_resonse_line_fail = ""
        self.send_client_service_not_ready = ""
        self.get_all_headers_fail = ""
        self.parse_req_fail = ""
        self.LB_switch_ok = ""
        self.Aflex_switch = ""
        self.line_too_long = ""
        self.insert_resonse_line_fail = ""
        self.request = ""
        self.line_extend = ""
        self.read_request_line_fail = ""
        self.recv_client_command_EHLO = ""
        self.recv_server_service_not_ready = ""
        self.TLS_established = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Smtp(A10BaseClass):
    
    """Class Description::
    Statistics for the object smtp.

    Class smtp supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/smtp/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "smtp"
        self.a10_url="/axapi/v3/slb/smtp/stats"
        self.DeviceProxy = ""
        self.stats = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


