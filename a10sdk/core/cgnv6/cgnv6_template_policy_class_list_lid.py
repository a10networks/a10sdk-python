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


class Lid(A10BaseClass):
    
    """Class Description::
    Limit ID.

    Class lid supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param request_limit: {"description": "Request limit (Specify request limit)", "format": "number", "type": "number", "maximum": 1048575, "minimum": 0, "optional": true}
    :param conn_limit: {"description": "Connection limit", "format": "number", "type": "number", "maximum": 1048575, "minimum": 0, "optional": true}
    :param interval: {"description": "Specify log interval in minutes, by default system will log every over limit instance", "format": "number", "type": "number", "maximum": 255, "minimum": 1, "optional": true}
    :param log: {"default": 0, "optional": true, "type": "number", "description": "Log a message", "format": "flag"}
    :param lidnum: {"description": "Specify a limit ID", "format": "number", "type": "number", "maximum": 31, "minimum": 1, "optional": false}
    :param request_rate_limit: {"description": "Request rate limit (Specify request rate limit)", "format": "number", "type": "number", "maximum": 4294967295, "minimum": 1, "optional": true}
    :param conn_per: {"description": "Per (Specify interval in number of 100ms)", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": true}
    :param request_per: {"description": "Per (Specify interval in number of 100ms)", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": true}
    :param conn_rate_limit: {"description": "Specify connection rate limit", "format": "number", "type": "number", "maximum": 2147483647, "minimum": 1, "optional": true}
    :param lockout: {"description": "Don't accept any new connection for certain time (Lockout duration in minutes)", "format": "number", "type": "number", "maximum": 1023, "minimum": 1, "optional": true}
    :param action_value: {"optional": true, "enum": ["forward", "reset"], "type": "string", "description": "'forward': Forward the traffic even it exceeds limit; 'reset': Reset the connection when it exceeds limit; ", "format": "enum"}
    :param over_limit_action: {"default": 0, "optional": true, "type": "number", "description": "Set action when exceeds limit", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/template/policy/{name}/class-list/lid/{lidnum}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "lidnum"]

        self.b_key = "lid"
        self.a10_url="/axapi/v3/cgnv6/template/policy/{name}/class-list/lid/{lidnum}"
        self.DeviceProxy = ""
        self.request_limit = ""
        self.conn_limit = ""
        self.interval = ""
        self.log = ""
        self.dns64 = {}
        self.lidnum = ""
        self.request_rate_limit = ""
        self.conn_per = ""
        self.request_per = ""
        self.conn_rate_limit = ""
        self.lockout = ""
        self.action_value = ""
        self.over_limit_action = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


