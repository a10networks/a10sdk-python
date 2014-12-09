from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param data_session_freed: {"description": "Data Session Freed", "format": "counter", "type": "number", "oid": "8", "optional": true, "size": "8"}
    :param port_overloading_smp_free_tcp: {"description": "TCP Port Overloading Session Freed", "format": "counter", "type": "number", "oid": "38", "optional": true, "size": "8"}
    :param total_udp_overloaded: {"description": "UDP Port Overloaded", "format": "counter", "type": "number", "oid": "35", "optional": true, "size": "8"}
    :param endpoint_indep_filter_match: {"description": "Endpoint-Independent Filtering Matched", "format": "counter", "type": "number", "oid": "30", "optional": true, "size": "8"}
    :param udp_fullcone_freed: {"description": "UDP Full-cone Session Freed", "format": "counter", "type": "number", "oid": "25", "optional": true, "size": "8"}
    :param nat_pool_unusable: {"description": "NAT Pool Unusable", "format": "counter", "type": "number", "oid": "40", "optional": true, "size": "8"}
    :param nat_port_unavailable_udp: {"description": "UDP NAT Port Unavailable", "format": "counter", "type": "number", "oid": "13", "optional": true, "size": "8"}
    :param lid_pass_through: {"description": "LSN LID Pass-through", "format": "counter", "type": "number", "oid": "45", "optional": true, "size": "8"}
    :param total_icmp_freed: {"description": "Total ICMP Ports Freed", "format": "counter", "type": "number", "oid": "6", "optional": true, "size": "8"}
    :param hairpin: {"description": "Hairpin Session Created", "format": "counter", "type": "number", "oid": "27", "optional": true, "size": "8"}
    :param tcp_fullcone_created: {"description": "TCP Full-cone Session Created", "format": "counter", "type": "number", "oid": "22", "optional": true, "size": "8"}
    :param nat_port_unavailable_icmp: {"description": "ICMP NAT Port Unavailable", "format": "counter", "type": "number", "oid": "14", "optional": true, "size": "8"}
    :param udp_fullcone_created: {"description": "UDP Full-cone Session Created", "format": "counter", "type": "number", "oid": "24", "optional": true, "size": "8"}
    :param extended_quota_matched: {"description": "Extended User-Quota Matched", "format": "counter", "type": "number", "oid": "19", "optional": true, "size": "8"}
    :param icmp_user_quota_exceeded: {"description": "ICMP User-Quota Exceeded", "format": "counter", "type": "number", "oid": "18", "optional": true, "size": "8"}
    :param ha_nat_pool_unusable: {"description": "HA NAT Pool Unusable", "format": "counter", "type": "number", "oid": "41", "optional": true, "size": "8"}
    :param port_overloading_smp_free_udp: {"description": "UDP Port Overloading Session Freed", "format": "counter", "type": "number", "oid": "39", "optional": true, "size": "8"}
    :param total_tcp_allocated: {"description": "Total TCP Ports Allocated", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}
    :param tcp_user_quota_exceeded: {"description": "TCP User-Quota Exceeded", "format": "counter", "type": "number", "oid": "16", "optional": true, "size": "8"}
    :param port_overloading_smp_inserted_tcp: {"description": "TCP Port Overloading Session Created", "format": "counter", "type": "number", "oid": "36", "optional": true, "size": "8"}
    :param eif_limit_exceeded: {"description": "Endpoint-Independent Filtering Inbound Limit Exceeded", "format": "counter", "type": "number", "oid": "32", "optional": true, "size": "8"}
    :param port_overloading_smp_inserted_udp: {"description": "UDP Port Overloading Session Created", "format": "counter", "type": "number", "oid": "37", "optional": true, "size": "8"}
    :param tcp_fullcone_freed: {"description": "TCP Full-cone Session Freed", "format": "counter", "type": "number", "oid": "23", "optional": true, "size": "8"}
    :param user_quota_failure: {"description": "User-Quota Creation Failed", "format": "counter", "type": "number", "oid": "11", "optional": true, "size": "8"}
    :param total_udp_freed: {"description": "Total UDP Ports Freed", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "8"}
    :param nat_port_unavailable_tcp: {"description": "TCP NAT Port Unavailable", "format": "counter", "type": "number", "oid": "12", "optional": true, "size": "8"}
    :param total_tcp_overloaded: {"description": "TCP Port Overloaded", "format": "counter", "type": "number", "oid": "34", "optional": true, "size": "8"}
    :param fullcone_failure: {"description": "Full-cone Session Creation Failed", "format": "counter", "type": "number", "oid": "26", "optional": true, "size": "8"}
    :param user_quota_created: {"description": "User-Quota Created", "format": "counter", "type": "number", "oid": "9", "optional": true, "size": "8"}
    :param data_sesn_user_quota_exceeded: {"description": "Data Session User-Quota Exceeded", "format": "counter", "type": "number", "oid": "21", "optional": true, "size": "8"}
    :param lid_drop: {"description": "LSN LID Drop", "format": "counter", "type": "number", "oid": "44", "optional": true, "size": "8"}
    :param truncated_packet: {"description": "Truncated Packet", "format": "counter", "type": "number", "oid": "43", "optional": true, "size": "8"}
    :param fullcone_self_hairpinning_drop: {"description": "Self-Hairpinning Drop", "format": "counter", "type": "number", "oid": "28", "optional": true, "size": "8"}
    :param nat_mismatch_drop: {"description": "NAT Pool Mismatch Drop", "format": "counter", "type": "number", "oid": "33", "optional": true, "size": "8"}
    :param class_list_permit_drop: {"description": "Permit Class-List Drop", "format": "counter", "type": "number", "oid": "47", "optional": true, "size": "8"}
    :param new_user_resource_unavailable: {"description": "New User NAT Resource Unavailable", "format": "counter", "type": "number", "oid": "15", "optional": true, "size": "8"}
    :param extended_quota_exceeded: {"description": "Extended User-Quota Exceeded", "format": "counter", "type": "number", "oid": "20", "optional": true, "size": "8"}
    :param total_udp_allocated: {"description": "Total UDP Ports Allocated", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "8"}
    :param data_session_created: {"description": "Data Session Created", "format": "counter", "type": "number", "oid": "7", "optional": true, "size": "8"}
    :param user_quota_put_in_del_q: {"description": "User-Quota Freed", "format": "counter", "type": "number", "oid": "10", "optional": true, "size": "8"}
    :param endpoint_indep_map_match: {"description": "Endpoint-Independent Mapping Matched", "format": "counter", "type": "number", "oid": "29", "optional": true, "size": "8"}
    :param udp_user_quota_exceeded: {"description": "UDP User-Quota Exceeded", "format": "counter", "type": "number", "oid": "17", "optional": true, "size": "8"}
    :param no_radius_profile_match: {"description": "No RADIUS Profile Match", "format": "counter", "type": "number", "oid": "42", "optional": true, "size": "8"}
    :param total_icmp_allocated: {"description": "Total ICMP Ports Allocated", "format": "counter", "type": "number", "oid": "5", "optional": true, "size": "8"}
    :param no_class_list_match: {"description": "No Class-List Match", "format": "counter", "type": "number", "oid": "46", "optional": true, "size": "8"}
    :param inbound_filtered: {"description": "Endpoint-Dependent Filtering Drop", "format": "counter", "type": "number", "oid": "31", "optional": true, "size": "8"}
    :param total_tcp_freed: {"description": "Total TCP Ports Freed", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "8"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.data_session_freed = ""
        self.port_overloading_smp_free_tcp = ""
        self.total_udp_overloaded = ""
        self.endpoint_indep_filter_match = ""
        self.udp_fullcone_freed = ""
        self.nat_pool_unusable = ""
        self.nat_port_unavailable_udp = ""
        self.lid_pass_through = ""
        self.total_icmp_freed = ""
        self.hairpin = ""
        self.tcp_fullcone_created = ""
        self.nat_port_unavailable_icmp = ""
        self.udp_fullcone_created = ""
        self.extended_quota_matched = ""
        self.icmp_user_quota_exceeded = ""
        self.ha_nat_pool_unusable = ""
        self.port_overloading_smp_free_udp = ""
        self.total_tcp_allocated = ""
        self.tcp_user_quota_exceeded = ""
        self.port_overloading_smp_inserted_tcp = ""
        self.eif_limit_exceeded = ""
        self.port_overloading_smp_inserted_udp = ""
        self.tcp_fullcone_freed = ""
        self.user_quota_failure = ""
        self.total_udp_freed = ""
        self.nat_port_unavailable_tcp = ""
        self.total_tcp_overloaded = ""
        self.fullcone_failure = ""
        self.user_quota_created = ""
        self.data_sesn_user_quota_exceeded = ""
        self.lid_drop = ""
        self.truncated_packet = ""
        self.fullcone_self_hairpinning_drop = ""
        self.nat_mismatch_drop = ""
        self.class_list_permit_drop = ""
        self.new_user_resource_unavailable = ""
        self.extended_quota_exceeded = ""
        self.total_udp_allocated = ""
        self.data_session_created = ""
        self.user_quota_put_in_del_q = ""
        self.endpoint_indep_map_match = ""
        self.udp_user_quota_exceeded = ""
        self.no_radius_profile_match = ""
        self.total_icmp_allocated = ""
        self.no_class_list_match = ""
        self.inbound_filtered = ""
        self.total_tcp_freed = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Global(A10BaseClass):
    
    """Class Description::
    Statistics for the object global.

    Class global supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/ds-lite/global/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "global"
        self.a10_url="/axapi/v3/cgnv6/ds-lite/global/stats"
        self.DeviceProxy = ""
        self.stats = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


