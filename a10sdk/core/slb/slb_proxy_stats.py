from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param start_server_conn: {"description": "Start server conn", "format": "counter", "type": "number", "oid": "23", "optional": true, "size": "8"}
    :param service_alloc_cb: {"description": "Service alloc callback", "format": "counter", "type": "number", "oid": "15", "optional": true, "size": "8"}
    :param start_server_conn_fail_tuple: {"description": "Fail Tuple Issue", "format": "counter", "type": "number", "oid": "30", "optional": true, "size": "8"}
    :param client_rst: {"description": "Client RST", "format": "counter", "type": "number", "oid": "10", "optional": true, "size": "8"}
    :param queue_depth_over_limit: {"description": "Queue depth over limit", "format": "counter", "type": "number", "oid": "12", "optional": true, "size": "8"}
    :param start_server_conn_fail_mem: {"description": "No memory", "format": "counter", "type": "number", "oid": "26", "optional": true, "size": "8"}
    :param start_server_conn_fail_server: {"description": "Fail Server issue", "format": "counter", "type": "number", "oid": "29", "optional": true, "size": "8"}
    :param service_free_cb_failed: {"description": "Service free callback failed", "format": "counter", "type": "number", "oid": "18", "optional": true, "size": "8"}
    :param est_event: {"description": "Connection established", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "8"}
    :param service_free_cb: {"description": "Service free callback", "format": "counter", "type": "number", "oid": "17", "optional": true, "size": "8"}
    :param data_cb_failed: {"description": "App DATA callback failed", "format": "counter", "type": "number", "oid": "20", "optional": true, "size": "8"}
    :param wbuf_event: {"description": "Ready to send data", "format": "counter", "type": "number", "oid": "7", "optional": true, "size": "8"}
    :param data_event: {"description": "Data received", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "8"}
    :param service_alloc_cb_failed: {"description": "Service alloc callback failed", "format": "counter", "type": "number", "oid": "16", "optional": true, "size": "8"}
    :param start_server_conn_fail_persist: {"description": "Fail Persistence", "format": "counter", "type": "number", "oid": "28", "optional": true, "size": "8"}
    :param server_fin: {"description": "Server FIN", "format": "counter", "type": "number", "oid": "6", "optional": true, "size": "8"}
    :param server_rst: {"description": "Server RST", "format": "counter", "type": "number", "oid": "11", "optional": true, "size": "8"}
    :param start_server_conn_fail_snat: {"description": "Failed Source NAT", "format": "counter", "type": "number", "oid": "27", "optional": true, "size": "8"}
    :param start_server_conn_no_route: {"description": "No route to server", "format": "counter", "type": "number", "oid": "25", "optional": true, "size": "8"}
    :param tcp_event: {"description": "TCP stack event", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "8"}
    :param no_mem: {"description": "No memory", "format": "counter", "type": "number", "oid": "9", "optional": true, "size": "8"}
    :param event_failed: {"description": "Event failed", "format": "counter", "type": "number", "oid": "13", "optional": true, "size": "8"}
    :param err_event: {"description": "Error occured", "format": "counter", "type": "number", "oid": "8", "optional": true, "size": "8"}
    :param line_too_long: {"description": "Line too long", "format": "counter", "type": "number", "oid": "31", "optional": true, "size": "8"}
    :param wbuf_cb_failed: {"description": "App WBUF callback failed", "format": "counter", "type": "number", "oid": "21", "optional": true, "size": "8"}
    :param err_cb_failed: {"description": "App ERR callback failed", "format": "counter", "type": "number", "oid": "22", "optional": true, "size": "8"}
    :param client_fin: {"description": "Client FIN", "format": "counter", "type": "number", "oid": "5", "optional": true, "size": "8"}
    :param est_cb_failed: {"description": "App EST callback failed", "format": "counter", "type": "number", "oid": "19", "optional": true, "size": "8"}
    :param start_server_conn_succ: {"description": "Success", "format": "counter", "type": "number", "oid": "24", "optional": true, "size": "8"}
    :param conn_not_exist: {"description": "Conn not exist", "format": "counter", "type": "number", "oid": "14", "optional": true, "size": "8"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.start_server_conn = ""
        self.service_alloc_cb = ""
        self.start_server_conn_fail_tuple = ""
        self.client_rst = ""
        self.queue_depth_over_limit = ""
        self.start_server_conn_fail_mem = ""
        self.start_server_conn_fail_server = ""
        self.service_free_cb_failed = ""
        self.est_event = ""
        self.service_free_cb = ""
        self.data_cb_failed = ""
        self.wbuf_event = ""
        self.data_event = ""
        self.service_alloc_cb_failed = ""
        self.start_server_conn_fail_persist = ""
        self.server_fin = ""
        self.server_rst = ""
        self.start_server_conn_fail_snat = ""
        self.start_server_conn_no_route = ""
        self.tcp_event = ""
        self.no_mem = ""
        self.event_failed = ""
        self.err_event = ""
        self.line_too_long = ""
        self.wbuf_cb_failed = ""
        self.err_cb_failed = ""
        self.client_fin = ""
        self.est_cb_failed = ""
        self.start_server_conn_succ = ""
        self.conn_not_exist = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Proxy(A10BaseClass):
    
    """Class Description::
    Statistics for the object proxy.

    Class proxy supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/proxy/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "proxy"
        self.a10_url="/axapi/v3/slb/proxy/stats"
        self.DeviceProxy = ""
        self.stats = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


