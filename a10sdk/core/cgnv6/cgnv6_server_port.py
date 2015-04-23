from a10sdk.common.A10BaseClass import A10BaseClass


class SamplingEnable(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param counters1: {"enum": ["all", "curr_conn", "curr_req", "total_req", "total_req_succ", "total_fwd_bytes", "total_fwd_pkts", "total_rev_bytes", "total_rev_pkts", "total_conn", "last_total_conn", "peak_conn", "es_resp_200", "es_resp_300", "es_resp_400", "es_resp_500", "es_resp_other", "es_req_count", "es_resp_count", "es_resp_invalid_http", "total_rev_pkts_inspected", "total_rev_pkts_inspected_good_status_code", "response_time", "fastest_rsp_time", "slowest_rsp_time"], "type": "string", "description": "'all': all; 'curr_conn': curr_conn; 'curr_req': curr_req; 'total_req': total_req; 'total_req_succ': total_req_succ; 'total_fwd_bytes': total_fwd_bytes; 'total_fwd_pkts': total_fwd_pkts; 'total_rev_bytes': total_rev_bytes; 'total_rev_pkts': total_rev_pkts; 'total_conn': total_conn; 'last_total_conn': last_total_conn; 'peak_conn': peak_conn; 'es_resp_200': es_resp_200; 'es_resp_300': es_resp_300; 'es_resp_400': es_resp_400; 'es_resp_500': es_resp_500; 'es_resp_other': es_resp_other; 'es_req_count': es_req_count; 'es_resp_count': es_resp_count; 'es_resp_invalid_http': es_resp_invalid_http; 'total_rev_pkts_inspected': total_rev_pkts_inspected; 'total_rev_pkts_inspected_good_status_code': total_rev_pkts_inspected_good_status_code; 'response_time': response_time; 'fastest_rsp_time': fastest_rsp_time; 'slowest_rsp_time': slowest_rsp_time; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "sampling-enable"
        self.DeviceProxy = ""
        self.counters1 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Port(A10BaseClass):
    
    """Class Description::
    Real Server Port.

    Class port supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param health_check_disable: {"description": "Disable health check", "format": "flag", "default": 0, "optional": true, "not": "health-check", "type": "number"}
    :param protocol: {"optional": false, "enum": ["tcp", "udp"], "type": "string", "description": "'tcp': TCP Port; 'udp': UDP Port; ", "format": "enum"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param port_number: {"description": "Port Number", "format": "number", "type": "number", "maximum": 65534, "minimum": 0, "optional": false}
    :param sampling_enable: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "curr_conn", "curr_req", "total_req", "total_req_succ", "total_fwd_bytes", "total_fwd_pkts", "total_rev_bytes", "total_rev_pkts", "total_conn", "last_total_conn", "peak_conn", "es_resp_200", "es_resp_300", "es_resp_400", "es_resp_500", "es_resp_other", "es_req_count", "es_resp_count", "es_resp_invalid_http", "total_rev_pkts_inspected", "total_rev_pkts_inspected_good_status_code", "response_time", "fastest_rsp_time", "slowest_rsp_time"], "type": "string", "description": "'all': all; 'curr_conn': curr_conn; 'curr_req': curr_req; 'total_req': total_req; 'total_req_succ': total_req_succ; 'total_fwd_bytes': total_fwd_bytes; 'total_fwd_pkts': total_fwd_pkts; 'total_rev_bytes': total_rev_bytes; 'total_rev_pkts': total_rev_pkts; 'total_conn': total_conn; 'last_total_conn': last_total_conn; 'peak_conn': peak_conn; 'es_resp_200': es_resp_200; 'es_resp_300': es_resp_300; 'es_resp_400': es_resp_400; 'es_resp_500': es_resp_500; 'es_resp_other': es_resp_other; 'es_req_count': es_req_count; 'es_resp_count': es_resp_count; 'es_resp_invalid_http': es_resp_invalid_http; 'total_rev_pkts_inspected': total_rev_pkts_inspected; 'total_rev_pkts_inspected_good_status_code': total_rev_pkts_inspected_good_status_code; 'response_time': response_time; 'fastest_rsp_time': fastest_rsp_time; 'slowest_rsp_time': slowest_rsp_time; ", "format": "enum"}}}]}
    :param action: {"description": "'enable': enable; 'disable': disable; ", "format": "enum", "default": "enable", "type": "string", "enum": ["enable", "disable"], "optional": true}
    :param health_check: {"description": "Health Check (Monitor Name)", "format": "string", "minLength": 1, "optional": true, "maxLength": 31, "not": "health-check-disable", "type": "string", "$ref": "/axapi/v3/health/monitor"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/server/{name}/port/{port_number}+{protocol}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "port_number","protocol"]

        self.b_key = "port"
        self.a10_url="/axapi/v3/cgnv6/server/{name}/port/{port_number}+{protocol}"
        self.DeviceProxy = ""
        self.health_check_disable = ""
        self.protocol = ""
        self.uuid = ""
        self.port_number = ""
        self.sampling_enable = []
        self.action = ""
        self.health_check = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


