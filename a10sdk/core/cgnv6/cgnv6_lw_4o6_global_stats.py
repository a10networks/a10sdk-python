from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param interface_not_configured: {"description": "LW-4over6 Interfaces not Configured Drops", "format": "counter", "type": "number", "oid": "9", "optional": true, "size": "8"}
    :param no_match_icmp_sent: {"description": "No-Reverse-Match ICMP Sent", "format": "counter", "type": "number", "oid": "5", "optional": true, "size": "8"}
    :param self_hairpinning_drop: {"description": "Self-Hairpinning Drops", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "8"}
    :param entry_count: {"description": "Total Entries Configured", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}
    :param all_hairpinning_drop: {"description": "All Hairpinning Drops", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "8"}
    :param icmp_inbound_drop: {"description": "Inbound ICMP Drops", "format": "counter", "type": "number", "oid": "6", "optional": true, "size": "8"}
    :param fwd_lookup_failed: {"description": "Forward Route Lookup Failed", "format": "counter", "type": "number", "oid": "7", "optional": true, "size": "8"}
    :param no_match_icmpv6_sent: {"description": "No-Forward-Match ICMPv6 Sent", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "8"}
    :param rev_lookup_failed: {"description": "Reverse Route Lookup Failed", "format": "counter", "type": "number", "oid": "8", "optional": true, "size": "8"}
    :param no_tep_drop: {"description": "LW-4over6 Tunnel Endpoint not Configured Drops", "format": "counter", "type": "number", "oid": "10", "optional": true, "size": "8"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.interface_not_configured = ""
        self.no_match_icmp_sent = ""
        self.self_hairpinning_drop = ""
        self.entry_count = ""
        self.all_hairpinning_drop = ""
        self.icmp_inbound_drop = ""
        self.fwd_lookup_failed = ""
        self.no_match_icmpv6_sent = ""
        self.rev_lookup_failed = ""
        self.no_tep_drop = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Global(A10BaseClass):
    
    """Class Description::
    Statistics for the object global.

    Class global supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/lw-4o6/global/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "global"
        self.a10_url="/axapi/v3/cgnv6/lw-4o6/global/stats"
        self.DeviceProxy = ""
        self.stats = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


