from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param hit: {"description": "Total cache hit", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "2"}
    :param ageout_weight: {"description": "Total aged for lower weight", "format": "counter", "type": "number", "oid": "16", "optional": true, "size": "2"}
    :param answer_r: {"description": "Response with multiple answers", "format": "counter", "type": "number", "oid": "12", "optional": true, "size": "2"}
    :param multiple_r: {"description": "Response with multiple questions", "format": "counter", "type": "number", "oid": "11", "optional": true, "size": "2"}
    :param multiple_q: {"description": "Query with multiple questions", "format": "counter", "type": "number", "oid": "6", "optional": true, "size": "2"}
    :param total_alloc: {"description": "Total allocated", "format": "counter", "type": "number", "oid": "18", "optional": true, "size": "2"}
    :param current_allocate: {"description": "Current allocate", "format": "counter", "type": "number", "oid": "20", "optional": true, "size": "8"}
    :param bad_q: {"description": "Query not passed", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "2"}
    :param bad_answer: {"description": "Bad Answer", "format": "counter", "type": "number", "oid": "15", "optional": true, "size": "2"}
    :param total_freed: {"description": "Total freed", "format": "counter", "type": "number", "oid": "19", "optional": true, "size": "2"}
    :param bad_r: {"description": "Response not passed", "format": "counter", "type": "number", "oid": "8", "optional": true, "size": "2"}
    :param encode_r: {"description": "Response encoded", "format": "counter", "type": "number", "oid": "10", "optional": true, "size": "2"}
    :param encode_q: {"description": "Query encoded", "format": "counter", "type": "number", "oid": "5", "optional": true, "size": "2"}
    :param ageout: {"description": "Total aged out", "format": "counter", "type": "number", "oid": "14", "optional": true, "size": "2"}
    :param total_q: {"description": "Total query", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "2"}
    :param total_r: {"description": "Total server response", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "2"}
    :param total_log: {"description": "Total stats log sent", "format": "counter", "type": "number", "oid": "17", "optional": true, "size": "2"}
    :param oversize_r: {"description": "Response exceed cache size", "format": "counter", "type": "number", "oid": "9", "optional": true, "size": "2"}
    :param current_data_allocate: {"description": "Current data allocate", "format": "counter", "type": "number", "oid": "21", "optional": true, "size": "8"}
    :param ttl_r: {"description": "Response with short TTL", "format": "counter", "type": "number", "oid": "13", "optional": true, "size": "2"}
    :param oversize_q: {"description": "Query exceed cache size", "format": "counter", "type": "number", "oid": "7", "optional": true, "size": "2"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.hit = ""
        self.ageout_weight = ""
        self.answer_r = ""
        self.multiple_r = ""
        self.multiple_q = ""
        self.total_alloc = ""
        self.current_allocate = ""
        self.bad_q = ""
        self.bad_answer = ""
        self.total_freed = ""
        self.bad_r = ""
        self.encode_r = ""
        self.encode_q = ""
        self.ageout = ""
        self.total_q = ""
        self.total_r = ""
        self.total_log = ""
        self.oversize_r = ""
        self.current_data_allocate = ""
        self.ttl_r = ""
        self.oversize_q = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class DnsCache(A10BaseClass):
    
    """Class Description::
    Statistics for the object dns-cache.

    Class dns-cache supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/dns-cache/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "dns-cache"
        self.a10_url="/axapi/v3/slb/dns-cache/stats"
        self.DeviceProxy = ""
        self.stats = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


