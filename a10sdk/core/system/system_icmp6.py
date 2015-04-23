from a10sdk.common.A10BaseClass import A10BaseClass


class SamplingEnable(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param counters1: {"enum": ["all", "in_msgs", "in_errors", "in_dest_un_reach", "in_pkt_too_big", "in_time_exceeds", "in_param_prob", "in_echoes", "in_exho_reply", "in_grp_mem_query", "in_grp_mem_resp", "in_grp_mem_reduction", "in_router_sol", "in_ra", "in_ns", "in_na", "in_redirect", "out_msg", "out_dst_un_reach", "out_pkt_too_big", "out_time_exceeds", "out_param_prob", "out_echo_req", "out_echo_replies", "out_rs", "out_ra", "out_ns", "out_na", "out_redirects", "out_mem_resp", "out_mem_reductions", "err_rs", "err_ra", "err_ns", "err_na", "err_redirects", "err_echoes", "err_echo_replies"], "type": "string", "description": "'all': all; 'in_msgs': In messages; 'in_errors': In Errors; 'in_dest_un_reach': In Destunation Unreachable; 'in_pkt_too_big': In Packet too big; 'in_time_exceeds': In TTL Exceeds; 'in_param_prob': In Parameter Problem; 'in_echoes': In Echo requests; 'in_exho_reply': In Echo replies; 'in_grp_mem_query': In Group member query; 'in_grp_mem_resp': In Group member reply; 'in_grp_mem_reduction': In Group member reduction; 'in_router_sol': In Router solicitation; 'in_ra': In Router advertisement; 'in_ns': In neighbor solicitation; 'in_na': In neighbor advertisement; 'in_redirect': In Redirects; 'out_msg': Out Messages; 'out_dst_un_reach': Out Destination Unreachable; 'out_pkt_too_big': Out Packet too big; 'out_time_exceeds': Out TTL Exceeds; 'out_param_prob': Out Parameter Problem; 'out_echo_req': Out Echo requests; 'out_echo_replies': Out Echo replies; 'out_rs': Out Router solicitation; 'out_ra': Out Router advertisement; 'out_ns': Out neighbor solicitation; 'out_na': Out neighbor advertisement; 'out_redirects': Out Redirects; 'out_mem_resp': Out Group member reply; 'out_mem_reductions': Out Group member reduction; 'err_rs': Error Router solicitation; 'err_ra': Error Router advertisement; 'err_ns': Error Neighbor solicitation; 'err_na': Error Neighbor advertisement; 'err_redirects': Error Redirects; 'err_echoes': Error Echo requests; 'err_echo_replies': Error Echo replies; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "sampling-enable"
        self.DeviceProxy = ""
        self.counters1 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Icmp6(A10BaseClass):
    
    """    :param sampling_enable: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "in_msgs", "in_errors", "in_dest_un_reach", "in_pkt_too_big", "in_time_exceeds", "in_param_prob", "in_echoes", "in_exho_reply", "in_grp_mem_query", "in_grp_mem_resp", "in_grp_mem_reduction", "in_router_sol", "in_ra", "in_ns", "in_na", "in_redirect", "out_msg", "out_dst_un_reach", "out_pkt_too_big", "out_time_exceeds", "out_param_prob", "out_echo_req", "out_echo_replies", "out_rs", "out_ra", "out_ns", "out_na", "out_redirects", "out_mem_resp", "out_mem_reductions", "err_rs", "err_ra", "err_ns", "err_na", "err_redirects", "err_echoes", "err_echo_replies"], "type": "string", "description": "'all': all; 'in_msgs': In messages; 'in_errors': In Errors; 'in_dest_un_reach': In Destunation Unreachable; 'in_pkt_too_big': In Packet too big; 'in_time_exceeds': In TTL Exceeds; 'in_param_prob': In Parameter Problem; 'in_echoes': In Echo requests; 'in_exho_reply': In Echo replies; 'in_grp_mem_query': In Group member query; 'in_grp_mem_resp': In Group member reply; 'in_grp_mem_reduction': In Group member reduction; 'in_router_sol': In Router solicitation; 'in_ra': In Router advertisement; 'in_ns': In neighbor solicitation; 'in_na': In neighbor advertisement; 'in_redirect': In Redirects; 'out_msg': Out Messages; 'out_dst_un_reach': Out Destination Unreachable; 'out_pkt_too_big': Out Packet too big; 'out_time_exceeds': Out TTL Exceeds; 'out_param_prob': Out Parameter Problem; 'out_echo_req': Out Echo requests; 'out_echo_replies': Out Echo replies; 'out_rs': Out Router solicitation; 'out_ra': Out Router advertisement; 'out_ns': Out neighbor solicitation; 'out_na': Out neighbor advertisement; 'out_redirects': Out Redirects; 'out_mem_resp': Out Group member reply; 'out_mem_reductions': Out Group member reduction; 'err_rs': Error Router solicitation; 'err_ra': Error Router advertisement; 'err_ns': Error Neighbor solicitation; 'err_na': Error Neighbor advertisement; 'err_redirects': Error Redirects; 'err_echoes': Error Echo requests; 'err_echo_replies': Error Echo replies; ", "format": "enum"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Display ICMPv6 statistics.

    Class icmp6 supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/system/icmp6`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "icmp6"
        self.a10_url="/axapi/v3/system/icmp6"
        self.DeviceProxy = ""
        self.sampling_enable = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


