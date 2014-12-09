from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param min_jiffie: {"description": "Minimum number of jiffies", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "8"}
    :param connect_failed: {"description": "Number of failed connections", "format": "counter", "type": "number", "oid": "8", "optional": true, "size": "8"}
    :param num_burst: {"description": "Number of burst", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}
    :param ext_health_rate_val: {"description": "External health rate value", "format": "counter", "type": "number", "oid": "21", "optional": true, "size": "8"}
    :param retry_times: {"description": "Retry times", "format": "counter", "type": "number", "oid": "13", "optional": true, "size": "8"}
    :param send_packet: {"description": "Number of packets sent", "format": "counter", "type": "number", "oid": "9", "optional": true, "size": "8"}
    :param status_other: {"description": "Number of other status", "format": "counter", "type": "number", "oid": "26", "optional": true, "size": "8"}
    :param unexpected_error: {"description": "Number of unexpected errors", "format": "counter", "type": "number", "oid": "15", "optional": true, "size": "8"}
    :param status_down: {"description": "Number of status downs", "format": "counter", "type": "number", "oid": "24", "optional": true, "size": "8"}
    :param recv_packet_failed: {"description": "Number of failed packet receives", "format": "counter", "type": "number", "oid": "12", "optional": true, "size": "8"}
    :param close_socket: {"description": "Number of closed sockets", "format": "counter", "type": "number", "oid": "7", "optional": true, "size": "8"}
    :param conn_imdt_succ: {"description": "Number of connection immediete success", "format": "counter", "type": "number", "oid": "16", "optional": true, "size": "8"}
    :param recv_packet: {"description": "Number of received packets", "format": "counter", "type": "number", "oid": "11", "optional": true, "size": "8"}
    :param curr_health_rate: {"description": "Current health rate", "format": "counter", "type": "number", "oid": "19", "optional": true, "size": "8"}
    :param open_socket_failed: {"description": "Number of failed open sockets", "format": "counter", "type": "number", "oid": "6", "optional": true, "size": "8"}
    :param send_packet_failed: {"description": "Number of packet send failures", "format": "counter", "type": "number", "oid": "10", "optional": true, "size": "8"}
    :param sock_close_before_17: {"description": "Number of sockets closed before l7", "format": "counter", "type": "number", "oid": "17", "optional": true, "size": "8"}
    :param total_number: {"description": "Total number", "format": "counter", "type": "number", "oid": "22", "optional": true, "size": "8"}
    :param status_unkn: {"description": "Number of status unknowns", "format": "counter", "type": "number", "oid": "25", "optional": true, "size": "8"}
    :param open_socket: {"description": "Number of open sockets", "format": "counter", "type": "number", "oid": "5", "optional": true, "size": "8"}
    :param sock_close_without_notify: {"description": "Number of sockets closed without notify", "format": "counter", "type": "number", "oid": "18", "optional": true, "size": "8"}
    :param status_up: {"description": "Number of status ups", "format": "counter", "type": "number", "oid": "23", "optional": true, "size": "8"}
    :param running_time: {"description": "Running time", "format": "counter", "type": "number", "oid": "27", "optional": true, "size": "8"}
    :param avg_jiffie: {"description": "Average number of jiffies", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "8"}
    :param max_jiffie: {"description": "Maximum number of jiffies", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "8"}
    :param ext_health_rate: {"description": "External health rate", "format": "counter", "type": "number", "oid": "20", "optional": true, "size": "8"}
    :param timeout: {"description": "Timouet value", "format": "counter", "type": "number", "oid": "14", "optional": true, "size": "8"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.min_jiffie = ""
        self.connect_failed = ""
        self.num_burst = ""
        self.ext_health_rate_val = ""
        self.retry_times = ""
        self.send_packet = ""
        self.status_other = ""
        self.unexpected_error = ""
        self.status_down = ""
        self.recv_packet_failed = ""
        self.close_socket = ""
        self.conn_imdt_succ = ""
        self.recv_packet = ""
        self.curr_health_rate = ""
        self.open_socket_failed = ""
        self.send_packet_failed = ""
        self.sock_close_before_17 = ""
        self.total_number = ""
        self.status_unkn = ""
        self.open_socket = ""
        self.sock_close_without_notify = ""
        self.status_up = ""
        self.running_time = ""
        self.avg_jiffie = ""
        self.max_jiffie = ""
        self.ext_health_rate = ""
        self.timeout = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class HealthStat(A10BaseClass):
    
    """Class Description::
    Statistics for the object health-stat.

    Class health-stat supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/health-stat/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "health-stat"
        self.a10_url="/axapi/v3/slb/health-stat/stats"
        self.DeviceProxy = ""
        self.stats = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


