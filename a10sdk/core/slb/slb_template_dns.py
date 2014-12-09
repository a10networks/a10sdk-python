from a10sdk.common.A10BaseClass import A10BaseClass


class Dns(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param cache_action: {"default": "cache-disable", "enum": ["cache-disable", "cache-enable"], "type": "string", "description": "'cache-disable': Disable dns cache; 'cache-enable': Enable dns cache; ", "format": "enum"}
    :param weight: {"description": "Weight for cache entry", "minimum": 1, "type": "number", "maximum": 7, "format": "number"}
    :param ttl: {"description": "TTL for cache entry (TTL in seconds)", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "dns"
        self.DeviceProxy = ""
        self.cache_action = ""
        self.weight = ""
        self.ttl = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class LidList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param over_limit_action: {"default": 0, "optional": true, "type": "number", "description": "Action when exceeds limit", "format": "flag"}
    :param log: {"default": 0, "optional": true, "type": "number", "description": "Log a message", "format": "flag"}
    :param lidnum: {"description": "Specify a limit ID", "format": "number", "type": "number", "maximum": 31, "minimum": 1, "optional": false}
    :param action_value: {"optional": true, "enum": ["dns-cache-disable", "dns-cache-enable", "forward"], "type": "string", "description": "'dns-cache-disable': Disable DNS cache when it exceeds limit; 'dns-cache-enable': Enable DNS cache when it exceeds limit; 'forward': Forward the traffic even it exceeds limit; ", "format": "enum"}
    :param per: {"description": "Per (Number of 100ms)", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": true}
    :param lockout: {"description": "Don't accept any new connection for certain time (Lockout duration in minutes)", "format": "number", "type": "number", "maximum": 1023, "minimum": 1, "optional": true}
    :param conn_rate_limit: {"description": "Connection rate limit", "format": "number", "type": "number", "maximum": 2147483647, "minimum": 1, "optional": true}
    :param log_interval: {"description": "Log interval (minute, by default system will log every over limit instance)", "format": "number", "type": "number", "maximum": 255, "minimum": 1, "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "lid-list"
        self.DeviceProxy = ""
        self.over_limit_action = ""
        self.log = ""
        self.lidnum = ""
        self.action_value = ""
        self.per = ""
        self.lockout = ""
        self.dns = {}
        self.conn_rate_limit = ""
        self.log_interval = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class ClassList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param lid_list: {"minItems": 1, "items": {"type": "lid"}, "uniqueItems": true, "array": [{"required": ["lidnum"], "properties": {"over-limit-action": {"default": 0, "optional": true, "type": "number", "description": "Action when exceeds limit", "format": "flag"}, "log": {"default": 0, "optional": true, "type": "number", "description": "Log a message", "format": "flag"}, "lidnum": {"description": "Specify a limit ID", "format": "number", "type": "number", "maximum": 31, "minimum": 1, "optional": false}, "action-value": {"optional": true, "enum": ["dns-cache-disable", "dns-cache-enable", "forward"], "type": "string", "description": "'dns-cache-disable': Disable DNS cache when it exceeds limit; 'dns-cache-enable': Enable DNS cache when it exceeds limit; 'forward': Forward the traffic even it exceeds limit; ", "format": "enum"}, "per": {"description": "Per (Number of 100ms)", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": true}, "lockout": {"description": "Don't accept any new connection for certain time (Lockout duration in minutes)", "format": "number", "type": "number", "maximum": 1023, "minimum": 1, "optional": true}, "dns": {"type": "object", "properties": {"cache-action": {"default": "cache-disable", "enum": ["cache-disable", "cache-enable"], "type": "string", "description": "'cache-disable': Disable dns cache; 'cache-enable': Enable dns cache; ", "format": "enum"}, "weight": {"description": "Weight for cache entry", "minimum": 1, "type": "number", "maximum": 7, "format": "number"}, "ttl": {"description": "TTL for cache entry (TTL in seconds)", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}}}, "conn-rate-limit": {"description": "Connection rate limit", "format": "number", "type": "number", "maximum": 2147483647, "minimum": 1, "optional": true}, "log-interval": {"description": "Log interval (minute, by default system will log every over limit instance)", "format": "number", "type": "number", "maximum": 255, "minimum": 1, "optional": true}}}], "type": "array", "$ref": "/axapi/v3/slb/template/dns/{name}/class-list/lid/{lidnum}"}
    :param name: {"minLength": 1, "maxLength": 63, "type": "string", "description": "Specify a class list name", "format": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "class-list"
        self.DeviceProxy = ""
        self.lid_list = []
        self.name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Dns(A10BaseClass):
    
    """Class Description::
    DNS template.

    Class dns supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param query_id_switch: {"default": 0, "optional": true, "type": "number", "description": "Use DNS query ID to create sesion", "format": "flag"}
    :param name: {"description": "DNS Template Name", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param drop: {"description": "Drop the malformed query", "format": "flag", "default": 0, "optional": true, "not": "forward", "type": "number"}
    :param period: {"description": "Period in minutes", "format": "number", "type": "number", "maximum": 10000, "minimum": 1, "optional": true}
    :param default_policy: {"optional": true, "enum": ["nocache", "cache"], "type": "string", "description": "'nocache': Cache disable; 'cache': Cache enable; ", "format": "enum"}
    :param enable_cache_sharing: {"default": 0, "optional": true, "type": "number", "description": "Enable DNS cache sharing", "format": "flag"}
    :param redirect_to_tcp_port: {"default": 0, "optional": true, "type": "number", "description": "Direct the client to retry with TCP for DNS UDP request", "format": "flag"}
    :param max_query_length: {"description": "Define Maximum DNS Query Length, default is unlimited (Specify Maximum Length)", "format": "number", "type": "number", "maximum": 4095, "minimum": 1, "optional": true}
    :param max_cache_size: {"platform-specific-range": 1, "platform-specific-default": 1, "description": "Define maximum cache size (Maximum cache entry per VIP)", "format": "number", "optional": true, "type": "number"}
    :param forward: {"description": "Forward to service group (Service group name)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 127, "not": "drop", "type": "string", "$ref": "/axapi/v3/slb/service-group"}
    :param disable_dns_template: {"default": 0, "optional": true, "type": "number", "description": "Disable DNS template", "format": "flag"}
    :param max_cache_entry_size: {"description": "Define maximum cache entry size (Maximum cache entry size per VIP)", "format": "number", "type": "number", "maximum": 4096, "minimum": 1, "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/template/dns/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "dns"
        self.a10_url="/axapi/v3/slb/template/dns/{name}"
        self.DeviceProxy = ""
        self.query_id_switch = ""
        self.name = ""
        self.class_list = {}
        self.drop = ""
        self.period = ""
        self.default_policy = ""
        self.enable_cache_sharing = ""
        self.redirect_to_tcp_port = ""
        self.max_query_length = ""
        self.max_cache_size = ""
        self.forward = ""
        self.disable_dns_template = ""
        self.max_cache_entry_size = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


