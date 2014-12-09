from a10sdk.common.A10BaseClass import A10BaseClass


class Ipv6(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param dns_ipv6_mapping_type: {"enum": ["addition", "answer", "exclusive", "replace"], "type": "string", "description": "'addition': Append Mapped Record in DNS Addition Section; 'answer': Append Mapped Record in DNS Answer Section; 'exclusive': Only return AAAA Record; 'replace': Replace Record with Mapped Record; ", "format": "enum"}
    :param dns_ipv6_option: {"enum": ["mix", "smart", "mapping"], "type": "string", "description": "'mix': Return both AAAA Record and A Record; 'smart': Return AAAA Record by DNS Query Type; 'mapping': Map A Record to AAAA Record; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ipv6"
        self.DeviceProxy = ""
        self.dns_ipv6_mapping_type = ""
        self.dns_ipv6_option = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class BlockValue(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param block_value: {"description": "Specify Type Number", "minimum": 1, "type": "number", "maximum": 255, "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "block-value"
        self.DeviceProxy = ""
        self.block_value = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class ProxyBlockPortRangeList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param proxy_block_range_from: {"type": "number", "description": "Specify Type Range (From)", "format": "number"}
    :param proxy_block_range_to: {"type": "number", "description": "To", "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "proxy-block-port-range-list"
        self.DeviceProxy = ""
        self.proxy_block_range_from = ""
        self.proxy_block_range_to = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Dns(A10BaseClass):
    
    """Class Description::
    DNS related policy.

    Class dns supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param external_soa: {"default": 0, "optional": true, "type": "number", "description": "Return DNS response with external SOA Record", "format": "flag"}
    :param server_sec: {"default": 0, "optional": true, "type": "number", "description": "Provide DNSSEC support", "format": "flag"}
    :param sticky_ipv6_mask: {"description": "Specify IPv6 mask length, default is 128", "format": "number", "default": 128, "optional": true, "maximum": 128, "minimum": 1, "type": "number"}
    :param sticky: {"default": 0, "optional": true, "type": "number", "description": "Make DNS Record sticky for certain time", "format": "flag"}
    :param delegation: {"default": 0, "optional": true, "type": "number", "description": "Zone Delegation", "format": "flag"}
    :param active_only_fail_safe: {"default": 0, "optional": true, "type": "number", "description": "Continue if no candidate", "format": "flag"}
    :param cname_detect: {"default": 1, "optional": true, "type": "number", "description": "Apply GSLB for DNS Server response when service is Canonical Name (CNAME)", "format": "flag"}
    :param ttl: {"description": "Specify the TTL value contained in DNS record (TTL value, unit: second, default is 10)", "format": "number", "default": 10, "optional": true, "maximum": 1000000000, "minimum": 0, "not": "use-server-ttl", "type": "number"}
    :param server_full_list: {"default": 0, "optional": true, "type": "number", "description": "Append All A Records in Authoritative Section", "format": "flag"}
    :param server_ptr: {"default": 0, "optional": true, "type": "number", "description": "Provide PTR Records", "format": "flag"}
    :param selected_only: {"default": 0, "optional": true, "type": "number", "description": "Only keep selected servers", "format": "flag"}
    :param dns_addition_mx: {"default": 0, "optional": true, "type": "number", "description": "Append MX Records in Addition Section", "format": "flag"}
    :param block_type: {"optional": true, "enum": ["a", "aaaa", "ns", "mx", "srv", "cname", "ptr", "soa", "txt"], "type": "string", "format": "enum-list"}
    :param backup_alias: {"default": 0, "optional": true, "type": "number", "description": "Return alias name when fail", "format": "flag"}
    :param server_any: {"default": 0, "optional": true, "type": "number", "description": "Provide All Records", "format": "flag"}
    :param hint: {"description": "'none': None; 'answer': Append Hint Records in DNS Answer Section; 'addition': Append Hint Records in DNS Addition Section; ", "format": "enum", "default": "addition", "type": "string", "enum": ["none", "answer", "addition"], "optional": true}
    :param cache: {"default": 0, "optional": true, "type": "number", "description": "Cache DNS Server response", "format": "flag"}
    :param external_ip: {"default": 1, "optional": true, "type": "number", "description": "Return DNS response with external IP address", "format": "flag"}
    :param server_txt: {"default": 0, "optional": true, "type": "number", "description": "Provide TXT Records", "format": "flag"}
    :param server_addition_mx: {"default": 0, "optional": true, "type": "number", "description": "Append MX Records in Addition Section", "format": "flag"}
    :param aging_time: {"description": "Specify aging-time, default is TTL in DNS record, unit: second (Aging time, default 0 means using TTL in DNS record as aging time)", "format": "number", "default": 0, "optional": true, "maximum": 1000000000, "minimum": 0, "type": "number"}
    :param block_action: {"default": 0, "optional": true, "type": "number", "description": "Specify Action", "format": "flag"}
    :param ipv6: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"dns-ipv6-mapping-type": {"enum": ["addition", "answer", "exclusive", "replace"], "type": "string", "description": "'addition': Append Mapped Record in DNS Addition Section; 'answer': Append Mapped Record in DNS Answer Section; 'exclusive': Only return AAAA Record; 'replace': Replace Record with Mapped Record; ", "format": "enum"}, "optional": true, "dns-ipv6-option": {"enum": ["mix", "smart", "mapping"], "type": "string", "description": "'mix': Return both AAAA Record and A Record; 'smart': Return AAAA Record by DNS Query Type; 'mapping': Map A Record to AAAA Record; ", "format": "enum"}}}]}
    :param selected_only_value: {"description": "Answer Number", "format": "number", "type": "number", "maximum": 128, "minimum": 1, "optional": true}
    :param geoloc_action: {"default": 0, "optional": true, "type": "number", "description": "Apply DNS action by geo-location", "format": "flag"}
    :param server_ns: {"default": 0, "optional": true, "type": "number", "description": "Provide NS Records", "format": "flag"}
    :param action_type: {"optional": true, "enum": ["drop", "reject", "ignore"], "type": "string", "description": "'drop': Drop query; 'reject': Send refuse response; 'ignore': Send empty response; ", "format": "enum"}
    :param active_only: {"default": 0, "optional": true, "type": "number", "description": "Only keep active servers", "format": "flag"}
    :param block_value: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "block-value": {"description": "Specify Type Number", "minimum": 1, "type": "number", "maximum": 255, "format": "number"}}}]}
    :param server_srv: {"default": 0, "optional": true, "type": "number", "description": "Provide SRV Records", "format": "flag"}
    :param server_auto_ptr: {"default": 0, "optional": true, "type": "number", "description": "Provide PTR Records automatically", "format": "flag"}
    :param server_authoritative: {"default": 0, "optional": true, "type": "number", "description": "As authoritative server", "format": "flag"}
    :param use_server_ttl: {"description": "Use DNS Server Response TTL value in GSLB Proxy mode", "format": "flag", "default": 0, "optional": true, "not": "ttl", "type": "number"}
    :param proxy_block_port_range_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"proxy-block-range-from": {"type": "number", "description": "Specify Type Range (From)", "format": "number"}, "optional": true, "proxy-block-range-to": {"type": "number", "description": "To", "format": "number"}}}]}
    :param ip_replace: {"default": 0, "optional": true, "type": "number", "description": "Replace DNS Server Response with GSLB Service-IPs", "format": "flag"}
    :param sticky_mask: {"optional": true, "type": "string", "description": "Specify IP mask, default is /32 default /32", "format": "ipv4-netmask-brief"}
    :param geoloc_alias: {"default": 0, "optional": true, "type": "number", "description": "Return alias name by geo-location", "format": "flag"}
    :param logging: {"optional": true, "enum": ["none", "query", "response", "both"], "type": "string", "description": "'none': None; 'query': DNS Query; 'response': DNS Response; 'both': Both DNS Query and Response; ", "format": "enum"}
    :param backup_server: {"default": 0, "optional": true, "type": "number", "description": "Return fallback server when fail", "format": "flag"}
    :param sticky_aging_time: {"description": "Specify aging-time, unit: min, default is 5 (Aging time)", "format": "number", "default": 5, "optional": true, "maximum": 65535, "minimum": 1, "type": "number"}
    :param geoloc_policy: {"default": 0, "optional": true, "type": "number", "description": "Apply different policy by geo-location", "format": "flag"}
    :param server: {"default": 0, "optional": true, "type": "number", "description": "Run GSLB as DNS server mode", "format": "flag"}
    :param server_ns_list: {"default": 0, "optional": true, "type": "number", "description": "Append All NS Records in Authoritative Section", "format": "flag"}
    :param server_auto_ns: {"default": 0, "optional": true, "type": "number", "description": "Provide PTR Records automatically", "format": "flag"}
    :param action: {"default": 0, "optional": true, "type": "number", "description": "Apply DNS action for service", "format": "flag"}
    :param dns_auto_map: {"default": 0, "optional": true, "type": "number", "description": "Automatically build DNS Infrastructure", "format": "flag"}
    :param server_mx: {"default": 0, "optional": true, "type": "number", "description": "Provide MX Records", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/gslb/policy/{name}/dns`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "dns"
        self.a10_url="/axapi/v3/gslb/policy/{name}/dns"
        self.DeviceProxy = ""
        self.external_soa = ""
        self.server_sec = ""
        self.sticky_ipv6_mask = ""
        self.sticky = ""
        self.delegation = ""
        self.active_only_fail_safe = ""
        self.cname_detect = ""
        self.ttl = ""
        self.server_full_list = ""
        self.server_ptr = ""
        self.selected_only = ""
        self.dns_addition_mx = ""
        self.block_type = ""
        self.backup_alias = ""
        self.server_any = ""
        self.hint = ""
        self.cache = ""
        self.external_ip = ""
        self.server_txt = ""
        self.server_addition_mx = ""
        self.aging_time = ""
        self.block_action = ""
        self.ipv6 = []
        self.selected_only_value = ""
        self.geoloc_action = ""
        self.server_ns = ""
        self.action_type = ""
        self.active_only = ""
        self.block_value = []
        self.server_srv = ""
        self.server_auto_ptr = ""
        self.server_authoritative = ""
        self.use_server_ttl = ""
        self.proxy_block_port_range_list = []
        self.ip_replace = ""
        self.sticky_mask = ""
        self.geoloc_alias = ""
        self.logging = ""
        self.backup_server = ""
        self.sticky_aging_time = ""
        self.geoloc_policy = ""
        self.server = ""
        self.server_ns_list = ""
        self.server_auto_ns = ""
        self.action = ""
        self.dns_auto_map = ""
        self.server_mx = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


