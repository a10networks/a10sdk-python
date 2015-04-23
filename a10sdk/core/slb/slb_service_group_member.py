from a10sdk.common.A10BaseClass import A10BaseClass


class SamplingEnable(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param counters1: {"enum": ["all", "curr_conn", "total_fwd_bytes", "total_fwd_pkts", "total_rev_bytes", "total_rev_pkts", "total_conn", "total_rev_pkts_inspected", "total_rev_pkts_inspected_status_code_2xx", "total_rev_pkts_inspected_status_code_non_5xx", "curr_req", "total_req", "total_req_succ", "peak_conn", "response_time", "fastest_rsp_time", "slowest_rsp_time"], "type": "string", "description": "'all': all; 'curr_conn': Current connections; 'total_fwd_bytes': Total forward bytes; 'total_fwd_pkts': Total forward packets; 'total_rev_bytes': Total reverse bytes; 'total_rev_pkts': Total reverse packets; 'total_conn': Total connections; 'total_rev_pkts_inspected': Total reverse packets inspected; 'total_rev_pkts_inspected_status_code_2xx': Total reverse packets inspected status code 2xx; 'total_rev_pkts_inspected_status_code_non_5xx': Total reverse packets inspected status code non 5xx; 'curr_req': Current requests; 'total_req': Total requests; 'total_req_succ': Total requests successful; 'peak_conn': Peak connections; 'response_time': Response time; 'fastest_rsp_time': Fastest response time; 'slowest_rsp_time': Slowest response time; ", "format": "enum"}
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

    :param member_priority: {"description": "Priority of Port in the Group (Priority of Port in the Group, default is 1)", "format": "number", "default": 1, "optional": true, "maximum": 16, "minimum": 1, "type": "number"}
    :param name: {"description": "Member name", "format": "comp-string", "minLength": 1, "optional": false, "maxLength": 127, "type": "string", "$ref": "/axapi/v3/slb/server"}
    :param fqdn_name: {"description": "Server hostname - Not applicable if real server is already defined", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param member_template: {"description": "Real server port template (Real server port template name)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/slb/template/port"}
    :param host: {"optional": true, "type": "string", "description": "IP Address - Not applicable if real server is already defined", "format": "ipv4-address"}
    :param sampling_enable: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "curr_conn", "total_fwd_bytes", "total_fwd_pkts", "total_rev_bytes", "total_rev_pkts", "total_conn", "total_rev_pkts_inspected", "total_rev_pkts_inspected_status_code_2xx", "total_rev_pkts_inspected_status_code_non_5xx", "curr_req", "total_req", "total_req_succ", "peak_conn", "response_time", "fastest_rsp_time", "slowest_rsp_time"], "type": "string", "description": "'all': all; 'curr_conn': Current connections; 'total_fwd_bytes': Total forward bytes; 'total_fwd_pkts': Total forward packets; 'total_rev_bytes': Total reverse bytes; 'total_rev_pkts': Total reverse packets; 'total_conn': Total connections; 'total_rev_pkts_inspected': Total reverse packets inspected; 'total_rev_pkts_inspected_status_code_2xx': Total reverse packets inspected status code 2xx; 'total_rev_pkts_inspected_status_code_non_5xx': Total reverse packets inspected status code non 5xx; 'curr_req': Current requests; 'total_req': Total requests; 'total_req_succ': Total requests successful; 'peak_conn': Peak connections; 'response_time': Response time; 'fastest_rsp_time': Fastest response time; 'slowest_rsp_time': Slowest response time; ", "format": "enum"}}}]}
    :param member_state: {"description": "'enable': Enable member service port; 'disable': Disable member service port; 'disable-with-health-check': disable member service port, but health check work; ", "format": "enum", "default": "enable", "type": "string", "enum": ["enable", "disable", "disable-with-health-check"], "optional": true}
    :param server_ipv6_addr: {"optional": true, "type": "string", "description": "IPV6 Address - Not applicable if real server is already defined", "format": "ipv6-address"}
    :param port: {"description": "Port number", "format": "number", "default": 65534, "optional": false, "maximum": 65534, "minimum": 0, "type": "number", "$ref": "/axapi/v3/slb/server/port"}
    :param member_stats_data_disable: {"default": 0, "optional": true, "type": "number", "description": "Disable statistical data collection", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/service-group/{name}/member/{name}+{port}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name","port"]

        self.b_key = "member"
        self.a10_url="/axapi/v3/slb/service-group/{name}/member/{name}+{port}"
        self.DeviceProxy = ""
        self.member_priority = ""
        self.name = ""
        self.fqdn_name = ""
        self.uuid = ""
        self.member_template = ""
        self.host = ""
        self.sampling_enable = []
        self.member_state = ""
        self.server_ipv6_addr = ""
        self.port = ""
        self.member_stats_data_disable = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


