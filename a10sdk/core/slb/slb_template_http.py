from a10sdk.common.A10BaseClass import A10BaseClass


class RequestHeaderEraseList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param request_header_erase: {"minLength": 1, "maxLength": 63, "type": "string", "description": "Erase a header from HTTP request (Header Name)", "format": "string-rlx"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "request-header-erase-list"
        self.DeviceProxy = ""
        self.request_header_erase = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class MatchList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param rewrite_to: {"minLength": 1, "maxLength": 63, "type": "string", "description": "Rewrite to Destination URL String", "format": "string-rlx"}
    :param redirect_match: {"minLength": 1, "maxLength": 63, "type": "string", "description": "URL Matching (Pattern URL String)", "format": "string-rlx"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "match-list"
        self.DeviceProxy = ""
        self.rewrite_to = ""
        self.redirect_match = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class RedirectRewrite(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param redirect_secure_port: {"description": "Port (Port Number)", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}
    :param redirect_secure: {"default": 0, "type": "number", "description": "Use HTTPS", "format": "flag"}
    :param match_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "rewrite-to": {"minLength": 1, "maxLength": 63, "type": "string", "description": "Rewrite to Destination URL String", "format": "string-rlx"}, "redirect-match": {"minLength": 1, "maxLength": 63, "type": "string", "description": "URL Matching (Pattern URL String)", "format": "string-rlx"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "redirect-rewrite"
        self.DeviceProxy = ""
        self.redirect_secure_port = ""
        self.redirect_secure = ""
        self.match_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class ResponseHeaderInsertList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param response_header_insert_type: {"enum": ["insert-if-not-exist", "insert-always"], "type": "string", "description": "'insert-if-not-exist': Only insert the header when it does not exist; 'insert-always': Always insert the header even when there is a header with the same name; ", "format": "enum"}
    :param response_header_insert: {"minLength": 1, "maxLength": 127, "type": "string", "description": "Insert a header into HTTP response (Header Content (Format: \"[name]: [value]\"))", "format": "string-rlx"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "response-header-insert-list"
        self.DeviceProxy = ""
        self.response_header_insert_type = ""
        self.response_header_insert = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class ResponseHeaderEraseList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param response_header_erase: {"minLength": 1, "maxLength": 63, "type": "string", "description": "Erase a header from HTTP response (Header Name)", "format": "string-rlx"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "response-header-erase-list"
        self.DeviceProxy = ""
        self.response_header_erase = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Template(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param logging: {"description": "Logging template (Logging Config name)", "format": "string", "minLength": 1, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/slb/template/logging"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "template"
        self.DeviceProxy = ""
        self.logging = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class UrlSwitching(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param url_service_group: {"description": "Create a Service Group comprising Servers (Service Group Name)", "format": "string-rlx", "minLength": 1, "maxLength": 127, "type": "string", "$ref": "/axapi/v3/slb/service-group"}
    :param url_match_string: {"minLength": 1, "maxLength": 63, "type": "string", "description": "URL String", "format": "string-rlx"}
    :param url_switching_type: {"enum": ["contains", "ends-with", "equals", "starts-with", "url-case-insensitive", "url-hits-enable"], "type": "string", "description": "'contains': Select service group if URL string contains another string; 'ends-with': Select service group if URL string ends with another string; 'equals': Select service group if URL string equals another string; 'starts-with': Select service group if URL string starts with another string; 'url-case-insensitive': Case insensitive URL switching; 'url-hits-enable': Enables URL Hits; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "url-switching"
        self.DeviceProxy = ""
        self.url_service_group = ""
        self.url_match_string = ""
        self.url_switching_type = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class HostSwitching(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param host_switching_type: {"enum": ["contains", "ends-with", "equals", "starts-with", "host-hits-enable"], "type": "string", "description": "'contains': Select service group if hostname contains another string; 'ends-with': Select service group if hostname ends with another string; 'equals': Select service group if hostname equals another string; 'starts-with': Select service group if hostname starts with another string; 'host-hits-enable': Enables Host Hits counters; ", "format": "enum"}
    :param host_service_group: {"description": "Create a Service Group comprising Servers (Service Group Name)", "format": "string-rlx", "minLength": 1, "maxLength": 127, "type": "string", "$ref": "/axapi/v3/slb/service-group"}
    :param host_match_string: {"minLength": 1, "maxLength": 63, "type": "string", "description": "Hostname String", "format": "string-rlx"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "host-switching"
        self.DeviceProxy = ""
        self.host_switching_type = ""
        self.host_service_group = ""
        self.host_match_string = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class ResponseContentReplaceList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param response_new_string: {"minLength": 1, "maxLength": 127, "type": "string", "description": "String will be in the http content", "format": "string-rlx"}
    :param response_content_replace: {"minLength": 1, "maxLength": 127, "type": "string", "description": "replace the data from HTTP response content (String in the http content need to be replaced)", "format": "string-rlx"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "response-content-replace-list"
        self.DeviceProxy = ""
        self.response_new_string = ""
        self.response_content_replace = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class RequestHeaderInsertList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param request_header_insert_type: {"enum": ["insert-if-not-exist", "insert-always"], "type": "string", "description": "'insert-if-not-exist': Only insert the header when it does not exist; 'insert-always': Always insert the header even when there is a header with the same name; ", "format": "enum"}
    :param request_header_insert: {"minLength": 1, "maxLength": 127, "type": "string", "description": "Insert a header into HTTP request (Header Content (Format: \"[name]: [value]\"))", "format": "string-rlx"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "request-header-insert-list"
        self.DeviceProxy = ""
        self.request_header_insert_type = ""
        self.request_header_insert = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class CompressionContentType(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param content_type: {"minLength": 1, "maxLength": 31, "type": "string", "description": "Compression content-type", "format": "string-rlx"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "compression-content-type"
        self.DeviceProxy = ""
        self.content_type = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class CompressionExcludeUri(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param exclude_uri: {"minLength": 1, "maxLength": 31, "type": "string", "description": "Compression exclude uri", "format": "string-rlx"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "compression-exclude-uri"
        self.DeviceProxy = ""
        self.exclude_uri = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class CompressionExcludeContentType(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param exclude_content_type: {"minLength": 1, "maxLength": 31, "type": "string", "description": "Compression exclude content-type (Compression exclude content type)", "format": "string-rlx"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "compression-exclude-content-type"
        self.DeviceProxy = ""
        self.exclude_content_type = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Http(A10BaseClass):
    
    """Class Description::
    HTTP.

    Class http supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param keep_client_alive: {"default": 0, "optional": true, "type": "number", "description": "Keep client alive", "format": "flag"}
    :param compression_auto_disable_on_high_cpu: {"description": "Auto-disable software compression on high cpu usage (Disable compression if cpu usage is above threshold. Default is off.)", "format": "number", "type": "number", "maximum": 100, "minimum": 1, "optional": true}
    :param req_hdr_wait_time: {"default": 0, "optional": true, "type": "number", "description": "HTTP request header wait time before abort connection", "format": "flag"}
    :param request_header_erase_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "request-header-erase": {"minLength": 1, "maxLength": 63, "type": "string", "description": "Erase a header from HTTP request (Header Name)", "format": "string-rlx"}}}]}
    :param compression_enable: {"default": 0, "optional": true, "type": "number", "description": "Enable Compression", "format": "flag"}
    :param compression_keep_accept_encoding: {"default": 0, "optional": true, "type": "number", "description": "Keep accept encoding", "format": "flag"}
    :param failover_url: {"description": "Failover to this URL (Failover URL Name)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 255, "type": "string"}
    :param compression_level: {"description": "compression level, default 1 (compression level value, default is 1)", "format": "number", "default": 1, "optional": true, "maximum": 9, "minimum": 1, "type": "number"}
    :param rd_port: {"description": "Port (Port Number)", "format": "number", "optional": true, "maximum": 65535, "minimum": 1, "not": "rd-simple-loc", "type": "number"}
    :param insert_client_port_header_name: {"description": "HTTP Header Name for inserting Client Port", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param url_hash_last: {"description": "Use the end part of URL to calculate hash value (URL string length to calculate hash value)", "format": "number", "optional": true, "maximum": 128, "minimum": 4, "not": "url-hash-first", "type": "number"}
    :param use_server_status: {"default": 0, "optional": true, "type": "number", "description": "Use Server-Status header to do URL hashing", "format": "flag"}
    :param req_hdr_wait_time_val: {"description": "Number of seconds wait for client request header (default is 7)", "format": "number", "default": 7, "optional": true, "maximum": 31, "minimum": 1, "type": "number"}
    :param response_header_insert_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"response-header-insert-type": {"enum": ["insert-if-not-exist", "insert-always"], "type": "string", "description": "'insert-if-not-exist': Only insert the header when it does not exist; 'insert-always': Always insert the header even when there is a header with the same name; ", "format": "enum"}, "response-header-insert": {"minLength": 1, "maxLength": 127, "type": "string", "description": "Insert a header into HTTP response (Header Content (Format: \"[name]: [value]\"))", "format": "string-rlx"}, "optional": true}}]}
    :param redirect: {"default": 0, "optional": true, "type": "number", "description": "Automatically send a redirect response", "format": "flag"}
    :param insert_client_port: {"default": 0, "optional": true, "type": "number", "description": "Insert Client Port address into HTTP header", "format": "flag"}
    :param retry_on_5xx_per_req: {"description": "Retry http request on HTTP 5xx code for each request", "format": "flag", "default": 0, "optional": true, "not": "retry-on-5xx", "type": "number"}
    :param url_hash_offset: {"description": "Skip part of URL to calculate hash value (Offset of the URL string)", "format": "number", "type": "number", "maximum": 255, "minimum": 0, "optional": true}
    :param rd_simple_loc: {"description": "Redirect location tag absolute URI string", "format": "string-rlx", "minLength": 1, "not-list": ["rd-secure", "rd-port"], "optional": true, "maxLength": 255, "type": "string"}
    :param client_port_hdr_replace: {"default": 0, "optional": true, "type": "number", "description": "Replace the existing header", "format": "flag"}
    :param non_http_bypass: {"default": 0, "optional": true, "type": "number", "description": "Bypass non-http traffic instead of dropping", "format": "flag"}
    :param response_header_erase_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"response-header-erase": {"minLength": 1, "maxLength": 63, "type": "string", "description": "Erase a header from HTTP response (Header Name)", "format": "string-rlx"}, "optional": true}}]}
    :param insert_client_ip: {"default": 0, "optional": true, "type": "number", "description": "Insert Client IP address into HTTP header", "format": "flag"}
    :param url_switching: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"url-service-group": {"description": "Create a Service Group comprising Servers (Service Group Name)", "format": "string-rlx", "minLength": 1, "maxLength": 127, "type": "string", "$ref": "/axapi/v3/slb/service-group"}, "url-match-string": {"minLength": 1, "maxLength": 63, "type": "string", "description": "URL String", "format": "string-rlx"}, "optional": true, "url-switching-type": {"enum": ["contains", "ends-with", "equals", "starts-with", "url-case-insensitive", "url-hits-enable"], "type": "string", "description": "'contains': Select service group if URL string contains another string; 'ends-with': Select service group if URL string ends with another string; 'equals': Select service group if URL string equals another string; 'starts-with': Select service group if URL string starts with another string; 'url-case-insensitive': Case insensitive URL switching; 'url-hits-enable': Enables URL Hits; ", "format": "enum"}}}]}
    :param rd_secure: {"description": "Use HTTPS", "format": "flag", "default": 0, "optional": true, "not": "rd-simple-loc", "type": "number"}
    :param host_switching: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"host-switching-type": {"enum": ["contains", "ends-with", "equals", "starts-with", "host-hits-enable"], "type": "string", "description": "'contains': Select service group if hostname contains another string; 'ends-with': Select service group if hostname ends with another string; 'equals': Select service group if hostname equals another string; 'starts-with': Select service group if hostname starts with another string; 'host-hits-enable': Enables Host Hits counters; ", "format": "enum"}, "host-service-group": {"description": "Create a Service Group comprising Servers (Service Group Name)", "format": "string-rlx", "minLength": 1, "maxLength": 127, "type": "string", "$ref": "/axapi/v3/slb/service-group"}, "host-match-string": {"minLength": 1, "maxLength": 63, "type": "string", "description": "Hostname String", "format": "string-rlx"}, "optional": true}}]}
    :param strict_transaction_switch: {"default": 0, "optional": true, "type": "number", "description": "Force server selection on every HTTP request", "format": "flag"}
    :param response_content_replace_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "response-new-string": {"minLength": 1, "maxLength": 127, "type": "string", "description": "String will be in the http content", "format": "string-rlx"}, "response-content-replace": {"minLength": 1, "maxLength": 127, "type": "string", "description": "replace the data from HTTP response content (String in the http content need to be replaced)", "format": "string-rlx"}}}]}
    :param request_header_insert_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "request-header-insert-type": {"enum": ["insert-if-not-exist", "insert-always"], "type": "string", "description": "'insert-if-not-exist': Only insert the header when it does not exist; 'insert-always': Always insert the header even when there is a header with the same name; ", "format": "enum"}, "request-header-insert": {"minLength": 1, "maxLength": 127, "type": "string", "description": "Insert a header into HTTP request (Header Content (Format: \"[name]: [value]\"))", "format": "string-rlx"}}}]}
    :param compression_minimum_content_length: {"description": "Minimum Content Length (Minimum content length for compression in bytes. Default is 120.)", "format": "number", "default": 120, "optional": true, "maximum": 2147483647, "minimum": 1, "type": "number"}
    :param rd_resp_code: {"optional": true, "enum": ["301", "302", "303", "307"], "type": "string", "description": "'301': Moved Permanently; '302': Found; '303': See Other; '307': Temporary Redirect; ", "format": "enum"}
    :param request_line_case_insensitive: {"default": 0, "optional": true, "type": "number", "description": "Parse http request line as case insensitive", "format": "flag"}
    :param url_hash_persist: {"default": 0, "optional": true, "type": "number", "description": "Use URL's hash value to select server", "format": "flag"}
    :param retry_on_5xx_per_req_val: {"description": "Number of times to retry (default is 3)", "format": "number", "default": 3, "optional": true, "maximum": 3, "minimum": 1, "type": "number"}
    :param bypass_sg: {"description": "Select service group for non-http traffic (Service Group Name)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 127, "type": "string", "$ref": "/axapi/v3/slb/service-group"}
    :param name: {"description": "HTTP Template Name", "format": "string-rlx", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param retry_on_5xx_val: {"description": "Number of times to retry (default is 3)", "format": "number", "default": 3, "optional": true, "maximum": 3, "minimum": 1, "type": "number"}
    :param url_hash_first: {"description": "Use the begining part of URL to calculate hash value (URL string length to calculate hash value)", "format": "number", "optional": true, "maximum": 128, "minimum": 4, "not": "url-hash-last", "type": "number"}
    :param compression_keep_accept_encoding_enable: {"default": 0, "optional": true, "type": "number", "description": "Enable Server Accept Encoding", "format": "flag"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param client_ip_hdr_replace: {"default": 0, "optional": true, "type": "number", "description": "Replace the existing header", "format": "flag"}
    :param compression_content_type: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "content-type": {"minLength": 1, "maxLength": 31, "type": "string", "description": "Compression content-type", "format": "string-rlx"}}}]}
    :param log_retry: {"default": 0, "optional": true, "type": "number", "description": "log when HTTP request retry", "format": "flag"}
    :param insert_client_ip_header_name: {"description": "HTTP Header Name for inserting Client IP", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param compression_exclude_uri: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "exclude-uri": {"minLength": 1, "maxLength": 31, "type": "string", "description": "Compression exclude uri", "format": "string-rlx"}}}]}
    :param retry_on_5xx: {"description": "Retry http request on HTTP 5xx code", "format": "flag", "default": 0, "optional": true, "not": "retry-on-5xx-per-req", "type": "number"}
    :param term_11client_hdr_conn_close: {"default": 0, "optional": true, "type": "number", "description": "Terminate HTTP 1.1 client when req has Connection: close", "format": "flag"}
    :param compression_exclude_content_type: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"exclude-content-type": {"minLength": 1, "maxLength": 31, "type": "string", "description": "Compression exclude content-type (Compression exclude content type)", "format": "string-rlx"}, "optional": true}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/template/http/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "http"
        self.a10_url="/axapi/v3/slb/template/http/{name}"
        self.DeviceProxy = ""
        self.keep_client_alive = ""
        self.compression_auto_disable_on_high_cpu = ""
        self.req_hdr_wait_time = ""
        self.request_header_erase_list = []
        self.compression_enable = ""
        self.compression_keep_accept_encoding = ""
        self.failover_url = ""
        self.redirect_rewrite = {}
        self.compression_level = ""
        self.rd_port = ""
        self.insert_client_port_header_name = ""
        self.url_hash_last = ""
        self.use_server_status = ""
        self.req_hdr_wait_time_val = ""
        self.response_header_insert_list = []
        self.redirect = ""
        self.insert_client_port = ""
        self.retry_on_5xx_per_req = ""
        self.url_hash_offset = ""
        self.rd_simple_loc = ""
        self.client_port_hdr_replace = ""
        self.non_http_bypass = ""
        self.response_header_erase_list = []
        self.insert_client_ip = ""
        self.template = {}
        self.url_switching = []
        self.rd_secure = ""
        self.host_switching = []
        self.strict_transaction_switch = ""
        self.response_content_replace_list = []
        self.request_header_insert_list = []
        self.compression_minimum_content_length = ""
        self.rd_resp_code = ""
        self.request_line_case_insensitive = ""
        self.url_hash_persist = ""
        self.retry_on_5xx_per_req_val = ""
        self.bypass_sg = ""
        self.name = ""
        self.retry_on_5xx_val = ""
        self.url_hash_first = ""
        self.compression_keep_accept_encoding_enable = ""
        self.uuid = ""
        self.client_ip_hdr_replace = ""
        self.compression_content_type = []
        self.log_retry = ""
        self.insert_client_ip_header_name = ""
        self.compression_exclude_uri = []
        self.retry_on_5xx = ""
        self.term_11client_hdr_conn_close = ""
        self.compression_exclude_content_type = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


