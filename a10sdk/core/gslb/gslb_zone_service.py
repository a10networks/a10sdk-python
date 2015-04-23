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


class SamplingEnable(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param counters1: {"enum": ["all", "received-query", "sent-response", "proxy-mode-response", "cache-mode-response", "server-mode-response", "sticky-mode-response", "backup-mode-response"], "type": "string", "description": "'all': all; 'received-query': Number of DNS queries received for the service; 'sent-response': Number of DNS replies sent to clients for the service; 'proxy-mode-response': Number of DNS replies sent to clients by the ACOS device as a DNS proxy for the service; 'cache-mode-response': Number of cached DNS replies sent to clients by the ACOS device for the service. (This statistic applies only if the DNS cache; 'server-mode-response': Number of DNS replies sent to clients by the ACOS device as a DNS server for the service. (This statistic applies only if the D; 'sticky-mode-response': Number of DNS replies sent to clients by the ACOS device to keep the clients on the same site. (This statistic applies only if; 'backup-mode-response': help Number of DNS replies sent to clients by the ACOS device in backup mode; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "sampling-enable"
        self.DeviceProxy = ""
        self.counters1 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Service(A10BaseClass):
    
    """Class Description::
    Service information for the GSLB zone.

    Class service supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param forward_type: {"optional": true, "enum": ["both", "query", "response"], "type": "string", "description": "'both': Forward both query and response; 'query': Forward query; 'response': Forward response; ", "format": "enum"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param health_check_port: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "health-check-port": {"description": "Check Related Port Status (Port Number)", "minimum": 0, "type": "number", "maximum": 65534, "format": "number"}}}]}
    :param policy: {"description": "Specify policy for this service (Specify policy name)", "format": "string", "minLength": 1, "maxLength": 63, "optional": true, "default-depends-on": "gslb.zone::policy", "type": "string"}
    :param dns_txt_record_list: {"minItems": 1, "items": {"type": "dns-txt-record"}, "uniqueItems": true, "array": [{"required": ["record-name"], "properties": {"uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}, "record-name": {"description": "Specify the Object Name for TXT Data", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}, "txt-data": {"description": "Specify TXT Data", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 1000, "type": "string"}, "ttl": {"description": "Specify TTL", "format": "number", "default": 0, "optional": true, "maximum": 2147483647, "minimum": 0, "type": "number"}}}], "type": "array", "$ref": "/axapi/v3/gslb/zone/{name}/service/{service-port}+{service-name}/dns-txt-record/{record-name}"}
    :param service_port: {"description": "Port number of the service", "format": "number", "type": "number", "maximum": 65534, "minimum": 0, "optional": false}
    :param dns_mx_record_list: {"minItems": 1, "items": {"type": "dns-mx-record"}, "uniqueItems": true, "array": [{"required": ["mx-name"], "properties": {"priority": {"description": "Specify Priority", "format": "number", "type": "number", "maximum": 65535, "minimum": 0, "optional": true}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}, "mx-name": {"description": "Specify Domain Name", "format": "string", "minLength": 1, "optional": false, "maxLength": 127, "type": "string"}, "ttl": {"description": "Specify TTL", "format": "number", "default": 0, "optional": true, "maximum": 2147483647, "minimum": 0, "type": "number"}}}], "type": "array", "$ref": "/axapi/v3/gslb/zone/{name}/service/{service-port}+{service-name}/dns-mx-record/{mx-name}"}
    :param dns_record_list: {"minItems": 1, "items": {"type": "dns-record"}, "uniqueItems": true, "array": [{"required": ["type"], "properties": {"data": {"description": "Specify DNS Data", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 512, "type": "string"}, "type": {"description": "Specify DNS Type", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": false}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/gslb/zone/{name}/service/{service-port}+{service-name}/dns-record/{type}"}
    :param dns_ns_record_list: {"minItems": 1, "items": {"type": "dns-ns-record"}, "uniqueItems": true, "array": [{"required": ["ns-name"], "properties": {"sampling-enable": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "hits"], "type": "string", "description": "'all': all; 'hits': Number of times the record has been used; ", "format": "enum"}}}]}, "ns-name": {"description": "Specify Domain Name", "format": "string", "minLength": 1, "optional": false, "maxLength": 127, "type": "string"}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}, "ttl": {"description": "Specify TTL", "format": "number", "default": 0, "optional": true, "maximum": 2147483647, "minimum": 0, "type": "number"}}}], "type": "array", "$ref": "/axapi/v3/gslb/zone/{name}/service/{service-port}+{service-name}/dns-ns-record/{ns-name}"}
    :param health_check_gateway: {"description": "'enable': Enable Gateway Status Check; 'disable': Disable Gateway Status Check; ", "format": "enum", "default": "enable", "type": "string", "enum": ["enable", "disable"], "optional": true}
    :param sampling_enable: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "received-query", "sent-response", "proxy-mode-response", "cache-mode-response", "server-mode-response", "sticky-mode-response", "backup-mode-response"], "type": "string", "description": "'all': all; 'received-query': Number of DNS queries received for the service; 'sent-response': Number of DNS replies sent to clients for the service; 'proxy-mode-response': Number of DNS replies sent to clients by the ACOS device as a DNS proxy for the service; 'cache-mode-response': Number of cached DNS replies sent to clients by the ACOS device for the service. (This statistic applies only if the DNS cache; 'server-mode-response': Number of DNS replies sent to clients by the ACOS device as a DNS server for the service. (This statistic applies only if the D; 'sticky-mode-response': Number of DNS replies sent to clients by the ACOS device to keep the clients on the same site. (This statistic applies only if; 'backup-mode-response': help Number of DNS replies sent to clients by the ACOS device in backup mode; ", "format": "enum"}}}]}
    :param disable: {"default": 0, "optional": true, "type": "number", "description": "Disable", "format": "flag"}
    :param dns_srv_record_list: {"minItems": 1, "items": {"type": "dns-srv-record"}, "uniqueItems": true, "array": [{"required": ["srv-name", "port"], "properties": {"srv-name": {"description": "Specify Domain Name", "format": "string", "minLength": 1, "optional": false, "maxLength": 127, "type": "string"}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}, "weight": {"description": "Specify Weight, default is 10", "format": "number", "default": 10, "optional": true, "maximum": 100, "minimum": 1, "type": "number"}, "priority": {"description": "Specify Priority", "format": "number", "type": "number", "maximum": 65535, "minimum": 0, "optional": true}, "ttl": {"description": "Specify TTL", "format": "number", "type": "number", "maximum": 2147483647, "minimum": 0, "optional": true}, "port": {"description": "Specify Port (Port Number)", "format": "number", "type": "number", "maximum": 65534, "minimum": 0, "optional": false}}}], "type": "array", "$ref": "/axapi/v3/gslb/zone/{name}/service/{service-port}+{service-name}/dns-srv-record/{srv-name}+{port}"}
    :param service_name: {"description": "Specify the service name for the zone, * for wildcard", "format": "string-rlx", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param action: {"optional": true, "enum": ["drop", "forward", "ignore", "reject"], "type": "string", "description": "'drop': Drop query; 'forward': Forward packet; 'ignore': Send empty response; 'reject': Send refuse response; ", "format": "enum"}
    :param dns_ptr_record_list: {"minItems": 1, "items": {"type": "dns-ptr-record"}, "uniqueItems": true, "array": [{"required": ["ptr-name"], "properties": {"ptr-name": {"description": "Specify Domain Name", "format": "string", "minLength": 1, "optional": false, "maxLength": 127, "type": "string"}, "sampling-enable": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "hits"], "type": "string", "description": "'all': all; 'hits': Number of times the record has been used; ", "format": "enum"}}}]}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}, "ttl": {"description": "Specify TTL", "format": "number", "default": 0, "optional": true, "maximum": 2147483647, "minimum": 0, "type": "number"}}}], "type": "array", "$ref": "/axapi/v3/gslb/zone/{name}/service/{service-port}+{service-name}/dns-ptr-record/{ptr-name}"}
    :param dns_cname_record_list: {"minItems": 1, "items": {"type": "dns-cname-record"}, "uniqueItems": true, "array": [{"required": ["alias-name"], "properties": {"as-backup": {"default": 0, "optional": true, "type": "number", "description": "As backup when fail", "format": "flag"}, "alias-name": {"description": "Specify the alias name", "format": "string", "minLength": 1, "optional": false, "maxLength": 127, "type": "string"}, "admin-preference": {"description": "Specify Administrative Preference, default is 100", "format": "number", "default": 100, "optional": true, "maximum": 255, "minimum": 0, "type": "number"}, "weight": {"description": "Specify Weight, default is 1", "format": "number", "default": 1, "optional": true, "maximum": 100, "minimum": 1, "type": "number"}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/gslb/zone/{name}/service/{service-port}+{service-name}/dns-cname-record/{alias-name}"}
    :param geo_location_list: {"minItems": 1, "items": {"type": "geo-location"}, "uniqueItems": true, "array": [{"required": ["geo-name"], "properties": {"forward-type": {"optional": true, "enum": ["both", "query", "response"], "type": "string", "description": "'both': Forward both query and response; 'query': Forward query from this geo-location; 'response': Forward response to this geo-location; ", "format": "enum"}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}, "alias": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"alias": {"minLength": 1, "maxLength": 127, "type": "string", "description": "Send CNAME response for this geo-location (Specify a CNAME record)", "format": "string"}, "optional": true}}]}, "action-type": {"optional": true, "enum": ["allow", "drop", "forward", "ignore", "reject"], "type": "string", "description": "'allow': Allow query from this geo-location; 'drop': Drop query from this geo-location; 'forward': Forward packet for this geo-location; 'ignore': Send empty response to this geo-location; 'reject': Send refuse response to this geo-location; ", "format": "enum"}, "policy": {"description": "Policy for this geo-location (Specify the policy name)", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "not": "action", "type": "string"}, "action": {"description": "Action for this geo-location", "format": "flag", "default": 0, "optional": true, "not": "policy", "type": "number"}, "geo-name": {"description": "Specify the geo-location", "format": "string", "minLength": 1, "optional": false, "maxLength": 127, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/gslb/zone/{name}/service/{service-port}+{service-name}/geo-location/{geo-name}"}
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
        self.uuid = ""
        self.health_check_port = []
        self.policy = ""
        self.dns_txt_record_list = []
        self.service_port = ""
        self.dns_mx_record_list = []
        self.dns_record_list = []
        self.dns_ns_record_list = []
        self.health_check_gateway = ""
        self.sampling_enable = []
        self.disable = ""
        self.dns_srv_record_list = []
        self.service_name = ""
        self.action = ""
        self.dns_ptr_record_list = []
        self.dns_cname_record_list = []
        self.geo_location_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


