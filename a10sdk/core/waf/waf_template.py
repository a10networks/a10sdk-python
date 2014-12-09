from a10sdk.common.A10BaseClass import A10BaseClass


class Template(A10BaseClass):
    
    """Class Description::
    WAF template.

    Class template supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param log_succ_reqs: {"default": 0, "optional": true, "type": "number", "description": "Log successful waf requests", "format": "flag"}
    :param keep_end: {"description": "Number of unmasked characters at the end (default: 0)", "format": "number", "type": "number", "maximum": 65535, "minimum": 0, "optional": true}
    :param max_cookie_len: {"description": "Max Cookie length allowed in request (default 4096) (Maximum length of cookie allowed (default 4096))", "format": "number", "default": 4096, "optional": true, "maximum": 65535, "minimum": 0, "type": "number"}
    :param deploy_mode: {"description": "'active': Deploy WAF in active (blocking) mode; 'passive': Deploy WAF in passive (log-only) mode; 'learning': Deploy WAF in learning mode; ", "format": "enum", "default": "active", "type": "string", "enum": ["active", "passive", "learning"], "optional": true}
    :param xml_format_check: {"default": 0, "optional": true, "type": "number", "description": "Check HTTP body for XML format compliance", "format": "flag"}
    :param max_string: {"description": "Maximum length of a string in a JSON request body (default 64) (Maximum length of a JSON string (default 64))", "format": "number", "default": 64, "optional": true, "maximum": 4096, "minimum": 0, "type": "number"}
    :param ccn_mask: {"default": 0, "optional": true, "type": "number", "description": "Mask credit card numbers in response", "format": "flag"}
    :param waf_blist_file: {"description": "Name of WAF policy list file", "format": "string", "minLength": 1, "optional": true, "maxLength": 128, "type": "string"}
    :param form_set_no_cache: {"default": 0, "optional": true, "type": "number", "description": "Disable caching of form-containing responses", "format": "flag"}
    :param http_redirect: {"description": "Send HTTP redirect response (302 Found) to specifed URL (URL to redirect to when denying request)", "format": "string-rlx", "minLength": 1, "not-list": ["http-resp-200", "reset-conn", "http-resp-403"], "optional": true, "maxLength": 255, "type": "string"}
    :param bot_check: {"default": 0, "optional": true, "type": "number", "description": "Check User-Agent for known bots", "format": "flag"}
    :param max_cookies_len: {"description": "Max Total Cookies length allowed in request (default 4096) (Maximum total length of cookies allowed (default 4096))", "format": "number", "default": 4096, "optional": true, "maximum": 65535, "minimum": 0, "type": "number"}
    :param url_check: {"default": 0, "optional": true, "type": "number", "description": "Check URL against list of previously learned URLs", "format": "flag"}
    :param max_parameter_value_len: {"description": "Max HTML parameter value length in an HTTP request (default 4096) (Maximum HTML parameter value in an HTTP request (default 4096))", "format": "number", "default": 4096, "optional": true, "maximum": 102400000, "minimum": 0, "type": "number"}
    :param max_entities: {"description": "Maximum number of MIME entities allowed in request (default 10)", "format": "number", "default": 10, "optional": true, "maximum": 63, "minimum": 0, "type": "number"}
    :param hide_resp_codes: {"default": 0, "optional": true, "type": "number", "description": "Hides response codes that are not allowed (default 4xx, 5xx)", "format": "flag"}
    :param max_depth: {"description": "Maximum recursion depth in a value in a JSON requesnt body (default 16) (Maximum recursion depth in a JSON value (default 16))", "format": "number", "default": 16, "optional": true, "maximum": 4096, "minimum": 0, "type": "number"}
    :param hide_resp_codes_file: {"description": "Name of WAF policy list file", "format": "string", "minLength": 1, "optional": true, "maxLength": 128, "type": "string"}
    :param max_elem_name_len: {"description": "Maximum length for an element name (default 128)", "format": "number", "default": 128, "optional": true, "maximum": 65535, "minimum": 0, "type": "number"}
    :param deny_password_autocomplete: {"default": 0, "optional": true, "type": "number", "description": "Check to protect against server-generated form which contain password fields that allow autocomplete", "format": "flag"}
    :param name: {"description": "WAF Template Name", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param http_resp_200: {"description": "Send HTTP response with status code 200 OK", "format": "flag", "default": 0, "optional": true, "not-list": ["http-redirect", "reset-conn", "http-resp-403"], "type": "number"}
    :param keep_start: {"description": "Number of unmasked characters at the beginning (default: 0)", "format": "number", "type": "number", "maximum": 65535, "minimum": 0, "optional": true}
    :param redirect_wlist: {"default": 0, "optional": true, "type": "number", "description": "Check Redirect URL against list of previously learned redirects", "format": "flag"}
    :param max_cookie_value_len: {"description": "Max Cookie Value length allowed in request (default 4096) (Maximum length of cookie value allowed (default 4096))", "format": "number", "default": 4096, "optional": true, "maximum": 65535, "minimum": 0, "type": "number"}
    :param max_cdata_len: {"description": "Maximum length of an CDATA section of an element (default 65535)", "format": "number", "default": 65535, "optional": true, "maximum": 65535, "minimum": 0, "type": "number"}
    :param max_hdr_value_len: {"description": "Max header value length allowed in request (default 4096) (Maximum length of header value allowed (default 4096))", "format": "number", "default": 4096, "optional": true, "maximum": 65535, "minimum": 0, "type": "number"}
    :param secret_encrypted: {"description": "Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED secret string)", "format": "encrypted", "minLength": 1, "optional": true, "maxLength": 255, "type": "encrypted"}
    :param cookie_name: {"description": "Cookie name (simple string or PCRE pattern)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param max_namespace_uri_len: {"description": "Maximum length of a namespace URI (default 256)", "format": "number", "default": 256, "optional": true, "maximum": 1024, "minimum": 0, "type": "number"}
    :param resp_url_403: {"description": "Response content to send client when denying request", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 255, "type": "string"}
    :param csrf_check: {"default": 0, "optional": true, "type": "number", "description": "Tag the form to protect against Cross-site Request Forgery", "format": "flag"}
    :param referer_domain_list: {"description": "List of referer domains allowed", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 255, "not": "referer-domain-list-only", "type": "string"}
    :param max_parameters: {"description": "Maximum number of HTML parameters allowed in request (default 64)", "format": "number", "default": 64, "optional": true, "maximum": 1024, "minimum": 0, "type": "number"}
    :param max_parameter_name_len: {"description": "Max HTML parameter name length in an HTTP request (default 256) (Maximum HTML parameter name length in an HTTP request (default 256))", "format": "number", "default": 256, "optional": true, "maximum": 1024, "minimum": 0, "type": "number"}
    :param deny_non_masked_passwords: {"default": 0, "optional": true, "type": "number", "description": "Denies forms that have a password field with a textual type, resulting in this field not being masked", "format": "flag"}
    :param max_hdr_name_len: {"description": "Max header name length allowed in request (default 63) (Maximum length of header name allowed (default 63))", "format": "number", "default": 63, "optional": true, "maximum": 63, "minimum": 0, "type": "number"}
    :param max_elem_depth: {"description": "Maximum recursion level for element definition (default 256)", "format": "number", "default": 256, "optional": true, "maximum": 4096, "minimum": 0, "type": "number"}
    :param form_consistency_check: {"default": 0, "optional": true, "type": "number", "description": "Form input consistency check", "format": "flag"}
    :param max_hdrs: {"description": "Maximum number of headers allowed in request (default 20)", "format": "number", "default": 20, "optional": true, "maximum": 255, "minimum": 0, "type": "number"}
    :param xml_xss_check: {"default": 0, "optional": true, "type": "number", "description": "Check XML data against XSS policy", "format": "flag"}
    :param referer_check: {"default": 0, "optional": true, "type": "number", "description": "Check referer to protect against CSRF attacks", "format": "flag"}
    :param wsdl_resp_val_file: {"description": "Specify name of WSDL file for verifying XML body contents", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "not": "wsdl-file", "type": "string"}
    :param logging: {"description": "Logging template (Logging Config name)", "format": "string", "minLength": 1, "optional": true, "maxLength": 128, "type": "string", "$ref": "/axapi/v3/slb/template/logging"}
    :param max_namespace: {"description": "Maximum number of namespace declarations (default 16)", "format": "number", "default": 16, "optional": true, "maximum": 256, "minimum": 0, "type": "number"}
    :param max_entity_exp: {"description": "Maximum number of entity expansions (default 1024)", "format": "number", "default": 1024, "optional": true, "maximum": 1024, "minimum": 0, "type": "number"}
    :param form_deny_non_post: {"default": 0, "optional": true, "type": "number", "description": "Deny request with forms if the method is not POST", "format": "flag"}
    :param cookie_encryption_secret: {"description": "Cookie encryption secret", "format": "password", "minLength": 1, "optional": true, "maxLength": 128, "type": "string"}
    :param decode_escaped_chars: {"default": 0, "optional": true, "type": "number", "description": "Decode escaped characters such as \\r \\n \\\" \\xXX \\u00YY in internal url", "format": "flag"}
    :param json_format_check: {"default": 0, "optional": true, "type": "number", "description": "Check HTTP body for JSON format compliance", "format": "flag"}
    :param bot_check_policy_file: {"description": "Name of WAF policy list file", "format": "string", "minLength": 1, "optional": true, "maxLength": 128, "type": "string"}
    :param xml_schema_resp_val_file: {"description": "Specify name of XML-Schema file for verifying XML body contents", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "not": "xml-schema-file", "type": "string"}
    :param allowed_http_methods: {"description": "List of allowed HTTP methods. Default is \"GET POST\". (List of HTTP methods allowed (default \"GET POST\"))", "format": "string-rlx", "default": "GET POST", "minLength": 1, "optional": true, "maxLength": 255, "type": "string"}
    :param remove_selfref: {"default": 0, "optional": true, "type": "number", "description": "Remove self-references such as /./ and /path/../ from internal url", "format": "flag"}
    :param max_elem_child: {"description": "Maximum number of children of an XML element (default 1024)", "format": "number", "default": 1024, "optional": true, "maximum": 4096, "minimum": 0, "type": "number"}
    :param max_entity_exp_depth: {"description": "Maximum nested depth of entity expansion (default 32)", "format": "number", "default": 32, "optional": true, "maximum": 32, "minimum": 0, "type": "number"}
    :param max_array_value_count: {"description": "Maximum number of values in an array in a JSON request body (default 256) (Maximum number of values in a JSON array (default 256))", "format": "number", "default": 256, "optional": true, "maximum": 4096, "minimum": 0, "type": "number"}
    :param max_elem: {"description": "Maximum number of XML elements (default 1024)", "format": "number", "default": 1024, "optional": true, "maximum": 8192, "minimum": 0, "type": "number"}
    :param sqlia_check: {"optional": true, "enum": ["reject", "sanitize"], "type": "string", "description": "'reject': Reject requests with SQLIA patterns; 'sanitize': Remove bad SQL from request; ", "format": "enum"}
    :param max_object_member_count: {"description": "Maximum number of members in an object in a JSON request body (default 256) (Maximum number of members in a JSON object (default 256))", "format": "number", "default": 256, "optional": true, "maximum": 4096, "minimum": 0, "type": "number"}
    :param http_resp_403: {"description": "Send HTTP response with status code 403 Forbidden (default)", "format": "flag", "default": 0, "optional": true, "not-list": ["http-redirect", "http-resp-200", "reset-conn"], "type": "number"}
    :param http_check: {"default": 0, "optional": true, "type": "number", "description": "Check request for HTTP protocol compliance", "format": "flag"}
    :param max_cookie_name_len: {"description": "Max Cookie Name length allowed in request (default 64) ( Maximum length of cookie name allowed (default 64))", "format": "number", "default": 64, "optional": true, "maximum": 65535, "minimum": 0, "type": "number"}
    :param remove_comments: {"default": 0, "optional": true, "type": "number", "description": "Remove comments from internal url", "format": "flag"}
    :param uri_wlist_check: {"default": 0, "optional": true, "type": "number", "description": "specify name of WAF policy list file to whitelist", "format": "flag"}
    :param form_deny_non_ssl: {"default": 0, "optional": true, "type": "number", "description": "Deny request with forms if the protocol is not SSL", "format": "flag"}
    :param xss_check: {"optional": true, "enum": ["reject", "sanitize"], "type": "string", "description": "'reject': Reject requests with bad cookies; 'sanitize': Remove bad cookies from request; ", "format": "enum"}
    :param reset_conn: {"description": "Reset the client connection", "format": "flag", "default": 0, "optional": true, "not-list": ["http-redirect", "http-resp-200", "http-resp-403"], "type": "number"}
    :param referer_safe_url: {"description": " Safe URL to redirect to if referer is missing", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 255, "type": "string"}
    :param max_attr_name_len: {"description": "Maximum length of an attribute name (default 128)", "format": "number", "default": 128, "optional": true, "maximum": 2048, "minimum": 0, "type": "number"}
    :param uri_blist_check: {"default": 0, "optional": true, "type": "number", "description": "specify name of WAF policy list file to blacklist", "format": "flag"}
    :param max_url_len: {"description": "Max URL length allowed in request (default 1024) (Maximum length of URL allowed (default 1024))", "format": "number", "default": 1024, "optional": true, "maximum": 16127, "minimum": 0, "type": "number"}
    :param max_hdrs_len: {"description": "Max headers length allowed in request (default 4096) (Maximum length of headers allowed (default 4096))", "format": "number", "default": 4096, "optional": true, "maximum": 65535, "minimum": 0, "type": "number"}
    :param waf_wlist_file: {"description": "Name of WAF policy list file", "format": "string", "minLength": 1, "optional": true, "maxLength": 128, "type": "string"}
    :param remove_spaces: {"default": 0, "optional": true, "type": "number", "description": "Remove spaces from internal url", "format": "flag"}
    :param lifetime: {"description": "Session lifetime in minutes (default 10)", "format": "number", "type": "number", "maximum": 1440, "minimum": 1, "optional": true}
    :param max_attr: {"description": "Maximum number of attributes of an XML element (default 256)", "format": "number", "default": 256, "optional": true, "maximum": 256, "minimum": 0, "type": "number"}
    :param xss_check_policy_file: {"description": "Name of WAF policy list file", "format": "string", "minLength": 1, "optional": true, "maxLength": 128, "type": "string"}
    :param resp_url_200: {"description": "Response content to send client when denying request", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 255, "type": "string"}
    :param max_post_size: {"description": "Max content length allowed in POST request (default 20480) (Maximum size allowed content in an HTTP POST request (default 20480))", "format": "number", "default": 20480, "optional": true, "maximum": 2147483647, "minimum": 0, "type": "number"}
    :param decode_hex_chars: {"default": 0, "optional": true, "type": "number", "description": "Decode hex chars such as \\%xx and \\%u00yy in internal url", "format": "flag"}
    :param max_line_len: {"description": "Max Line length allowed in request (default 1024) (Maximum length of Request line allowed (default 1024))", "format": "number", "default": 1024, "optional": true, "maximum": 16127, "minimum": 0, "type": "number"}
    :param max_query_len: {"description": "Max Query length allowed in request (default 1024) (Maximum length of Request query allowed (default 1024))", "format": "number", "default": 1024, "optional": true, "maximum": 16127, "minimum": 0, "type": "number"}
    :param sqlia_check_policy_file: {"description": "Name of WAF policy list file", "format": "string", "minLength": 1, "optional": true, "maxLength": 128, "type": "string"}
    :param deny_non_ssl_passwords: {"default": 0, "optional": true, "type": "number", "description": "Denies any form that has a password field if the form is not sent over an SSL connection", "format": "flag"}
    :param max_data_parse: {"description": "Max data parsed for Web Application Firewall (default 65536) (Maximum data parsed for Web Application Firewall (default 65536))", "format": "number", "default": 65536, "optional": true, "maximum": 1048575, "minimum": 0, "type": "number"}
    :param max_parameter_total_len: {"description": "Max HTML parameter tatal length in an HTTP request (default 4096) (Maximum HTML parameter total length in an HTTP request (default 4096))", "format": "number", "default": 4096, "optional": true, "maximum": 102400000, "minimum": 0, "type": "number"}
    :param wsdl_file: {"description": "Specify name of WSDL file for verifying XML body contents", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "not": "wsdl-resp-val-file", "type": "string"}
    :param session_check: {"default": 0, "optional": true, "type": "number", "description": "Enable session checking via session cookie", "format": "flag"}
    :param disable: {"default": 0, "optional": true, "type": "number", "description": "Disable buffer overflow protection", "format": "flag"}
    :param filter_resp_hdrs: {"default": 0, "optional": true, "type": "number", "description": "Removes web server's identifying headers", "format": "flag"}
    :param max_cookies: {"description": "Maximum number of cookies allowed in request (default 20)", "format": "number", "default": 20, "optional": true, "maximum": 63, "minimum": 0, "type": "number"}
    :param decode_entities: {"default": 0, "optional": true, "type": "number", "description": "Decode entities in internal url", "format": "flag"}
    :param mask: {"description": "Character to mask the matched pattern (default: X)", "format": "string", "minLength": 1, "optional": true, "maxLength": 1, "type": "string"}
    :param referer_domain_list_only: {"description": "List of referer domains allowed", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 255, "not": "referer-domain-list", "type": "string"}
    :param max_attr_value_len: {"description": "Maximum length of an attribute text value (default 128)", "format": "number", "default": 128, "optional": true, "maximum": 4096, "minimum": 0, "type": "number"}
    :param pcre_mask: {"description": "Mask matched PCRE pattern in response", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param soap_format_check: {"default": 0, "optional": true, "type": "number", "description": "Check XML document for SOAP format compliance", "format": "flag"}
    :param xml_schema_file: {"description": "Specify name of XML-Schema file for verifying XML body contents", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "not": "xml-schema-resp-val-file", "type": "string"}
    :param ssn_mask: {"default": 0, "optional": true, "type": "number", "description": "Mask US Social Security numbers in response", "format": "flag"}
    :param xml_sqlia_check: {"default": 0, "optional": true, "type": "number", "description": "Check XML data against SQLIA policy", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/waf/template/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "template"
        self.a10_url="/axapi/v3/waf/template/{name}"
        self.DeviceProxy = ""
        self.log_succ_reqs = ""
        self.keep_end = ""
        self.max_cookie_len = ""
        self.deploy_mode = ""
        self.xml_format_check = ""
        self.max_string = ""
        self.ccn_mask = ""
        self.waf_blist_file = ""
        self.form_set_no_cache = ""
        self.http_redirect = ""
        self.bot_check = ""
        self.max_cookies_len = ""
        self.url_check = ""
        self.max_parameter_value_len = ""
        self.max_entities = ""
        self.hide_resp_codes = ""
        self.max_depth = ""
        self.hide_resp_codes_file = ""
        self.max_elem_name_len = ""
        self.deny_password_autocomplete = ""
        self.name = ""
        self.http_resp_200 = ""
        self.keep_start = ""
        self.redirect_wlist = ""
        self.max_cookie_value_len = ""
        self.max_cdata_len = ""
        self.max_hdr_value_len = ""
        self.secret_encrypted = ""
        self.cookie_name = ""
        self.max_namespace_uri_len = ""
        self.resp_url_403 = ""
        self.csrf_check = ""
        self.referer_domain_list = ""
        self.max_parameters = ""
        self.max_parameter_name_len = ""
        self.deny_non_masked_passwords = ""
        self.max_hdr_name_len = ""
        self.max_elem_depth = ""
        self.form_consistency_check = ""
        self.max_hdrs = ""
        self.xml_xss_check = ""
        self.referer_check = ""
        self.wsdl_resp_val_file = ""
        self.logging = ""
        self.max_namespace = ""
        self.max_entity_exp = ""
        self.form_deny_non_post = ""
        self.cookie_encryption_secret = ""
        self.decode_escaped_chars = ""
        self.json_format_check = ""
        self.bot_check_policy_file = ""
        self.xml_schema_resp_val_file = ""
        self.allowed_http_methods = ""
        self.remove_selfref = ""
        self.max_elem_child = ""
        self.max_entity_exp_depth = ""
        self.max_array_value_count = ""
        self.max_elem = ""
        self.sqlia_check = ""
        self.max_object_member_count = ""
        self.http_resp_403 = ""
        self.http_check = ""
        self.max_cookie_name_len = ""
        self.remove_comments = ""
        self.uri_wlist_check = ""
        self.form_deny_non_ssl = ""
        self.xss_check = ""
        self.reset_conn = ""
        self.referer_safe_url = ""
        self.max_attr_name_len = ""
        self.uri_blist_check = ""
        self.max_url_len = ""
        self.max_hdrs_len = ""
        self.waf_wlist_file = ""
        self.remove_spaces = ""
        self.lifetime = ""
        self.max_attr = ""
        self.xss_check_policy_file = ""
        self.resp_url_200 = ""
        self.max_post_size = ""
        self.decode_hex_chars = ""
        self.max_line_len = ""
        self.max_query_len = ""
        self.sqlia_check_policy_file = ""
        self.deny_non_ssl_passwords = ""
        self.max_data_parse = ""
        self.max_parameter_total_len = ""
        self.wsdl_file = ""
        self.session_check = ""
        self.disable = ""
        self.filter_resp_hdrs = ""
        self.max_cookies = ""
        self.decode_entities = ""
        self.mask = ""
        self.referer_domain_list_only = ""
        self.max_attr_value_len = ""
        self.pcre_mask = ""
        self.soap_format_check = ""
        self.xml_schema_file = ""
        self.ssn_mask = ""
        self.xml_sqlia_check = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


