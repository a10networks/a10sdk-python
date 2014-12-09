from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param inbound_icmp_packets_received: {"description": "Inbound ICMP packets received", "format": "counter", "type": "number", "oid": "10", "optional": true, "size": "2"}
    :param outbound_tcp_packets_received: {"description": "Outbound TCP packets received", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "2"}
    :param outbound_icmp_packets_received: {"description": "Outbound ICMP packets received", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "2"}
    :param vport_matched: {"description": "Traffic match SLB virtual port", "format": "counter", "type": "number", "oid": "16", "optional": true, "size": "2"}
    :param inbound_ipv4_dest_unreachable: {"description": "Inbound IPv4 destination unreachable", "format": "counter", "type": "number", "oid": "13", "optional": true, "size": "2"}
    :param not_local_ip: {"description": "Not local IP", "format": "counter", "type": "number", "oid": "19", "optional": true, "size": "2"}
    :param inbound_packets_drop: {"description": "Inbound packets dropped", "format": "counter", "type": "number", "oid": "12", "optional": true, "size": "2"}
    :param inbound_fragment_ipv4: {"description": "Inbound Fragmented IPv4", "format": "counter", "type": "number", "oid": "14", "optional": true, "size": "2"}
    :param fragment_error: {"description": "Fragment processing errors", "format": "counter", "type": "number", "oid": "20", "optional": true, "size": "2"}
    :param outbound_packets_drop: {"description": "Outbound packets dropped", "format": "counter", "type": "number", "oid": "5", "optional": true, "size": "2"}
    :param outbound_fragment_ipv6: {"description": "Outbound Fragmented IPv6", "format": "counter", "type": "number", "oid": "7", "optional": true, "size": "2"}
    :param outbound_ipv6_dest_unreachable: {"description": "Outbound IPv6 destination unreachable", "format": "counter", "type": "number", "oid": "6", "optional": true, "size": "2"}
    :param inbound_tunnel_fragment_ipv6: {"description": "Inbound Fragmented IPv6 in tunnel", "format": "counter", "type": "number", "oid": "15", "optional": true, "size": "2"}
    :param other_error: {"description": "Other errors", "format": "counter", "type": "number", "oid": "21", "optional": true, "size": "2"}
    :param outbound_udp_packets_received: {"description": "Outbound UDP packets received", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "2"}
    :param inbound_other_packets_received: {"description": "Inbound other packets received", "format": "counter", "type": "number", "oid": "11", "optional": true, "size": "2"}
    :param inbound_udp_packets_received: {"description": "Inbound UDP packets received", "format": "counter", "type": "number", "oid": "9", "optional": true, "size": "2"}
    :param outbound_other_packets_received: {"description": "Outbound other packets received", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "2"}
    :param packet_too_big: {"description": "Packet too big", "format": "counter", "type": "number", "oid": "18", "optional": true, "size": "2"}
    :param inbound_tcp_packets_received: {"description": "Inbound TCP packets received", "format": "counter", "type": "number", "oid": "8", "optional": true, "size": "2"}
    :param unknown_delegated_prefix: {"description": "Unknown 6rd delegated prefix", "format": "counter", "type": "number", "oid": "17", "optional": true, "size": "2"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.inbound_icmp_packets_received = ""
        self.outbound_tcp_packets_received = ""
        self.outbound_icmp_packets_received = ""
        self.vport_matched = ""
        self.inbound_ipv4_dest_unreachable = ""
        self.not_local_ip = ""
        self.inbound_packets_drop = ""
        self.inbound_fragment_ipv4 = ""
        self.fragment_error = ""
        self.outbound_packets_drop = ""
        self.outbound_fragment_ipv6 = ""
        self.outbound_ipv6_dest_unreachable = ""
        self.inbound_tunnel_fragment_ipv6 = ""
        self.other_error = ""
        self.outbound_udp_packets_received = ""
        self.inbound_other_packets_received = ""
        self.inbound_udp_packets_received = ""
        self.outbound_other_packets_received = ""
        self.packet_too_big = ""
        self.inbound_tcp_packets_received = ""
        self.unknown_delegated_prefix = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Domain(A10BaseClass):
    
    """Class Description::
    Statistics for the object domain.

    Class domain supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param name: {"description": "6rd Domain name", "format": "string", "minLength": 1, "oid": "1001", "optional": false, "maxLength": 63, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/sixrd/domain/{name}/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "domain"
        self.a10_url="/axapi/v3/cgnv6/sixrd/domain/{name}/stats"
        self.DeviceProxy = ""
        self.stats = {}
        self.name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


