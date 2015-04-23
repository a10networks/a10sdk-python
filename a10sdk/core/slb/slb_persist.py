from a10sdk.common.A10BaseClass import A10BaseClass


class SamplingEnable(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param counters1: {"enum": ["all", "hash_tbl_trylock_fail", "hash_tbl_create_ok", "hash_tbl_create_fail", "hash_tbl_free", "hash_tbl_rst_updown", "hash_tbl_rst_adddel", "url_hash_pri", "url_hash_enqueue", "url_hash_sec", "url_hash_fail", "header_hash_pri", "header_hash_enqueue", "header_hash_sec", "header_hash_fail", "src_ip", "src_ip_enqueue", "src_ip_fail", "src_ip_new_sess_cache", "src_ip_new_sess_cache_fail", "src_ip_new_sess_sel", "src_ip_new_sess_sel_fail", "src_ip_hash_pri", "src_ip_hash_enqueue", "src_ip_hash_sec", "src_ip_hash_fail", "src_ip_enforce", "dst_ip", "dst_ip_enqueue", "dst_ip_fail", "dst_ip_new_sess_cache", "dst_ip_new_sess_cache_fail", "dst_ip_new_sess_sel", "dst_ip_new_sess_sel_fail", "dst_ip_hash_pri", "dst_ip_hash_enqueue", "dst_ip_hash_sec", "dst_ip_hash_fail", "cssl_sid_not_found", "cssl_sid_match", "cssl_sid_not_match", "sssl_sid_not_found", "sssl_sid_reset", "sssl_sid_match", "sssl_sid_not_match", "ssl_sid_persist_ok", "ssl_sid_persist_fail", "ssl_sid_session_ok", "ssl_sid_session_fail", "cookie_persist_ok", "cookie_persist_fail", "cookie_not_found", "cookie_pass_thru", "cookie_invalid"], "type": "string", "description": "'all': all; 'hash_tbl_trylock_fail': Hash tbl lock fail; 'hash_tbl_create_ok': Hash tbl create ok; 'hash_tbl_create_fail': Hash tbl create fail; 'hash_tbl_free': Hash tbl free; 'hash_tbl_rst_updown': Hash tbl reset (up/down); 'hash_tbl_rst_adddel': Hash tbl reset (add/del); 'url_hash_pri': URL hash persist (pri); 'url_hash_enqueue': URL hash persist (enQ); 'url_hash_sec': URL hash persist (sec); 'url_hash_fail': URL hash persist fail; 'header_hash_pri': Header hash persist(pri); 'header_hash_enqueue': Header hash persist(enQ); 'header_hash_sec': Header hash persist(sec); 'header_hash_fail': Header hash persist fail; 'src_ip': SRC IP persist ok; 'src_ip_enqueue': SRC IP persist enqueue; 'src_ip_fail': SRC IP persist fail; 'src_ip_new_sess_cache': SRC IP new sess (cache); 'src_ip_new_sess_cache_fail': SRC IP new sess fail (c); 'src_ip_new_sess_sel': SRC IP new sess (select); 'src_ip_new_sess_sel_fail': SRC IP new sess fail (s); 'src_ip_hash_pri': SRC IP hash persist(pri); 'src_ip_hash_enqueue': SRC IP hash persist(enQ); 'src_ip_hash_sec': SRC IP hash persist(sec); 'src_ip_hash_fail': SRC IP hash persist fail; 'src_ip_enforce': Enforce higher priority; 'dst_ip': DST IP persist ok; 'dst_ip_enqueue': DST IP persist enqueue; 'dst_ip_fail': DST IP persist fail; 'dst_ip_new_sess_cache': DST IP new sess (cache); 'dst_ip_new_sess_cache_fail': DST IP new sess fail (c); 'dst_ip_new_sess_sel': DST IP new sess (select); 'dst_ip_new_sess_sel_fail': DST IP new sess fail (s); 'dst_ip_hash_pri': DST IP hash persist(pri); 'dst_ip_hash_enqueue': DST IP hash persist(enQ); 'dst_ip_hash_sec': DST IP hash persist(sec); 'dst_ip_hash_fail': DST IP hash persist fail; 'cssl_sid_not_found': Client SSL SID not found; 'cssl_sid_match': Client SSL SID match; 'cssl_sid_not_match': Client SSL SID not match; 'sssl_sid_not_found': Server SSL SID not found; 'sssl_sid_reset': Server SSL SID reset; 'sssl_sid_match': Server SSL SID match; 'sssl_sid_not_match': Server SSL SID not match; 'ssl_sid_persist_ok': SSL SID persist ok; 'ssl_sid_persist_fail': SSL SID persist fail; 'ssl_sid_session_ok': Create SSL SID ok; 'ssl_sid_session_fail': Create SSL SID fail; 'cookie_persist_ok': Cookie persist ok; 'cookie_persist_fail': Cookie persist fail; 'cookie_not_found': Persist cookie not found; 'cookie_pass_thru': Persist cookie Pass-thru; 'cookie_invalid': Invalid persist cookie; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "sampling-enable"
        self.DeviceProxy = ""
        self.counters1 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Persist(A10BaseClass):
    
    """    :param sampling_enable: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "hash_tbl_trylock_fail", "hash_tbl_create_ok", "hash_tbl_create_fail", "hash_tbl_free", "hash_tbl_rst_updown", "hash_tbl_rst_adddel", "url_hash_pri", "url_hash_enqueue", "url_hash_sec", "url_hash_fail", "header_hash_pri", "header_hash_enqueue", "header_hash_sec", "header_hash_fail", "src_ip", "src_ip_enqueue", "src_ip_fail", "src_ip_new_sess_cache", "src_ip_new_sess_cache_fail", "src_ip_new_sess_sel", "src_ip_new_sess_sel_fail", "src_ip_hash_pri", "src_ip_hash_enqueue", "src_ip_hash_sec", "src_ip_hash_fail", "src_ip_enforce", "dst_ip", "dst_ip_enqueue", "dst_ip_fail", "dst_ip_new_sess_cache", "dst_ip_new_sess_cache_fail", "dst_ip_new_sess_sel", "dst_ip_new_sess_sel_fail", "dst_ip_hash_pri", "dst_ip_hash_enqueue", "dst_ip_hash_sec", "dst_ip_hash_fail", "cssl_sid_not_found", "cssl_sid_match", "cssl_sid_not_match", "sssl_sid_not_found", "sssl_sid_reset", "sssl_sid_match", "sssl_sid_not_match", "ssl_sid_persist_ok", "ssl_sid_persist_fail", "ssl_sid_session_ok", "ssl_sid_session_fail", "cookie_persist_ok", "cookie_persist_fail", "cookie_not_found", "cookie_pass_thru", "cookie_invalid"], "type": "string", "description": "'all': all; 'hash_tbl_trylock_fail': Hash tbl lock fail; 'hash_tbl_create_ok': Hash tbl create ok; 'hash_tbl_create_fail': Hash tbl create fail; 'hash_tbl_free': Hash tbl free; 'hash_tbl_rst_updown': Hash tbl reset (up/down); 'hash_tbl_rst_adddel': Hash tbl reset (add/del); 'url_hash_pri': URL hash persist (pri); 'url_hash_enqueue': URL hash persist (enQ); 'url_hash_sec': URL hash persist (sec); 'url_hash_fail': URL hash persist fail; 'header_hash_pri': Header hash persist(pri); 'header_hash_enqueue': Header hash persist(enQ); 'header_hash_sec': Header hash persist(sec); 'header_hash_fail': Header hash persist fail; 'src_ip': SRC IP persist ok; 'src_ip_enqueue': SRC IP persist enqueue; 'src_ip_fail': SRC IP persist fail; 'src_ip_new_sess_cache': SRC IP new sess (cache); 'src_ip_new_sess_cache_fail': SRC IP new sess fail (c); 'src_ip_new_sess_sel': SRC IP new sess (select); 'src_ip_new_sess_sel_fail': SRC IP new sess fail (s); 'src_ip_hash_pri': SRC IP hash persist(pri); 'src_ip_hash_enqueue': SRC IP hash persist(enQ); 'src_ip_hash_sec': SRC IP hash persist(sec); 'src_ip_hash_fail': SRC IP hash persist fail; 'src_ip_enforce': Enforce higher priority; 'dst_ip': DST IP persist ok; 'dst_ip_enqueue': DST IP persist enqueue; 'dst_ip_fail': DST IP persist fail; 'dst_ip_new_sess_cache': DST IP new sess (cache); 'dst_ip_new_sess_cache_fail': DST IP new sess fail (c); 'dst_ip_new_sess_sel': DST IP new sess (select); 'dst_ip_new_sess_sel_fail': DST IP new sess fail (s); 'dst_ip_hash_pri': DST IP hash persist(pri); 'dst_ip_hash_enqueue': DST IP hash persist(enQ); 'dst_ip_hash_sec': DST IP hash persist(sec); 'dst_ip_hash_fail': DST IP hash persist fail; 'cssl_sid_not_found': Client SSL SID not found; 'cssl_sid_match': Client SSL SID match; 'cssl_sid_not_match': Client SSL SID not match; 'sssl_sid_not_found': Server SSL SID not found; 'sssl_sid_reset': Server SSL SID reset; 'sssl_sid_match': Server SSL SID match; 'sssl_sid_not_match': Server SSL SID not match; 'ssl_sid_persist_ok': SSL SID persist ok; 'ssl_sid_persist_fail': SSL SID persist fail; 'ssl_sid_session_ok': Create SSL SID ok; 'ssl_sid_session_fail': Create SSL SID fail; 'cookie_persist_ok': Cookie persist ok; 'cookie_persist_fail': Cookie persist fail; 'cookie_not_found': Persist cookie not found; 'cookie_pass_thru': Persist cookie Pass-thru; 'cookie_invalid': Invalid persist cookie; ", "format": "enum"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Show persist statistics.

    Class persist supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/persist`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "persist"
        self.a10_url="/axapi/v3/slb/persist"
        self.DeviceProxy = ""
        self.sampling_enable = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


