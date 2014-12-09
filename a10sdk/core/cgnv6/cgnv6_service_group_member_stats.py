from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param curr_req: {"optional": true, "size": "8", "type": "number", "oid": "10", "format": "counter"}
    :param total_fwd_bytes: {"optional": true, "size": "8", "type": "number", "oid": "2", "format": "counter"}
    :param peak_conn: {"optional": true, "size": "8", "type": "number", "oid": "13", "format": "counter"}
    :param total_req: {"optional": true, "size": "8", "type": "number", "oid": "11", "format": "counter"}
    :param total_conn: {"optional": true, "size": "8", "type": "number", "oid": "6", "format": "counter"}
    :param fastest_rsp_time: {"optional": true, "size": "8", "type": "number", "oid": "15", "format": "counter"}
    :param total_fwd_pkts: {"optional": true, "size": "8", "type": "number", "oid": "3", "format": "counter"}
    :param total_rev_pkts_inspected_status_code_non_5xx: {"optional": true, "size": "8", "type": "number", "oid": "9", "format": "counter"}
    :param total_rev_pkts: {"optional": true, "size": "8", "type": "number", "oid": "5", "format": "counter"}
    :param total_rev_pkts_inspected_status_code_2xx: {"optional": true, "size": "8", "type": "number", "oid": "8", "format": "counter"}
    :param total_req_succ: {"optional": true, "size": "8", "type": "number", "oid": "12", "format": "counter"}
    :param curr_conn: {"optional": true, "size": "8", "type": "number", "oid": "1", "format": "counter"}
    :param total_rev_pkts_inspected: {"optional": true, "size": "8", "type": "number", "oid": "7", "format": "counter"}
    :param total_rev_bytes: {"optional": true, "size": "8", "type": "number", "oid": "4", "format": "counter"}
    :param slowest_rsp_time: {"optional": true, "size": "8", "type": "number", "oid": "16", "format": "counter"}
    :param response_time: {"optional": true, "size": "8", "type": "number", "oid": "14", "format": "counter"}
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
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/service-group/{name}/member/{name}+{port}/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name","port"]

        self.b_key = "member"
        self.a10_url="/axapi/v3/cgnv6/service-group/{name}/member/{name}+{port}/stats"
        self.DeviceProxy = ""
        self.stats = {}
        self.name = ""
        self.port = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


