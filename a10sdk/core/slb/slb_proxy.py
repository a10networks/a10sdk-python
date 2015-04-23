from a10sdk.common.A10BaseClass import A10BaseClass


class SamplingEnable(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param counters1: {"enum": ["all", "num", "tcp_event", "est_event", "data_event", "client_fin", "server_fin", "wbuf_event", "err_event", "no_mem", "client_rst", "server_rst", "queue_depth_over_limit", "event_failed", "conn_not_exist", "service_alloc_cb", "service_alloc_cb_failed", "service_free_cb", "service_free_cb_failed", "est_cb_failed", "data_cb_failed", "wbuf_cb_failed", "err_cb_failed", "start_server_conn", "start_server_conn_succ", "start_server_conn_no_route", "start_server_conn_fail_mem", "start_server_conn_fail_snat", "start_server_conn_fail_persist", "start_server_conn_fail_server", "start_server_conn_fail_tuple", "line_too_long"], "type": "string", "description": "'all': all; 'num': Num; 'tcp_event': TCP stack event; 'est_event': Connection established; 'data_event': Data received; 'client_fin': Client FIN; 'server_fin': Server FIN; 'wbuf_event': Ready to send data; 'err_event': Error occured; 'no_mem': No memory; 'client_rst': Client RST; 'server_rst': Server RST; 'queue_depth_over_limit': Queue depth over limit; 'event_failed': Event failed; 'conn_not_exist': Conn not exist; 'service_alloc_cb': Service alloc callback; 'service_alloc_cb_failed': Service alloc callback failed; 'service_free_cb': Service free callback; 'service_free_cb_failed': Service free callback failed; 'est_cb_failed': App EST callback failed; 'data_cb_failed': App DATA callback failed; 'wbuf_cb_failed': App WBUF callback failed; 'err_cb_failed': App ERR callback failed; 'start_server_conn': Start server conn; 'start_server_conn_succ': Success; 'start_server_conn_no_route': No route to server; 'start_server_conn_fail_mem': No memory; 'start_server_conn_fail_snat': Failed Source NAT; 'start_server_conn_fail_persist': Fail Persistence; 'start_server_conn_fail_server': Fail Server issue; 'start_server_conn_fail_tuple': Fail Tuple Issue; 'line_too_long': Line too long; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "sampling-enable"
        self.DeviceProxy = ""
        self.counters1 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Proxy(A10BaseClass):
    
    """    :param sampling_enable: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "num", "tcp_event", "est_event", "data_event", "client_fin", "server_fin", "wbuf_event", "err_event", "no_mem", "client_rst", "server_rst", "queue_depth_over_limit", "event_failed", "conn_not_exist", "service_alloc_cb", "service_alloc_cb_failed", "service_free_cb", "service_free_cb_failed", "est_cb_failed", "data_cb_failed", "wbuf_cb_failed", "err_cb_failed", "start_server_conn", "start_server_conn_succ", "start_server_conn_no_route", "start_server_conn_fail_mem", "start_server_conn_fail_snat", "start_server_conn_fail_persist", "start_server_conn_fail_server", "start_server_conn_fail_tuple", "line_too_long"], "type": "string", "description": "'all': all; 'num': Num; 'tcp_event': TCP stack event; 'est_event': Connection established; 'data_event': Data received; 'client_fin': Client FIN; 'server_fin': Server FIN; 'wbuf_event': Ready to send data; 'err_event': Error occured; 'no_mem': No memory; 'client_rst': Client RST; 'server_rst': Server RST; 'queue_depth_over_limit': Queue depth over limit; 'event_failed': Event failed; 'conn_not_exist': Conn not exist; 'service_alloc_cb': Service alloc callback; 'service_alloc_cb_failed': Service alloc callback failed; 'service_free_cb': Service free callback; 'service_free_cb_failed': Service free callback failed; 'est_cb_failed': App EST callback failed; 'data_cb_failed': App DATA callback failed; 'wbuf_cb_failed': App WBUF callback failed; 'err_cb_failed': App ERR callback failed; 'start_server_conn': Start server conn; 'start_server_conn_succ': Success; 'start_server_conn_no_route': No route to server; 'start_server_conn_fail_mem': No memory; 'start_server_conn_fail_snat': Failed Source NAT; 'start_server_conn_fail_persist': Fail Persistence; 'start_server_conn_fail_server': Fail Server issue; 'start_server_conn_fail_tuple': Fail Tuple Issue; 'line_too_long': Line too long; ", "format": "enum"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Show Proxy Global Statistics.

    Class proxy supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/proxy`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "proxy"
        self.a10_url="/axapi/v3/slb/proxy"
        self.DeviceProxy = ""
        self.sampling_enable = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


