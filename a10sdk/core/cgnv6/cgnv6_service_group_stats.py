from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param server_selection_fail_drop: {"optional": true, "size": "8", "type": "number", "oid": "1", "format": "counter"}
    :param server_selection_fail_reset: {"optional": true, "size": "8", "type": "number", "oid": "2", "format": "counter"}
    :param service_peak_conn: {"optional": true, "size": "8", "type": "number", "oid": "3", "format": "counter"}
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

    :param member_list: {"minItems": 1, "items": {"type": "member"}, "uniqueItems": true, "array": [{"required": ["name", "port"], "properties": {"stats": {"type": "object", "properties": {"curr_req": {"optional": true, "size": "8", "type": "number", "oid": "10", "format": "counter"}, "total_fwd_bytes": {"optional": true, "size": "8", "type": "number", "oid": "2", "format": "counter"}, "peak_conn": {"optional": true, "size": "8", "type": "number", "oid": "13", "format": "counter"}, "total_req": {"optional": true, "size": "8", "type": "number", "oid": "11", "format": "counter"}, "total_conn": {"optional": true, "size": "8", "type": "number", "oid": "6", "format": "counter"}, "fastest_rsp_time": {"optional": true, "size": "8", "type": "number", "oid": "15", "format": "counter"}, "total_fwd_pkts": {"optional": true, "size": "8", "type": "number", "oid": "3", "format": "counter"}, "total_rev_pkts_inspected_status_code_non_5xx": {"optional": true, "size": "8", "type": "number", "oid": "9", "format": "counter"}, "total_rev_pkts": {"optional": true, "size": "8", "type": "number", "oid": "5", "format": "counter"}, "total_rev_pkts_inspected_status_code_2xx": {"optional": true, "size": "8", "type": "number", "oid": "8", "format": "counter"}, "total_req_succ": {"optional": true, "size": "8", "type": "number", "oid": "12", "format": "counter"}, "curr_conn": {"optional": true, "size": "8", "type": "number", "oid": "1", "format": "counter"}, "total_rev_pkts_inspected": {"optional": true, "size": "8", "type": "number", "oid": "7", "format": "counter"}, "total_rev_bytes": {"optional": true, "size": "8", "type": "number", "oid": "4", "format": "counter"}, "slowest_rsp_time": {"optional": true, "size": "8", "type": "number", "oid": "16", "format": "counter"}, "response_time": {"optional": true, "size": "8", "type": "number", "oid": "14", "format": "counter"}}}, "name": {"description": "Member name", "format": "comp-string", "minLength": 1, "oid": "1001", "optional": false, "maxLength": 127, "type": "string"}, "port": {"description": "Port number", "format": "number", "default": 65534, "optional": false, "oid": "1002", "maximum": 65534, "minimum": 0, "type": "number"}}}], "type": "array", "$ref": "/axapi/v3/cgnv6/service-group/{name}/member/{name}+{port}"}
    :param name: {"description": "CGNV6 Service Name", "format": "string-rlx", "minLength": 1, "oid": "1001", "optional": false, "maxLength": 127, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/service-group/{name}/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "service-group"
        self.a10_url="/axapi/v3/cgnv6/service-group/{name}/stats"
        self.DeviceProxy = ""
        self.member_list = []
        self.stats = {}
        self.name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


