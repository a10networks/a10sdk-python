from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param invalid_frame_size: {"description": "Invalid frame size", "format": "counter", "type": "number", "oid": "69", "optional": true, "size": "2"}
    :param data_cb_no_tuple: {"description": "Data callback no tuple", "format": "counter", "type": "number", "oid": "36", "optional": true, "size": "2"}
    :param compress_ctx_alloc_fail: {"description": "Compression context allocation fail", "format": "counter", "type": "number", "oid": "72", "optional": true, "size": "2"}
    :param stream_found: {"description": "Stream found", "format": "counter", "type": "number", "oid": "40", "optional": true, "size": "2"}
    :param total_proxy: {"description": "Total Proxy Conns", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "2"}
    :param curr_http_proxy: {"description": "Curr HTTP Proxy Conns", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "2"}
    :param total_v2_proxy: {"description": "Version 2 Streams", "format": "counter", "type": "number", "oid": "5", "optional": true, "size": "2"}
    :param syn_stream_exist_or_even: {"description": "Stream already exists", "format": "counter", "type": "number", "oid": "61", "optional": true, "size": "2"}
    :param close_stream_stream_not_found: {"description": "Close stream stream not found", "format": "counter", "type": "number", "oid": "42", "optional": true, "size": "2"}
    :param client_rst: {"optional": true, "size": "2", "type": "number", "oid": "10", "format": "counter"}
    :param est_cb_no_tuple: {"description": "Est callback no tuple", "format": "counter", "type": "number", "oid": "35", "optional": true, "size": "2"}
    :param stream_alloc_fail: {"description": "Stream alloc fail", "format": "counter", "type": "number", "oid": "47", "optional": true, "size": "2"}
    :param max_concurrent_stream_limit: {"description": "Max concurrent stream limit", "format": "counter", "type": "number", "oid": "46", "optional": true, "size": "2"}
    :param deflate_ctx: {"description": "Deflate context", "format": "counter", "type": "number", "oid": "16", "optional": true, "size": "2"}
    :param client_goaway: {"optional": true, "size": "2", "type": "number", "oid": "12", "format": "counter"}
    :param ping_sent: {"description": "PING sent", "format": "counter", "type": "number", "oid": "17", "optional": true, "size": "2"}
    :param server_goaway: {"description": "Server GOAWAY sent", "format": "counter", "type": "number", "oid": "13", "optional": true, "size": "2"}
    :param session_needs_requeue: {"description": "Session needs requeue", "format": "counter", "type": "number", "oid": "77", "optional": true, "size": "2"}
    :param syn_reply_alr_rcvd: {"description": "SYN reply already received", "format": "counter", "type": "number", "oid": "63", "optional": true, "size": "2"}
    :param total_http_proxy: {"description": "Total HTTP Proxy Conns", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "2"}
    :param close_stream_session_close: {"description": "Stream close session close", "format": "counter", "type": "number", "oid": "44", "optional": true, "size": "2"}
    :param decompress_fail: {"description": "Decompress fail", "format": "counter", "type": "number", "oid": "58", "optional": true, "size": "2"}
    :param ping_frame: {"description": "Ping frame received", "format": "counter", "type": "number", "oid": "30", "optional": true, "size": "2"}
    :param inflate_ctx: {"description": "Inflate context", "format": "counter", "type": "number", "oid": "15", "optional": true, "size": "2"}
    :param name_value_total_len_ex: {"description": "Name value total length exceeded", "format": "counter", "type": "number", "oid": "50", "optional": true, "size": "2"}
    :param http_err_stream_closed: {"description": "HTTP error stream already closed", "format": "counter", "type": "number", "oid": "81", "optional": true, "size": "2"}
    :param http_hdr_stream_close: {"description": "HTTP header stream already closed", "format": "counter", "type": "number", "oid": "82", "optional": true, "size": "2"}
    :param http_data_stream_close: {"description": "HTTP data stream already closed", "format": "counter", "type": "number", "oid": "83", "optional": true, "size": "2"}
    :param control_frame: {"description": "Control frame received", "format": "counter", "type": "number", "oid": "24", "optional": true, "size": "2"}
    :param session_close: {"description": "Session close", "format": "counter", "type": "number", "oid": "84", "optional": true, "size": "2"}
    :param name_value_connection: {"description": "Name value connection", "format": "counter", "type": "number", "oid": "53", "optional": true, "size": "2"}
    :param fin_stream_closed: {"description": "HTTP FIN stream already closed", "format": "counter", "type": "number", "oid": "79", "optional": true, "size": "2"}
    :param stream_close: {"description": "Stream close", "format": "counter", "type": "number", "oid": "21", "optional": true, "size": "2"}
    :param total_stream: {"description": "Total Streams", "format": "counter", "type": "number", "oid": "8", "optional": true, "size": "2"}
    :param window_no_stream: {"description": "Window update no stream found", "format": "counter", "type": "number", "oid": "65", "optional": true, "size": "2"}
    :param server_rst_close_stream: {"description": "Server RST close stream", "format": "counter", "type": "number", "oid": "39", "optional": true, "size": "2"}
    :param data_no_stream: {"description": "Data no stream found", "format": "counter", "type": "number", "oid": "32", "optional": true, "size": "2"}
    :param new_stream_session_del: {"description": "New Stream after Session delete", "format": "counter", "type": "number", "oid": "78", "optional": true, "size": "2"}
    :param ctx_alloc_fail: {"description": "Context alloc fail", "format": "counter", "type": "number", "oid": "37", "optional": true, "size": "2"}
    :param close_stream_session_not_found: {"description": "Close stream session not found", "format": "counter", "type": "number", "oid": "41", "optional": true, "size": "2"}
    :param invalid_version: {"description": "Invalid version", "format": "counter", "type": "number", "oid": "70", "optional": true, "size": "2"}
    :param server_fin: {"description": "Server FIN", "format": "counter", "type": "number", "oid": "20", "optional": true, "size": "2"}
    :param window_frame: {"description": "Window update frame received", "format": "counter", "type": "number", "oid": "29", "optional": true, "size": "2"}
    :param close_session_already_closed: {"description": "Closing closed session", "format": "counter", "type": "number", "oid": "45", "optional": true, "size": "2"}
    :param headers_frame: {"description": "Headers frame received", "format": "counter", "type": "number", "oid": "27", "optional": true, "size": "2"}
    :param server_rst: {"description": "Server RST sent", "format": "counter", "type": "number", "oid": "11", "optional": true, "size": "2"}
    :param header_compress_fail: {"description": "Header compress fail", "format": "counter", "type": "number", "oid": "73", "optional": true, "size": "2"}
    :param tcp_err: {"description": "TCP sock error", "format": "counter", "type": "number", "oid": "14", "optional": true, "size": "2"}
    :param curr_proxy: {"description": "Curr Proxy Conns", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "2"}
    :param name_value_zero_len: {"description": "Name value zero name length", "format": "counter", "type": "number", "oid": "51", "optional": true, "size": "2"}
    :param name_value_keepalive: {"description": "Name value keep alive", "format": "counter", "type": "number", "oid": "54", "optional": true, "size": "2"}
    :param http_close_stream_closed: {"description": "HTTP close stream already closed", "format": "counter", "type": "number", "oid": "80", "optional": true, "size": "2"}
    :param syn_frame: {"description": "SYN stream frame received", "format": "counter", "type": "number", "oid": "25", "optional": true, "size": "2"}
    :param data_frame: {"description": "Data frame received", "format": "counter", "type": "number", "oid": "31", "optional": true, "size": "2"}
    :param total_stream_succ: {"description": "Streams(succ)", "format": "counter", "type": "number", "oid": "9", "optional": true, "size": "2"}
    :param data_no_stream_goaway_close: {"description": "Data no stream and no goaway and close session", "format": "counter", "type": "number", "oid": "34", "optional": true, "size": "2"}
    :param name_value_proxy_conn: {"description": "Name value proxy-connection", "format": "counter", "type": "number", "oid": "55", "optional": true, "size": "2"}
    :param request_header_alloc_fail: {"description": "Request/Header allocation fail", "format": "counter", "type": "number", "oid": "49", "optional": true, "size": "2"}
    :param unknown_control_frame: {"description": "Unknown control frame", "format": "counter", "type": "number", "oid": "67", "optional": true, "size": "2"}
    :param http_data_stream_not_found: {"description": "HTTP data stream not found", "format": "counter", "type": "number", "oid": "75", "optional": true, "size": "2"}
    :param stream_lt_prev: {"description": "Stream id less than previous", "format": "counter", "type": "number", "oid": "60", "optional": true, "size": "2"}
    :param settings_frame: {"description": "Setting frame received", "format": "counter", "type": "number", "oid": "28", "optional": true, "size": "2"}
    :param curr_stream: {"description": "Curr Streams", "format": "counter", "type": "number", "oid": "7", "optional": true, "size": "2"}
    :param close_stream_already_closed: {"description": "Closing closed stream", "format": "counter", "type": "number", "oid": "43", "optional": true, "size": "2"}
    :param data_on_closed_stream: {"description": "Data on closed stream", "format": "counter", "type": "number", "oid": "68", "optional": true, "size": "2"}
    :param name_value_trasnfer_encod: {"description": "Name value transfer encoding", "format": "counter", "type": "number", "oid": "56", "optional": true, "size": "2"}
    :param http_conn_alloc_fail: {"description": "HTTP connection allocation fail", "format": "counter", "type": "number", "oid": "48", "optional": true, "size": "2"}
    :param fin_close_session: {"description": "FIN close session", "format": "counter", "type": "number", "oid": "38", "optional": true, "size": "2"}
    :param name_value_no_must_have: {"description": "Name value no must have", "format": "counter", "type": "number", "oid": "57", "optional": true, "size": "2"}
    :param syn_after_goaway: {"description": "SYN after goaway", "format": "counter", "type": "number", "oid": "59", "optional": true, "size": "2"}
    :param syn_reply_frame: {"description": "SYN reply frame received", "format": "counter", "type": "number", "oid": "26", "optional": true, "size": "2"}
    :param name_value_invalid_http_ver: {"description": "Name value invalid http version", "format": "counter", "type": "number", "oid": "52", "optional": true, "size": "2"}
    :param client_rst_nostream: {"description": "Close RST stream not found", "format": "counter", "type": "number", "oid": "64", "optional": true, "size": "2"}
    :param header_after_session_close: {"description": "Header after session close", "format": "counter", "type": "number", "oid": "71", "optional": true, "size": "2"}
    :param stream_not_found: {"description": "STREAM not found", "format": "counter", "type": "number", "oid": "18", "optional": true, "size": "2"}
    :param client_fin: {"description": "Client FIN", "format": "counter", "type": "number", "oid": "19", "optional": true, "size": "2"}
    :param stream_err: {"description": "Stream err", "format": "counter", "type": "number", "oid": "22", "optional": true, "size": "2"}
    :param total_v3_proxy: {"description": "Version 3 Streams", "format": "counter", "type": "number", "oid": "6", "optional": true, "size": "2"}
    :param syn_unidir: {"description": "Unidirectional SYN", "format": "counter", "type": "number", "oid": "62", "optional": true, "size": "2"}
    :param http_data_session_close: {"description": "HTTP data session close", "format": "counter", "type": "number", "oid": "74", "optional": true, "size": "2"}
    :param session_err: {"description": "Session err", "format": "counter", "type": "number", "oid": "23", "optional": true, "size": "2"}
    :param close_stream_not_http_proxy: {"description": "Close Stream not http-proxy", "format": "counter", "type": "number", "oid": "76", "optional": true, "size": "2"}
    :param data_no_stream_no_goaway: {"description": "Data no stream and no goaway", "format": "counter", "type": "number", "oid": "33", "optional": true, "size": "2"}
    :param invalid_window_size: {"description": "Invalid window size", "format": "counter", "type": "number", "oid": "66", "optional": true, "size": "2"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.invalid_frame_size = ""
        self.data_cb_no_tuple = ""
        self.compress_ctx_alloc_fail = ""
        self.stream_found = ""
        self.total_proxy = ""
        self.curr_http_proxy = ""
        self.total_v2_proxy = ""
        self.syn_stream_exist_or_even = ""
        self.close_stream_stream_not_found = ""
        self.client_rst = ""
        self.est_cb_no_tuple = ""
        self.stream_alloc_fail = ""
        self.max_concurrent_stream_limit = ""
        self.deflate_ctx = ""
        self.client_goaway = ""
        self.ping_sent = ""
        self.server_goaway = ""
        self.session_needs_requeue = ""
        self.syn_reply_alr_rcvd = ""
        self.total_http_proxy = ""
        self.close_stream_session_close = ""
        self.decompress_fail = ""
        self.ping_frame = ""
        self.inflate_ctx = ""
        self.name_value_total_len_ex = ""
        self.http_err_stream_closed = ""
        self.http_hdr_stream_close = ""
        self.http_data_stream_close = ""
        self.control_frame = ""
        self.session_close = ""
        self.name_value_connection = ""
        self.fin_stream_closed = ""
        self.stream_close = ""
        self.total_stream = ""
        self.window_no_stream = ""
        self.server_rst_close_stream = ""
        self.data_no_stream = ""
        self.new_stream_session_del = ""
        self.ctx_alloc_fail = ""
        self.close_stream_session_not_found = ""
        self.invalid_version = ""
        self.server_fin = ""
        self.window_frame = ""
        self.close_session_already_closed = ""
        self.headers_frame = ""
        self.server_rst = ""
        self.header_compress_fail = ""
        self.tcp_err = ""
        self.curr_proxy = ""
        self.name_value_zero_len = ""
        self.name_value_keepalive = ""
        self.http_close_stream_closed = ""
        self.syn_frame = ""
        self.data_frame = ""
        self.total_stream_succ = ""
        self.data_no_stream_goaway_close = ""
        self.name_value_proxy_conn = ""
        self.request_header_alloc_fail = ""
        self.unknown_control_frame = ""
        self.http_data_stream_not_found = ""
        self.stream_lt_prev = ""
        self.settings_frame = ""
        self.curr_stream = ""
        self.close_stream_already_closed = ""
        self.data_on_closed_stream = ""
        self.name_value_trasnfer_encod = ""
        self.http_conn_alloc_fail = ""
        self.fin_close_session = ""
        self.name_value_no_must_have = ""
        self.syn_after_goaway = ""
        self.syn_reply_frame = ""
        self.name_value_invalid_http_ver = ""
        self.client_rst_nostream = ""
        self.header_after_session_close = ""
        self.stream_not_found = ""
        self.client_fin = ""
        self.stream_err = ""
        self.total_v3_proxy = ""
        self.syn_unidir = ""
        self.http_data_session_close = ""
        self.session_err = ""
        self.close_stream_not_http_proxy = ""
        self.data_no_stream_no_goaway = ""
        self.invalid_window_size = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class SpdyProxy(A10BaseClass):
    
    """Class Description::
    Statistics for the object spdy-proxy.

    Class spdy-proxy supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/spdy-proxy/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "spdy-proxy"
        self.a10_url="/axapi/v3/slb/spdy-proxy/stats"
        self.DeviceProxy = ""
        self.stats = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


