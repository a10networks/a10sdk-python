from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param no_rev_route: {"description": "No Reverse Route for Session", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "8"}
    :param tcp_rst_sent: {"description": "TCP RST Sent", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "8"}
    :param icmp_reply_no_session_drop: {"description": "ICMP Reply No Session Drop", "format": "counter", "type": "number", "oid": "8", "optional": true, "size": "8"}
    :param ipv6_src_invalid_unicast: {"description": "IPv6 Source Not Valid Unicast", "format": "counter", "type": "number", "oid": "12", "optional": true, "size": "8"}
    :param icmp_filtered_sent: {"description": "ICMP Administratively Filtered Sent", "format": "counter", "type": "number", "oid": "6", "optional": true, "size": "8"}
    :param ipv6_dst_invalid_unicast: {"description": "IPv6 Destination Not Valid Unicast", "format": "counter", "type": "number", "oid": "13", "optional": true, "size": "8"}
    :param ipip_icmp_reply_sent: {"description": "IPIP ICMP Echo Reply Sent", "format": "counter", "type": "number", "oid": "5", "optional": true, "size": "8"}
    :param ip_dst_invalid_unicast: {"description": "IPv4 Destination Not Valid Unicast", "format": "counter", "type": "number", "oid": "11", "optional": true, "size": "8"}
    :param no_fwd_route: {"description": "No Forward Route for Session", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}
    :param ip_src_invalid_unicast: {"description": "IPv4 Source Not Valid Unicast", "format": "counter", "type": "number", "oid": "10", "optional": true, "size": "8"}
    :param icmp_host_unreachable_sent: {"description": "ICMP Host Unreachable Sent", "format": "counter", "type": "number", "oid": "7", "optional": true, "size": "8"}
    :param out_of_session_memory: {"description": "Out of Session Memory", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "8"}
    :param ipip_truncated: {"description": "IPIP Truncated Packet", "format": "counter", "type": "number", "oid": "9", "optional": true, "size": "8"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.no_rev_route = ""
        self.tcp_rst_sent = ""
        self.icmp_reply_no_session_drop = ""
        self.ipv6_src_invalid_unicast = ""
        self.icmp_filtered_sent = ""
        self.ipv6_dst_invalid_unicast = ""
        self.ipip_icmp_reply_sent = ""
        self.ip_dst_invalid_unicast = ""
        self.no_fwd_route = ""
        self.ip_src_invalid_unicast = ""
        self.icmp_host_unreachable_sent = ""
        self.out_of_session_memory = ""
        self.ipip_truncated = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class L4(A10BaseClass):
    
    """Class Description::
    Statistics for the object l4.

    Class l4 supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/l4/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "l4"
        self.a10_url="/axapi/v3/cgnv6/l4/stats"
        self.DeviceProxy = ""
        self.stats = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


