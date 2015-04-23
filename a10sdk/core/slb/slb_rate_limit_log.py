from a10sdk.common.A10BaseClass import A10BaseClass


class SamplingEnable(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param counters1: {"enum": ["all", "total_log_times", "total_log_msg", "local_log_msg", "remote_log_msg", "local_log_rate", "remote_log_rate", "msg_too_big", "buff_alloc_fail", "no_route", "buff_send_fail", "alloc_conn", "free_conn", "conn_alloc_fail", "no_repeat_msg"], "type": "string", "description": "'all': all; 'total_log_times': Total log times; 'total_log_msg': Total log messages; 'local_log_msg': Local log messages; 'remote_log_msg': Remote log messages; 'local_log_rate': Local rate (per sec); 'remote_log_rate': Remote rate (per sec); 'msg_too_big': Log message too big; 'buff_alloc_fail': Buffer alloc fail; 'no_route': No route; 'buff_send_fail': Buffer send fail; 'alloc_conn': Log-session alloc; 'free_conn': Log-session free; 'conn_alloc_fail': Log-session alloc fail; 'no_repeat_msg': No repeat message; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "sampling-enable"
        self.DeviceProxy = ""
        self.counters1 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class RateLimitLog(A10BaseClass):
    
    """    :param sampling_enable: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "total_log_times", "total_log_msg", "local_log_msg", "remote_log_msg", "local_log_rate", "remote_log_rate", "msg_too_big", "buff_alloc_fail", "no_route", "buff_send_fail", "alloc_conn", "free_conn", "conn_alloc_fail", "no_repeat_msg"], "type": "string", "description": "'all': all; 'total_log_times': Total log times; 'total_log_msg': Total log messages; 'local_log_msg': Local log messages; 'remote_log_msg': Remote log messages; 'local_log_rate': Local rate (per sec); 'remote_log_rate': Remote rate (per sec); 'msg_too_big': Log message too big; 'buff_alloc_fail': Buffer alloc fail; 'no_route': No route; 'buff_send_fail': Buffer send fail; 'alloc_conn': Log-session alloc; 'free_conn': Log-session free; 'conn_alloc_fail': Log-session alloc fail; 'no_repeat_msg': No repeat message; ", "format": "enum"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Show rate limit logging statistics.

    Class rate-limit-log supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/rate-limit-log`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "rate-limit-log"
        self.a10_url="/axapi/v3/slb/rate-limit-log"
        self.DeviceProxy = ""
        self.sampling_enable = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


