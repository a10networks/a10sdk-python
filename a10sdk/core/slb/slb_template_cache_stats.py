from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param nm_response: {"optional": true, "size": "2", "type": "number", "oid": "11", "format": "counter"}
    :param rsp_type_304: {"optional": true, "size": "2", "type": "number", "oid": "14", "format": "counter"}
    :param rsp_other: {"optional": true, "size": "2", "type": "number", "oid": "19", "format": "counter"}
    :param content_toosmall: {"optional": true, "size": "2", "type": "number", "oid": "24", "format": "counter"}
    :param entry_create_failures: {"optional": true, "size": "2", "type": "number", "oid": "25", "format": "counter"}
    :param nocache_match: {"optional": true, "size": "2", "type": "number", "oid": "20", "format": "counter"}
    :param content_toobig: {"optional": true, "size": "2", "type": "number", "oid": "23", "format": "counter"}
    :param nc_res_header: {"optional": true, "size": "2", "type": "number", "oid": "7", "format": "counter"}
    :param miss: {"optional": true, "size": "2", "type": "number", "oid": "2", "format": "counter"}
    :param nc_req_header: {"optional": true, "size": "2", "type": "number", "oid": "6", "format": "counter"}
    :param replaced_entry: {"optional": true, "size": "8", "type": "number", "oid": "28", "format": "counter"}
    :param aging_entry: {"optional": true, "size": "8", "type": "number", "oid": "29", "format": "counter"}
    :param mem_size: {"optional": true, "size": "8", "type": "number", "oid": "26", "format": "counter"}
    :param rsp_deflate: {"optional": true, "size": "2", "type": "number", "oid": "18", "format": "counter"}
    :param invalidate_match: {"optional": true, "size": "2", "type": "number", "oid": "22", "format": "counter"}
    :param match: {"optional": true, "size": "2", "type": "number", "oid": "21", "format": "counter"}
    :param cleaned_entry: {"optional": true, "size": "8", "type": "number", "oid": "30", "format": "counter"}
    :param entry_num: {"optional": true, "size": "8", "type": "number", "oid": "27", "format": "counter"}
    :param total_req: {"optional": true, "size": "2", "type": "number", "oid": "4", "format": "counter"}
    :param bytes_served: {"optional": true, "size": "2", "type": "number", "oid": "3", "format": "counter"}
    :param rv_success: {"optional": true, "size": "2", "type": "number", "oid": "8", "format": "counter"}
    :param rv_failure: {"optional": true, "size": "2", "type": "number", "oid": "9", "format": "counter"}
    :param rsp_gzip: {"optional": true, "size": "2", "type": "number", "oid": "17", "format": "counter"}
    :param hits: {"optional": true, "size": "2", "type": "number", "oid": "1", "format": "counter"}
    :param rsp_type_other: {"optional": true, "size": "2", "type": "number", "oid": "15", "format": "counter"}
    :param rsp_type_CE: {"optional": true, "size": "2", "type": "number", "oid": "13", "format": "counter"}
    :param rsp_no_compress: {"optional": true, "size": "2", "type": "number", "oid": "16", "format": "counter"}
    :param rsp_type_CL: {"optional": true, "size": "2", "type": "number", "oid": "12", "format": "counter"}
    :param caching_req: {"optional": true, "size": "2", "type": "number", "oid": "5", "format": "counter"}
    :param ims_request: {"optional": true, "size": "2", "type": "number", "oid": "10", "format": "counter"}
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


class Cache(A10BaseClass):
    
    """Class Description::
    Statistics for the object cache.

    Class cache supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param name: {"description": "Specify cache template name", "format": "string-rlx", "minLength": 1, "oid": "1001", "optional": false, "maxLength": 63, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/template/cache/{name}/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "cache"
        self.a10_url="/axapi/v3/slb/template/cache/{name}/stats"
        self.DeviceProxy = ""
        self.stats = {}
        self.name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


