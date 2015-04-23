from a10sdk.common.A10BaseClass import A10BaseClass


class SamplingEnable(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param counters1: {"enum": ["all", "session_created", "session_freed", "response_checked", "rrs_replaced", "session_created_shadow", "session_freed_shadow", "udp_received", "tcp_received", "query_flagged_as_response", "query_non_query_opcode", "query_rcode_error", "query_truncated", "query_no_questions", "query_checked", "query_questions_ptr_replaced", "query_questions_not_replaced", "query_questions_truncated", "query_questions_error", "response_flagged_as_query", "response_non_query_opcode", "response_rcode_error", "response_truncated", "response_no_rrs_to_check", "response_checked_shadow", "response_questions_truncated", "response_questions_error", "rr_name_truncated", "response_clist_exclude", "rrs_replaced_shadow", "rrs_not_replaced", "rrs_truncated", "tcp_truncated_dropped", "tcp_ofo_dropped", "tcp_ofm_dropped", "tcp_queue_resent", "tcp_queue_full_dropped", "rdata_too_fragmented", "rdata_too_big", "rdata_len_ipv4_incorrect", "parse_list_questions_error", "parse_list_answers_error", "parse_list_authorities_error", "parse_list_additional_error"], "type": "string", "description": "'all': all; 'session_created': Session Created; 'session_freed': Session Freed; 'response_checked': Response Checked; 'rrs_replaced': Resource Records Replaced; 'session_created_shadow': Session Created Shadow; 'session_freed_shadow': Session Freed Shadow; 'udp_received': UDP Received; 'tcp_received': TCP Received; 'query_flagged_as_response': Query Response Flagged; 'query_non_query_opcode': Query Non-Query Opcode; 'query_rcode_error': Query Rcode Error; 'query_truncated': Query Truncated; 'query_no_questions': Query No Questions; 'query_checked': Query Checked; 'query_questions_ptr_replaced': Query PTR Question Replaced; 'query_questions_not_replaced': Query Question Not Replaced; 'query_questions_truncated': Query Questions Truncated; 'query_questions_error': Query Questions Error; 'response_flagged_as_query': Response From Client; 'response_non_query_opcode': Response Non-Query Opcode; 'response_rcode_error': Response Rcode Error; 'response_truncated': Truncate Flagged Response; 'response_no_rrs_to_check': No RRs to Check; 'response_checked_shadow': Response Checked Shadow; 'response_questions_truncated': Response Questions Truncated; 'response_questions_error': Response Questions Error; 'rr_name_truncated': RR Name Truncated; 'response_clist_exclude': Response Excluded By Class-List; 'rrs_replaced_shadow': Resource Records Replaced Shadow; 'rrs_not_replaced': RRs Not Replaced; 'rrs_truncated': RRs Truncated; 'tcp_truncated_dropped': TCP Truncated Dropped; 'tcp_ofo_dropped': TCP Out-of-order Dropped; 'tcp_ofm_dropped': TCP Out-of-memory Dropped; 'tcp_queue_resent': TCP Resent from Queue; 'tcp_queue_full_dropped': TCP Queue Full Dropped; 'rdata_too_fragmented': Rdata Too Fragmented; 'rdata_too_big': Rdata Too Big; 'rdata_len_ipv4_incorrect': Rdata IPv4 Length Incorrect; 'parse_list_questions_error': Parse Questions Error; 'parse_list_answers_error': Parse Answers Error; 'parse_list_authorities_error': Parse Authorities Error; 'parse_list_additional_error': Parse Additional Error; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "sampling-enable"
        self.DeviceProxy = ""
        self.counters1 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class DnsAlg(A10BaseClass):
    
    """    :param sampling_enable: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "session_created", "session_freed", "response_checked", "rrs_replaced", "session_created_shadow", "session_freed_shadow", "udp_received", "tcp_received", "query_flagged_as_response", "query_non_query_opcode", "query_rcode_error", "query_truncated", "query_no_questions", "query_checked", "query_questions_ptr_replaced", "query_questions_not_replaced", "query_questions_truncated", "query_questions_error", "response_flagged_as_query", "response_non_query_opcode", "response_rcode_error", "response_truncated", "response_no_rrs_to_check", "response_checked_shadow", "response_questions_truncated", "response_questions_error", "rr_name_truncated", "response_clist_exclude", "rrs_replaced_shadow", "rrs_not_replaced", "rrs_truncated", "tcp_truncated_dropped", "tcp_ofo_dropped", "tcp_ofm_dropped", "tcp_queue_resent", "tcp_queue_full_dropped", "rdata_too_fragmented", "rdata_too_big", "rdata_len_ipv4_incorrect", "parse_list_questions_error", "parse_list_answers_error", "parse_list_authorities_error", "parse_list_additional_error"], "type": "string", "description": "'all': all; 'session_created': Session Created; 'session_freed': Session Freed; 'response_checked': Response Checked; 'rrs_replaced': Resource Records Replaced; 'session_created_shadow': Session Created Shadow; 'session_freed_shadow': Session Freed Shadow; 'udp_received': UDP Received; 'tcp_received': TCP Received; 'query_flagged_as_response': Query Response Flagged; 'query_non_query_opcode': Query Non-Query Opcode; 'query_rcode_error': Query Rcode Error; 'query_truncated': Query Truncated; 'query_no_questions': Query No Questions; 'query_checked': Query Checked; 'query_questions_ptr_replaced': Query PTR Question Replaced; 'query_questions_not_replaced': Query Question Not Replaced; 'query_questions_truncated': Query Questions Truncated; 'query_questions_error': Query Questions Error; 'response_flagged_as_query': Response From Client; 'response_non_query_opcode': Response Non-Query Opcode; 'response_rcode_error': Response Rcode Error; 'response_truncated': Truncate Flagged Response; 'response_no_rrs_to_check': No RRs to Check; 'response_checked_shadow': Response Checked Shadow; 'response_questions_truncated': Response Questions Truncated; 'response_questions_error': Response Questions Error; 'rr_name_truncated': RR Name Truncated; 'response_clist_exclude': Response Excluded By Class-List; 'rrs_replaced_shadow': Resource Records Replaced Shadow; 'rrs_not_replaced': RRs Not Replaced; 'rrs_truncated': RRs Truncated; 'tcp_truncated_dropped': TCP Truncated Dropped; 'tcp_ofo_dropped': TCP Out-of-order Dropped; 'tcp_ofm_dropped': TCP Out-of-memory Dropped; 'tcp_queue_resent': TCP Resent from Queue; 'tcp_queue_full_dropped': TCP Queue Full Dropped; 'rdata_too_fragmented': Rdata Too Fragmented; 'rdata_too_big': Rdata Too Big; 'rdata_len_ipv4_incorrect': Rdata IPv4 Length Incorrect; 'parse_list_questions_error': Parse Questions Error; 'parse_list_answers_error': Parse Answers Error; 'parse_list_authorities_error': Parse Authorities Error; 'parse_list_additional_error': Parse Additional Error; ", "format": "enum"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Configure DNS-ALG.

    Class dns-alg supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/dns-alg`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "dns-alg"
        self.a10_url="/axapi/v3/cgnv6/dns-alg"
        self.DeviceProxy = ""
        self.sampling_enable = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


