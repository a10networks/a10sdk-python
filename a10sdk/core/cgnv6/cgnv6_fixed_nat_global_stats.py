from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param dslite_data_session_freed: {"description": "DS-Lite Data Sessions Freed", "format": "counter", "type": "number", "oid": "13", "optional": true, "size": "8"}
    :param nat64_eim_match: {"description": "NAT64 Endpoint-Independent-Mapping Matched", "format": "counter", "type": "number", "oid": "41", "optional": true, "size": "8"}
    :param total_icmp_freed: {"description": "Total ICMP Ports Freed", "format": "counter", "type": "number", "oid": "7", "optional": true, "size": "8"}
    :param nat64_udp_alg_fullcone_created: {"description": "NAT64 UDP ALG Full-Cone Created", "format": "counter", "type": "number", "oid": "31", "optional": true, "size": "8"}
    :param fullcone_failure: {"description": "Full-Cone Session Creation Failed", "format": "counter", "type": "number", "oid": "39", "optional": true, "size": "8"}
    :param nat44_eim_match: {"description": "NAT44 Endpoint-Independent-Mapping Matched", "format": "counter", "type": "number", "oid": "40", "optional": true, "size": "8"}
    :param nat44_tcp_fullcone_created: {"description": "NAT44 TCP Full-Cone Created", "format": "counter", "type": "number", "oid": "21", "optional": true, "size": "8"}
    :param nat44_eif_match: {"description": "NAT44 Endpoint-Independent-Filtering Matched", "format": "counter", "type": "number", "oid": "43", "optional": true, "size": "8"}
    :param nat64_data_session_created: {"description": "NAT64 Data Sessions Created", "format": "counter", "type": "number", "oid": "10", "optional": true, "size": "8"}
    :param nat64_eif_match: {"description": "NAT64 Endpoint-Independent-Filtering Matched", "format": "counter", "type": "number", "oid": "44", "optional": true, "size": "8"}
    :param nat44_hairpin: {"description": "NAT44 Hairpin Session Created", "format": "counter", "type": "number", "oid": "52", "optional": true, "size": "8"}
    :param total_icmp_allocated: {"description": "Total ICMP Ports Allocated", "format": "counter", "type": "number", "oid": "6", "optional": true, "size": "8"}
    :param nat64_udp_fullcone_freed: {"description": "NAT64 UDP Full-Cone Freed", "format": "counter", "type": "number", "oid": "30", "optional": true, "size": "8"}
    :param total_tcp_freed: {"description": "Total TCP Ports Freed", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "8"}
    :param dest_rlist_snat_drop: {"description": "Fixed NAT Dest Rules List Source NAT Drop", "format": "counter", "type": "number", "oid": "60", "optional": true, "size": "8"}
    :param nat44_udp_alg_fullcone_freed: {"description": "NAT44 UDP ALG Full-Cone Freed", "format": "counter", "type": "number", "oid": "26", "optional": true, "size": "8"}
    :param dslite_tcp_fullcone_freed: {"description": "DS-Lite TCP Full-Cone Freed", "format": "counter", "type": "number", "oid": "34", "optional": true, "size": "8"}
    :param 6rd_drop: {"description": "Fixed NAT IPv6 in IPv4 Packet Drop", "format": "counter", "type": "number", "oid": "57", "optional": true, "size": "8"}
    :param nat64_inbound_filtered: {"description": "NAT64 Endpoint-Dependent Filtering Drop", "format": "counter", "type": "number", "oid": "47", "optional": true, "size": "8"}
    :param dslite_hairpin: {"description": "DS-Lite Hairpin Session Created", "format": "counter", "type": "number", "oid": "54", "optional": true, "size": "8"}
    :param nat44_udp_alg_fullcone_created: {"description": "NAT44 UDP ALG Full-Cone Created", "format": "counter", "type": "number", "oid": "25", "optional": true, "size": "8"}
    :param nat_port_unavailable_udp: {"description": "UDP NAT Port Unavailable", "format": "counter", "type": "number", "oid": "15", "optional": true, "size": "8"}
    :param nat64_tcp_fullcone_created: {"description": "NAT64 TCP Full-Cone Created", "format": "counter", "type": "number", "oid": "27", "optional": true, "size": "8"}
    :param dest_rlist_pass_through: {"description": "Fixed NAT Dest Rule List Pass-Through", "format": "counter", "type": "number", "oid": "59", "optional": true, "size": "8"}
    :param nat64_tcp_fullcone_freed: {"description": "NAT64 TCP Full-Cone Freed", "format": "counter", "type": "number", "oid": "28", "optional": true, "size": "8"}
    :param dslite_udp_fullcone_created: {"description": "DS-Lite UDP Full-Cone Created", "format": "counter", "type": "number", "oid": "35", "optional": true, "size": "8"}
    :param total_udp_freed: {"description": "Total UDP Ports Freed", "format": "counter", "type": "number", "oid": "5", "optional": true, "size": "8"}
    :param nat44_eif_limit_exceeded: {"description": "NAT44 Endpoint-Independent-Filtering Limit Exceeded", "format": "counter", "type": "number", "oid": "49", "optional": true, "size": "8"}
    :param dslite_udp_alg_fullcone_created: {"description": "DS-Lite UDP ALG Full-Cone Created", "format": "counter", "type": "number", "oid": "37", "optional": true, "size": "8"}
    :param total_tcp_allocated: {"description": "Total TCP Ports Allocated", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "8"}
    :param nat64_udp_fullcone_created: {"description": "NAT64 UDP Full-Cone Created", "format": "counter", "type": "number", "oid": "29", "optional": true, "size": "8"}
    :param nat44_tcp_fullcone_freed: {"description": "NAT44 TCP Full-Cone Freed", "format": "counter", "type": "number", "oid": "22", "optional": true, "size": "8"}
    :param dslite_tcp_fullcone_created: {"description": "DS-Lite TCP Full-Cone Created", "format": "counter", "type": "number", "oid": "33", "optional": true, "size": "8"}
    :param dslite_inbound_filtered: {"description": "DS-Lite Endpoint-Dependent Filtering Drop", "format": "counter", "type": "number", "oid": "48", "optional": true, "size": "8"}
    :param nat44_udp_fullcone_created: {"description": "NAT44 UDP Full-Cone Created", "format": "counter", "type": "number", "oid": "23", "optional": true, "size": "8"}
    :param nat_port_unavailable_tcp: {"description": "TCP NAT Port Unavailable", "format": "counter", "type": "number", "oid": "14", "optional": true, "size": "8"}
    :param nat_port_unavailable_icmp: {"description": "ICMP NAT Port Unavailable", "format": "counter", "type": "number", "oid": "16", "optional": true, "size": "8"}
    :param nat44_data_session_created: {"description": "NAT44 Data Sessions Created", "format": "counter", "type": "number", "oid": "8", "optional": true, "size": "8"}
    :param nat44_inbound_filtered: {"description": "NAT44 Endpoint-Dependent Filtering Drop", "format": "counter", "type": "number", "oid": "46", "optional": true, "size": "8"}
    :param nat64_hairpin: {"description": "NAT64 Hairpin Session Created", "format": "counter", "type": "number", "oid": "53", "optional": true, "size": "8"}
    :param total_nat_in_use: {"description": "Total NAT Addresses in-use", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}
    :param dslite_data_session_created: {"description": "DS-Lite Data Sessions Created", "format": "counter", "type": "number", "oid": "12", "optional": true, "size": "8"}
    :param nat64_eif_limit_exceeded: {"description": "NAT64 Endpoint-Independent-Filtering Limit Exceeded", "format": "counter", "type": "number", "oid": "50", "optional": true, "size": "8"}
    :param nat64_data_session_freed: {"description": "NAT64 Data Sessions Freed", "format": "counter", "type": "number", "oid": "11", "optional": true, "size": "8"}
    :param standby_drop: {"description": "Fixed NAT LID Standby Drop", "format": "counter", "type": "number", "oid": "55", "optional": true, "size": "8"}
    :param dslite_udp_fullcone_freed: {"description": "DS-Lite UDP Full-Cone Freed", "format": "counter", "type": "number", "oid": "36", "optional": true, "size": "8"}
    :param fixed_nat_fullcone_self_hairpinning_drop: {"description": "Self-Hairpinning Drop", "format": "counter", "type": "number", "oid": "56", "optional": true, "size": "8"}
    :param dslite_eim_match: {"description": "DS-Lite Endpoint-Independent-Mapping Matched", "format": "counter", "type": "number", "oid": "42", "optional": true, "size": "8"}
    :param total_udp_allocated: {"description": "Total UDP Ports Allocated", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "8"}
    :param dslite_udp_alg_fullcone_freed: {"description": "DS-Lite UDP ALG Full-Cone Freed", "format": "counter", "type": "number", "oid": "38", "optional": true, "size": "8"}
    :param dest_rlist_drop: {"description": "Fixed NAT Dest Rule List Drop", "format": "counter", "type": "number", "oid": "58", "optional": true, "size": "8"}
    :param nat64_udp_alg_fullcone_freed: {"description": "NAT64 UDP ALG Full-Cone Freed", "format": "counter", "type": "number", "oid": "32", "optional": true, "size": "8"}
    :param session_user_quota_exceeded: {"description": "Sessions User Quota Exceeded", "format": "counter", "type": "number", "oid": "20", "optional": true, "size": "8"}
    :param dslite_eif_limit_exceeded: {"description": "DS-Lite Endpoint-Independent-Filtering Limit Exceeded", "format": "counter", "type": "number", "oid": "51", "optional": true, "size": "8"}
    :param dslite_eif_match: {"description": "DS-Lite Endpoint-Independent-Filtering Matched", "format": "counter", "type": "number", "oid": "45", "optional": true, "size": "8"}
    :param nat44_data_session_freed: {"description": "NAT44 Data Sessions Freed", "format": "counter", "type": "number", "oid": "9", "optional": true, "size": "8"}
    :param nat44_udp_fullcone_freed: {"description": "NAT44 UDP Full-Cone Freed", "format": "counter", "type": "number", "oid": "24", "optional": true, "size": "8"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.dslite_data_session_freed = ""
        self.nat64_eim_match = ""
        self.total_icmp_freed = ""
        self.nat64_udp_alg_fullcone_created = ""
        self.fullcone_failure = ""
        self.nat44_eim_match = ""
        self.nat44_tcp_fullcone_created = ""
        self.nat44_eif_match = ""
        self.nat64_data_session_created = ""
        self.nat64_eif_match = ""
        self.nat44_hairpin = ""
        self.total_icmp_allocated = ""
        self.nat64_udp_fullcone_freed = ""
        self.total_tcp_freed = ""
        self.dest_rlist_snat_drop = ""
        self.nat44_udp_alg_fullcone_freed = ""
        self.dslite_tcp_fullcone_freed = ""
        self.A10WW_6rd_drop = ""
        self.nat64_inbound_filtered = ""
        self.dslite_hairpin = ""
        self.nat44_udp_alg_fullcone_created = ""
        self.nat_port_unavailable_udp = ""
        self.nat64_tcp_fullcone_created = ""
        self.dest_rlist_pass_through = ""
        self.nat64_tcp_fullcone_freed = ""
        self.dslite_udp_fullcone_created = ""
        self.total_udp_freed = ""
        self.nat44_eif_limit_exceeded = ""
        self.dslite_udp_alg_fullcone_created = ""
        self.total_tcp_allocated = ""
        self.nat64_udp_fullcone_created = ""
        self.nat44_tcp_fullcone_freed = ""
        self.dslite_tcp_fullcone_created = ""
        self.dslite_inbound_filtered = ""
        self.nat44_udp_fullcone_created = ""
        self.nat_port_unavailable_tcp = ""
        self.nat_port_unavailable_icmp = ""
        self.nat44_data_session_created = ""
        self.nat44_inbound_filtered = ""
        self.nat64_hairpin = ""
        self.total_nat_in_use = ""
        self.dslite_data_session_created = ""
        self.nat64_eif_limit_exceeded = ""
        self.nat64_data_session_freed = ""
        self.standby_drop = ""
        self.dslite_udp_fullcone_freed = ""
        self.fixed_nat_fullcone_self_hairpinning_drop = ""
        self.dslite_eim_match = ""
        self.total_udp_allocated = ""
        self.dslite_udp_alg_fullcone_freed = ""
        self.dest_rlist_drop = ""
        self.nat64_udp_alg_fullcone_freed = ""
        self.session_user_quota_exceeded = ""
        self.dslite_eif_limit_exceeded = ""
        self.dslite_eif_match = ""
        self.nat44_data_session_freed = ""
        self.nat44_udp_fullcone_freed = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Global(A10BaseClass):
    
    """Class Description::
    Statistics for the object global.

    Class global supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/fixed-nat/global/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "global"
        self.a10_url="/axapi/v3/cgnv6/fixed-nat/global/stats"
        self.DeviceProxy = ""
        self.stats = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


