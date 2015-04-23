from a10sdk.common.A10BaseClass import A10BaseClass


class SamplingEnable(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param counters1: {"enum": ["all", "Admin-Bind-success", "Admin-Bind-failure", "Bind-success", "Bind-failure", "Search-success", "Search-failure", "Authorize-success", "Authorize-failure", "Timeout-error", "Other-error", "Request"], "type": "string", "description": "'all': all; 'Admin-Bind-success': Total Admin Bind Success; 'Admin-Bind-failure': Total Admin Bind Failure; 'Bind-success': Total User Bind Success; 'Bind-failure': Total User Bind Failure; 'Search-success': Total Search Success; 'Search-failure': Total Search Failure; 'Authorize-success': Total Authorization Success; 'Authorize-failure': Total Authorization Failure; 'Timeout-error': Total Timeout; 'Other-error': Total Other Error; 'Request': Total Request; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "sampling-enable"
        self.DeviceProxy = ""
        self.counters1 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Ldap(A10BaseClass):
    
    """    :param sampling_enable: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "Admin-Bind-success", "Admin-Bind-failure", "Bind-success", "Bind-failure", "Search-success", "Search-failure", "Authorize-success", "Authorize-failure", "Timeout-error", "Other-error", "Request"], "type": "string", "description": "'all': all; 'Admin-Bind-success': Total Admin Bind Success; 'Admin-Bind-failure': Total Admin Bind Failure; 'Bind-success': Total User Bind Success; 'Bind-failure': Total User Bind Failure; 'Search-success': Total Search Success; 'Search-failure': Total Search Failure; 'Authorize-success': Total Authorization Success; 'Authorize-failure': Total Authorization Failure; 'Timeout-error': Total Timeout; 'Other-error': Total Other Error; 'Request': Total Request; ", "format": "enum"}}}]}
    :param instance_list: {"minItems": 1, "items": {"type": "instance"}, "uniqueItems": true, "array": [{"required": ["name"], "properties": {"uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}, "health-check-string": {"description": "Health monitor name", "format": "string", "minLength": 1, "optional": true, "maxLength": 31, "type": "string", "$ref": "/axapi/v3/health/monitor"}, "port-hm": {"description": "Check port's health status", "format": "string", "minLength": 1, "optional": true, "maxLength": 31, "not": "port-hm-disable", "type": "string", "$ref": "/axapi/v3/health/monitor"}, "name": {"description": "Specify LDAP authentication server name", "format": "string-rlx", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}, "port-hm-disable": {"description": "Disable configured port health check configuration", "format": "flag", "default": 0, "optional": true, "not": "port-hm", "type": "number"}, "admin-dn": {"description": "The LDAP server's admin DN", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 127, "type": "string"}, "encrypted": {"optional": true, "type": "encrypted", "description": "Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED secret string)", "format": "encrypted"}, "default-domain": {"description": "Specify default domain for LDAP", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}, "health-check-disable": {"description": "Disable configured health check configuration", "format": "flag", "default": 0, "optional": true, "not": "health-check", "type": "number"}, "admin-secret": {"default": 0, "optional": true, "type": "number", "description": "Specify the LDAP server's admin secret password", "format": "flag"}, "health-check": {"description": "Check server's health status", "format": "flag", "default": 0, "optional": true, "not": "health-check-disable", "type": "number"}, "bind-with-dn": {"default": 0, "optional": true, "type": "number", "description": "Enforce using DN for LDAP binding(All user input name will be used to create DN)", "format": "flag"}, "host": {"type": "object", "properties": {"hostipv6": {"not": "hostip", "type": "string", "description": "Server's IPV6 address", "format": "ipv6-address"}, "hostip": {"description": "Server's hostname(Length 1-31) or IP address", "format": "host", "minLength": 1, "maxLength": 31, "not": "hostipv6", "type": "string"}}}, "base": {"description": "Specify the LDAP server's search base", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 127, "type": "string"}, "dn-attribute": {"description": "Specify Distinguished Name attribute, default is CN", "format": "string-rlx", "default": "cn", "minLength": 1, "optional": true, "maxLength": 31, "type": "string"}, "timeout": {"description": "Specify timout for LDAP, default is 10 seconds (The timeout, default is 10 seconds)", "format": "number", "default": 10, "optional": true, "maximum": 255, "minimum": 1, "type": "number"}, "pwdmaxage": {"description": "Specify the LDAP server's default password expiration time (in seconds) (The LDAP server's default password expiration time (in seconds), default is 0 (no expiration))", "format": "number", "default": 0, "optional": true, "maximum": 4294967295, "minimum": 0, "type": "number"}, "derive-bind-dn": {"type": "object", "properties": {"username-attr": {"minLength": 1, "maxLength": 31, "type": "string", "description": "Specify attribute name of username", "format": "string-rlx"}}}, "port": {"description": "Specify the LDAP server's authentication port, default is 389", "format": "number", "default": 389, "optional": true, "maximum": 65534, "minimum": 1, "type": "number"}, "secret-string": {"description": "secret password", "format": "password", "minLength": 1, "optional": true, "maxLength": 128, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/aam/authentication/server/ldap/instance/{name}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    LDAP Authentication Server.

    Class ldap supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/aam/authentication/server/ldap`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "ldap"
        self.a10_url="/axapi/v3/aam/authentication/server/ldap"
        self.DeviceProxy = ""
        self.sampling_enable = []
        self.instance_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


