from a10sdk.common.A10BaseClass import A10BaseClass


class SamplingEnable(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param counters1: {"enum": ["all", "hits", "miss", "bytes_served", "total_req", "caching_req", "nc_req_header", "nc_res_header", "rv_success", "rv_failure", "ims_request", "nm_response", "rsp_type_CL", "rsp_type_CE", "rsp_type_304", "rsp_type_other", "rsp_no_compress", "rsp_gzip", "rsp_deflate", "rsp_other", "nocache_match", "match", "invalidate_match", "content_toobig", "content_toosmall", "entry_create_failures", "mem_size", "entry_num", "replaced_entry", "aging_entry", "cleaned_entry"], "type": "string", "description": "'all': all; 'hits': Cache Hits; 'miss': Cache Misses; 'bytes_served': Bytes Served; 'total_req': Total Requests; 'caching_req': Cacheable Requests; 'nc_req_header': No-cache Request; 'nc_res_header': Not cacheable; 'rv_success': Revalidation Successes; 'rv_failure': Revalidation Failures; 'ims_request': IMS Requests; 'nm_response': Responses from cache 304 Not Modified; 'rsp_type_CL': Responses from server 200 OK - Cont Len; 'rsp_type_CE': Responses from server 200 OK - Chnk Enc; 'rsp_type_304': Responses from server 304 Not Modified; 'rsp_type_other': Responses from server 200 OK - Other; 'rsp_no_compress': Responses from cache 200 OK - No Comp; 'rsp_gzip': Responses from cache 200 OK - Gzip; 'rsp_deflate': Responses from cache 200 OK - Deflate; 'rsp_other': Responses from cache Other; 'nocache_match': Policy URI nocache; 'match': Policy URI cache; 'invalidate_match': Policy URI invalidate; 'content_toobig': Policy Content Too Big; 'content_toosmall': Policy Content Too Small; 'entry_create_failures': Entry Create failures; 'mem_size': Memory Used; 'entry_num': Entry Cached; 'replaced_entry': Entry Replaced; 'aging_entry': Entry Aged Out; 'cleaned_entry': Entry Cleaned; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "sampling-enable"
        self.DeviceProxy = ""
        self.counters1 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class RcCacheGlobal(A10BaseClass):
    
    """    :param sampling_enable: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "hits", "miss", "bytes_served", "total_req", "caching_req", "nc_req_header", "nc_res_header", "rv_success", "rv_failure", "ims_request", "nm_response", "rsp_type_CL", "rsp_type_CE", "rsp_type_304", "rsp_type_other", "rsp_no_compress", "rsp_gzip", "rsp_deflate", "rsp_other", "nocache_match", "match", "invalidate_match", "content_toobig", "content_toosmall", "entry_create_failures", "mem_size", "entry_num", "replaced_entry", "aging_entry", "cleaned_entry"], "type": "string", "description": "'all': all; 'hits': Cache Hits; 'miss': Cache Misses; 'bytes_served': Bytes Served; 'total_req': Total Requests; 'caching_req': Cacheable Requests; 'nc_req_header': No-cache Request; 'nc_res_header': Not cacheable; 'rv_success': Revalidation Successes; 'rv_failure': Revalidation Failures; 'ims_request': IMS Requests; 'nm_response': Responses from cache 304 Not Modified; 'rsp_type_CL': Responses from server 200 OK - Cont Len; 'rsp_type_CE': Responses from server 200 OK - Chnk Enc; 'rsp_type_304': Responses from server 304 Not Modified; 'rsp_type_other': Responses from server 200 OK - Other; 'rsp_no_compress': Responses from cache 200 OK - No Comp; 'rsp_gzip': Responses from cache 200 OK - Gzip; 'rsp_deflate': Responses from cache 200 OK - Deflate; 'rsp_other': Responses from cache Other; 'nocache_match': Policy URI nocache; 'match': Policy URI cache; 'invalidate_match': Policy URI invalidate; 'content_toobig': Policy Content Too Big; 'content_toosmall': Policy Content Too Small; 'entry_create_failures': Entry Create failures; 'mem_size': Memory Used; 'entry_num': Entry Cached; 'replaced_entry': Entry Replaced; 'aging_entry': Entry Aged Out; 'cleaned_entry': Entry Cleaned; ", "format": "enum"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    global ram cache stats.

    Class rc-cache-global supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/rc-cache-global`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "rc-cache-global"
        self.a10_url="/axapi/v3/slb/rc-cache-global"
        self.DeviceProxy = ""
        self.sampling_enable = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


