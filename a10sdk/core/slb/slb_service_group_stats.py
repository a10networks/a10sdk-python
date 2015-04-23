from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param server_selection_fail_drop: {"description": "Service selection fail drop", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}
    :param server_selection_fail_reset: {"description": "Service selection fail reset", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "8"}
    :param service_peak_conn: {"description": "Service peak connection", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "8"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.server_selection_fail_drop = ""
        self.server_selection_fail_reset = ""
        self.service_peak_conn = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class ServiceGroup(A10BaseClass):
    
    """Class Description::
    Statistics for the object service-group.

    Class service-group supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param member_list: {"minItems": 1, "items": {"type": "member"}, "uniqueItems": true, "array": [{"required": ["name", "port"], "properties": {"stats": {"type": "object", "properties": {"curr_req": {"description": "Current requests", "format": "counter", "type": "number", "oid": "10", "optional": true, "size": "8"}, "total_fwd_bytes": {"description": "Total forward bytes", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "8"}, "peak_conn": {"description": "Peak connections", "format": "counter", "type": "number", "oid": "13", "optional": true, "size": "8"}, "total_req": {"description": "Total requests", "format": "counter", "type": "number", "oid": "11", "optional": true, "size": "8"}, "total_conn": {"description": "Total connections", "format": "counter", "type": "number", "oid": "6", "optional": true, "size": "8"}, "fastest_rsp_time": {"description": "Fastest response time", "format": "counter", "type": "number", "oid": "15", "optional": true, "size": "8"}, "total_fwd_pkts": {"description": "Total forward packets", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "8"}, "total_rev_pkts_inspected_status_code_non_5xx": {"description": "Total reverse packets inspected status code non 5xx", "format": "counter", "type": "number", "oid": "9", "optional": true, "size": "8"}, "total_rev_pkts": {"description": "Total reverse packets", "format": "counter", "type": "number", "oid": "5", "optional": true, "size": "8"}, "total_rev_pkts_inspected_status_code_2xx": {"description": "Total reverse packets inspected status code 2xx", "format": "counter", "type": "number", "oid": "8", "optional": true, "size": "8"}, "total_req_succ": {"description": "Total requests successful", "format": "counter", "type": "number", "oid": "12", "optional": true, "size": "8"}, "curr_conn": {"description": "Current connections", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}, "total_rev_pkts_inspected": {"description": "Total reverse packets inspected", "format": "counter", "type": "number", "oid": "7", "optional": true, "size": "8"}, "total_rev_bytes": {"description": "Total reverse bytes", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "8"}, "slowest_rsp_time": {"description": "Slowest response time", "format": "counter", "type": "number", "oid": "16", "optional": true, "size": "8"}, "response_time": {"description": "Response time", "format": "counter", "type": "number", "oid": "14", "optional": true, "size": "8"}}}, "name": {"description": "Member name", "format": "comp-string", "minLength": 1, "oid": "1001", "optional": false, "maxLength": 127, "type": "string"}, "port": {"description": "Port number", "format": "number", "default": 65534, "optional": false, "oid": "1002", "maximum": 65534, "minimum": 0, "type": "number"}}}], "type": "array", "$ref": "/axapi/v3/slb/service-group/{name}/member/{name}+{port}"}
    :param name: {"description": "SLB Service Name", "format": "string-rlx", "minLength": 1, "oid": "1001", "optional": false, "maxLength": 127, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/service-group/{name}/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "service-group"
        self.a10_url="/axapi/v3/slb/service-group/{name}/stats"
        self.DeviceProxy = ""
        self.member_list = []
        self.stats = {}
        self.name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


