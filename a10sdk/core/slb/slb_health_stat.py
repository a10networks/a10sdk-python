from a10sdk.common.A10BaseClass import A10BaseClass


class SamplingEnable(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param counters1: {"enum": ["all", "num_burst", "max_jiffie", "min_jiffie", "avg_jiffie", "open_socket", "open_socket_failed", "close_socket", "connect_failed", "send_packet", "send_packet_failed", "recv_packet", "recv_packet_failed", "retry_times", "timeout", "unexpected_error", "conn_imdt_succ", "sock_close_before_17", "sock_close_without_notify", "curr_health_rate", "ext_health_rate", "ext_health_rate_val", "total_number", "status_up", "status_down", "status_unkn", "status_other", "running_time"], "type": "string", "description": "'all': all; 'num_burst': Number of burst; 'max_jiffie': Maximum number of jiffies; 'min_jiffie': Minimum number of jiffies; 'avg_jiffie': Average number of jiffies; 'open_socket': Number of open sockets; 'open_socket_failed': Number of failed open sockets; 'close_socket': Number of closed sockets; 'connect_failed': Number of failed connections; 'send_packet': Number of packets sent; 'send_packet_failed': Number of packet send failures; 'recv_packet': Number of received packets; 'recv_packet_failed': Number of failed packet receives; 'retry_times': Retry times; 'timeout': Timouet value; 'unexpected_error': Number of unexpected errors; 'conn_imdt_succ': Number of connection immediete success; 'sock_close_before_17': Number of sockets closed before l7; 'sock_close_without_notify': Number of sockets closed without notify; 'curr_health_rate': Current health rate; 'ext_health_rate': External health rate; 'ext_health_rate_val': External health rate value; 'total_number': Total number; 'status_up': Number of status ups; 'status_down': Number of status downs; 'status_unkn': Number of status unknowns; 'status_other': Number of other status; 'running_time': Running time; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "sampling-enable"
        self.DeviceProxy = ""
        self.counters1 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class HealthStat(A10BaseClass):
    
    """    :param sampling_enable: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "num_burst", "max_jiffie", "min_jiffie", "avg_jiffie", "open_socket", "open_socket_failed", "close_socket", "connect_failed", "send_packet", "send_packet_failed", "recv_packet", "recv_packet_failed", "retry_times", "timeout", "unexpected_error", "conn_imdt_succ", "sock_close_before_17", "sock_close_without_notify", "curr_health_rate", "ext_health_rate", "ext_health_rate_val", "total_number", "status_up", "status_down", "status_unkn", "status_other", "running_time"], "type": "string", "description": "'all': all; 'num_burst': Number of burst; 'max_jiffie': Maximum number of jiffies; 'min_jiffie': Minimum number of jiffies; 'avg_jiffie': Average number of jiffies; 'open_socket': Number of open sockets; 'open_socket_failed': Number of failed open sockets; 'close_socket': Number of closed sockets; 'connect_failed': Number of failed connections; 'send_packet': Number of packets sent; 'send_packet_failed': Number of packet send failures; 'recv_packet': Number of received packets; 'recv_packet_failed': Number of failed packet receives; 'retry_times': Retry times; 'timeout': Timouet value; 'unexpected_error': Number of unexpected errors; 'conn_imdt_succ': Number of connection immediete success; 'sock_close_before_17': Number of sockets closed before l7; 'sock_close_without_notify': Number of sockets closed without notify; 'curr_health_rate': Current health rate; 'ext_health_rate': External health rate; 'ext_health_rate_val': External health rate value; 'total_number': Total number; 'status_up': Number of status ups; 'status_down': Number of status downs; 'status_unkn': Number of status unknowns; 'status_other': Number of other status; 'running_time': Running time; ", "format": "enum"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Show health monitor statistics.

    Class health-stat supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/health-stat`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "health-stat"
        self.a10_url="/axapi/v3/slb/health-stat"
        self.DeviceProxy = ""
        self.sampling_enable = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


