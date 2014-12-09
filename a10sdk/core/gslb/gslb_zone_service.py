from a10sdk.common.A10BaseClass import A10BaseClass


class HealthCheckPort(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param health_check_port: {"description": "Check Related Port Status (Port Number)", "minimum": 0, "type": "number", "maximum": 65534, "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "health-check-port"
        self.DeviceProxy = ""
        self.health_check_port = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Service(A10BaseClass):
    
    """Class Description::
    Service information for the GSLB zone.

    Class service supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param forward_type: {"optional": true, "enum": ["both", "query", "response"], "type": "string", "description": "'both': Forward both query and response; 'query': Forward query; 'response': Forward response; ", "format": "enum"}
    :param dns_cname_record_list: {"minItems": 1, "items": {"type": "dns-cname-record"}, "uniqueItems": true, "array": [{"required": ["alias-name"], "properties": {"as-backup": {"default": 0, "optional": true, "type": "number", "description": "As backup when fail", "format": "flag"}, "alias-name": {"description": "Specify the alias name", "format": "string", "minLength": 1, "optional": false, "maxLength": 127, "type": "string"}, "admin-preference": {"description": "Specify Administrative Preference, default is 100", "format": "number", "default": 100, "optional": true, "maximum": 255, "minimum": 0, "type": "number"}, "weight": {"description": "Specify Weight, default is 1", "format": "number", "default": 1, "optional": true, "maximum": 100, "minimum": 1, "type": "number"}}}], "type": "array", "$ref": "/axapi/v3/gslb/zone/{name}/service/{service-port}+{service-name}/dns-cname-record/{alias-name}"}
    :param health_check_port: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "health-check-port": {"description": "Check Related Port Status (Port Number)", "minimum": 0, "type": "number", "maximum": 65534, "format": "number"}}}]}
    :param policy: {"description": "Specify policy for this service (Specify policy name)", "format": "string", "default": "default", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param dns_txt_record_list: {"minItems": 1, "items": {"type": "dns-txt-record"}, "uniqueItems": true, "array": [{"required": ["record-name"], "properties": {"record-name": {"description": "Specify the Object Name for TXT Data", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}, "txt-data": {"description": "Specify TXT Data", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 1000, "type": "string"}, "ttl": {"optional": true, "type": "number", "description": "Specify TTL", "format": "number"}}}], "type": "array", "$ref": "/axapi/v3/gslb/zone/{name}/service/{service-port}+{service-name}/dns-txt-record/{record-name}"}
    :param service_port: {"description": "Port number of the service", "format": "number", "type": "number", "maximum": 65534, "minimum": 0, "optional": false}
    :param dns_mx_record_list: {"minItems": 1, "items": {"type": "dns-mx-record"}, "uniqueItems": true, "array": [{"required": ["mx-name"], "properties": {"priority": {"description": "Specify Priority", "format": "number", "type": "number", "maximum": 65535, "minimum": 0, "optional": true}, "mx-name": {"description": "Specify Domain Name", "format": "string", "minLength": 1, "optional": false, "maxLength": 127, "type": "string"}, "ttl": {"optional": true, "type": "number", "description": "Specify TTL", "format": "number"}}}], "type": "array", "$ref": "/axapi/v3/gslb/zone/{name}/service/{service-port}+{service-name}/dns-mx-record/{mx-name}"}
    :param dns_record_list: {"minItems": 1, "items": {"type": "dns-record"}, "uniqueItems": true, "array": [{"required": ["type"], "properties": {"data": {"description": "Specify DNS Data", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 512, "type": "string"}, "type": {"description": "Specify DNS Type", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": false}}}], "type": "array", "$ref": "/axapi/v3/gslb/zone/{name}/service/{service-port}+{service-name}/dns-record/{type}"}
    :param dns_ns_record_list: {"minItems": 1, "items": {"type": "dns-ns-record"}, "uniqueItems": true, "array": [{"required": ["ns-name"], "properties": {"ns-name": {"description": "Specify Domain Name", "format": "string", "minLength": 1, "optional": false, "maxLength": 127, "type": "string"}, "ttl": {"optional": true, "type": "number", "description": "Specify TTL", "format": "number"}}}], "type": "array", "$ref": "/axapi/v3/gslb/zone/{name}/service/{service-port}+{service-name}/dns-ns-record/{ns-name}"}
    :param health_check_gateway: {"description": "'enable': Enable Gateway Status Check; 'disable': Disable Gateway Status Check; ", "format": "enum", "default": "enable", "type": "string", "enum": ["enable", "disable"], "optional": true}
    :param disable: {"default": 0, "optional": true, "type": "number", "description": "Disable", "format": "flag"}
    :param dns_srv_record_list: {"minItems": 1, "items": {"type": "dns-srv-record"}, "uniqueItems": true, "array": [{"required": ["srv-name", "port"], "properties": {"priority": {"description": "Specify Priority", "format": "number", "type": "number", "maximum": 65535, "minimum": 0, "optional": true}, "srv-name": {"description": "Specify Domain Name", "format": "string", "minLength": 1, "optional": false, "maxLength": 127, "type": "string"}, "port": {"description": "Specify Port (Port Number)", "format": "number", "type": "number", "maximum": 65534, "minimum": 0, "optional": false}, "weight": {"description": "Specify Weight, default is 10", "format": "number", "default": 10, "optional": true, "maximum": 100, "minimum": 1, "type": "number"}, "ttl": {"optional": true, "type": "number", "description": "Specify TTL", "format": "number"}}}], "type": "array", "$ref": "/axapi/v3/gslb/zone/{name}/service/{service-port}+{service-name}/dns-srv-record/{srv-name}+{port}"}
    :param service_name: {"description": "Specify the service name for the zone, * for wildcard", "format": "string-rlx", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param action: {"optional": true, "enum": ["drop", "forward", "ignore", "reject"], "type": "string", "description": "'drop': Drop query; 'forward': Forward packet; 'ignore': Send empty response; 'reject': Send refuse response; ", "format": "enum"}
    :param dns_ptr_record_list: {"minItems": 1, "items": {"type": "dns-ptr-record"}, "uniqueItems": true, "array": [{"required": ["ptr-name"], "properties": {"ptr-name": {"description": "Specify Domain Name", "format": "string", "minLength": 1, "optional": false, "maxLength": 127, "type": "string"}, "ttl": {"optional": true, "type": "number", "description": "Specify TTL", "format": "number"}}}], "type": "array", "$ref": "/axapi/v3/gslb/zone/{name}/service/{service-port}+{service-name}/dns-ptr-record/{ptr-name}"}
    :param geo_location_list: {"minItems": 1, "items": {"type": "geo-location"}, "uniqueItems": true, "array": [{"required": ["geo-name"], "properties": {"forward-type": {"optional": true, "enum": ["both", "query", "response"], "type": "string", "description": "'both': Forward both query and response; 'query': Forward query from this geo-location; 'response': Forward response to this geo-location; ", "format": "enum"}, "alias": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"alias": {"minLength": 1, "maxLength": 127, "type": "string", "description": "Send CNAME response for this geo-location (Specify a CNAME record)", "format": "string"}, "optional": true}}]}, "action-type": {"optional": true, "enum": ["allow", "drop", "forward", "ignore", "reject"], "type": "string", "description": "'allow': Allow query from this geo-location; 'drop': Drop query from this geo-location; 'forward': Forward packet for this geo-location; 'ignore': Send empty response to this geo-location; 'reject': Send refuse response to this geo-location; ", "format": "enum"}, "policy": {"description": "Policy for this geo-location (Specify the policy name)", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "not": "action", "type": "string"}, "action": {"description": "Action for this geo-location", "format": "flag", "default": 0, "optional": true, "not": "policy", "type": "number"}, "geo-name": {"description": "Specify the geo-location", "format": "string", "minLength": 1, "optional": false, "maxLength": 127, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/gslb/zone/{name}/service/{service-port}+{service-name}/geo-location/{geo-name}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/gslb/zone/{name}/service/{service_port}+{service_name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "service_port","service_name"]

        self.b_key = "service"
        self.a10_url="/axapi/v3/gslb/zone/{name}/service/{service_port}+{service_name}"
        self.DeviceProxy = ""
        self.dns_a_record = {}
        self.forward_type = ""
        self.dns_cname_record_list = []
        self.health_check_port = []
        self.policy = ""
        self.dns_txt_record_list = []
        self.service_port = ""
        self.dns_mx_record_list = []
        self.dns_record_list = []
        self.dns_ns_record_list = []
        self.health_check_gateway = ""
        self.disable = ""
        self.dns_srv_record_list = []
        self.service_name = ""
        self.action = ""
        self.dns_ptr_record_list = []
        self.geo_location_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


