from a10sdk.common.A10BaseClass import A10BaseClass


class Dns64(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param exclusive_answer: {"default": 0, "type": "number", "description": "Exclusive Answer in DNS Response", "format": "flag"}
    :param prefix: {"type": "string", "description": "IPv6 prefix", "format": "ipv6-address-plen"}
    :param disable: {"default": 0, "type": "number", "description": "Disable", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "dns64"
        self.DeviceProxy = ""
        self.exclusive_answer = ""
        self.prefix = ""
        self.disable = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Dns(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param action: {"default": "cache-disable", "enum": ["cache-disable", "cache-enable"], "type": "string", "description": "'cache-disable': Disable dns cache; 'cache-enable': Enable dns cache; ", "format": "enum"}
    :param weight: {"description": "Weight for cache entry", "minimum": 1, "type": "number", "maximum": 7, "format": "number"}
    :param ttl: {"description": "TTL for cache entry (TTL in seconds)", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "dns"
        self.DeviceProxy = ""
        self.action = ""
        self.weight = ""
        self.ttl = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Glid(A10BaseClass):
    
    """Class Description::
    Configure global limit ID.

    Class glid supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param request_limit: {"description": "Request limit", "format": "number", "type": "number", "maximum": 1048575, "minimum": 0, "optional": true}
    :param conn_limit: {"description": "Connection Limit for the GLID", "format": "number", "type": "number", "maximum": 1048575, "minimum": 1, "optional": true}
    :param log: {"default": 0, "optional": true, "type": "number", "description": "Log a message", "format": "flag"}
    :param request_rate_limit_interval: {"description": "Number of 100ms", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": true}
    :param request_rate_limit: {"description": "Request rate limit", "format": "number", "type": "number", "maximum": 4294967295, "minimum": 1, "optional": true}
    :param conn_rate_limit_interval: {"optional": true, "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}
    :param num: {"description": "Global Limit ID", "format": "number", "type": "number", "maximum": 1023, "minimum": 1, "optional": false}
    :param conn_rate_limit: {"description": "Connection rate Limit for the GLID", "format": "number", "type": "number", "maximum": 2147483647, "minimum": 1, "optional": true}
    :param lockout: {"description": "Don't accept any new connection for certain time (Lockout duration in minutes)", "format": "number", "type": "number", "maximum": 1023, "minimum": 1, "optional": true}
    :param action_value: {"optional": true, "enum": ["drop", "dns-cache-disable", "dns-cache-enable", "forward", "reset"], "type": "string", "description": "'drop': Silently Drop the new connection / new packet when it exceeds limit; 'dns-cache-disable': Disable dns cache when it exceeds limit; 'dns-cache-enable': Enable dns cache when it exceeds limit; 'forward': Forward the traffic even it exceeds limit; 'reset': Reset the connection when it exceeds limit; ", "format": "enum"}
    :param over_limit_action: {"default": 0, "optional": true, "type": "number", "description": "Action when exceeds limit", "format": "flag"}
    :param log_interval: {"description": "Log interval (minute, by default system will log every over limit instance)", "format": "number", "type": "number", "maximum": 255, "minimum": 1, "optional": true}
    :param use_nat_pool: {"description": "Use NAT pool specified to do reverse NAT for class list members bound to the lid", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/glid/{num}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "num"]

        self.b_key = "glid"
        self.a10_url="/axapi/v3/glid/{num}"
        self.DeviceProxy = ""
        self.request_limit = ""
        self.conn_limit = ""
        self.log = ""
        self.request_rate_limit_interval = ""
        self.dns64 = {}
        self.request_rate_limit = ""
        self.conn_rate_limit_interval = ""
        self.num = ""
        self.conn_rate_limit = ""
        self.dns = {}
        self.lockout = ""
        self.action_value = ""
        self.over_limit_action = ""
        self.log_interval = ""
        self.use_nat_pool = ""
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


