from a10sdk.common.A10BaseClass import A10BaseClass


class SamplingEnable(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param counters1: {"enum": ["all", "curr_conn", "total_fwd_bytes", "total_fwd_pkts", "total_rev_bytes", "total_rev_pkts", "total_conn", "total_rev_pkts_inspected", "total_rev_pkts_inspected_status_code_2xx", "total_rev_pkts_inspected_status_code_non_5xx", "curr_req", "total_req", "total_req_succ", "peak_conn", "response_time", "fastest_rsp_time", "slowest_rsp_time"], "type": "string", "description": "'all': all; 'curr_conn': curr_conn; 'total_fwd_bytes': total_fwd_bytes; 'total_fwd_pkts': total_fwd_pkts; 'total_rev_bytes': total_rev_bytes; 'total_rev_pkts': total_rev_pkts; 'total_conn': total_conn; 'total_rev_pkts_inspected': total_rev_pkts_inspected; 'total_rev_pkts_inspected_status_code_2xx': total_rev_pkts_inspected_status_code_2xx; 'total_rev_pkts_inspected_status_code_non_5xx': total_rev_pkts_inspected_status_code_non_5xx; 'curr_req': curr_req; 'total_req': total_req; 'total_req_succ': total_req_succ; 'peak_conn': peak_conn; 'response_time': response_time; 'fastest_rsp_time': fastest_rsp_time; 'slowest_rsp_time': slowest_rsp_time; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "sampling-enable"
        self.DeviceProxy = ""
        self.counters1 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Member(A10BaseClass):
    
    """Class Description::
    Service Group Member.

    Class member supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param sampling_enable: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "curr_conn", "total_fwd_bytes", "total_fwd_pkts", "total_rev_bytes", "total_rev_pkts", "total_conn", "total_rev_pkts_inspected", "total_rev_pkts_inspected_status_code_2xx", "total_rev_pkts_inspected_status_code_non_5xx", "curr_req", "total_req", "total_req_succ", "peak_conn", "response_time", "fastest_rsp_time", "slowest_rsp_time"], "type": "string", "description": "'all': all; 'curr_conn': curr_conn; 'total_fwd_bytes': total_fwd_bytes; 'total_fwd_pkts': total_fwd_pkts; 'total_rev_bytes': total_rev_bytes; 'total_rev_pkts': total_rev_pkts; 'total_conn': total_conn; 'total_rev_pkts_inspected': total_rev_pkts_inspected; 'total_rev_pkts_inspected_status_code_2xx': total_rev_pkts_inspected_status_code_2xx; 'total_rev_pkts_inspected_status_code_non_5xx': total_rev_pkts_inspected_status_code_non_5xx; 'curr_req': curr_req; 'total_req': total_req; 'total_req_succ': total_req_succ; 'peak_conn': peak_conn; 'response_time': response_time; 'fastest_rsp_time': fastest_rsp_time; 'slowest_rsp_time': slowest_rsp_time; ", "format": "enum"}}}]}
    :param name: {"description": "Member name", "format": "comp-string", "minLength": 1, "optional": false, "maxLength": 127, "type": "string", "$ref": "/axapi/v3/cgnv6/server"}
    :param port: {"description": "Port number", "format": "number", "default": 65534, "optional": false, "maximum": 65534, "minimum": 0, "type": "number", "$ref": "/axapi/v3/cgnv6/server/port"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/service-group/{name}/member/{name}+{port}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name","port"]

        self.b_key = "member"
        self.a10_url="/axapi/v3/cgnv6/service-group/{name}/member/{name}+{port}"
        self.DeviceProxy = ""
        self.uuid = ""
        self.sampling_enable = []
        self.name = ""
        self.port = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


