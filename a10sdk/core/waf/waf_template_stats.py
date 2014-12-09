from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param redirect_wlist_fail: {"description": "Redirect Whitelist Failure", "format": "counter", "type": "number", "oid": "119", "optional": true, "size": "2"}
    :param cookie_encrypt_limit_exceeded: {"description": "Cookie Encrypt Limit Exceeded", "format": "counter", "type": "number", "oid": "43", "optional": true, "size": "2"}
    :param wsdl_succ: {"description": "WSDL Success", "format": "counter", "type": "number", "oid": "75", "optional": true, "size": "2"}
    :param sqlia_chk_url_succ: {"description": "SQLIA Check URL Success", "format": "counter", "type": "number", "oid": "47", "optional": true, "size": "2"}
    :param bot_check_succ: {"description": "Botnet Check Success", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "2"}
    :param buf_ovf_cookie_name_len_fail: {"description": "Buffer Overflow - Cookie Name Length Failure", "format": "counter", "type": "number", "oid": "98", "optional": true, "size": "2"}
    :param redirect_wlist_learn: {"description": "Redirect Whitelist Learn", "format": "counter", "type": "number", "oid": "120", "optional": true, "size": "2"}
    :param xml_limit_elem_child: {"description": "XML Limit Element Child", "format": "counter", "type": "number", "oid": "104", "optional": true, "size": "2"}
    :param buf_ovf_parameter_value_len_fail: {"description": "Buffer Overflow - HTML Parameter Value Length Failure", "format": "counter", "type": "number", "oid": "93", "optional": true, "size": "2"}
    :param ccn_mask_visa: {"description": "Credit Card Number Mask Visa", "format": "counter", "type": "number", "oid": "35", "optional": true, "size": "2"}
    :param xss_chk_cookie_succ: {"description": "XSS Check Cookie Success", "format": "counter", "type": "number", "oid": "53", "optional": true, "size": "2"}
    :param buf_ovf_cookies_len_fail: {"description": "Buffer Overflow - Cookies Length Failure", "format": "counter", "type": "number", "oid": "87", "optional": true, "size": "2"}
    :param redirect_wlist_succ: {"description": "Redirect Whitelist Success", "format": "counter", "type": "number", "oid": "118", "optional": true, "size": "2"}
    :param json_check_failure: {"description": "JSON Check Failure", "format": "counter", "type": "number", "oid": "82", "optional": true, "size": "2"}
    :param xss_chk_post_reject: {"description": "XSS Check Post Rejected", "format": "counter", "type": "number", "oid": "61", "optional": true, "size": "2"}
    :param xss_chk_url_reject: {"description": "XSS Check URL Rejected", "format": "counter", "type": "number", "oid": "58", "optional": true, "size": "2"}
    :param form_consistency_succ: {"description": "Form Consistency Success", "format": "counter", "type": "number", "oid": "6", "optional": true, "size": "2"}
    :param xml_limit_cdata_len: {"description": "XML Limit CData Length", "format": "counter", "type": "number", "oid": "102", "optional": true, "size": "2"}
    :param xml_check_failure: {"description": "XML Check Failure", "format": "counter", "type": "number", "oid": "84", "optional": true, "size": "2"}
    :param num_resets: {"description": "Number Resets", "format": "counter", "type": "number", "oid": "66", "optional": true, "size": "2"}
    :param referer_check_succ: {"description": "Referer Check Success", "format": "counter", "type": "number", "oid": "23", "optional": true, "size": "2"}
    :param sqlia_chk_post_succ: {"description": "SQLIA Check Post Success", "format": "counter", "type": "number", "oid": "50", "optional": true, "size": "2"}
    :param xss_chk_url_sanitize: {"description": "XSS Check URL Sanitized", "format": "counter", "type": "number", "oid": "57", "optional": true, "size": "2"}
    :param cookie_encrypt_succ: {"description": "Cookie Encrypt Success", "format": "counter", "type": "number", "oid": "41", "optional": true, "size": "2"}
    :param buf_ovf_parameter_total_len_fail: {"description": "Buffer Overflow - HTML Parameter Total Length Failure", "format": "counter", "type": "number", "oid": "94", "optional": true, "size": "2"}
    :param soap_check_succ: {"description": "Soap Check Success", "format": "counter", "type": "number", "oid": "72", "optional": true, "size": "2"}
    :param max_cookies_fail: {"description": "Max Cookies Failure", "format": "counter", "type": "number", "oid": "17", "optional": true, "size": "2"}
    :param json_limit_array_value_count: {"description": "JSON Limit Array Value Count", "format": "counter", "type": "number", "oid": "111", "optional": true, "size": "2"}
    :param xml_limit_entity_exp_depth: {"description": "XML Limit Entity Exp Depth", "format": "counter", "type": "number", "oid": "108", "optional": true, "size": "2"}
    :param json_check_succ: {"description": "JSON Check Success", "format": "counter", "type": "number", "oid": "83", "optional": true, "size": "2"}
    :param resp_code_hidden: {"description": "Response Code Hidden", "format": "counter", "type": "number", "oid": "62", "optional": true, "size": "2"}
    :param xml_sqlia_chk_fail: {"description": "XML Sqlia Check Failure", "format": "counter", "type": "number", "oid": "78", "optional": true, "size": "2"}
    :param xss_chk_post_succ: {"description": "XSS Check Post Success", "format": "counter", "type": "number", "oid": "59", "optional": true, "size": "2"}
    :param form_consistency_fail: {"description": "Form Consistency Failure", "format": "counter", "type": "number", "oid": "7", "optional": true, "size": "2"}
    :param http_check_fail: {"description": "Http Check Failure", "format": "counter", "type": "number", "oid": "22", "optional": true, "size": "2"}
    :param url_check_succ: {"description": "URL Check Success", "format": "counter", "type": "number", "oid": "10", "optional": true, "size": "2"}
    :param sqlia_chk_url_sanitize: {"description": "SQLIA Check URL Sanitized", "format": "counter", "type": "number", "oid": "48", "optional": true, "size": "2"}
    :param xss_chk_cookie_reject: {"description": "XSS Check Cookie Rejected", "format": "counter", "type": "number", "oid": "55", "optional": true, "size": "2"}
    :param max_entities_fail: {"description": "Max Entities Failure", "format": "counter", "type": "number", "oid": "96", "optional": true, "size": "2"}
    :param xml_limit_attr: {"description": "XML Limit Attribue", "format": "counter", "type": "number", "oid": "99", "optional": true, "size": "2"}
    :param http_method_check_fail: {"description": "Http Method Check Failure", "format": "counter", "type": "number", "oid": "20", "optional": true, "size": "2"}
    :param form_non_ssl_reject: {"description": "Form Non SSL Rejected", "format": "counter", "type": "number", "oid": "67", "optional": true, "size": "2"}
    :param xss_chk_post_sanitize: {"description": "XSS Check Post Sanitized", "format": "counter", "type": "number", "oid": "60", "optional": true, "size": "2"}
    :param form_set_no_cache: {"description": "Form Set No Cache", "format": "counter", "type": "number", "oid": "121", "optional": true, "size": "2"}
    :param xml_schema_succ: {"description": "XML Schema Success", "format": "counter", "type": "number", "oid": "77", "optional": true, "size": "2"}
    :param sqlia_chk_url_reject: {"description": "SQLIA Check URL Rejected", "format": "counter", "type": "number", "oid": "49", "optional": true, "size": "2"}
    :param xml_check_succ: {"description": "XML Check Success", "format": "counter", "type": "number", "oid": "85", "optional": true, "size": "2"}
    :param sess_check_none: {"description": "Session Check None", "format": "counter", "type": "number", "oid": "69", "optional": true, "size": "2"}
    :param xml_limit_namespace: {"description": "XML Limit Namespace", "format": "counter", "type": "number", "oid": "109", "optional": true, "size": "2"}
    :param wsdl_fail: {"description": "WSDL Failure", "format": "counter", "type": "number", "oid": "74", "optional": true, "size": "2"}
    :param post_form_check_succ: {"description": "Post Form Check Success", "format": "counter", "type": "number", "oid": "30", "optional": true, "size": "2"}
    :param buf_ovf_query_len_fail: {"description": "Buffer Overflow - Query Length Failure", "format": "counter", "type": "number", "oid": "95", "optional": true, "size": "2"}
    :param sqlia_chk_post_reject: {"description": "SQLIA Check Post Rejected", "format": "counter", "type": "number", "oid": "52", "optional": true, "size": "2"}
    :param form_password_autocomplete: {"description": "Form Password Autocomplete", "format": "counter", "type": "number", "oid": "117", "optional": true, "size": "2"}
    :param xml_xss_chk_fail: {"description": "XML XSS Check Failure", "format": "counter", "type": "number", "oid": "80", "optional": true, "size": "2"}
    :param buf_ovf_url_len_fail: {"description": "Buffer Overflow - URL Length Failure", "format": "counter", "type": "number", "oid": "13", "optional": true, "size": "2"}
    :param buf_ovf_cookie_len_fail: {"description": "Buffer Overflow - Cookie Length Failure", "format": "counter", "type": "number", "oid": "14", "optional": true, "size": "2"}
    :param form_csrf_tag_succ: {"description": "Form CSRF tag Success", "format": "counter", "type": "number", "oid": "8", "optional": true, "size": "2"}
    :param xss_chk_cookie_sanitize: {"description": "XSS Check Cookie Sanitized", "format": "counter", "type": "number", "oid": "54", "optional": true, "size": "2"}
    :param xml_limit_entity_exp: {"description": "XML Limit Entity Exp", "format": "counter", "type": "number", "oid": "107", "optional": true, "size": "2"}
    :param ccn_mask_diners: {"description": "Credit Card Number Mask Diners", "format": "counter", "type": "number", "oid": "34", "optional": true, "size": "2"}
    :param sess_check_succ: {"description": "Session Check Success", "format": "counter", "type": "number", "oid": "70", "optional": true, "size": "2"}
    :param json_limit_depth: {"description": "JSON Limit Depth", "format": "counter", "type": "number", "oid": "112", "optional": true, "size": "2"}
    :param cookie_encrypt_skip_rcache: {"description": "Cookie Encrypt Skip RCache", "format": "counter", "type": "number", "oid": "44", "optional": true, "size": "2"}
    :param learn_updates: {"description": "Learning Updates", "format": "counter", "type": "number", "oid": "64", "optional": true, "size": "2"}
    :param req_denied: {"description": "Requests Denied", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "2"}
    :param http_check_succ: {"description": "Http Check Success", "format": "counter", "type": "number", "oid": "21", "optional": true, "size": "2"}
    :param req_allowed: {"description": "Requests Allowed", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "2"}
    :param json_limit_object_member_count: {"description": "JSON Limit Object Number Count", "format": "counter", "type": "number", "oid": "113", "optional": true, "size": "2"}
    :param bot_check_fail: {"description": "Botnet Check Failure", "format": "counter", "type": "number", "oid": "5", "optional": true, "size": "2"}
    :param uri_wlist_fail: {"description": "URI White List Failure", "format": "counter", "type": "number", "oid": "27", "optional": true, "size": "2"}
    :param uri_blist_fail: {"description": "URI Black List Failure", "format": "counter", "type": "number", "oid": "29", "optional": true, "size": "2"}
    :param xml_limit_namespace_uri_len: {"description": "XML Limit Namespace URI Length", "format": "counter", "type": "number", "oid": "110", "optional": true, "size": "2"}
    :param sqlia_chk_post_sanitize: {"description": "SQLIA Check Post Sanitized", "format": "counter", "type": "number", "oid": "51", "optional": true, "size": "2"}
    :param ccn_mask_amex: {"description": "Credit Card Number Mask Amex", "format": "counter", "type": "number", "oid": "33", "optional": true, "size": "2"}
    :param num_drops: {"description": "Number Drops", "format": "counter", "type": "number", "oid": "65", "optional": true, "size": "2"}
    :param referer_check_fail: {"description": "Referer Check Failure", "format": "counter", "type": "number", "oid": "24", "optional": true, "size": "2"}
    :param post_form_check_sanitize: {"description": "Post Form Check Sanitized", "format": "counter", "type": "number", "oid": "31", "optional": true, "size": "2"}
    :param cookie_decrypt_succ: {"description": "Cookie Decrypt Success", "format": "counter", "type": "number", "oid": "45", "optional": true, "size": "2"}
    :param max_parameters_fail: {"description": "Max Parameters Failure", "format": "counter", "type": "number", "oid": "97", "optional": true, "size": "2"}
    :param url_check_fail: {"description": "URL Check Failure", "format": "counter", "type": "number", "oid": "11", "optional": true, "size": "2"}
    :param xml_schema_fail: {"description": "XML Schema Failure", "format": "counter", "type": "number", "oid": "76", "optional": true, "size": "2"}
    :param form_non_post_reject: {"description": "Form Non Post Rejected", "format": "counter", "type": "number", "oid": "68", "optional": true, "size": "2"}
    :param buf_ovf_hdrs_len_fail: {"description": "Buffer Overflow - Headers length Failure", "format": "counter", "type": "number", "oid": "15", "optional": true, "size": "2"}
    :param uri_wlist_succ: {"description": "URI White List Success", "format": "counter", "type": "number", "oid": "26", "optional": true, "size": "2"}
    :param form_non_masked_password: {"description": "Form Non Masked Password", "format": "counter", "type": "number", "oid": "115", "optional": true, "size": "2"}
    :param buf_ovf_line_len_fail: {"description": "Buffer Overflow - Line Length Failure", "format": "counter", "type": "number", "oid": "91", "optional": true, "size": "2"}
    :param ccn_mask_discover: {"description": "Credit Card Number Mask Discover", "format": "counter", "type": "number", "oid": "37", "optional": true, "size": "2"}
    :param ssn_mask: {"description": "Social Security Number Mask", "format": "counter", "type": "number", "oid": "39", "optional": true, "size": "2"}
    :param json_limit_string: {"description": "JSON Limit String", "format": "counter", "type": "number", "oid": "114", "optional": true, "size": "2"}
    :param resp_hdrs_filtered: {"description": "Response Headers Filtered", "format": "counter", "type": "number", "oid": "63", "optional": true, "size": "2"}
    :param ccn_mask_mastercard: {"description": "Credit Card Number Mask Mastercard", "format": "counter", "type": "number", "oid": "36", "optional": true, "size": "2"}
    :param xml_sqlia_chk_succ: {"description": "XML Sqlia Check Success", "format": "counter", "type": "number", "oid": "79", "optional": true, "size": "2"}
    :param max_hdrs_fail: {"description": "Max Headers Failure", "format": "counter", "type": "number", "oid": "18", "optional": true, "size": "2"}
    :param xml_limit_attr_name_len: {"description": "XML Limit Name Length", "format": "counter", "type": "number", "oid": "100", "optional": true, "size": "2"}
    :param form_non_ssl_password: {"description": "Form Non SSL Password", "format": "counter", "type": "number", "oid": "116", "optional": true, "size": "2"}
    :param buf_ovf_hdr_value_len_fail: {"description": "Buffer Overflow - Header Value Length Failure", "format": "counter", "type": "number", "oid": "89", "optional": true, "size": "2"}
    :param uri_blist_succ: {"description": "URI Black List Success", "format": "counter", "type": "number", "oid": "28", "optional": true, "size": "2"}
    :param sess_check_fail: {"description": "Session Check Failure", "format": "counter", "type": "number", "oid": "71", "optional": true, "size": "2"}
    :param buf_ovf_hdr_name_len_fail: {"description": "Buffer Overflow - Header Name Length Failure", "format": "counter", "type": "number", "oid": "88", "optional": true, "size": "2"}
    :param resp_denied: {"description": "Responses Denied", "format": "counter", "type": "number", "oid": "122", "optional": true, "size": "2"}
    :param pcre_mask: {"description": "PCRE Mask", "format": "counter", "type": "number", "oid": "40", "optional": true, "size": "2"}
    :param xml_limit_elem: {"description": "XML Limit Element", "format": "counter", "type": "number", "oid": "103", "optional": true, "size": "2"}
    :param buf_ovf_parameter_name_len_fail: {"description": "Buffer Overflow - HTML Parameter Name Length Failure", "format": "counter", "type": "number", "oid": "92", "optional": true, "size": "2"}
    :param xml_limit_attr_value_len: {"description": "XML Limit Value Length", "format": "counter", "type": "number", "oid": "101", "optional": true, "size": "2"}
    :param xml_limit_elem_depth: {"description": "XML Limit Element Depth", "format": "counter", "type": "number", "oid": "105", "optional": true, "size": "2"}
    :param ccn_mask_jcb: {"description": "Credit Card Number Mask Jcb", "format": "counter", "type": "number", "oid": "38", "optional": true, "size": "2"}
    :param cookie_decrypt_fail: {"description": "Cookie Decrypt Failure", "format": "counter", "type": "number", "oid": "46", "optional": true, "size": "2"}
    :param buf_ovf_cookie_value_len_fail: {"description": "Buffer Overflow - Cookie Value Length Failure", "format": "counter", "type": "number", "oid": "86", "optional": true, "size": "2"}
    :param buf_ovf_max_data_parse_fail: {"description": "Buffer Overflow - Max Data Parse Failure", "format": "counter", "type": "number", "oid": "90", "optional": true, "size": "2"}
    :param total_req: {"description": "Total Requests", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "2"}
    :param xml_limit_elem_name_len: {"description": "XML Limit Element Name Length", "format": "counter", "type": "number", "oid": "106", "optional": true, "size": "2"}
    :param url_check_learn: {"description": "URL Check Learn", "format": "counter", "type": "number", "oid": "12", "optional": true, "size": "2"}
    :param http_method_check_succ: {"description": "Http Method Check Success", "format": "counter", "type": "number", "oid": "19", "optional": true, "size": "2"}
    :param xss_chk_url_succ: {"description": "XSS Check URL Success", "format": "counter", "type": "number", "oid": "56", "optional": true, "size": "2"}
    :param referer_check_redirect: {"description": "Referer Check Redirect", "format": "counter", "type": "number", "oid": "25", "optional": true, "size": "2"}
    :param post_form_check_reject: {"description": "Post Form Check Rejected", "format": "counter", "type": "number", "oid": "32", "optional": true, "size": "2"}
    :param cookie_encrypt_fail: {"description": "Cookie Encrypt Failure", "format": "counter", "type": "number", "oid": "42", "optional": true, "size": "2"}
    :param soap_check_failure: {"description": "Soap Check Failure", "format": "counter", "type": "number", "oid": "73", "optional": true, "size": "2"}
    :param form_csrf_tag_fail: {"description": "Form CSRF tag Failure", "format": "counter", "type": "number", "oid": "9", "optional": true, "size": "2"}
    :param xml_xss_chk_succ: {"description": "XML XSS Check Success", "format": "counter", "type": "number", "oid": "81", "optional": true, "size": "2"}
    :param buf_ovf_post_size_fail: {"description": "Buffer Overflow - Post size Failure", "format": "counter", "type": "number", "oid": "16", "optional": true, "size": "2"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.redirect_wlist_fail = ""
        self.cookie_encrypt_limit_exceeded = ""
        self.wsdl_succ = ""
        self.sqlia_chk_url_succ = ""
        self.bot_check_succ = ""
        self.buf_ovf_cookie_name_len_fail = ""
        self.redirect_wlist_learn = ""
        self.xml_limit_elem_child = ""
        self.buf_ovf_parameter_value_len_fail = ""
        self.ccn_mask_visa = ""
        self.xss_chk_cookie_succ = ""
        self.buf_ovf_cookies_len_fail = ""
        self.redirect_wlist_succ = ""
        self.json_check_failure = ""
        self.xss_chk_post_reject = ""
        self.xss_chk_url_reject = ""
        self.form_consistency_succ = ""
        self.xml_limit_cdata_len = ""
        self.xml_check_failure = ""
        self.num_resets = ""
        self.referer_check_succ = ""
        self.sqlia_chk_post_succ = ""
        self.xss_chk_url_sanitize = ""
        self.cookie_encrypt_succ = ""
        self.buf_ovf_parameter_total_len_fail = ""
        self.soap_check_succ = ""
        self.max_cookies_fail = ""
        self.json_limit_array_value_count = ""
        self.xml_limit_entity_exp_depth = ""
        self.json_check_succ = ""
        self.resp_code_hidden = ""
        self.xml_sqlia_chk_fail = ""
        self.xss_chk_post_succ = ""
        self.form_consistency_fail = ""
        self.http_check_fail = ""
        self.url_check_succ = ""
        self.sqlia_chk_url_sanitize = ""
        self.xss_chk_cookie_reject = ""
        self.max_entities_fail = ""
        self.xml_limit_attr = ""
        self.http_method_check_fail = ""
        self.form_non_ssl_reject = ""
        self.xss_chk_post_sanitize = ""
        self.form_set_no_cache = ""
        self.xml_schema_succ = ""
        self.sqlia_chk_url_reject = ""
        self.xml_check_succ = ""
        self.sess_check_none = ""
        self.xml_limit_namespace = ""
        self.wsdl_fail = ""
        self.post_form_check_succ = ""
        self.buf_ovf_query_len_fail = ""
        self.sqlia_chk_post_reject = ""
        self.form_password_autocomplete = ""
        self.xml_xss_chk_fail = ""
        self.buf_ovf_url_len_fail = ""
        self.buf_ovf_cookie_len_fail = ""
        self.form_csrf_tag_succ = ""
        self.xss_chk_cookie_sanitize = ""
        self.xml_limit_entity_exp = ""
        self.ccn_mask_diners = ""
        self.sess_check_succ = ""
        self.json_limit_depth = ""
        self.cookie_encrypt_skip_rcache = ""
        self.learn_updates = ""
        self.req_denied = ""
        self.http_check_succ = ""
        self.req_allowed = ""
        self.json_limit_object_member_count = ""
        self.bot_check_fail = ""
        self.uri_wlist_fail = ""
        self.uri_blist_fail = ""
        self.xml_limit_namespace_uri_len = ""
        self.sqlia_chk_post_sanitize = ""
        self.ccn_mask_amex = ""
        self.num_drops = ""
        self.referer_check_fail = ""
        self.post_form_check_sanitize = ""
        self.cookie_decrypt_succ = ""
        self.max_parameters_fail = ""
        self.url_check_fail = ""
        self.xml_schema_fail = ""
        self.form_non_post_reject = ""
        self.buf_ovf_hdrs_len_fail = ""
        self.uri_wlist_succ = ""
        self.form_non_masked_password = ""
        self.buf_ovf_line_len_fail = ""
        self.ccn_mask_discover = ""
        self.ssn_mask = ""
        self.json_limit_string = ""
        self.resp_hdrs_filtered = ""
        self.ccn_mask_mastercard = ""
        self.xml_sqlia_chk_succ = ""
        self.max_hdrs_fail = ""
        self.xml_limit_attr_name_len = ""
        self.form_non_ssl_password = ""
        self.buf_ovf_hdr_value_len_fail = ""
        self.uri_blist_succ = ""
        self.sess_check_fail = ""
        self.buf_ovf_hdr_name_len_fail = ""
        self.resp_denied = ""
        self.pcre_mask = ""
        self.xml_limit_elem = ""
        self.buf_ovf_parameter_name_len_fail = ""
        self.xml_limit_attr_value_len = ""
        self.xml_limit_elem_depth = ""
        self.ccn_mask_jcb = ""
        self.cookie_decrypt_fail = ""
        self.buf_ovf_cookie_value_len_fail = ""
        self.buf_ovf_max_data_parse_fail = ""
        self.total_req = ""
        self.xml_limit_elem_name_len = ""
        self.url_check_learn = ""
        self.http_method_check_succ = ""
        self.xss_chk_url_succ = ""
        self.referer_check_redirect = ""
        self.post_form_check_reject = ""
        self.cookie_encrypt_fail = ""
        self.soap_check_failure = ""
        self.form_csrf_tag_fail = ""
        self.xml_xss_chk_succ = ""
        self.buf_ovf_post_size_fail = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Template(A10BaseClass):
    
    """Class Description::
    Statistics for the object template.

    Class template supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param name: {"description": "WAF Template Name", "format": "string", "minLength": 1, "oid": "1001", "optional": false, "maxLength": 63, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/waf/template/{name}/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "template"
        self.a10_url="/axapi/v3/waf/template/{name}/stats"
        self.DeviceProxy = ""
        self.stats = {}
        self.name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


