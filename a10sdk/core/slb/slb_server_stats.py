from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param peak_conn: {"description": "Peak connections", "format": "counter", "type": "number", "oid": "5", "optional": true, "size": "8"}
    :param curr_conn: {"description": "Current connections", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}
    :param rev_pkt: {"description": "Reverse packets", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "8"}
    :param fwd_pkt: {"description": "Forward packets", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "8"}
    :param total_conn: {"description": "Total connections", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "8"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.peak_conn = ""
        self.curr_conn = ""
        self.rev_pkt = ""
        self.fwd_pkt = ""
        self.total_conn = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Server(A10BaseClass):
    
    """Class Description::
    Statistics for the object server.

    Class server supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param port_list: {"minItems": 1, "items": {"type": "port"}, "uniqueItems": true, "array": [{"required": ["port-number", "protocol"], "properties": {"stats": {"type": "object", "properties": {"es_resp_invalid_http": {"description": "Total non-http response", "format": "counter", "type": "number", "oid": "19", "optional": true, "size": "8"}, "curr_req": {"description": "Current requests", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "8"}, "total_rev_pkts_inspected_good_status_code": {"description": "Total reverse packets with good status code inspected", "format": "counter", "type": "number", "oid": "21", "optional": true, "size": "8"}, "es_resp_count": {"description": "Total proxy response", "format": "counter", "type": "number", "oid": "18", "optional": true, "size": "8"}, "total_fwd_bytes": {"description": "Forward bytes", "format": "counter", "type": "number", "oid": "5", "optional": true, "size": "8"}, "es_resp_other": {"description": "Response status other", "format": "counter", "type": "number", "oid": "16", "optional": true, "size": "8"}, "fastest_rsp_time": {"description": "Fastest response time", "format": "counter", "type": "number", "oid": "23", "optional": true, "size": "8"}, "total_fwd_pkts": {"description": "Forward packets", "format": "counter", "type": "number", "oid": "6", "optional": true, "size": "8"}, "es_req_count": {"description": "Total proxy request", "format": "counter", "type": "number", "oid": "17", "optional": true, "size": "8"}, "es_resp_500": {"description": "Response status 500", "format": "counter", "type": "number", "oid": "15", "optional": true, "size": "8"}, "peak_conn": {"description": "Peak connections", "format": "counter", "type": "number", "oid": "11", "optional": true, "size": "8"}, "total_req": {"description": "Total Requests", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "8"}, "es_resp_400": {"description": "Response status 400", "format": "counter", "type": "number", "oid": "14", "optional": true, "size": "8"}, "es_resp_300": {"description": "Response status 300", "format": "counter", "type": "number", "oid": "13", "optional": true, "size": "8"}, "curr_conn": {"description": "Current connections", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}, "es_resp_200": {"description": "Response status 200", "format": "counter", "type": "number", "oid": "12", "optional": true, "size": "8"}, "total_rev_bytes": {"description": "Reverse bytes", "format": "counter", "type": "number", "oid": "7", "optional": true, "size": "8"}, "response_time": {"description": "Response time", "format": "counter", "type": "number", "oid": "22", "optional": true, "size": "8"}, "total_conn": {"description": "Total connections", "format": "counter", "type": "number", "oid": "9", "optional": true, "size": "8"}, "total_rev_pkts": {"description": "Reverse packets", "format": "counter", "type": "number", "oid": "8", "optional": true, "size": "8"}, "total_req_succ": {"description": "Total requests succ", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "8"}, "last_total_conn": {"description": "Last total connections", "format": "counter", "type": "number", "oid": "10", "optional": true, "size": "8"}, "total_rev_pkts_inspected": {"description": "Total reverse packets inspected", "format": "counter", "type": "number", "oid": "20", "optional": true, "size": "8"}, "slowest_rsp_time": {"description": "Slowest response time", "format": "counter", "type": "number", "oid": "24", "optional": true, "size": "8"}}}, "protocol": {"enum": ["tcp", "udp"], "description": "'tcp': TCP Port; 'udp': UDP Port; ", "format": "enum", "type": "string", "oid": "1002", "optional": false}, "port-number": {"description": "Port Number", "format": "number", "optional": false, "oid": "1001", "maximum": 65534, "minimum": 0, "type": "number"}}}], "type": "array", "$ref": "/axapi/v3/slb/server/{name}/port/{port-number}+{protocol}"}
    :param name: {"description": "Server Name", "format": "string-rlx", "minLength": 1, "oid": "1001", "optional": false, "maxLength": 127, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/server/{name}/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "server"
        self.a10_url="/axapi/v3/slb/server/{name}/stats"
        self.DeviceProxy = ""
        self.port_list = []
        self.stats = {}
        self.name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


