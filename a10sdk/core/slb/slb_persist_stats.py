from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ssl_sid_session_ok: {"description": "Create SSL SID ok", "format": "counter", "type": "number", "oid": "47", "optional": true, "size": "8"}
    :param sssl_sid_not_match: {"description": "Server SSL SID not match", "format": "counter", "type": "number", "oid": "44", "optional": true, "size": "8"}
    :param cookie_invalid: {"description": "Invalid persist cookie", "format": "counter", "type": "number", "oid": "53", "optional": true, "size": "8"}
    :param cookie_persist_fail: {"description": "Cookie persist fail", "format": "counter", "type": "number", "oid": "50", "optional": true, "size": "8"}
    :param url_hash_sec: {"description": "URL hash persist (sec)", "format": "counter", "type": "number", "oid": "9", "optional": true, "size": "8"}
    :param header_hash_pri: {"description": "Header hash persist(pri)", "format": "counter", "type": "number", "oid": "11", "optional": true, "size": "8"}
    :param src_ip_hash_pri: {"description": "SRC IP hash persist(pri)", "format": "counter", "type": "number", "oid": "22", "optional": true, "size": "8"}
    :param src_ip_new_sess_cache: {"description": "SRC IP new sess (cache)", "format": "counter", "type": "number", "oid": "18", "optional": true, "size": "8"}
    :param src_ip_new_sess_sel_fail: {"description": "SRC IP new sess fail (s)", "format": "counter", "type": "number", "oid": "21", "optional": true, "size": "8"}
    :param sssl_sid_match: {"description": "Server SSL SID match", "format": "counter", "type": "number", "oid": "43", "optional": true, "size": "8"}
    :param dst_ip_hash_sec: {"description": "DST IP hash persist(sec)", "format": "counter", "type": "number", "oid": "36", "optional": true, "size": "8"}
    :param src_ip_hash_sec: {"description": "SRC IP hash persist(sec)", "format": "counter", "type": "number", "oid": "24", "optional": true, "size": "8"}
    :param cookie_not_found: {"description": "Persist cookie not found", "format": "counter", "type": "number", "oid": "51", "optional": true, "size": "8"}
    :param dst_ip_new_sess_cache: {"description": "DST IP new sess (cache)", "format": "counter", "type": "number", "oid": "30", "optional": true, "size": "8"}
    :param cssl_sid_match: {"description": "Client SSL SID match", "format": "counter", "type": "number", "oid": "39", "optional": true, "size": "8"}
    :param hash_tbl_create_fail: {"description": "Hash tbl create fail", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "8"}
    :param dst_ip_new_sess_sel: {"description": "DST IP new sess (select)", "format": "counter", "type": "number", "oid": "32", "optional": true, "size": "8"}
    :param src_ip: {"description": "SRC IP persist ok", "format": "counter", "type": "number", "oid": "15", "optional": true, "size": "8"}
    :param ssl_sid_persist_fail: {"description": "SSL SID persist fail", "format": "counter", "type": "number", "oid": "46", "optional": true, "size": "8"}
    :param dst_ip_hash_fail: {"description": "DST IP hash persist fail", "format": "counter", "type": "number", "oid": "37", "optional": true, "size": "8"}
    :param hash_tbl_rst_adddel: {"description": "Hash tbl reset (add/del)", "format": "counter", "type": "number", "oid": "6", "optional": true, "size": "8"}
    :param cssl_sid_not_match: {"description": "Client SSL SID not match", "format": "counter", "type": "number", "oid": "40", "optional": true, "size": "8"}
    :param ssl_sid_session_fail: {"description": "Create SSL SID fail", "format": "counter", "type": "number", "oid": "48", "optional": true, "size": "8"}
    :param dst_ip_hash_pri: {"description": "DST IP hash persist(pri)", "format": "counter", "type": "number", "oid": "34", "optional": true, "size": "8"}
    :param url_hash_enqueue: {"description": "URL hash persist (enQ)", "format": "counter", "type": "number", "oid": "8", "optional": true, "size": "8"}
    :param hash_tbl_create_ok: {"description": "Hash tbl create ok", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "8"}
    :param cookie_pass_thru: {"description": "Persist cookie Pass-thru", "format": "counter", "type": "number", "oid": "52", "optional": true, "size": "8"}
    :param sssl_sid_reset: {"description": "Server SSL SID reset", "format": "counter", "type": "number", "oid": "42", "optional": true, "size": "8"}
    :param src_ip_new_sess_cache_fail: {"description": "SRC IP new sess fail (c)", "format": "counter", "type": "number", "oid": "19", "optional": true, "size": "8"}
    :param dst_ip_new_sess_sel_fail: {"description": "DST IP new sess fail (s)", "format": "counter", "type": "number", "oid": "33", "optional": true, "size": "8"}
    :param url_hash_pri: {"description": "URL hash persist (pri)", "format": "counter", "type": "number", "oid": "7", "optional": true, "size": "8"}
    :param url_hash_fail: {"description": "URL hash persist fail", "format": "counter", "type": "number", "oid": "10", "optional": true, "size": "8"}
    :param hash_tbl_free: {"description": "Hash tbl free", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "8"}
    :param src_ip_enforce: {"description": "Enforce higher priority", "format": "counter", "type": "number", "oid": "26", "optional": true, "size": "8"}
    :param hash_tbl_rst_updown: {"description": "Hash tbl reset (up/down)", "format": "counter", "type": "number", "oid": "5", "optional": true, "size": "8"}
    :param hash_tbl_trylock_fail: {"description": "Hash tbl lock fail", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}
    :param cssl_sid_not_found: {"description": "Client SSL SID not found", "format": "counter", "type": "number", "oid": "38", "optional": true, "size": "8"}
    :param dst_ip_hash_enqueue: {"description": "DST IP hash persist(enQ)", "format": "counter", "type": "number", "oid": "35", "optional": true, "size": "8"}
    :param header_hash_sec: {"description": "Header hash persist(sec)", "format": "counter", "type": "number", "oid": "13", "optional": true, "size": "8"}
    :param sssl_sid_not_found: {"description": "Server SSL SID not found", "format": "counter", "type": "number", "oid": "41", "optional": true, "size": "8"}
    :param src_ip_new_sess_sel: {"description": "SRC IP new sess (select)", "format": "counter", "type": "number", "oid": "20", "optional": true, "size": "8"}
    :param header_hash_fail: {"description": "Header hash persist fail", "format": "counter", "type": "number", "oid": "14", "optional": true, "size": "8"}
    :param dst_ip_fail: {"description": "DST IP persist fail", "format": "counter", "type": "number", "oid": "29", "optional": true, "size": "8"}
    :param src_ip_hash_enqueue: {"description": "SRC IP hash persist(enQ)", "format": "counter", "type": "number", "oid": "23", "optional": true, "size": "8"}
    :param header_hash_enqueue: {"description": "Header hash persist(enQ)", "format": "counter", "type": "number", "oid": "12", "optional": true, "size": "8"}
    :param src_ip_enqueue: {"description": "SRC IP persist enqueue", "format": "counter", "type": "number", "oid": "16", "optional": true, "size": "8"}
    :param src_ip_hash_fail: {"description": "SRC IP hash persist fail", "format": "counter", "type": "number", "oid": "25", "optional": true, "size": "8"}
    :param cookie_persist_ok: {"description": "Cookie persist ok", "format": "counter", "type": "number", "oid": "49", "optional": true, "size": "8"}
    :param dst_ip_enqueue: {"description": "DST IP persist enqueue", "format": "counter", "type": "number", "oid": "28", "optional": true, "size": "8"}
    :param dst_ip_new_sess_cache_fail: {"description": "DST IP new sess fail (c)", "format": "counter", "type": "number", "oid": "31", "optional": true, "size": "8"}
    :param dst_ip: {"description": "DST IP persist ok", "format": "counter", "type": "number", "oid": "27", "optional": true, "size": "8"}
    :param src_ip_fail: {"description": "SRC IP persist fail", "format": "counter", "type": "number", "oid": "17", "optional": true, "size": "8"}
    :param ssl_sid_persist_ok: {"description": "SSL SID persist ok", "format": "counter", "type": "number", "oid": "45", "optional": true, "size": "8"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.ssl_sid_session_ok = ""
        self.sssl_sid_not_match = ""
        self.cookie_invalid = ""
        self.cookie_persist_fail = ""
        self.url_hash_sec = ""
        self.header_hash_pri = ""
        self.src_ip_hash_pri = ""
        self.src_ip_new_sess_cache = ""
        self.src_ip_new_sess_sel_fail = ""
        self.sssl_sid_match = ""
        self.dst_ip_hash_sec = ""
        self.src_ip_hash_sec = ""
        self.cookie_not_found = ""
        self.dst_ip_new_sess_cache = ""
        self.cssl_sid_match = ""
        self.hash_tbl_create_fail = ""
        self.dst_ip_new_sess_sel = ""
        self.src_ip = ""
        self.ssl_sid_persist_fail = ""
        self.dst_ip_hash_fail = ""
        self.hash_tbl_rst_adddel = ""
        self.cssl_sid_not_match = ""
        self.ssl_sid_session_fail = ""
        self.dst_ip_hash_pri = ""
        self.url_hash_enqueue = ""
        self.hash_tbl_create_ok = ""
        self.cookie_pass_thru = ""
        self.sssl_sid_reset = ""
        self.src_ip_new_sess_cache_fail = ""
        self.dst_ip_new_sess_sel_fail = ""
        self.url_hash_pri = ""
        self.url_hash_fail = ""
        self.hash_tbl_free = ""
        self.src_ip_enforce = ""
        self.hash_tbl_rst_updown = ""
        self.hash_tbl_trylock_fail = ""
        self.cssl_sid_not_found = ""
        self.dst_ip_hash_enqueue = ""
        self.header_hash_sec = ""
        self.sssl_sid_not_found = ""
        self.src_ip_new_sess_sel = ""
        self.header_hash_fail = ""
        self.dst_ip_fail = ""
        self.src_ip_hash_enqueue = ""
        self.header_hash_enqueue = ""
        self.src_ip_enqueue = ""
        self.src_ip_hash_fail = ""
        self.cookie_persist_ok = ""
        self.dst_ip_enqueue = ""
        self.dst_ip_new_sess_cache_fail = ""
        self.dst_ip = ""
        self.src_ip_fail = ""
        self.ssl_sid_persist_ok = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Persist(A10BaseClass):
    
    """Class Description::
    Statistics for the object persist.

    Class persist supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/persist/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "persist"
        self.a10_url="/axapi/v3/slb/persist/stats"
        self.DeviceProxy = ""
        self.stats = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


