from a10sdk.common.A10BaseClass import A10BaseClass


class TcpProxy(A10BaseClass):
    
    """Class Description::
    TCP Proxy.

    Class tcp-proxy supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param qos: {"description": "QOS level (number)", "format": "number", "type": "number", "maximum": 63, "minimum": 1, "optional": true}
    :param init_cwnd: {"description": "The initial congestion control window size (packets), default is 4 (number)", "format": "number", "default": 4, "optional": true, "maximum": 10, "minimum": 1, "type": "number"}
    :param idle_timeout: {"description": "Idle Timeout (sec), default is 600 (number)", "format": "number", "default": 600, "optional": true, "maximum": 2097151, "minimum": 1, "type": "number"}
    :param fin_timeout: {"description": "FIN timeout (sec), default is 5 (number)", "format": "number", "default": 5, "optional": true, "maximum": 60, "minimum": 1, "type": "number"}
    :param half_open_idle_timeout: {"description": "TCP Half Open Idle Timeout (sec), default is off (number)", "format": "number", "type": "number", "maximum": 60, "minimum": 1, "optional": true}
    :param reno: {"default": 0, "optional": true, "type": "number", "description": "Enable Reno Congestion Control Algorithm", "format": "flag"}
    :param timewait: {"description": "Timewait Threshold (sec), default 5 (number)", "format": "number", "default": 5, "optional": true, "maximum": 60, "minimum": 1, "type": "number"}
    :param dynamic_buffer_allocation: {"default": 0, "optional": true, "type": "number", "description": "Optimally adjust the transmit and receive buffer sizes of TCP proxy while keeping their sum constant", "format": "flag"}
    :param alive_if_active: {"default": 0, "optional": true, "type": "number", "description": "keep connection alive if active traffic", "format": "flag"}
    :param mss: {"description": "Responding MSS to use if client MSS is large, default is off (number)", "format": "number", "default": 1460, "optional": true, "maximum": 4312, "minimum": 128, "type": "number"}
    :param keepalive_interval: {"description": "Interval between keepalive probes (sec), default is off (number)", "format": "number", "type": "number", "maximum": 12000, "minimum": 60, "optional": true}
    :param retransmit_retries: {"description": "Number of Retries for Retransmit, default is 3", "format": "number", "default": 3, "optional": true, "maximum": 20, "minimum": 1, "type": "number"}
    :param insert_client_ip: {"default": 0, "optional": true, "type": "number", "description": "Insert client ip into TCP option", "format": "flag"}
    :param nagle: {"default": 0, "optional": true, "type": "number", "description": "Enable Nagle Algorithm", "format": "flag"}
    :param force_delete_timeout_100ms: {"description": "The maximum time that a session can stay in the system before being deleted, default is off (number in 100ms)", "format": "number", "optional": true, "maximum": 31, "minimum": 1, "not": "force-delete-timeout", "type": "number"}
    :param initial_window_size: {"description": "Set the initial window size, default is off (number)", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": true}
    :param keepalive_probes: {"description": "Number of keepalive probes sent, default is off", "format": "number", "type": "number", "maximum": 10, "minimum": 2, "optional": true}
    :param ack_aggressiveness: {"description": "'low': Delayed ACK; 'medium': Delayed ACK, with ACK on each packet with PUSH flag; 'high': ACK on each packet; ", "format": "enum", "default": "low", "type": "string", "enum": ["low", "medium", "high"], "optional": true}
    :param backend_wscale: {"description": "The TCP window scale used for the server side, default is off (number)", "format": "number", "type": "number", "maximum": 14, "minimum": 1, "optional": true}
    :param reset_rev: {"default": 0, "optional": true, "type": "number", "description": "send reset to client if error happens", "format": "flag"}
    :param receive_buffer: {"description": "TCP Receive Buffer (default 50k) (number)", "format": "number", "default": 51200, "optional": true, "maximum": 2147483647, "minimum": 1, "type": "number"}
    :param transmit_buffer: {"description": "TCP Transmit Buffer (default 50k) (number)", "format": "number", "default": 51200, "optional": true, "maximum": 2147483647, "minimum": 1, "type": "number"}
    :param name: {"description": "TCP Proxy Template Name", "format": "string", "default": "default", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param reset_fwd: {"default": 0, "optional": true, "type": "number", "description": "send reset to server if error happens", "format": "flag"}
    :param syn_retries: {"description": "SYN Retry Numbers, default is 5", "format": "number", "default": 5, "optional": true, "maximum": 20, "minimum": 1, "type": "number"}
    :param force_delete_timeout: {"description": "The maximum time that a session can stay in the system before being deleted, default is off (number (second))", "format": "number", "optional": true, "maximum": 31, "minimum": 1, "not": "force-delete-timeout-100ms", "type": "number"}
    :param half_close_idle_timeout: {"description": "TCP Half Close Idle Timeout (sec), default is off (number)", "format": "number", "type": "number", "maximum": 120, "minimum": 60, "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/template/tcp-proxy/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "tcp-proxy"
        self.a10_url="/axapi/v3/slb/template/tcp-proxy/{name}"
        self.DeviceProxy = ""
        self.qos = ""
        self.init_cwnd = ""
        self.idle_timeout = ""
        self.fin_timeout = ""
        self.half_open_idle_timeout = ""
        self.reno = ""
        self.timewait = ""
        self.dynamic_buffer_allocation = ""
        self.alive_if_active = ""
        self.mss = ""
        self.keepalive_interval = ""
        self.retransmit_retries = ""
        self.insert_client_ip = ""
        self.nagle = ""
        self.force_delete_timeout_100ms = ""
        self.initial_window_size = ""
        self.keepalive_probes = ""
        self.ack_aggressiveness = ""
        self.backend_wscale = ""
        self.reset_rev = ""
        self.receive_buffer = ""
        self.transmit_buffer = ""
        self.name = ""
        self.reset_fwd = ""
        self.syn_retries = ""
        self.force_delete_timeout = ""
        self.half_close_idle_timeout = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


