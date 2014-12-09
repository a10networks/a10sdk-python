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


class Lid(A10BaseClass):
    
    """Class Description::
    Limit ID.

    Class lid supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param over_limit_action: {"default": 0, "optional": true, "type": "number", "description": "Action when exceeds limit", "format": "flag"}
    :param log: {"default": 0, "optional": true, "type": "number", "description": "Log a message", "format": "flag"}
    :param lidnum: {"description": "Specify a limit ID", "format": "number", "type": "number", "maximum": 31, "minimum": 1, "optional": false}
    :param action_value: {"optional": true, "enum": ["dns-cache-disable", "dns-cache-enable", "forward"], "type": "string", "description": "'dns-cache-disable': Disable DNS cache when it exceeds limit; 'dns-cache-enable': Enable DNS cache when it exceeds limit; 'forward': Forward the traffic even it exceeds limit; ", "format": "enum"}
    :param per: {"description": "Per (Number of 100ms)", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": true}
    :param lockout: {"description": "Don't accept any new connection for certain time (Lockout duration in minutes)", "format": "number", "type": "number", "maximum": 1023, "minimum": 1, "optional": true}
    :param conn_rate_limit: {"description": "Connection rate limit", "format": "number", "type": "number", "maximum": 2147483647, "minimum": 1, "optional": true}
    :param log_interval: {"description": "Log interval (minute, by default system will log every over limit instance)", "format": "number", "type": "number", "maximum": 255, "minimum": 1, "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/template/dns/{name}/class-list/lid/{lidnum}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "lidnum"]

        self.b_key = "lid"
        self.a10_url="/axapi/v3/slb/template/dns/{name}/class-list/lid/{lidnum}"
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


