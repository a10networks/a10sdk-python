from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param 64_known_drop: {"description": "NAT64 Forward Known ICMPv6 Drop", "format": "counter", "type": "number", "oid": "13", "optional": true, "size": "8"}
    :param 46_no_prefix_for_ipv4: {"description": "NAT64 Reverse No Prefix Match for IPv4", "format": "counter", "type": "number", "oid": "18", "optional": true, "size": "8"}
    :param icmp_bad_type: {"description": "Bad Embedded ICMP Type", "format": "counter", "type": "number", "oid": "11", "optional": true, "size": "8"}
    :param icmpv6_unknown_type: {"description": "ICMPv6 Unknown Type", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "8"}
    :param icmp_to_icmp: {"description": "ICMP to ICMP Conversion", "format": "counter", "type": "number", "oid": "7", "optional": true, "size": "8"}
    :param icmpv6_bad_type: {"description": "Bad Embedded ICMPv6 Type", "format": "counter", "type": "number", "oid": "12", "optional": true, "size": "8"}
    :param icmpv6_to_icmpv6: {"description": "ICMPv6 to ICMPv6 Conversion", "format": "counter", "type": "number", "oid": "10", "optional": true, "size": "8"}
    :param icmpv6_to_icmp: {"description": "ICMPv6 to ICMP Conversion", "format": "counter", "type": "number", "oid": "9", "optional": true, "size": "8"}
    :param icmp_no_session_drop: {"description": "ICMP No Matching Session Drop", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "8"}
    :param icmpv6_no_port_info: {"description": "ICMPv6 Port Info Not Included", "format": "counter", "type": "number", "oid": "5", "optional": true, "size": "8"}
    :param 64_unknown_drop: {"description": "NAT64 Forward Unknown ICMPv6 Drop", "format": "counter", "type": "number", "oid": "14", "optional": true, "size": "8"}
    :param 64_midpoint_hop: {"description": "NAT64 Forward Unknown Source Drop", "format": "counter", "type": "number", "oid": "15", "optional": true, "size": "8"}
    :param 46_unknown_drop: {"description": "NAT64 Reverse Known ICMPv6 Drop", "format": "counter", "type": "number", "oid": "17", "optional": true, "size": "8"}
    :param icmp_no_port_info: {"description": "ICMP Port Info Not Included", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "8"}
    :param icmpv6_no_session_drop: {"description": "ICMPv6 No Matching Session Drop", "format": "counter", "type": "number", "oid": "6", "optional": true, "size": "8"}
    :param 46_known_drop: {"description": "NAT64 Reverse Known ICMP Drop", "format": "counter", "type": "number", "oid": "16", "optional": true, "size": "8"}
    :param icmp_to_icmpv6: {"description": "ICMP to ICMPv6 Conversion", "format": "counter", "type": "number", "oid": "8", "optional": true, "size": "8"}
    :param icmp_unknown_type: {"description": "ICMP Unknown Type", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.A10WW_64_known_drop = ""
        self.A10WW_46_no_prefix_for_ipv4 = ""
        self.icmp_bad_type = ""
        self.icmpv6_unknown_type = ""
        self.icmp_to_icmp = ""
        self.icmpv6_bad_type = ""
        self.icmpv6_to_icmpv6 = ""
        self.icmpv6_to_icmp = ""
        self.icmp_no_session_drop = ""
        self.icmpv6_no_port_info = ""
        self.A10WW_64_unknown_drop = ""
        self.A10WW_64_midpoint_hop = ""
        self.A10WW_46_unknown_drop = ""
        self.icmp_no_port_info = ""
        self.icmpv6_no_session_drop = ""
        self.A10WW_46_known_drop = ""
        self.icmp_to_icmpv6 = ""
        self.icmp_unknown_type = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Icmp(A10BaseClass):
    
    """Class Description::
    Statistics for the object icmp.

    Class icmp supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/icmp/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "icmp"
        self.a10_url="/axapi/v3/cgnv6/icmp/stats"
        self.DeviceProxy = ""
        self.stats = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


