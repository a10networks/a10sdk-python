from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param es_resp_invalid_http: {"optional": true, "size": "8", "type": "number", "oid": "19", "format": "counter"}
    :param curr_req: {"optional": true, "size": "8", "type": "number", "oid": "2", "format": "counter"}
    :param total_rev_pkts_inspected_good_status_code: {"optional": true, "size": "8", "type": "number", "oid": "21", "format": "counter"}
    :param es_resp_count: {"optional": true, "size": "8", "type": "number", "oid": "18", "format": "counter"}
    :param total_fwd_bytes: {"optional": true, "size": "8", "type": "number", "oid": "5", "format": "counter"}
    :param es_resp_other: {"optional": true, "size": "8", "type": "number", "oid": "16", "format": "counter"}
    :param fastest_rsp_time: {"optional": true, "size": "8", "type": "number", "oid": "23", "format": "counter"}
    :param total_fwd_pkts: {"optional": true, "size": "8", "type": "number", "oid": "6", "format": "counter"}
    :param es_req_count: {"optional": true, "size": "8", "type": "number", "oid": "17", "format": "counter"}
    :param es_resp_500: {"optional": true, "size": "8", "type": "number", "oid": "15", "format": "counter"}
    :param peak_conn: {"optional": true, "size": "8", "type": "number", "oid": "11", "format": "counter"}
    :param total_req: {"optional": true, "size": "8", "type": "number", "oid": "3", "format": "counter"}
    :param es_resp_400: {"optional": true, "size": "8", "type": "number", "oid": "14", "format": "counter"}
    :param es_resp_300: {"optional": true, "size": "8", "type": "number", "oid": "13", "format": "counter"}
    :param curr_conn: {"optional": true, "size": "8", "type": "number", "oid": "1", "format": "counter"}
    :param es_resp_200: {"optional": true, "size": "8", "type": "number", "oid": "12", "format": "counter"}
    :param total_rev_bytes: {"optional": true, "size": "8", "type": "number", "oid": "7", "format": "counter"}
    :param response_time: {"optional": true, "size": "8", "type": "number", "oid": "22", "format": "counter"}
    :param total_conn: {"optional": true, "size": "8", "type": "number", "oid": "9", "format": "counter"}
    :param total_rev_pkts: {"optional": true, "size": "8", "type": "number", "oid": "8", "format": "counter"}
    :param total_req_succ: {"optional": true, "size": "8", "type": "number", "oid": "4", "format": "counter"}
    :param last_total_conn: {"optional": true, "size": "8", "type": "number", "oid": "10", "format": "counter"}
    :param total_rev_pkts_inspected: {"optional": true, "size": "8", "type": "number", "oid": "20", "format": "counter"}
    :param slowest_rsp_time: {"optional": true, "size": "8", "type": "number", "oid": "24", "format": "counter"}
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
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/server/{name}/port/{port_number}+{protocol}/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "port_number","protocol"]

        self.b_key = "port"
        self.a10_url="/axapi/v3/cgnv6/server/{name}/port/{port_number}+{protocol}/stats"
        self.DeviceProxy = ""
        self.stats = {}
        self.protocol = ""
        self.port_number = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


