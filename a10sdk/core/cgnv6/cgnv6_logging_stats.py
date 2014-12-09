from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param tcp_port_overloading_allocated: {"description": "TCP Port Overloading Allocated", "format": "counter", "type": "number", "oid": "38", "optional": true, "size": "8"}
    :param tcp_session_deleted: {"description": "TCP Session Deleted", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "8"}
    :param gre_session_created: {"description": "GRE Session Created", "format": "counter", "type": "number", "oid": "21", "optional": true, "size": "8"}
    :param icmpv6_resource_freed: {"description": "ICMPV6 Resource Freed", "format": "counter", "type": "number", "oid": "20", "optional": true, "size": "8"}
    :param icmpv6_session_created: {"description": "ICMPV6 Session Created", "format": "counter", "type": "number", "oid": "17", "optional": true, "size": "8"}
    :param fixed_nat_periodic_config_logs_sent: {"description": "Fixed NAT Disabled Configs Logged", "format": "counter", "type": "number", "oid": "32", "optional": true, "size": "8"}
    :param udp_port_overloading_freed: {"description": "UDP Port Overloading Freed", "format": "counter", "type": "number", "oid": "41", "optional": true, "size": "8"}
    :param tcp_session_created: {"description": "TCP Session Created", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}
    :param log_sent: {"description": "Log Packets Sent", "format": "counter", "type": "number", "oid": "34", "optional": true, "size": "8"}
    :param udp_port_allocated: {"description": "UDP Port Allocated", "format": "counter", "type": "number", "oid": "9", "optional": true, "size": "8"}
    :param conn_tcp_dropped: {"description": "TCP Connection Lost", "format": "counter", "type": "number", "oid": "37", "optional": true, "size": "8"}
    :param esp_session_deleted: {"description": "ESP Session Deleted", "format": "counter", "type": "number", "oid": "26", "optional": true, "size": "8"}
    :param udp_session_created: {"description": "UDP Session Created", "format": "counter", "type": "number", "oid": "7", "optional": true, "size": "8"}
    :param gre_resource_allocated: {"description": "GRE Resource Allocated", "format": "counter", "type": "number", "oid": "23", "optional": true, "size": "8"}
    :param udp_port_batch_freed: {"description": "UDP Port Batch Freed", "format": "counter", "type": "number", "oid": "12", "optional": true, "size": "8"}
    :param fixed_nat_periodic_config_logged: {"description": "Fixed NAT Disabled Config Logs Sent", "format": "counter", "type": "number", "oid": "33", "optional": true, "size": "8"}
    :param fixed_nat_disable_config_logged: {"description": "Fixed NAT Periodic Configs Logged", "format": "counter", "type": "number", "oid": "30", "optional": true, "size": "8"}
    :param esp_resource_allocated: {"description": "ESP Resource Allocated", "format": "counter", "type": "number", "oid": "27", "optional": true, "size": "8"}
    :param tcp_port_allocated: {"description": "TCP Port Allocated", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "8"}
    :param http_request_logged: {"description": "HTTP Request Logged", "format": "counter", "type": "number", "oid": "42", "optional": true, "size": "8"}
    :param icmp_resource_allocated: {"description": "ICMP Resource Allocated", "format": "counter", "type": "number", "oid": "15", "optional": true, "size": "8"}
    :param esp_session_created: {"description": "ESP Session Created", "format": "counter", "type": "number", "oid": "25", "optional": true, "size": "8"}
    :param icmp_resource_freed: {"description": "ICMP Resource Freed", "format": "counter", "type": "number", "oid": "16", "optional": true, "size": "8"}
    :param icmpv6_session_deleted: {"description": "ICMPV6 Session Deleted", "format": "counter", "type": "number", "oid": "18", "optional": true, "size": "8"}
    :param tcp_port_overloading_freed: {"description": "TCP Port Overloading Freed", "format": "counter", "type": "number", "oid": "39", "optional": true, "size": "8"}
    :param gre_resource_freed: {"description": "GRE Resource Freed", "format": "counter", "type": "number", "oid": "24", "optional": true, "size": "8"}
    :param gre_session_deleted: {"description": "GRE Session Deleted", "format": "counter", "type": "number", "oid": "22", "optional": true, "size": "8"}
    :param udp_port_overloading_allocated: {"description": "UDP Port Overloading Allocated", "format": "counter", "type": "number", "oid": "40", "optional": true, "size": "8"}
    :param fixed_nat_user_ports: {"description": "Fixed NAT Inside User Port Mapping", "format": "counter", "type": "number", "oid": "29", "optional": true, "size": "8"}
    :param tcp_port_freed: {"description": "TCP Port Freed", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "8"}
    :param icmp_session_deleted: {"description": "ICMP Session Deleted", "format": "counter", "type": "number", "oid": "14", "optional": true, "size": "8"}
    :param icmp_session_created: {"description": "ICMP Session Created", "format": "counter", "type": "number", "oid": "13", "optional": true, "size": "8"}
    :param conn_tcp_established: {"description": "TCP Connection Established", "format": "counter", "type": "number", "oid": "36", "optional": true, "size": "8"}
    :param fixed_nat_disable_config_logs_sent: {"description": "Fixed NAT Periodic Config Logs Sent", "format": "counter", "type": "number", "oid": "31", "optional": true, "size": "8"}
    :param udp_port_batch_allocated: {"description": "UDP Port Batch Allocated", "format": "counter", "type": "number", "oid": "11", "optional": true, "size": "8"}
    :param udp_port_freed: {"description": "UDP Port Freed", "format": "counter", "type": "number", "oid": "10", "optional": true, "size": "8"}
    :param esp_resource_freed: {"description": "ESP Resource Freed", "format": "counter", "type": "number", "oid": "28", "optional": true, "size": "8"}
    :param tcp_port_batch_freed: {"description": "TCP Port Batch Freed", "format": "counter", "type": "number", "oid": "6", "optional": true, "size": "8"}
    :param log_dropped: {"description": "Log Packets Dropped", "format": "counter", "type": "number", "oid": "35", "optional": true, "size": "8"}
    :param icmpv6_resource_allocated: {"description": "ICMPV6 Resource Allocated", "format": "counter", "type": "number", "oid": "19", "optional": true, "size": "8"}
    :param udp_session_deleted: {"description": "UDP Session Deleted", "format": "counter", "type": "number", "oid": "8", "optional": true, "size": "8"}
    :param tcp_port_batch_allocated: {"description": "TCP Port Batch Allocated", "format": "counter", "type": "number", "oid": "5", "optional": true, "size": "8"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.tcp_port_overloading_allocated = ""
        self.tcp_session_deleted = ""
        self.gre_session_created = ""
        self.icmpv6_resource_freed = ""
        self.icmpv6_session_created = ""
        self.fixed_nat_periodic_config_logs_sent = ""
        self.udp_port_overloading_freed = ""
        self.tcp_session_created = ""
        self.log_sent = ""
        self.udp_port_allocated = ""
        self.conn_tcp_dropped = ""
        self.esp_session_deleted = ""
        self.udp_session_created = ""
        self.gre_resource_allocated = ""
        self.udp_port_batch_freed = ""
        self.fixed_nat_periodic_config_logged = ""
        self.fixed_nat_disable_config_logged = ""
        self.esp_resource_allocated = ""
        self.tcp_port_allocated = ""
        self.http_request_logged = ""
        self.icmp_resource_allocated = ""
        self.esp_session_created = ""
        self.icmp_resource_freed = ""
        self.icmpv6_session_deleted = ""
        self.tcp_port_overloading_freed = ""
        self.gre_resource_freed = ""
        self.gre_session_deleted = ""
        self.udp_port_overloading_allocated = ""
        self.fixed_nat_user_ports = ""
        self.tcp_port_freed = ""
        self.icmp_session_deleted = ""
        self.icmp_session_created = ""
        self.conn_tcp_established = ""
        self.fixed_nat_disable_config_logs_sent = ""
        self.udp_port_batch_allocated = ""
        self.udp_port_freed = ""
        self.esp_resource_freed = ""
        self.tcp_port_batch_freed = ""
        self.log_dropped = ""
        self.icmpv6_resource_allocated = ""
        self.udp_session_deleted = ""
        self.tcp_port_batch_allocated = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Logging(A10BaseClass):
    
    """Class Description::
    Statistics for the object logging.

    Class logging supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/logging/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "logging"
        self.a10_url="/axapi/v3/cgnv6/logging/stats"
        self.DeviceProxy = ""
        self.stats = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


