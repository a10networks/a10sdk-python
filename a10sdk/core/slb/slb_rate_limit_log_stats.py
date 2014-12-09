from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param msg_too_big: {"description": "Log message too big", "format": "counter", "type": "number", "oid": "7", "optional": true, "size": "8"}
    :param buff_send_fail: {"description": "Buffer send fail", "format": "counter", "type": "number", "oid": "10", "optional": true, "size": "8"}
    :param remote_log_rate: {"description": "Remote rate (per sec)", "format": "counter", "type": "number", "oid": "6", "optional": true, "size": "8"}
    :param alloc_conn: {"description": "Log-session alloc", "format": "counter", "type": "number", "oid": "11", "optional": true, "size": "8"}
    :param no_repeat_msg: {"description": "No repeat message", "format": "counter", "type": "number", "oid": "14", "optional": true, "size": "8"}
    :param free_conn: {"description": "Log-session free", "format": "counter", "type": "number", "oid": "12", "optional": true, "size": "8"}
    :param conn_alloc_fail: {"description": "Log-session alloc fail", "format": "counter", "type": "number", "oid": "13", "optional": true, "size": "8"}
    :param local_log_msg: {"description": "Local log messages", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "8"}
    :param total_log_msg: {"description": "Total log messages", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "8"}
    :param no_route: {"description": "No route", "format": "counter", "type": "number", "oid": "9", "optional": true, "size": "8"}
    :param remote_log_msg: {"description": "Remote log messages", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "8"}
    :param buff_alloc_fail: {"description": "Buffer alloc fail", "format": "counter", "type": "number", "oid": "8", "optional": true, "size": "8"}
    :param local_log_rate: {"description": "Local rate (per sec)", "format": "counter", "type": "number", "oid": "5", "optional": true, "size": "8"}
    :param total_log_times: {"description": "Total log times", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.msg_too_big = ""
        self.buff_send_fail = ""
        self.remote_log_rate = ""
        self.alloc_conn = ""
        self.no_repeat_msg = ""
        self.free_conn = ""
        self.conn_alloc_fail = ""
        self.local_log_msg = ""
        self.total_log_msg = ""
        self.no_route = ""
        self.remote_log_msg = ""
        self.buff_alloc_fail = ""
        self.local_log_rate = ""
        self.total_log_times = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class RateLimitLog(A10BaseClass):
    
    """Class Description::
    Statistics for the object rate-limit-log.

    Class rate-limit-log supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/rate-limit-log/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "rate-limit-log"
        self.a10_url="/axapi/v3/slb/rate-limit-log/stats"
        self.DeviceProxy = ""
        self.stats = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


