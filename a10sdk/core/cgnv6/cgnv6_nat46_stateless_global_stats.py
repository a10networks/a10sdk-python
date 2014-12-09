from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param inbound_ipv6_fragment_received: {"description": "Inbound IPv6 fragment packets received", "format": "counter", "type": "number", "oid": "8", "optional": true, "size": "8"}
    :param inbound_ipv4_unreachable: {"description": "Inbound IPv4 destination unreachable", "format": "counter", "type": "number", "oid": "9", "optional": true, "size": "8"}
    :param icmp_to_icmpv6: {"description": "ICMP to ICMPv6", "format": "counter", "type": "number", "oid": "15", "optional": true, "size": "8"}
    :param outbound_ipv4_fragment_received: {"description": "Outbound IPv4 fragment packets received", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "8"}
    :param outbound_ipv4_received: {"description": "Outbound IPv4 packets received", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}
    :param outbound_ipv6_fragmented: {"description": "Outbound IPv6 packets fragmented", "format": "counter", "type": "number", "oid": "5", "optional": true, "size": "8"}
    :param ha_standby: {"description": "HA is standby", "format": "counter", "type": "number", "oid": "17", "optional": true, "size": "8"}
    :param packet_too_big: {"description": "Packet too big", "format": "counter", "type": "number", "oid": "11", "optional": true, "size": "8"}
    :param inbound_ipv6_received: {"description": "Inbound IPv6 packets received", "format": "counter", "type": "number", "oid": "6", "optional": true, "size": "8"}
    :param fragment_error: {"description": "Fragment processing errors", "format": "counter", "type": "number", "oid": "12", "optional": true, "size": "8"}
    :param inbound_ipv6_drop: {"description": "Inbound IPv6 packets dropped", "format": "counter", "type": "number", "oid": "7", "optional": true, "size": "8"}
    :param icmpv6_to_icmp: {"description": "ICMPv6 to ICMP", "format": "counter", "type": "number", "oid": "13", "optional": true, "size": "8"}
    :param outbound_ipv4_drop: {"description": "Outbound IPv4 packets dropped", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "8"}
    :param icmpv6_to_icmp_error: {"description": "ICMPv6 to ICMP errors", "format": "counter", "type": "number", "oid": "14", "optional": true, "size": "8"}
    :param inbound_ipv4_fragmented: {"description": "Inbound IPv4 packets fragmented", "format": "counter", "type": "number", "oid": "10", "optional": true, "size": "8"}
    :param outbound_ipv6_unreachable: {"description": "Outbound IPv6 destination unreachable", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "8"}
    :param other_error: {"description": "Other errors", "format": "counter", "type": "number", "oid": "18", "optional": true, "size": "8"}
    :param icmp_to_icmpv6_error: {"description": "ICMP to ICMPv6 errors", "format": "counter", "type": "number", "oid": "16", "optional": true, "size": "8"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.inbound_ipv6_fragment_received = ""
        self.inbound_ipv4_unreachable = ""
        self.icmp_to_icmpv6 = ""
        self.outbound_ipv4_fragment_received = ""
        self.outbound_ipv4_received = ""
        self.outbound_ipv6_fragmented = ""
        self.ha_standby = ""
        self.packet_too_big = ""
        self.inbound_ipv6_received = ""
        self.fragment_error = ""
        self.inbound_ipv6_drop = ""
        self.icmpv6_to_icmp = ""
        self.outbound_ipv4_drop = ""
        self.icmpv6_to_icmp_error = ""
        self.inbound_ipv4_fragmented = ""
        self.outbound_ipv6_unreachable = ""
        self.other_error = ""
        self.icmp_to_icmpv6_error = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Global(A10BaseClass):
    
    """Class Description::
    Statistics for the object global.

    Class global supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/nat46-stateless/global/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "global"
        self.a10_url="/axapi/v3/cgnv6/nat46-stateless/global/stats"
        self.DeviceProxy = ""
        self.stats = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


