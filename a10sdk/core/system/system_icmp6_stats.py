from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param out_echo_req: {"description": "Out Echo requests", "format": "counter", "type": "number", "oid": "22", "optional": true, "size": "2"}
    :param out_param_prob: {"description": "Out Parameter Problem", "format": "counter", "type": "number", "oid": "21", "optional": true, "size": "2"}
    :param out_pkt_too_big: {"description": "Out Packet too big", "format": "counter", "type": "number", "oid": "19", "optional": true, "size": "2"}
    :param out_na: {"description": "Out neighbor advertisement", "format": "counter", "type": "number", "oid": "27", "optional": true, "size": "2"}
    :param out_rs: {"description": "Out Router solicitation", "format": "counter", "type": "number", "oid": "24", "optional": true, "size": "2"}
    :param err_ns: {"description": "Error Neighbor solicitation", "format": "counter", "type": "number", "oid": "33", "optional": true, "size": "2"}
    :param in_redirect: {"description": "In Redirects", "format": "counter", "type": "number", "oid": "16", "optional": true, "size": "2"}
    :param in_echoes: {"description": "In Echo requests", "format": "counter", "type": "number", "oid": "7", "optional": true, "size": "2"}
    :param out_ns: {"description": "Out neighbor solicitation", "format": "counter", "type": "number", "oid": "26", "optional": true, "size": "2"}
    :param err_na: {"description": "Error Neighbor advertisement", "format": "counter", "type": "number", "oid": "34", "optional": true, "size": "2"}
    :param out_ra: {"description": "Out Router advertisement", "format": "counter", "type": "number", "oid": "25", "optional": true, "size": "2"}
    :param out_mem_reductions: {"description": "Out Group member reduction", "format": "counter", "type": "number", "oid": "30", "optional": true, "size": "2"}
    :param out_dst_un_reach: {"description": "Out Destination Unreachable", "format": "counter", "type": "number", "oid": "18", "optional": true, "size": "2"}
    :param in_msgs: {"description": "In messages", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "2"}
    :param in_param_prob: {"description": "In Parameter Problem", "format": "counter", "type": "number", "oid": "6", "optional": true, "size": "2"}
    :param in_pkt_too_big: {"description": "In Packet too big", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "2"}
    :param err_ra: {"description": "Error Router advertisement", "format": "counter", "type": "number", "oid": "32", "optional": true, "size": "2"}
    :param in_grp_mem_resp: {"description": "In Group member reply", "format": "counter", "type": "number", "oid": "10", "optional": true, "size": "2"}
    :param err_echoes: {"description": "Error Echo requests", "format": "counter", "type": "number", "oid": "36", "optional": true, "size": "2"}
    :param in_errors: {"description": "In Errors", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "2"}
    :param out_echo_replies: {"description": "Out Echo replies", "format": "counter", "type": "number", "oid": "23", "optional": true, "size": "2"}
    :param in_na: {"description": "In neighbor advertisement", "format": "counter", "type": "number", "oid": "15", "optional": true, "size": "2"}
    :param in_ra: {"description": "In Router advertisement", "format": "counter", "type": "number", "oid": "13", "optional": true, "size": "2"}
    :param err_rs: {"description": "Error Router solicitation", "format": "counter", "type": "number", "oid": "31", "optional": true, "size": "2"}
    :param err_redirects: {"description": "Error Redirects", "format": "counter", "type": "number", "oid": "35", "optional": true, "size": "2"}
    :param err_echo_replies: {"description": "Error Echo replies", "format": "counter", "type": "number", "oid": "37", "optional": true, "size": "2"}
    :param in_ns: {"description": "In neighbor solicitation", "format": "counter", "type": "number", "oid": "14", "optional": true, "size": "2"}
    :param out_msg: {"description": "Out Messages", "format": "counter", "type": "number", "oid": "17", "optional": true, "size": "2"}
    :param out_mem_resp: {"description": "Out Group member reply", "format": "counter", "type": "number", "oid": "29", "optional": true, "size": "2"}
    :param out_time_exceeds: {"description": "Out TTL Exceeds", "format": "counter", "type": "number", "oid": "20", "optional": true, "size": "2"}
    :param in_exho_reply: {"description": "In Echo replies", "format": "counter", "type": "number", "oid": "8", "optional": true, "size": "2"}
    :param in_router_sol: {"description": "In Router solicitation", "format": "counter", "type": "number", "oid": "12", "optional": true, "size": "2"}
    :param in_grp_mem_query: {"description": "In Group member query", "format": "counter", "type": "number", "oid": "9", "optional": true, "size": "2"}
    :param out_redirects: {"description": "Out Redirects", "format": "counter", "type": "number", "oid": "28", "optional": true, "size": "2"}
    :param in_time_exceeds: {"description": "In TTL Exceeds", "format": "counter", "type": "number", "oid": "5", "optional": true, "size": "2"}
    :param in_grp_mem_reduction: {"description": "In Group member reduction", "format": "counter", "type": "number", "oid": "11", "optional": true, "size": "2"}
    :param in_dest_un_reach: {"description": "In Destunation Unreachable", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "2"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.out_echo_req = ""
        self.out_param_prob = ""
        self.out_pkt_too_big = ""
        self.out_na = ""
        self.out_rs = ""
        self.err_ns = ""
        self.in_redirect = ""
        self.in_echoes = ""
        self.out_ns = ""
        self.err_na = ""
        self.out_ra = ""
        self.out_mem_reductions = ""
        self.out_dst_un_reach = ""
        self.in_msgs = ""
        self.in_param_prob = ""
        self.in_pkt_too_big = ""
        self.err_ra = ""
        self.in_grp_mem_resp = ""
        self.err_echoes = ""
        self.in_errors = ""
        self.out_echo_replies = ""
        self.in_na = ""
        self.in_ra = ""
        self.err_rs = ""
        self.err_redirects = ""
        self.err_echo_replies = ""
        self.in_ns = ""
        self.out_msg = ""
        self.out_mem_resp = ""
        self.out_time_exceeds = ""
        self.in_exho_reply = ""
        self.in_router_sol = ""
        self.in_grp_mem_query = ""
        self.out_redirects = ""
        self.in_time_exceeds = ""
        self.in_grp_mem_reduction = ""
        self.in_dest_un_reach = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Icmp6(A10BaseClass):
    
    """Class Description::
    Statistics for the object icmp6.

    Class icmp6 supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/system/icmp6/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "icmp6"
        self.a10_url="/axapi/v3/system/icmp6/stats"
        self.DeviceProxy = ""
        self.stats = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


