from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param query_passive: {"description": "Query Passive", "format": "counter", "type": "number", "oid": "5", "optional": true, "size": "8"}
    :param resp_local: {"description": "Response Local", "format": "counter", "type": "number", "oid": "12", "optional": true, "size": "8"}
    :param adjust: {"description": "Translated", "format": "counter", "type": "number", "oid": "13", "optional": true, "size": "8"}
    :param query_bad_pkt: {"description": "Query Bad Packet", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "8"}
    :param resp: {"description": "Response", "format": "counter", "type": "number", "oid": "6", "optional": true, "size": "8"}
    :param cache: {"description": "Cache", "format": "counter", "type": "number", "oid": "14", "optional": true, "size": "8"}
    :param resp_empty: {"description": "Response Empty", "format": "counter", "type": "number", "oid": "11", "optional": true, "size": "8"}
    :param resp_chg: {"description": "Response Changed", "format": "counter", "type": "number", "oid": "9", "optional": true, "size": "8"}
    :param query_parallel: {"description": "Query Parallel", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "8"}
    :param resp_bad_qr: {"description": "Response Bad Query", "format": "counter", "type": "number", "oid": "8", "optional": true, "size": "8"}
    :param query: {"description": "Query", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}
    :param drop: {"description": "Dropped", "format": "counter", "type": "number", "oid": "15", "optional": true, "size": "8"}
    :param resp_err: {"description": "Response Error", "format": "counter", "type": "number", "oid": "10", "optional": true, "size": "8"}
    :param resp_bad_pkt: {"description": "Response Bad Packet", "format": "counter", "type": "number", "oid": "7", "optional": true, "size": "8"}
    :param query_chg: {"description": "Query Changed", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "8"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.query_passive = ""
        self.resp_local = ""
        self.adjust = ""
        self.query_bad_pkt = ""
        self.resp = ""
        self.cache = ""
        self.resp_empty = ""
        self.resp_chg = ""
        self.query_parallel = ""
        self.resp_bad_qr = ""
        self.query = ""
        self.drop = ""
        self.resp_err = ""
        self.resp_bad_pkt = ""
        self.query_chg = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Dns64(A10BaseClass):
    
    """Class Description::
    Statistics for the object dns64.

    Class dns64 supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/dns64/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "dns64"
        self.a10_url="/axapi/v3/cgnv6/dns64/stats"
        self.DeviceProxy = ""
        self.stats = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


