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


class LidList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

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
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "lid-list"
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
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class ClassList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param header_name: {"minLength": 1, "maxLength": 63, "type": "string", "description": "Specify L7 header name", "format": "string"}
    :param lid_list: {"minItems": 1, "items": {"type": "lid"}, "uniqueItems": true, "array": [{"required": ["lidnum"], "properties": {"request-limit": {"description": "Request limit (Specify request limit)", "format": "number", "type": "number", "maximum": 1048575, "minimum": 0, "optional": true}, "conn-limit": {"description": "Connection limit", "format": "number", "type": "number", "maximum": 1048575, "minimum": 0, "optional": true}, "interval": {"description": "Specify log interval in minutes, by default system will log every over limit instance", "format": "number", "type": "number", "maximum": 255, "minimum": 1, "optional": true}, "log": {"default": 0, "optional": true, "type": "number", "description": "Log a message", "format": "flag"}, "dns64": {"type": "object", "properties": {"exclusive-answer": {"default": 0, "type": "number", "description": "Exclusive Answer in DNS Response", "format": "flag"}, "prefix": {"type": "string", "description": "IPv6 prefix", "format": "ipv6-address-plen"}, "disable": {"default": 0, "type": "number", "description": "Disable", "format": "flag"}}}, "lidnum": {"description": "Specify a limit ID", "format": "number", "type": "number", "maximum": 31, "minimum": 1, "optional": false}, "request-rate-limit": {"description": "Request rate limit (Specify request rate limit)", "format": "number", "type": "number", "maximum": 4294967295, "minimum": 1, "optional": true}, "conn-per": {"description": "Per (Specify interval in number of 100ms)", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": true}, "request-per": {"description": "Per (Specify interval in number of 100ms)", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": true}, "conn-rate-limit": {"description": "Specify connection rate limit", "format": "number", "type": "number", "maximum": 2147483647, "minimum": 1, "optional": true}, "lockout": {"description": "Don't accept any new connection for certain time (Lockout duration in minutes)", "format": "number", "type": "number", "maximum": 1023, "minimum": 1, "optional": true}, "action-value": {"optional": true, "enum": ["forward", "reset"], "type": "string", "description": "'forward': Forward the traffic even it exceeds limit; 'reset': Reset the connection when it exceeds limit; ", "format": "enum"}, "over-limit-action": {"default": 0, "optional": true, "type": "number", "description": "Set action when exceeds limit", "format": "flag"}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/slb/template/policy/{name}/class-list/lid/{lidnum}"}
    :param name: {"minLength": 1, "maxLength": 63, "type": "string", "description": "Class list name or geo-location-class-list name", "format": "string-rlx"}
    :param client_ip_l3_dest: {"default": 0, "not": "client-ip-l7-header", "type": "number", "description": "Use destination IP as client IP address", "format": "flag"}
    :param client_ip_l7_header: {"default": 0, "not": "client-ip-l3-dest", "type": "number", "description": "Use extract client IP address from L7 header", "format": "flag"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "class-list"
        self.DeviceProxy = ""
        self.header_name = ""
        self.lid_list = []
        self.name = ""
        self.client_ip_l3_dest = ""
        self.client_ip_l7_header = ""
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class BwListId(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param pbslb_interval: {"description": "Specify logging interval in minutes", "format": "number", "default": 3, "maximum": 60, "minimum": 0, "type": "number"}
    :param action_interval: {"description": "Specify logging interval in minute (default is 3)", "format": "number", "default": 3, "maximum": 60, "minimum": 0, "type": "number"}
    :param service_group: {"description": "Specify a service group (Specify the service group name)", "format": "string-rlx", "minLength": 1, "maxLength": 127, "not": "bw-list-action", "type": "string", "$ref": "/axapi/v3/slb/service-group"}
    :param logging_drp_rst: {"default": 0, "type": "number", "description": "Configure PBSLB logging", "format": "flag"}
    :param fail: {"default": 0, "type": "number", "description": "Only log unsuccessful connections", "format": "flag"}
    :param pbslb_logging: {"default": 0, "type": "number", "description": "Configure PBSLB logging", "format": "flag"}
    :param id: {"description": "Specify id that maps to service group (The id number)", "minimum": 0, "type": "number", "maximum": 31, "format": "number"}
    :param bw_list_action: {"not": "service-group", "enum": ["drop", "reset"], "type": "string", "description": "'drop': drop the packet; 'reset': Send reset back; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "bw-list-id"
        self.DeviceProxy = ""
        self.pbslb_interval = ""
        self.action_interval = ""
        self.service_group = ""
        self.logging_drp_rst = ""
        self.fail = ""
        self.pbslb_logging = ""
        self.A10WW_id = ""
        self.bw_list_action = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Policy(A10BaseClass):
    
    """Class Description::
    Policy config.

    Class policy supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param use_destination_ip: {"default": 0, "optional": true, "type": "number", "description": "Use destination IP to match the policy", "format": "flag"}
    :param name: {"description": "Policy template name", "format": "string-rlx", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param over_limit: {"default": 0, "optional": true, "type": "number", "description": "Specify operation in case over limit", "format": "flag"}
    :param full_domain_tree: {"default": 0, "optional": true, "type": "number", "description": "Share counters between geo-location and sub regions", "format": "flag"}
    :param interval: {"description": "Log interval (minute)", "format": "number", "type": "number", "maximum": 255, "minimum": 1, "optional": true}
    :param share: {"default": 0, "optional": true, "type": "number", "description": "Share counters between virtual ports and virtual servers", "format": "flag"}
    :param over_limit_lockup: {"description": "Don't accept any new connection for certain time (Lockup duration (minute))", "format": "number", "type": "number", "maximum": 127, "minimum": 1, "optional": true}
    :param over_limit_logging: {"default": 0, "optional": true, "type": "number", "description": "Log a message", "format": "flag"}
    :param bw_list_id: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"pbslb-interval": {"description": "Specify logging interval in minutes", "format": "number", "default": 3, "maximum": 60, "minimum": 0, "type": "number"}, "action-interval": {"description": "Specify logging interval in minute (default is 3)", "format": "number", "default": 3, "maximum": 60, "minimum": 0, "type": "number"}, "service-group": {"description": "Specify a service group (Specify the service group name)", "format": "string-rlx", "minLength": 1, "maxLength": 127, "not": "bw-list-action", "type": "string", "$ref": "/axapi/v3/slb/service-group"}, "logging-drp-rst": {"default": 0, "type": "number", "description": "Configure PBSLB logging", "format": "flag"}, "fail": {"default": 0, "type": "number", "description": "Only log unsuccessful connections", "format": "flag"}, "pbslb-logging": {"default": 0, "type": "number", "description": "Configure PBSLB logging", "format": "flag"}, "optional": true, "id": {"description": "Specify id that maps to service group (The id number)", "minimum": 0, "type": "number", "maximum": 31, "format": "number"}, "bw-list-action": {"not": "service-group", "enum": ["drop", "reset"], "type": "string", "description": "'drop': drop the packet; 'reset': Send reset back; ", "format": "enum"}}}]}
    :param bw_list_name: {"description": "Specify a blacklist/whitelist name", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param overlap: {"default": 0, "optional": true, "type": "number", "description": "Use overlap mode for geo-location to do longest match", "format": "flag"}
    :param timeout: {"description": "Define timeout value of PBSLB dynamic entry (Timeout value (minute, default is 5))", "format": "number", "default": 5, "optional": true, "maximum": 127, "minimum": 1, "type": "number"}
    :param over_limit_reset: {"default": 0, "optional": true, "type": "number", "description": "Reset the connection when it exceeds limit", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/template/policy/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "policy"
        self.a10_url="/axapi/v3/slb/template/policy/{name}"
        self.DeviceProxy = ""
        self.use_destination_ip = ""
        self.name = ""
        self.over_limit = ""
        self.class_list = {}
        self.full_domain_tree = ""
        self.interval = ""
        self.share = ""
        self.over_limit_lockup = ""
        self.over_limit_logging = ""
        self.bw_list_id = []
        self.bw_list_name = ""
        self.overlap = ""
        self.timeout = ""
        self.over_limit_reset = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


