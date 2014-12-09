from a10sdk.common.A10BaseClass import A10BaseClass


class ClassList(A10BaseClass):
    
    """Class Description::
    Configure classification list.

    Class class-list supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param header_name: {"description": "Specify L7 header name", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param client_ip_l7_header: {"description": "Use extract client IP address from L7 header", "format": "flag", "default": 0, "optional": true, "not": "client-ip-l3-dest", "type": "number"}
    :param client_ip_l3_dest: {"description": "Use destination IP as client IP address", "format": "flag", "default": 0, "optional": true, "not": "client-ip-l7-header", "type": "number"}
    :param lid_list: {"minItems": 1, "items": {"type": "lid"}, "uniqueItems": true, "array": [{"required": ["lidnum"], "properties": {"request-limit": {"description": "Request limit (Specify request limit)", "format": "number", "type": "number", "maximum": 1048575, "minimum": 0, "optional": true}, "conn-limit": {"description": "Connection limit", "format": "number", "type": "number", "maximum": 1048575, "minimum": 0, "optional": true}, "interval": {"description": "Specify log interval in minutes, by default system will log every over limit instance", "format": "number", "type": "number", "maximum": 255, "minimum": 1, "optional": true}, "log": {"default": 0, "optional": true, "type": "number", "description": "Log a message", "format": "flag"}, "dns64": {"type": "object", "properties": {"exclusive-answer": {"default": 0, "type": "number", "description": "Exclusive Answer in DNS Response", "format": "flag"}, "prefix": {"type": "string", "description": "IPv6 prefix", "format": "ipv6-address-plen"}, "disable": {"default": 0, "type": "number", "description": "Disable", "format": "flag"}}}, "lidnum": {"description": "Specify a limit ID", "format": "number", "type": "number", "maximum": 31, "minimum": 1, "optional": false}, "request-rate-limit": {"description": "Request rate limit (Specify request rate limit)", "format": "number", "type": "number", "maximum": 4294967295, "minimum": 1, "optional": true}, "conn-per": {"description": "Per (Specify interval in number of 100ms)", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": true}, "request-per": {"description": "Per (Specify interval in number of 100ms)", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": true}, "conn-rate-limit": {"description": "Specify connection rate limit", "format": "number", "type": "number", "maximum": 2147483647, "minimum": 1, "optional": true}, "lockout": {"description": "Don't accept any new connection for certain time (Lockout duration in minutes)", "format": "number", "type": "number", "maximum": 1023, "minimum": 1, "optional": true}, "action-value": {"optional": true, "enum": ["forward", "reset"], "type": "string", "description": "'forward': Forward the traffic even it exceeds limit; 'reset': Reset the connection when it exceeds limit; ", "format": "enum"}, "over-limit-action": {"default": 0, "optional": true, "type": "number", "description": "Set action when exceeds limit", "format": "flag"}}}], "type": "array", "$ref": "/axapi/v3/slb/template/policy/{name}/class-list/lid/{lidnum}"}
    :param name: {"description": "Class list name or geo-location-class-list name", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/template/policy/{name}/class-list`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "class-list"
        self.a10_url="/axapi/v3/slb/template/policy/{name}/class-list"
        self.DeviceProxy = ""
        self.header_name = ""
        self.client_ip_l7_header = ""
        self.client_ip_l3_dest = ""
        self.lid_list = []
        self.name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


