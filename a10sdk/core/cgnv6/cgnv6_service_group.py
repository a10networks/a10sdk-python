from a10sdk.common.A10BaseClass import A10BaseClass


class SamplingEnable(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param counters1: {"enum": ["all", "server_selection_fail_drop", "server_selection_fail_reset", "service_peak_conn"], "type": "string", "description": "'all': all; 'server_selection_fail_drop': server_selection_fail_drop; 'server_selection_fail_reset': server_selection_fail_reset; 'service_peak_conn': service_peak_conn; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "sampling-enable"
        self.DeviceProxy = ""
        self.counters1 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class ServiceGroup(A10BaseClass):
    
    """Class Description::
    Service Group.

    Class service-group supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param shared_partition: {"description": "Share with a single partition (Partition Name)", "partition-visibility": "shared", "minLength": 1, "format": "string", "optional": true, "maxLength": 14, "not": "shared-group", "type": "string"}
    :param protocol: {"description": "'tcp': TCP LB service; 'udp': UDP LB service; ", "format": "enum", "type": "string", "enum": ["tcp", "udp"], "modify-not-allowed": 1, "optional": true}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param health_check: {"description": "Health Check (Monitor Name)", "format": "string", "minLength": 1, "optional": true, "maxLength": 31, "type": "string", "$ref": "/axapi/v3/health/monitor"}
    :param sampling_enable: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "server_selection_fail_drop", "server_selection_fail_reset", "service_peak_conn"], "type": "string", "description": "'all': all; 'server_selection_fail_drop': server_selection_fail_drop; 'server_selection_fail_reset': server_selection_fail_reset; 'service_peak_conn': service_peak_conn; ", "format": "enum"}}}]}
    :param member_list: {"minItems": 1, "items": {"type": "member"}, "uniqueItems": true, "array": [{"required": ["name", "port"], "properties": {"uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}, "sampling-enable": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "curr_conn", "total_fwd_bytes", "total_fwd_pkts", "total_rev_bytes", "total_rev_pkts", "total_conn", "total_rev_pkts_inspected", "total_rev_pkts_inspected_status_code_2xx", "total_rev_pkts_inspected_status_code_non_5xx", "curr_req", "total_req", "total_req_succ", "peak_conn", "response_time", "fastest_rsp_time", "slowest_rsp_time"], "type": "string", "description": "'all': all; 'curr_conn': curr_conn; 'total_fwd_bytes': total_fwd_bytes; 'total_fwd_pkts': total_fwd_pkts; 'total_rev_bytes': total_rev_bytes; 'total_rev_pkts': total_rev_pkts; 'total_conn': total_conn; 'total_rev_pkts_inspected': total_rev_pkts_inspected; 'total_rev_pkts_inspected_status_code_2xx': total_rev_pkts_inspected_status_code_2xx; 'total_rev_pkts_inspected_status_code_non_5xx': total_rev_pkts_inspected_status_code_non_5xx; 'curr_req': curr_req; 'total_req': total_req; 'total_req_succ': total_req_succ; 'peak_conn': peak_conn; 'response_time': response_time; 'fastest_rsp_time': fastest_rsp_time; 'slowest_rsp_time': slowest_rsp_time; ", "format": "enum"}}}]}, "name": {"description": "Member name", "format": "comp-string", "minLength": 1, "optional": false, "maxLength": 127, "type": "string", "$ref": "/axapi/v3/cgnv6/server"}, "port": {"description": "Port number", "format": "number", "default": 65534, "optional": false, "maximum": 65534, "minimum": 0, "type": "number", "$ref": "/axapi/v3/cgnv6/server/port"}}}], "type": "array", "$ref": "/axapi/v3/cgnv6/service-group/{name}/member/{name}+{port}"}
    :param shared_group: {"description": "Share with a partition group (Partition Group Name)", "partition-visibility": "shared", "minLength": 1, "format": "string", "optional": true, "maxLength": 63, "not": "shared-partition", "type": "string"}
    :param name: {"description": "CGNV6 Service Name", "format": "string-rlx", "minLength": 1, "optional": false, "maxLength": 127, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/service-group/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "service-group"
        self.a10_url="/axapi/v3/cgnv6/service-group/{name}"
        self.DeviceProxy = ""
        self.shared_partition = ""
        self.protocol = ""
        self.uuid = ""
        self.health_check = ""
        self.sampling_enable = []
        self.member_list = []
        self.shared_group = ""
        self.name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


