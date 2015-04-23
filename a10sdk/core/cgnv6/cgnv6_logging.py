from a10sdk.common.A10BaseClass import A10BaseClass


class SamplingEnable(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param counters1: {"enum": ["all", "tcp-session-created", "tcp-session-deleted", "tcp-port-allocated", "tcp-port-freed", "tcp-port-batch-allocated", "tcp-port-batch-freed", "udp-session-created", "udp-session-deleted", "udp-port-allocated", "udp-port-freed", "udp-port-batch-allocated", "udp-port-batch-freed", "icmp-session-created", "icmp-session-deleted", "icmp-resource-allocated", "icmp-resource-freed", "icmpv6-session-created", "icmpv6-session-deleted", "icmpv6-resource-allocated", "icmpv6-resource-freed", "gre-session-created", "gre-session-deleted", "gre-resource-allocated", "gre-resource-freed", "esp-session-created", "esp-session-deleted", "esp-resource-allocated", "esp-resource-freed", "fixed-nat-user-ports", "fixed-nat-disable-config-logged", "fixed-nat-disable-config-logs-sent", "fixed-nat-periodic-config-logs-sent", "fixed-nat-periodic-config-logged", "log-sent", "log-dropped", "conn-tcp-established", "conn-tcp-dropped", "tcp-port-overloading-allocated", "tcp-port-overloading-freed", "udp-port-overloading-allocated", "udp-port-overloading-freed", "http-request-logged", "out-of-buffers", "add-msg-failed", "rtsp-port-allocated", "rtsp-port-freed", "conn-tcp-create-failed", "ipv4-frag-applied", "ipv4-frag-failed", "ipv6-frag-applied", "ipv6-frag-failed"], "type": "string", "description": "'all': all; 'tcp-session-created': TCP Session Created; 'tcp-session-deleted': TCP Session Deleted; 'tcp-port-allocated': TCP Port Allocated; 'tcp-port-freed': TCP Port Freed; 'tcp-port-batch-allocated': TCP Port Batch Allocated; 'tcp-port-batch-freed': TCP Port Batch Freed; 'udp-session-created': UDP Session Created; 'udp-session-deleted': UDP Session Deleted; 'udp-port-allocated': UDP Port Allocated; 'udp-port-freed': UDP Port Freed; 'udp-port-batch-allocated': UDP Port Batch Allocated; 'udp-port-batch-freed': UDP Port Batch Freed; 'icmp-session-created': ICMP Session Created; 'icmp-session-deleted': ICMP Session Deleted; 'icmp-resource-allocated': ICMP Resource Allocated; 'icmp-resource-freed': ICMP Resource Freed; 'icmpv6-session-created': ICMPV6 Session Created; 'icmpv6-session-deleted': ICMPV6 Session Deleted; 'icmpv6-resource-allocated': ICMPV6 Resource Allocated; 'icmpv6-resource-freed': ICMPV6 Resource Freed; 'gre-session-created': GRE Session Created; 'gre-session-deleted': GRE Session Deleted; 'gre-resource-allocated': GRE Resource Allocated; 'gre-resource-freed': GRE Resource Freed; 'esp-session-created': ESP Session Created; 'esp-session-deleted': ESP Session Deleted; 'esp-resource-allocated': ESP Resource Allocated; 'esp-resource-freed': ESP Resource Freed; 'fixed-nat-user-ports': Fixed NAT Inside User Port Mapping; 'fixed-nat-disable-config-logged': Fixed NAT Periodic Configs Logged; 'fixed-nat-disable-config-logs-sent': Fixed NAT Periodic Config Logs Sent; 'fixed-nat-periodic-config-logs-sent': Fixed NAT Disabled Configs Logged; 'fixed-nat-periodic-config-logged': Fixed NAT Disabled Config Logs Sent; 'log-sent': Log Packets Sent; 'log-dropped': Log Packets Dropped; 'conn-tcp-established': TCP Connection Established; 'conn-tcp-dropped': TCP Connection Lost; 'tcp-port-overloading-allocated': TCP Port Overloading Allocated; 'tcp-port-overloading-freed': TCP Port Overloading Freed; 'udp-port-overloading-allocated': UDP Port Overloading Allocated; 'udp-port-overloading-freed': UDP Port Overloading Freed; 'http-request-logged': HTTP Request Logged; 'out-of-buffers': Out of Buffers; 'add-msg-failed': Add Message to Buffer Failed; 'rtsp-port-allocated': RTSP UDP Port Allocated; 'rtsp-port-freed': RTSP UDP Port Freed; 'conn-tcp-create-failed': TCP Connection Failed; 'ipv4-frag-applied': IPv4 Fragmentation Applied; 'ipv4-frag-failed': IPv4 Fragmentation Failed; 'ipv6-frag-applied': IPv6 Fragmentation Applied; 'ipv6-frag-failed': IPv6 Fragmentation Failed; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "sampling-enable"
        self.DeviceProxy = ""
        self.counters1 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Logging(A10BaseClass):
    
    """    :param sampling_enable: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "tcp-session-created", "tcp-session-deleted", "tcp-port-allocated", "tcp-port-freed", "tcp-port-batch-allocated", "tcp-port-batch-freed", "udp-session-created", "udp-session-deleted", "udp-port-allocated", "udp-port-freed", "udp-port-batch-allocated", "udp-port-batch-freed", "icmp-session-created", "icmp-session-deleted", "icmp-resource-allocated", "icmp-resource-freed", "icmpv6-session-created", "icmpv6-session-deleted", "icmpv6-resource-allocated", "icmpv6-resource-freed", "gre-session-created", "gre-session-deleted", "gre-resource-allocated", "gre-resource-freed", "esp-session-created", "esp-session-deleted", "esp-resource-allocated", "esp-resource-freed", "fixed-nat-user-ports", "fixed-nat-disable-config-logged", "fixed-nat-disable-config-logs-sent", "fixed-nat-periodic-config-logs-sent", "fixed-nat-periodic-config-logged", "log-sent", "log-dropped", "conn-tcp-established", "conn-tcp-dropped", "tcp-port-overloading-allocated", "tcp-port-overloading-freed", "udp-port-overloading-allocated", "udp-port-overloading-freed", "http-request-logged", "out-of-buffers", "add-msg-failed", "rtsp-port-allocated", "rtsp-port-freed", "conn-tcp-create-failed", "ipv4-frag-applied", "ipv4-frag-failed", "ipv6-frag-applied", "ipv6-frag-failed"], "type": "string", "description": "'all': all; 'tcp-session-created': TCP Session Created; 'tcp-session-deleted': TCP Session Deleted; 'tcp-port-allocated': TCP Port Allocated; 'tcp-port-freed': TCP Port Freed; 'tcp-port-batch-allocated': TCP Port Batch Allocated; 'tcp-port-batch-freed': TCP Port Batch Freed; 'udp-session-created': UDP Session Created; 'udp-session-deleted': UDP Session Deleted; 'udp-port-allocated': UDP Port Allocated; 'udp-port-freed': UDP Port Freed; 'udp-port-batch-allocated': UDP Port Batch Allocated; 'udp-port-batch-freed': UDP Port Batch Freed; 'icmp-session-created': ICMP Session Created; 'icmp-session-deleted': ICMP Session Deleted; 'icmp-resource-allocated': ICMP Resource Allocated; 'icmp-resource-freed': ICMP Resource Freed; 'icmpv6-session-created': ICMPV6 Session Created; 'icmpv6-session-deleted': ICMPV6 Session Deleted; 'icmpv6-resource-allocated': ICMPV6 Resource Allocated; 'icmpv6-resource-freed': ICMPV6 Resource Freed; 'gre-session-created': GRE Session Created; 'gre-session-deleted': GRE Session Deleted; 'gre-resource-allocated': GRE Resource Allocated; 'gre-resource-freed': GRE Resource Freed; 'esp-session-created': ESP Session Created; 'esp-session-deleted': ESP Session Deleted; 'esp-resource-allocated': ESP Resource Allocated; 'esp-resource-freed': ESP Resource Freed; 'fixed-nat-user-ports': Fixed NAT Inside User Port Mapping; 'fixed-nat-disable-config-logged': Fixed NAT Periodic Configs Logged; 'fixed-nat-disable-config-logs-sent': Fixed NAT Periodic Config Logs Sent; 'fixed-nat-periodic-config-logs-sent': Fixed NAT Disabled Configs Logged; 'fixed-nat-periodic-config-logged': Fixed NAT Disabled Config Logs Sent; 'log-sent': Log Packets Sent; 'log-dropped': Log Packets Dropped; 'conn-tcp-established': TCP Connection Established; 'conn-tcp-dropped': TCP Connection Lost; 'tcp-port-overloading-allocated': TCP Port Overloading Allocated; 'tcp-port-overloading-freed': TCP Port Overloading Freed; 'udp-port-overloading-allocated': UDP Port Overloading Allocated; 'udp-port-overloading-freed': UDP Port Overloading Freed; 'http-request-logged': HTTP Request Logged; 'out-of-buffers': Out of Buffers; 'add-msg-failed': Add Message to Buffer Failed; 'rtsp-port-allocated': RTSP UDP Port Allocated; 'rtsp-port-freed': RTSP UDP Port Freed; 'conn-tcp-create-failed': TCP Connection Failed; 'ipv4-frag-applied': IPv4 Fragmentation Applied; 'ipv4-frag-failed': IPv4 Fragmentation Failed; 'ipv6-frag-applied': IPv6 Fragmentation Applied; 'ipv6-frag-failed': IPv6 Fragmentation Failed; ", "format": "enum"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    CGNV6 Logging Statistics.

    Class logging supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/logging`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "logging"
        self.a10_url="/axapi/v3/cgnv6/logging"
        self.DeviceProxy = ""
        self.sampling_enable = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


