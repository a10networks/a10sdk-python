from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param peak_conn: {"optional": true, "size": "8", "type": "number", "oid": "5", "format": "counter"}
    :param curr_conn: {"optional": true, "size": "8", "type": "number", "oid": "1", "format": "counter"}
    :param rev_pkt: {"optional": true, "size": "8", "type": "number", "oid": "4", "format": "counter"}
    :param fwd_pkt: {"optional": true, "size": "8", "type": "number", "oid": "3", "format": "counter"}
    :param total_conn: {"optional": true, "size": "8", "type": "number", "oid": "2", "format": "counter"}
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

    :param port_list: {"minItems": 1, "items": {"type": "port"}, "uniqueItems": true, "array": [{"required": ["port-number", "protocol"], "properties": {"stats": {"type": "object", "properties": {"es_resp_invalid_http": {"optional": true, "size": "8", "type": "number", "oid": "19", "format": "counter"}, "curr_req": {"optional": true, "size": "8", "type": "number", "oid": "2", "format": "counter"}, "total_rev_pkts_inspected_good_status_code": {"optional": true, "size": "8", "type": "number", "oid": "21", "format": "counter"}, "es_resp_count": {"optional": true, "size": "8", "type": "number", "oid": "18", "format": "counter"}, "total_fwd_bytes": {"optional": true, "size": "8", "type": "number", "oid": "5", "format": "counter"}, "es_resp_other": {"optional": true, "size": "8", "type": "number", "oid": "16", "format": "counter"}, "fastest_rsp_time": {"optional": true, "size": "8", "type": "number", "oid": "23", "format": "counter"}, "total_fwd_pkts": {"optional": true, "size": "8", "type": "number", "oid": "6", "format": "counter"}, "es_req_count": {"optional": true, "size": "8", "type": "number", "oid": "17", "format": "counter"}, "es_resp_500": {"optional": true, "size": "8", "type": "number", "oid": "15", "format": "counter"}, "peak_conn": {"optional": true, "size": "8", "type": "number", "oid": "11", "format": "counter"}, "total_req": {"optional": true, "size": "8", "type": "number", "oid": "3", "format": "counter"}, "es_resp_400": {"optional": true, "size": "8", "type": "number", "oid": "14", "format": "counter"}, "es_resp_300": {"optional": true, "size": "8", "type": "number", "oid": "13", "format": "counter"}, "curr_conn": {"optional": true, "size": "8", "type": "number", "oid": "1", "format": "counter"}, "es_resp_200": {"optional": true, "size": "8", "type": "number", "oid": "12", "format": "counter"}, "total_rev_bytes": {"optional": true, "size": "8", "type": "number", "oid": "7", "format": "counter"}, "response_time": {"optional": true, "size": "8", "type": "number", "oid": "22", "format": "counter"}, "total_conn": {"optional": true, "size": "8", "type": "number", "oid": "9", "format": "counter"}, "total_rev_pkts": {"optional": true, "size": "8", "type": "number", "oid": "8", "format": "counter"}, "total_req_succ": {"optional": true, "size": "8", "type": "number", "oid": "4", "format": "counter"}, "last_total_conn": {"optional": true, "size": "8", "type": "number", "oid": "10", "format": "counter"}, "total_rev_pkts_inspected": {"optional": true, "size": "8", "type": "number", "oid": "20", "format": "counter"}, "slowest_rsp_time": {"optional": true, "size": "8", "type": "number", "oid": "24", "format": "counter"}}}, "protocol": {"enum": ["tcp", "udp"], "description": "'tcp': TCP Port; 'udp': UDP Port; ", "format": "enum", "type": "string", "oid": "1002", "optional": false}, "port-number": {"description": "Port Number", "format": "number", "optional": false, "oid": "1001", "maximum": 65534, "minimum": 0, "type": "number"}}}], "type": "array", "$ref": "/axapi/v3/cgnv6/server/{name}/port/{port-number}+{protocol}"}
    :param name: {"description": "Server Name", "format": "string-rlx", "minLength": 1, "oid": "1001", "optional": false, "maxLength": 127, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/server/{name}/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "server"
        self.a10_url="/axapi/v3/cgnv6/server/{name}/stats"
        self.DeviceProxy = ""
        self.port_list = []
        self.stats = {}
        self.name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


