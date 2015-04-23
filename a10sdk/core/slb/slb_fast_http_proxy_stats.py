from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param new_svrconn: {"description": "Server conn made", "format": "counter", "type": "number", "oid": "24", "optional": true, "size": "8"}
    :param tcpoutrst: {"description": "Out RSTs", "format": "counter", "type": "number", "oid": "26", "optional": true, "size": "8"}
    :param total_proxy: {"description": "Total Proxy Conns", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "8"}
    :param fwdreqdata_fail: {"description": "Fwd req data fail", "format": "counter", "type": "number", "oid": "19", "optional": true, "size": "8"}
    :param client_rst: {"description": "Client RST", "format": "counter", "type": "number", "oid": "7", "optional": true, "size": "8"}
    :param svrsel_fail: {"description": "Server selection fail", "format": "counter", "type": "number", "oid": "11", "optional": true, "size": "8"}
    :param req_retran: {"description": "Packets retrans", "format": "counter", "type": "number", "oid": "20", "optional": true, "size": "8"}
    :param close_on_ddos: {"description": "Close on DDoS", "format": "counter", "type": "number", "oid": "195", "optional": true, "size": "8"}
    :param req_over_limit: {"description": "Request over limit", "format": "counter", "type": "number", "oid": "31", "optional": true, "size": "8"}
    :param noproxy: {"description": "No proxy error", "format": "counter", "type": "number", "oid": "6", "optional": true, "size": "8"}
    :param svr_prem_close: {"description": "Server premature close", "format": "counter", "type": "number", "oid": "23", "optional": true, "size": "8"}
    :param parsereq_fail: {"description": "Parse req fail", "format": "counter", "type": "number", "oid": "10", "optional": true, "size": "8"}
    :param req: {"description": "HTTP requests", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "8"}
    :param full_proxy: {"description": "Full proxy tot", "format": "counter", "type": "number", "oid": "27", "optional": true, "size": "8"}
    :param full_proxy_put: {"description": "Full proxy PUT", "format": "counter", "type": "number", "oid": "259", "optional": true, "size": "8"}
    :param full_proxy_fpga_err: {"description": "Full proxy fpga err", "format": "counter", "type": "number", "oid": "30", "optional": true, "size": "8"}
    :param server_rst: {"description": "Server RST", "format": "counter", "type": "number", "oid": "8", "optional": true, "size": "8"}
    :param notuple: {"description": "No tuple error", "format": "counter", "type": "number", "oid": "9", "optional": true, "size": "8"}
    :param curr_proxy: {"description": "Curr Proxy Conns", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "8"}
    :param server_resel: {"description": "Server reselection", "format": "counter", "type": "number", "oid": "22", "optional": true, "size": "8"}
    :param req_ofo: {"description": "Packets ofo", "format": "counter", "type": "number", "oid": "21", "optional": true, "size": "8"}
    :param full_proxy_post: {"description": "Full proxy POST", "format": "counter", "type": "number", "oid": "28", "optional": true, "size": "8"}
    :param snat_fail: {"description": "Source NAT failure", "format": "counter", "type": "number", "oid": "25", "optional": true, "size": "8"}
    :param req_rate_over_limit: {"description": "Request rate over limit", "format": "counter", "type": "number", "oid": "32", "optional": true, "size": "8"}
    :param full_proxy_pipeline: {"description": "Full proxy pipeline", "format": "counter", "type": "number", "oid": "29", "optional": true, "size": "8"}
    :param fwdreq_fail: {"description": "Fwd req fail", "format": "counter", "type": "number", "oid": "12", "optional": true, "size": "8"}
    :param req_succ: {"description": "HTTP requests(succ)", "format": "counter", "type": "number", "oid": "5", "optional": true, "size": "8"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.new_svrconn = ""
        self.tcpoutrst = ""
        self.total_proxy = ""
        self.fwdreqdata_fail = ""
        self.client_rst = ""
        self.svrsel_fail = ""
        self.req_retran = ""
        self.close_on_ddos = ""
        self.req_over_limit = ""
        self.noproxy = ""
        self.svr_prem_close = ""
        self.parsereq_fail = ""
        self.req = ""
        self.full_proxy = ""
        self.full_proxy_put = ""
        self.full_proxy_fpga_err = ""
        self.server_rst = ""
        self.notuple = ""
        self.curr_proxy = ""
        self.server_resel = ""
        self.req_ofo = ""
        self.full_proxy_post = ""
        self.snat_fail = ""
        self.req_rate_over_limit = ""
        self.full_proxy_pipeline = ""
        self.fwdreq_fail = ""
        self.req_succ = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class FastHttpProxy(A10BaseClass):
    
    """Class Description::
    Statistics for the object fast-http-proxy.

    Class fast-http-proxy supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/fast-http-proxy/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "fast-http-proxy"
        self.a10_url="/axapi/v3/slb/fast-http-proxy/stats"
        self.DeviceProxy = ""
        self.stats = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


