from a10sdk.common.A10BaseClass import A10BaseClass


class LocalUriPolicy(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param local_uri: {"minLength": 1, "maxLength": 63, "type": "string", "description": "Specify Local URI for caching (Specify URI pattern that the policy should be applied to, maximum 63 charaters)", "format": "string-rlx"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "local-uri-policy"
        self.DeviceProxy = ""
        self.local_uri = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class SamplingEnable(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param counters1: {"enum": ["all", "hits", "miss", "bytes_served", "total_req", "caching_req", "nc_req_header", "nc_res_header", "rv_success", "rv_failure", "ims_request", "nm_response", "rsp_type_CL", "rsp_type_CE", "rsp_type_304", "rsp_type_other", "rsp_no_compress", "rsp_gzip", "rsp_deflate", "rsp_other", "nocache_match", "match", "invalidate_match", "content_toobig", "content_toosmall", "entry_create_failures", "mem_size", "entry_num", "replaced_entry", "aging_entry", "cleaned_entry"], "type": "string", "description": "'all': all; 'hits': hits; 'miss': miss; 'bytes_served': bytes_served; 'total_req': total_req; 'caching_req': caching_req; 'nc_req_header': nc_req_header; 'nc_res_header': nc_res_header; 'rv_success': rv_success; 'rv_failure': rv_failure; 'ims_request': ims_request; 'nm_response': nm_response; 'rsp_type_CL': rsp_type_CL; 'rsp_type_CE': rsp_type_CE; 'rsp_type_304': rsp_type_304; 'rsp_type_other': rsp_type_other; 'rsp_no_compress': rsp_no_compress; 'rsp_gzip': rsp_gzip; 'rsp_deflate': rsp_deflate; 'rsp_other': rsp_other; 'nocache_match': nocache_match; 'match': match; 'invalidate_match': invalidate_match; 'content_toobig': content_toobig; 'content_toosmall': content_toosmall; 'entry_create_failures': entry_create_failures; 'mem_size': mem_size; 'entry_num': entry_num; 'replaced_entry': replaced_entry; 'aging_entry': aging_entry; 'cleaned_entry': cleaned_entry; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "sampling-enable"
        self.DeviceProxy = ""
        self.counters1 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class UriPolicy(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param cache_action: {"enum": ["cache", "nocache"], "type": "string", "description": "'cache': Specify if certain URIs should be cached; 'nocache': Specify if certain URIs should not be cached; ", "format": "enum"}
    :param invalidate: {"minLength": 1, "maxLength": 128, "type": "string", "description": "Specify if URI should invalidate chache entries matching pattern (pattern that would match entries to be invalidated (64 chars max))", "format": "string"}
    :param uri: {"minLength": 1, "maxLength": 63, "type": "string", "description": "Specify URI for cache policy (Specify URI pattern that the policy should be applied to, maximum 63 charaters)", "format": "string-rlx"}
    :param cache_value: {"description": "Specify seconds that content should be cached, default is age specified in cache template", "minimum": 1, "type": "number", "maximum": 999999, "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "uri-policy"
        self.DeviceProxy = ""
        self.cache_action = ""
        self.invalidate = ""
        self.uri = ""
        self.cache_value = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Cache(A10BaseClass):
    
    """Class Description::
    RAM caching template.

    Class cache supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param accept_reload_req: {"default": 0, "optional": true, "type": "number", "description": "Accept reload requests via cache-control directives in HTTP headers", "format": "flag"}
    :param name: {"description": "Specify cache template name", "format": "string-rlx", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param age: {"description": "Specify duration in seconds cached content valid, default is 3600 seconds (seconds that the cached content is valid (default 3600 seconds))", "format": "number", "default": 3600, "optional": true, "maximum": 999999, "minimum": 1, "type": "number"}
    :param disable_insert_via: {"default": 0, "optional": true, "type": "number", "description": "Disable insertion of via header in response served from RAM cache", "format": "flag"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param disable_insert_age: {"default": 0, "optional": true, "type": "number", "description": "Disable insertion of age header in response served from RAM cache", "format": "flag"}
    :param local_uri_policy: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "local-uri": {"minLength": 1, "maxLength": 63, "type": "string", "description": "Specify Local URI for caching (Specify URI pattern that the policy should be applied to, maximum 63 charaters)", "format": "string-rlx"}}}]}
    :param sampling_enable: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "hits", "miss", "bytes_served", "total_req", "caching_req", "nc_req_header", "nc_res_header", "rv_success", "rv_failure", "ims_request", "nm_response", "rsp_type_CL", "rsp_type_CE", "rsp_type_304", "rsp_type_other", "rsp_no_compress", "rsp_gzip", "rsp_deflate", "rsp_other", "nocache_match", "match", "invalidate_match", "content_toobig", "content_toosmall", "entry_create_failures", "mem_size", "entry_num", "replaced_entry", "aging_entry", "cleaned_entry"], "type": "string", "description": "'all': all; 'hits': hits; 'miss': miss; 'bytes_served': bytes_served; 'total_req': total_req; 'caching_req': caching_req; 'nc_req_header': nc_req_header; 'nc_res_header': nc_res_header; 'rv_success': rv_success; 'rv_failure': rv_failure; 'ims_request': ims_request; 'nm_response': nm_response; 'rsp_type_CL': rsp_type_CL; 'rsp_type_CE': rsp_type_CE; 'rsp_type_304': rsp_type_304; 'rsp_type_other': rsp_type_other; 'rsp_no_compress': rsp_no_compress; 'rsp_gzip': rsp_gzip; 'rsp_deflate': rsp_deflate; 'rsp_other': rsp_other; 'nocache_match': nocache_match; 'match': match; 'invalidate_match': invalidate_match; 'content_toobig': content_toobig; 'content_toosmall': content_toosmall; 'entry_create_failures': entry_create_failures; 'mem_size': mem_size; 'entry_num': entry_num; 'replaced_entry': replaced_entry; 'aging_entry': aging_entry; 'cleaned_entry': cleaned_entry; ", "format": "enum"}}}]}
    :param replacement_policy: {"description": "'LFU': LFU; ", "format": "enum", "default": "LFU", "type": "string", "enum": ["LFU"], "optional": true}
    :param min_content_size: {"description": "Minimum size (bytes) of response that can be cached - default 512", "format": "number", "default": 512, "optional": true, "maximum": 268435455, "minimum": 0, "type": "number"}
    :param max_content_size: {"description": "Maximum size (bytes) of response that can be cached - default 81920 (80KB)", "format": "number", "default": 81920, "optional": true, "maximum": 268435455, "minimum": 0, "type": "number"}
    :param max_cache_size: {"description": "Specify maximum cache size in megabytes, default is 80MB (RAM cache size in megabytes (default 80MB))", "format": "number", "default": 80, "optional": true, "maximum": 4096, "minimum": 1, "type": "number"}
    :param logging: {"description": "Specify logging template (Logging Config name)", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/slb/template/logging"}
    :param remove_cookies: {"default": 0, "optional": true, "type": "number", "description": "Remove cookies in response and cache", "format": "flag"}
    :param verify_host: {"default": 0, "optional": true, "type": "number", "description": "Verify request using host before sending response from RAM cache", "format": "flag"}
    :param default_policy_nocache: {"default": 0, "optional": true, "type": "number", "description": "Specify default policy to be to not cache", "format": "flag"}
    :param uri_policy: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"cache-action": {"enum": ["cache", "nocache"], "type": "string", "description": "'cache': Specify if certain URIs should be cached; 'nocache': Specify if certain URIs should not be cached; ", "format": "enum"}, "invalidate": {"minLength": 1, "maxLength": 128, "type": "string", "description": "Specify if URI should invalidate chache entries matching pattern (pattern that would match entries to be invalidated (64 chars max))", "format": "string"}, "uri": {"minLength": 1, "maxLength": 63, "type": "string", "description": "Specify URI for cache policy (Specify URI pattern that the policy should be applied to, maximum 63 charaters)", "format": "string-rlx"}, "optional": true, "cache-value": {"description": "Specify seconds that content should be cached, default is age specified in cache template", "minimum": 1, "type": "number", "maximum": 999999, "format": "number"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/template/cache/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "cache"
        self.a10_url="/axapi/v3/slb/template/cache/{name}"
        self.DeviceProxy = ""
        self.accept_reload_req = ""
        self.name = ""
        self.age = ""
        self.disable_insert_via = ""
        self.uuid = ""
        self.disable_insert_age = ""
        self.local_uri_policy = []
        self.sampling_enable = []
        self.replacement_policy = ""
        self.min_content_size = ""
        self.max_content_size = ""
        self.max_cache_size = ""
        self.logging = ""
        self.remove_cookies = ""
        self.verify_host = ""
        self.default_policy_nocache = ""
        self.uri_policy = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


