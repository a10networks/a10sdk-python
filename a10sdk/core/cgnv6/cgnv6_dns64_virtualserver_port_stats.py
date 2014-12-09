from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param curr_req: {"optional": true, "size": "8", "type": "number", "oid": "19", "format": "counter"}
    :param total_fwd_bytes: {"optional": true, "size": "8", "type": "number", "oid": "6", "format": "counter"}
    :param compression_miss: {"optional": true, "size": "2", "type": "number", "oid": "16", "format": "counter"}
    :param fastest_rsp_time: {"optional": true, "size": "8", "type": "number", "oid": "25", "format": "counter"}
    :param total_fwd_pkts: {"optional": true, "size": "8", "type": "number", "oid": "7", "format": "counter"}
    :param total_mf_dns_pkts: {"optional": true, "size": "2", "type": "number", "oid": "11", "format": "counter"}
    :param compression_miss_template_exclusion: {"optional": true, "size": "2", "type": "number", "oid": "18", "format": "counter"}
    :param total_dns_pkts: {"optional": true, "size": "2", "type": "number", "oid": "10", "format": "counter"}
    :param peak_conn: {"optional": true, "size": "8", "type": "number", "oid": "22", "format": "counter"}
    :param compression_bytes_after: {"optional": true, "size": "2", "type": "number", "oid": "14", "format": "counter"}
    :param toatal_tcp_conn: {"optional": true, "size": "8", "type": "number", "oid": "4", "format": "counter"}
    :param total_req: {"optional": true, "size": "8", "type": "number", "oid": "20", "format": "counter"}
    :param compression_bytes_before: {"optional": true, "size": "2", "type": "number", "oid": "13", "format": "counter"}
    :param last_rsp_time: {"optional": true, "size": "8", "type": "number", "oid": "24", "format": "counter"}
    :param curr_conn: {"optional": true, "size": "8", "type": "number", "oid": "1", "format": "counter"}
    :param total_rev_bytes: {"optional": true, "size": "8", "type": "number", "oid": "8", "format": "counter"}
    :param curr_conn_rate: {"optional": true, "size": "8", "type": "number", "oid": "23", "format": "counter"}
    :param compression_miss_no_client: {"optional": true, "size": "2", "type": "number", "oid": "17", "format": "counter"}
    :param es_total_failure_actions: {"optional": true, "size": "2", "type": "number", "oid": "12", "format": "counter"}
    :param total_conn: {"optional": true, "size": "8", "type": "number", "oid": "5", "format": "counter"}
    :param total_rev_pkts: {"optional": true, "size": "8", "type": "number", "oid": "9", "format": "counter"}
    :param total_l7_conn: {"optional": true, "size": "8", "type": "number", "oid": "3", "format": "counter"}
    :param total_req_succ: {"optional": true, "size": "8", "type": "number", "oid": "21", "format": "counter"}
    :param total_l4_conn: {"optional": true, "size": "8", "type": "number", "oid": "2", "format": "counter"}
    :param slowest_rsp_time: {"optional": true, "size": "8", "type": "number", "oid": "26", "format": "counter"}
    :param compression_hit: {"optional": true, "size": "2", "type": "number", "oid": "15", "format": "counter"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.curr_req = ""
        self.total_fwd_bytes = ""
        self.compression_miss = ""
        self.fastest_rsp_time = ""
        self.total_fwd_pkts = ""
        self.total_mf_dns_pkts = ""
        self.compression_miss_template_exclusion = ""
        self.total_dns_pkts = ""
        self.peak_conn = ""
        self.compression_bytes_after = ""
        self.toatal_tcp_conn = ""
        self.total_req = ""
        self.compression_bytes_before = ""
        self.last_rsp_time = ""
        self.curr_conn = ""
        self.total_rev_bytes = ""
        self.curr_conn_rate = ""
        self.compression_miss_no_client = ""
        self.es_total_failure_actions = ""
        self.total_conn = ""
        self.total_rev_pkts = ""
        self.total_l7_conn = ""
        self.total_req_succ = ""
        self.total_l4_conn = ""
        self.slowest_rsp_time = ""
        self.compression_hit = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Port(A10BaseClass):
    
    """Class Description::
    Statistics for the object port.

    Class port supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param protocol: {"enum": ["dns-udp"], "description": "'dns-udp': DNS service over UDP; ", "format": "enum", "type": "string", "oid": "1002", "optional": false}
    :param port_number: {"description": "Port", "format": "number", "optional": false, "oid": "1001", "maximum": 65534, "minimum": 0, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/dns64-virtualserver/{name}/port/{port_number}+{protocol}/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "port_number","protocol"]

        self.b_key = "port"
        self.a10_url="/axapi/v3/cgnv6/dns64-virtualserver/{name}/port/{port_number}+{protocol}/stats"
        self.DeviceProxy = ""
        self.stats = {}
        self.protocol = ""
        self.port_number = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


