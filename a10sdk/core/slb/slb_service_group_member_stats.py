from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param curr_req: {"description": "Current requests", "format": "counter", "type": "number", "oid": "10", "optional": true, "size": "8"}
    :param total_fwd_bytes: {"description": "Total forward bytes", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "8"}
    :param peak_conn: {"description": "Peak connections", "format": "counter", "type": "number", "oid": "13", "optional": true, "size": "8"}
    :param total_req: {"description": "Total requests", "format": "counter", "type": "number", "oid": "11", "optional": true, "size": "8"}
    :param total_conn: {"description": "Total connections", "format": "counter", "type": "number", "oid": "6", "optional": true, "size": "8"}
    :param fastest_rsp_time: {"description": "Fastest response time", "format": "counter", "type": "number", "oid": "15", "optional": true, "size": "8"}
    :param total_fwd_pkts: {"description": "Total forward packets", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "8"}
    :param total_rev_pkts_inspected_status_code_non_5xx: {"description": "Total reverse packets inspected status code non 5xx", "format": "counter", "type": "number", "oid": "9", "optional": true, "size": "8"}
    :param total_rev_pkts: {"description": "Total reverse packets", "format": "counter", "type": "number", "oid": "5", "optional": true, "size": "8"}
    :param total_rev_pkts_inspected_status_code_2xx: {"description": "Total reverse packets inspected status code 2xx", "format": "counter", "type": "number", "oid": "8", "optional": true, "size": "8"}
    :param total_req_succ: {"description": "Total requests successful", "format": "counter", "type": "number", "oid": "12", "optional": true, "size": "8"}
    :param curr_conn: {"description": "Current connections", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}
    :param total_rev_pkts_inspected: {"description": "Total reverse packets inspected", "format": "counter", "type": "number", "oid": "7", "optional": true, "size": "8"}
    :param total_rev_bytes: {"description": "Total reverse bytes", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "8"}
    :param slowest_rsp_time: {"description": "Slowest response time", "format": "counter", "type": "number", "oid": "16", "optional": true, "size": "8"}
    :param response_time: {"description": "Response time", "format": "counter", "type": "number", "oid": "14", "optional": true, "size": "8"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.curr_req = ""
        self.total_fwd_bytes = ""
        self.peak_conn = ""
        self.total_req = ""
        self.total_conn = ""
        self.fastest_rsp_time = ""
        self.total_fwd_pkts = ""
        self.total_rev_pkts_inspected_status_code_non_5xx = ""
        self.total_rev_pkts = ""
        self.total_rev_pkts_inspected_status_code_2xx = ""
        self.total_req_succ = ""
        self.curr_conn = ""
        self.total_rev_pkts_inspected = ""
        self.total_rev_bytes = ""
        self.slowest_rsp_time = ""
        self.response_time = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Member(A10BaseClass):
    
    """Class Description::
    Statistics for the object member.

    Class member supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param name: {"description": "Member name", "format": "comp-string", "minLength": 1, "oid": "1001", "optional": false, "maxLength": 127, "type": "string"}
    :param port: {"description": "Port number", "format": "number", "default": 65534, "optional": false, "oid": "1002", "maximum": 65534, "minimum": 0, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/service-group/{name}/member/{name}+{port}/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name","port"]

        self.b_key = "member"
        self.a10_url="/axapi/v3/slb/service-group/{name}/member/{name}+{port}/stats"
        self.DeviceProxy = ""
        self.stats = {}
        self.name = ""
        self.port = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


