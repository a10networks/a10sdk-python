from a10sdk.common.A10BaseClass import A10BaseClass


class ClassList(A10BaseClass):
    
    """Class Description::
    Classification list.

    Class class-list supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param lid_list: {"minItems": 1, "items": {"type": "lid"}, "uniqueItems": true, "array": [{"required": ["lidnum"], "properties": {"over-limit-action": {"default": 0, "optional": true, "type": "number", "description": "Action when exceeds limit", "format": "flag"}, "log": {"default": 0, "optional": true, "type": "number", "description": "Log a message", "format": "flag"}, "lidnum": {"description": "Specify a limit ID", "format": "number", "type": "number", "maximum": 31, "minimum": 1, "optional": false}, "action-value": {"optional": true, "enum": ["dns-cache-disable", "dns-cache-enable", "forward"], "type": "string", "description": "'dns-cache-disable': Disable DNS cache when it exceeds limit; 'dns-cache-enable': Enable DNS cache when it exceeds limit; 'forward': Forward the traffic even it exceeds limit; ", "format": "enum"}, "per": {"description": "Per (Number of 100ms)", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": true}, "lockout": {"description": "Don't accept any new connection for certain time (Lockout duration in minutes)", "format": "number", "type": "number", "maximum": 1023, "minimum": 1, "optional": true}, "dns": {"type": "object", "properties": {"cache-action": {"default": "cache-disable", "enum": ["cache-disable", "cache-enable"], "type": "string", "description": "'cache-disable': Disable dns cache; 'cache-enable': Enable dns cache; ", "format": "enum"}, "weight": {"description": "Weight for cache entry", "minimum": 1, "type": "number", "maximum": 7, "format": "number"}, "ttl": {"description": "TTL for cache entry (TTL in seconds)", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}}}, "conn-rate-limit": {"description": "Connection rate limit", "format": "number", "type": "number", "maximum": 2147483647, "minimum": 1, "optional": true}, "log-interval": {"description": "Log interval (minute, by default system will log every over limit instance)", "format": "number", "type": "number", "maximum": 255, "minimum": 1, "optional": true}}}], "type": "array", "$ref": "/axapi/v3/cgnv6/template/dns/{name}/class-list/lid/{lidnum}"}
    :param name: {"description": "Specify a class list name", "format": "string-rlx", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/template/dns/{name}/class-list`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "class-list"
        self.a10_url="/axapi/v3/cgnv6/template/dns/{name}/class-list"
        self.DeviceProxy = ""
        self.lid_list = []
        self.name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


