from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param es_resp_invalid_http: {"description": "Total non-http response", "format": "counter", "type": "number", "oid": "19", "optional": true, "size": "8"}
    :param curr_req: {"description": "Current requests", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "8"}
    :param total_rev_pkts_inspected_good_status_code: {"description": "Total reverse packets with good status code inspected", "format": "counter", "type": "number", "oid": "21", "optional": true, "size": "8"}
    :param es_resp_count: {"description": "Total proxy response", "format": "counter", "type": "number", "oid": "18", "optional": true, "size": "8"}
    :param total_fwd_bytes: {"description": "Forward bytes", "format": "counter", "type": "number", "oid": "5", "optional": true, "size": "8"}
    :param es_resp_other: {"description": "Response status other", "format": "counter", "type": "number", "oid": "16", "optional": true, "size": "8"}
    :param fastest_rsp_time: {"description": "Fastest response time", "format": "counter", "type": "number", "oid": "23", "optional": true, "size": "8"}
    :param total_fwd_pkts: {"description": "Forward packets", "format": "counter", "type": "number", "oid": "6", "optional": true, "size": "8"}
    :param es_req_count: {"description": "Total proxy request", "format": "counter", "type": "number", "oid": "17", "optional": true, "size": "8"}
    :param es_resp_500: {"description": "Response status 500", "format": "counter", "type": "number", "oid": "15", "optional": true, "size": "8"}
    :param peak_conn: {"description": "Peak connections", "format": "counter", "type": "number", "oid": "11", "optional": true, "size": "8"}
    :param total_req: {"description": "Total Requests", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "8"}
    :param es_resp_400: {"description": "Response status 400", "format": "counter", "type": "number", "oid": "14", "optional": true, "size": "8"}
    :param es_resp_300: {"description": "Response status 300", "format": "counter", "type": "number", "oid": "13", "optional": true, "size": "8"}
    :param curr_conn: {"description": "Current connections", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}
    :param es_resp_200: {"description": "Response status 200", "format": "counter", "type": "number", "oid": "12", "optional": true, "size": "8"}
    :param total_rev_bytes: {"description": "Reverse bytes", "format": "counter", "type": "number", "oid": "7", "optional": true, "size": "8"}
    :param response_time: {"description": "Response time", "format": "counter", "type": "number", "oid": "22", "optional": true, "size": "8"}
    :param total_conn: {"description": "Total connections", "format": "counter", "type": "number", "oid": "9", "optional": true, "size": "8"}
    :param total_rev_pkts: {"description": "Reverse packets", "format": "counter", "type": "number", "oid": "8", "optional": true, "size": "8"}
    :param total_req_succ: {"description": "Total requests succ", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "8"}
    :param last_total_conn: {"description": "Last total connections", "format": "counter", "type": "number", "oid": "10", "optional": true, "size": "8"}
    :param total_rev_pkts_inspected: {"description": "Total reverse packets inspected", "format": "counter", "type": "number", "oid": "20", "optional": true, "size": "8"}
    :param slowest_rsp_time: {"description": "Slowest response time", "format": "counter", "type": "number", "oid": "24", "optional": true, "size": "8"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.es_resp_invalid_http = ""
        self.curr_req = ""
        self.total_rev_pkts_inspected_good_status_code = ""
        self.es_resp_count = ""
        self.total_fwd_bytes = ""
        self.es_resp_other = ""
        self.fastest_rsp_time = ""
        self.total_fwd_pkts = ""
        self.es_req_count = ""
        self.es_resp_500 = ""
        self.peak_conn = ""
        self.total_req = ""
        self.es_resp_400 = ""
        self.es_resp_300 = ""
        self.curr_conn = ""
        self.es_resp_200 = ""
        self.total_rev_bytes = ""
        self.response_time = ""
        self.total_conn = ""
        self.total_rev_pkts = ""
        self.total_req_succ = ""
        self.last_total_conn = ""
        self.total_rev_pkts_inspected = ""
        self.slowest_rsp_time = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Port(A10BaseClass):
    
    """Class Description::
    Statistics for the object port.

    Class port supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param protocol: {"enum": ["tcp", "udp"], "description": "'tcp': TCP Port; 'udp': UDP Port; ", "format": "enum", "type": "string", "oid": "1002", "optional": false}
    :param port_number: {"description": "Port Number", "format": "number", "optional": false, "oid": "1001", "maximum": 65534, "minimum": 0, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/server/{name}/port/{port_number}+{protocol}/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "port_number","protocol"]

        self.b_key = "port"
        self.a10_url="/axapi/v3/slb/server/{name}/port/{port_number}+{protocol}/stats"
        self.DeviceProxy = ""
        self.stats = {}
        self.protocol = ""
        self.port_number = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


