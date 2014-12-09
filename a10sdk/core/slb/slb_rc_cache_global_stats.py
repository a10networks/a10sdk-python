from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param nm_response: {"description": "Responses from cache 304 Not Modified", "format": "counter", "type": "number", "oid": "11", "optional": true, "size": "8"}
    :param rsp_type_304: {"description": "Responses from server 304 Not Modified", "format": "counter", "type": "number", "oid": "14", "optional": true, "size": "8"}
    :param rsp_other: {"description": "Responses from cache Other", "format": "counter", "type": "number", "oid": "19", "optional": true, "size": "8"}
    :param content_toosmall: {"description": "Policy Content Too Small", "format": "counter", "type": "number", "oid": "24", "optional": true, "size": "8"}
    :param entry_create_failures: {"description": "Entry Create failures", "format": "counter", "type": "number", "oid": "25", "optional": true, "size": "8"}
    :param nocache_match: {"description": "Policy URI nocache", "format": "counter", "type": "number", "oid": "20", "optional": true, "size": "8"}
    :param content_toobig: {"description": "Policy Content Too Big", "format": "counter", "type": "number", "oid": "23", "optional": true, "size": "8"}
    :param nc_res_header: {"description": "Not cacheable", "format": "counter", "type": "number", "oid": "7", "optional": true, "size": "8"}
    :param miss: {"description": "Cache Misses", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "8"}
    :param nc_req_header: {"description": "No-cache Request", "format": "counter", "type": "number", "oid": "6", "optional": true, "size": "8"}
    :param replaced_entry: {"description": "Entry Replaced", "format": "counter", "type": "number", "oid": "28", "optional": true, "size": "8"}
    :param aging_entry: {"description": "Entry Aged Out", "format": "counter", "type": "number", "oid": "29", "optional": true, "size": "8"}
    :param mem_size: {"description": "Memory Used", "format": "counter", "type": "number", "oid": "26", "optional": true, "size": "8"}
    :param rsp_deflate: {"description": "Responses from cache 200 OK - Deflate", "format": "counter", "type": "number", "oid": "18", "optional": true, "size": "8"}
    :param invalidate_match: {"description": "Policy URI invalidate", "format": "counter", "type": "number", "oid": "22", "optional": true, "size": "8"}
    :param match: {"description": "Policy URI cache", "format": "counter", "type": "number", "oid": "21", "optional": true, "size": "8"}
    :param cleaned_entry: {"description": "Entry Cleaned", "format": "counter", "type": "number", "oid": "30", "optional": true, "size": "8"}
    :param entry_num: {"description": "Entry Cached", "format": "counter", "type": "number", "oid": "27", "optional": true, "size": "8"}
    :param total_req: {"description": "Total Requests", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "8"}
    :param bytes_served: {"description": "Bytes Served", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "8"}
    :param rv_success: {"description": "Revalidation Successes", "format": "counter", "type": "number", "oid": "8", "optional": true, "size": "8"}
    :param rv_failure: {"description": "Revalidation Failures", "format": "counter", "type": "number", "oid": "9", "optional": true, "size": "8"}
    :param rsp_gzip: {"description": "Responses from cache 200 OK - Gzip", "format": "counter", "type": "number", "oid": "17", "optional": true, "size": "8"}
    :param hits: {"description": "Cache Hits", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}
    :param rsp_type_other: {"description": "Responses from server 200 OK - Other", "format": "counter", "type": "number", "oid": "15", "optional": true, "size": "8"}
    :param rsp_type_CE: {"description": "Responses from server 200 OK - Chnk Enc", "format": "counter", "type": "number", "oid": "13", "optional": true, "size": "8"}
    :param rsp_no_compress: {"description": "Responses from cache 200 OK - No Comp", "format": "counter", "type": "number", "oid": "16", "optional": true, "size": "8"}
    :param rsp_type_CL: {"description": "Responses from server 200 OK - Cont Len", "format": "counter", "type": "number", "oid": "12", "optional": true, "size": "8"}
    :param caching_req: {"description": "Cacheable Requests", "format": "counter", "type": "number", "oid": "5", "optional": true, "size": "8"}
    :param ims_request: {"description": "IMS Requests", "format": "counter", "type": "number", "oid": "10", "optional": true, "size": "8"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.nm_response = ""
        self.rsp_type_304 = ""
        self.rsp_other = ""
        self.content_toosmall = ""
        self.entry_create_failures = ""
        self.nocache_match = ""
        self.content_toobig = ""
        self.nc_res_header = ""
        self.miss = ""
        self.nc_req_header = ""
        self.replaced_entry = ""
        self.aging_entry = ""
        self.mem_size = ""
        self.rsp_deflate = ""
        self.invalidate_match = ""
        self.match = ""
        self.cleaned_entry = ""
        self.entry_num = ""
        self.total_req = ""
        self.bytes_served = ""
        self.rv_success = ""
        self.rv_failure = ""
        self.rsp_gzip = ""
        self.hits = ""
        self.rsp_type_other = ""
        self.rsp_type_CE = ""
        self.rsp_no_compress = ""
        self.rsp_type_CL = ""
        self.caching_req = ""
        self.ims_request = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class RcCacheGlobal(A10BaseClass):
    
    """Class Description::
    Statistics for the object rc-cache-global.

    Class rc-cache-global supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/rc-cache-global/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "rc-cache-global"
        self.a10_url="/axapi/v3/slb/rc-cache-global/stats"
        self.DeviceProxy = ""
        self.stats = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


