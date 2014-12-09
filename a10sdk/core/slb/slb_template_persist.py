from a10sdk.common.A10BaseClass import A10BaseClass


class Persist(A10BaseClass):
    
    """Class Description::
    Persistence.

    Class persist supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param destination_ip_list: {"minItems": 1, "items": {"type": "destination-ip"}, "uniqueItems": true, "array": [{"required": ["name"], "properties": {"netmask6": {"description": "IPV6 subnet mask", "format": "number", "default": 128, "optional": true, "maximum": 128, "minimum": 1, "type": "number"}, "scan-all-members": {"default": 0, "optional": true, "type": "number", "description": "Persist with SCAN of all members", "format": "flag"}, "name": {"description": "Destination IP persistence template name", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}, "dont-honor-conn-rules": {"default": 0, "optional": true, "type": "number", "description": "Do not observe connection rate rules", "format": "flag"}, "netmask": {"default": "255.255.255.255", "optional": true, "type": "string", "description": "IP subnet mask", "format": "ipv4-netmask"}, "server": {"description": "Persist to the same server, default is port", "format": "flag", "default": 0, "optional": true, "not": "service-group", "type": "number"}, "service-group": {"description": "Persist within the same service group", "format": "flag", "default": 0, "optional": true, "not": "server", "type": "number"}, "timeout": {"description": "Persistence timeout (in minutes)", "format": "number", "default": 5, "optional": true, "maximum": 2000, "minimum": 1, "type": "number"}, "hash-persist": {"default": 0, "optional": true, "type": "number", "description": "Use hash value of destination IP address", "format": "flag"}, "match-type": {"default": 0, "optional": true, "type": "number", "description": "Persistence type", "format": "flag"}}}], "type": "array", "$ref": "/axapi/v3/slb/template/persist/destination-ip/{name}"}
    :param source_ip_list: {"minItems": 1, "items": {"type": "source-ip"}, "uniqueItems": true, "array": [{"required": ["name"], "properties": {"scan-all-members": {"default": 0, "optional": true, "type": "number", "description": "Persist with SCAN of all members", "format": "flag"}, "netmask6": {"description": "IPV6 subnet mask", "format": "number", "default": 128, "optional": true, "maximum": 128, "minimum": 1, "type": "number"}, "incl-dst-ip": {"default": 0, "optional": true, "type": "number", "description": "Include destination IP on the persist", "format": "flag"}, "name": {"description": "Source IP persistence template name", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}, "dont-honor-conn-rules": {"default": 0, "optional": true, "type": "number", "description": "Do not observe connection rate rules", "format": "flag"}, "service-group": {"description": "Persist within the same service group", "format": "flag", "default": 0, "optional": true, "not": "server", "type": "number"}, "server": {"description": "Persist to the same server, default is port", "format": "flag", "default": 0, "optional": true, "not": "service-group", "type": "number"}, "incl-sport": {"default": 0, "optional": true, "type": "number", "description": "Include source port on the persist", "format": "flag"}, "netmask": {"default": "255.255.255.255", "optional": true, "type": "string", "description": "IP subnet mask", "format": "ipv4-netmask"}, "timeout": {"description": "Persistence timeout (in minutes)", "format": "number", "default": 5, "optional": true, "maximum": 2000, "minimum": 1, "type": "number"}, "hash-persist": {"default": 0, "optional": true, "type": "number", "description": "Use hash value of source IP address", "format": "flag"}, "enforce-higher-priority": {"default": 0, "optional": true, "type": "number", "description": "Enforce to use high priority node if available", "format": "flag"}, "match-type": {"default": 0, "optional": true, "type": "number", "description": "Persistence type", "format": "flag"}}}], "type": "array", "$ref": "/axapi/v3/slb/template/persist/source-ip/{name}"}
    :param cookie_list: {"minItems": 1, "items": {"type": "cookie"}, "uniqueItems": true, "array": [{"required": ["name"], "properties": {"domain": {"description": "Set cookie domain", "format": "string", "minLength": 1, "optional": true, "maxLength": 31, "type": "string"}, "secure": {"default": 0, "optional": true, "type": "number", "description": "Enable secure attribute", "format": "flag"}, "cookie-name": {"description": "Set cookie name", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}, "dont-honor-conn-rules": {"default": 0, "optional": true, "type": "number", "description": "Do not observe connection rate rules", "format": "flag"}, "server": {"description": "Persist to the same server, default is port", "format": "flag", "default": 0, "optional": true, "not": "service-group", "type": "number"}, "server-service-group": {"default": 0, "optional": true, "type": "number", "description": "Persist to the same server and within the same service group", "format": "flag"}, "service-group": {"description": "Persist within the same service group", "format": "flag", "default": 0, "optional": true, "not": "server", "type": "number"}, "expire": {"description": "Set cookie expiration time (Expiration in seconds)", "format": "number", "default": 0, "optional": true, "maximum": 31536000, "minimum": 0, "type": "number"}, "match-type": {"default": 0, "optional": true, "type": "number", "description": "Persist for server, default is port", "format": "flag"}, "path": {"description": "Set cookie path (Cookie path, default is \"/\")", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 31, "type": "string"}, "pass-thru": {"default": 0, "optional": true, "type": "number", "description": "Pass thru mode - Server sends the persist cookie", "format": "flag"}, "scan-all-members": {"default": 0, "optional": true, "type": "number", "description": "Persist within the same server SCAN", "format": "flag"}, "insert-always": {"default": 0, "optional": true, "type": "number", "description": "Insert persist cookie to every reponse", "format": "flag"}, "httponly": {"default": 0, "optional": true, "type": "number", "description": "Enable HttpOnly attribute", "format": "flag"}, "name": {"description": "Cookie persistence (Cookie persistence template name)", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/slb/template/persist/cookie/{name}"}
    :param ssl_sid_list: {"minItems": 1, "items": {"type": "ssl-sid"}, "uniqueItems": true, "array": [{"required": ["name"], "properties": {"dont-honor-conn-rules": {"default": 0, "optional": true, "type": "number", "description": "Do not observe connection rate rules", "format": "flag"}, "name": {"description": "SSL session ID persistence template name", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}, "timeout": {"description": "Persistence timeout (in minutes)", "format": "number", "type": "number", "maximum": 2000, "minimum": 1, "optional": true}}}], "type": "array", "$ref": "/axapi/v3/slb/template/persist/ssl-sid/{name}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/template/persist`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "persist"
        self.a10_url="/axapi/v3/slb/template/persist"
        self.DeviceProxy = ""
        self.destination_ip_list = []
        self.source_ip_list = []
        self.cookie_list = []
        self.ssl_sid_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


