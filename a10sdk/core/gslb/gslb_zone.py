from a10sdk.common.A10BaseClass import A10BaseClass


class Template(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param dnssec: {"minLength": 1, "maxLength": 63, "type": "string", "description": "Specify DNSSEC template (Specify template name)", "format": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "template"
        self.DeviceProxy = ""
        self.dnssec = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class DnsSoaRecord(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param retry: {"default": 900, "type": "number", "description": "Specify Retry Time Interval, default is 900", "format": "number"}
    :param soa_name: {"minLength": 1, "maxLength": 127, "type": "string", "description": "DNS Server Name", "format": "string"}
    :param ex_retry: {"default": 900, "type": "number", "description": "Specify Retry Time Interval, default is 900", "format": "number"}
    :param ex_soa_ttl: {"type": "number", "description": "Specify Negative caching TTL, default is Zone TTL", "format": "number"}
    :param ex_serial: {"type": "number", "description": "Specify Serial Number, default is Current Time (Time Interval)", "format": "number"}
    :param refresh: {"default": 3600, "type": "number", "description": "Specify Refresh Time Interval, default is 3600", "format": "number"}
    :param ex_mail: {"minLength": 1, "maxLength": 127, "type": "string", "description": "Mailbox", "format": "string"}
    :param expire: {"default": 1209600, "type": "number", "description": "Specify Expire Time Interval, default is 1209600", "format": "number"}
    :param ex_expire: {"default": 1209600, "type": "number", "description": "Specify Expire Time Interval, default is 1209600", "format": "number"}
    :param external: {"minLength": 1, "maxLength": 127, "type": "string", "description": "Specify External SOA Record (DNS Server Name)", "format": "string"}
    :param mail: {"minLength": 1, "maxLength": 127, "type": "string", "description": "Mailbox", "format": "string"}
    :param serial: {"type": "number", "description": "Specify Serial Number, default is Current Time (Time Interval)", "format": "number"}
    :param ex_refresh: {"default": 3600, "type": "number", "description": "Specify Refresh Time Interval, default is 3600", "format": "number"}
    :param soa_ttl: {"type": "number", "description": "Specify Negative caching TTL, default is Zone TTL", "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "dns-soa-record"
        self.DeviceProxy = ""
        self.retry = ""
        self.soa_name = ""
        self.ex_retry = ""
        self.ex_soa_ttl = ""
        self.ex_serial = ""
        self.refresh = ""
        self.ex_mail = ""
        self.expire = ""
        self.ex_expire = ""
        self.external = ""
        self.mail = ""
        self.serial = ""
        self.ex_refresh = ""
        self.soa_ttl = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Zone(A10BaseClass):
    
    """Class Description::
    Specify the DNS zone name for which global SLB is provided.

    Class zone supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param name: {"description": "Specify the name for the DNS zone", "format": "string-rlx", "minLength": 1, "optional": false, "maxLength": 127, "type": "string"}
    :param dns_ns_record_list: {"minItems": 1, "items": {"type": "dns-ns-record"}, "uniqueItems": true, "array": [{"required": ["ns-name"], "properties": {"ns-name": {"description": "Specify Domain Name", "format": "string", "minLength": 1, "optional": false, "maxLength": 127, "type": "string"}, "ttl": {"optional": true, "type": "number", "description": "Specify TTL", "format": "number"}}}], "type": "array", "$ref": "/axapi/v3/gslb/zone/{name}/dns-ns-record/{ns-name}"}
    :param dns_mx_record_list: {"minItems": 1, "items": {"type": "dns-mx-record"}, "uniqueItems": true, "array": [{"required": ["mx-name"], "properties": {"priority": {"description": "Specify Priority", "format": "number", "type": "number", "maximum": 65535, "minimum": 0, "optional": true}, "mx-name": {"description": "Specify Domain Name", "format": "string", "minLength": 1, "optional": false, "maxLength": 127, "type": "string"}, "ttl": {"optional": true, "type": "number", "description": "Specify TTL", "format": "number"}}}], "type": "array", "$ref": "/axapi/v3/gslb/zone/{name}/dns-mx-record/{mx-name}"}
    :param disable: {"default": 0, "optional": true, "type": "number", "description": "Disable all services in the GSLB zone", "format": "flag"}
    :param ttl: {"description": "Specify the zone ttl value (TTL value, unit: second, default is 10)", "format": "number", "default": 10, "optional": true, "maximum": 1000000000, "minimum": 0, "not": "use-server-ttl", "type": "number"}
    :param policy: {"description": "Specify the policy for this zone (Specify policy name)", "format": "string", "default": "default", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param use_server_ttl: {"description": "Use DNS Server Response TTL value in GSLB Proxy mode", "format": "flag", "default": 0, "optional": true, "not": "ttl", "type": "number"}
    :param service_list: {"minItems": 1, "items": {"type": "service"}, "uniqueItems": true, "array": [{"required": ["service-port", "service-name"], "properties": {"dns-a-record": {"type": "object", "properties": {"dns-a-record-ipv6-list": {"minItems": 1, "items": {"type": "dns-a-record-ipv6"}, "uniqueItems": true, "array": [{"required": ["dns-a-record-ipv6"], "properties": {"as-replace": {"default": 0, "optional": true, "type": "number", "description": "Return this Service-IP when enable ip-replace", "format": "flag"}, "dns-a-record-ipv6": {"optional": false, "type": "string", "description": "IPV6 address", "format": "ipv6-address"}, "as-backup": {"default": 0, "optional": true, "type": "number", "description": "As backup when fail", "format": "flag"}, "weight": {"description": "Specify weight for Service-IP (Weight value)", "format": "number", "type": "number", "maximum": 100, "minimum": 1, "optional": true}, "disable": {"default": 0, "optional": true, "type": "number", "description": "Disable this Service-IP", "format": "flag"}, "static": {"default": 0, "optional": true, "type": "number", "description": "Return this Service-IP in DNS server mode", "format": "flag"}, "ttl": {"optional": true, "type": "number", "description": "Specify TTL for Service-IP", "format": "number"}, "admin-ip": {"description": "Specify admin priority of Service-IP (Specify the priority)", "format": "number", "type": "number", "maximum": 255, "minimum": 1, "optional": true}, "no-resp": {"default": 0, "optional": true, "type": "number", "description": "Don't use this Service-IP as DNS response", "format": "flag"}}}], "type": "array", "$ref": "/axapi/v3/gslb/zone/{name}/service/{service-port}+{service-name}/dns-a-record/dns-a-record-ipv6/{dns-a-record-ipv6}"}, "dns-a-record-ipv4-list": {"minItems": 1, "items": {"type": "dns-a-record-ipv4"}, "uniqueItems": true, "array": [{"required": ["dns-a-record-ip"], "properties": {"as-replace": {"default": 0, "optional": true, "type": "number", "description": "Return this Service-IP when enable ip-replace", "format": "flag"}, "dns-a-record-ip": {"optional": false, "type": "string", "description": "Specify IP address", "format": "ipv4-address"}, "as-backup": {"default": 0, "optional": true, "type": "number", "description": "As backup when fail", "format": "flag"}, "weight": {"description": "Specify weight for Service-IP (Weight value)", "format": "number", "type": "number", "maximum": 100, "minimum": 1, "optional": true}, "disable": {"default": 0, "optional": true, "type": "number", "description": "Disable this Service-IP", "format": "flag"}, "static": {"default": 0, "optional": true, "type": "number", "description": "Return this Service-IP in DNS server mode", "format": "flag"}, "ttl": {"optional": true, "type": "number", "description": "Specify TTL for Service-IP", "format": "number"}, "admin-ip": {"description": "Specify admin priority of Service-IP (Specify the priority)", "format": "number", "type": "number", "maximum": 255, "minimum": 1, "optional": true}, "no-resp": {"default": 0, "optional": true, "type": "number", "description": "Don't use this Service-IP as DNS response", "format": "flag"}}}], "type": "array", "$ref": "/axapi/v3/gslb/zone/{name}/service/{service-port}+{service-name}/dns-a-record/dns-a-record-ipv4/{dns-a-record-ip}"}, "dns-a-record-srv-list": {"minItems": 1, "items": {"type": "dns-a-record-srv"}, "uniqueItems": true, "array": [{"required": ["svrname"], "properties": {"as-replace": {"default": 0, "optional": true, "type": "number", "description": "Return this Service-IP when enable ip-replace", "format": "flag"}, "as-backup": {"default": 0, "optional": true, "type": "number", "description": "As backup when fail", "format": "flag"}, "weight": {"description": "Specify weight for Service-IP (Weight value)", "format": "number", "type": "number", "maximum": 100, "minimum": 1, "optional": true}, "svrname": {"description": "Specify name", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/gslb/service-ip"}, "disable": {"default": 0, "optional": true, "type": "number", "description": "Disable this Service-IP", "format": "flag"}, "static": {"default": 0, "optional": true, "type": "number", "description": "Return this Service-IP in DNS server mode", "format": "flag"}, "ttl": {"optional": true, "type": "number", "description": "Specify TTL for Service-IP", "format": "number"}, "admin-ip": {"description": "Specify admin priority of Service-IP (Specify the priority)", "format": "number", "type": "number", "maximum": 255, "minimum": 1, "optional": true}, "no-resp": {"default": 0, "optional": true, "type": "number", "description": "Don't use this Service-IP as DNS response", "format": "flag"}}}], "type": "array", "$ref": "/axapi/v3/gslb/zone/{name}/service/{service-port}+{service-name}/dns-a-record/dns-a-record-srv/{svrname}"}}}, "forward-type": {"optional": true, "enum": ["both", "query", "response"], "type": "string", "description": "'both': Forward both query and response; 'query': Forward query; 'response': Forward response; ", "format": "enum"}, "dns-cname-record-list": {"minItems": 1, "items": {"type": "dns-cname-record"}, "uniqueItems": true, "array": [{"required": ["alias-name"], "properties": {"as-backup": {"default": 0, "optional": true, "type": "number", "description": "As backup when fail", "format": "flag"}, "alias-name": {"description": "Specify the alias name", "format": "string", "minLength": 1, "optional": false, "maxLength": 127, "type": "string"}, "admin-preference": {"description": "Specify Administrative Preference, default is 100", "format": "number", "default": 100, "optional": true, "maximum": 255, "minimum": 0, "type": "number"}, "weight": {"description": "Specify Weight, default is 1", "format": "number", "default": 1, "optional": true, "maximum": 100, "minimum": 1, "type": "number"}}}], "type": "array", "$ref": "/axapi/v3/gslb/zone/{name}/service/{service-port}+{service-name}/dns-cname-record/{alias-name}"}, "health-check-port": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "health-check-port": {"description": "Check Related Port Status (Port Number)", "minimum": 0, "type": "number", "maximum": 65534, "format": "number"}}}]}, "policy": {"description": "Specify policy for this service (Specify policy name)", "format": "string", "default": "default", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}, "dns-txt-record-list": {"minItems": 1, "items": {"type": "dns-txt-record"}, "uniqueItems": true, "array": [{"required": ["record-name"], "properties": {"record-name": {"description": "Specify the Object Name for TXT Data", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}, "txt-data": {"description": "Specify TXT Data", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 1000, "type": "string"}, "ttl": {"optional": true, "type": "number", "description": "Specify TTL", "format": "number"}}}], "type": "array", "$ref": "/axapi/v3/gslb/zone/{name}/service/{service-port}+{service-name}/dns-txt-record/{record-name}"}, "service-port": {"description": "Port number of the service", "format": "number", "type": "number", "maximum": 65534, "minimum": 0, "optional": false}, "dns-mx-record-list": {"minItems": 1, "items": {"type": "dns-mx-record"}, "uniqueItems": true, "array": [{"required": ["mx-name"], "properties": {"priority": {"description": "Specify Priority", "format": "number", "type": "number", "maximum": 65535, "minimum": 0, "optional": true}, "mx-name": {"description": "Specify Domain Name", "format": "string", "minLength": 1, "optional": false, "maxLength": 127, "type": "string"}, "ttl": {"optional": true, "type": "number", "description": "Specify TTL", "format": "number"}}}], "type": "array", "$ref": "/axapi/v3/gslb/zone/{name}/service/{service-port}+{service-name}/dns-mx-record/{mx-name}"}, "dns-record-list": {"minItems": 1, "items": {"type": "dns-record"}, "uniqueItems": true, "array": [{"required": ["type"], "properties": {"data": {"description": "Specify DNS Data", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 512, "type": "string"}, "type": {"description": "Specify DNS Type", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": false}}}], "type": "array", "$ref": "/axapi/v3/gslb/zone/{name}/service/{service-port}+{service-name}/dns-record/{type}"}, "dns-ns-record-list": {"minItems": 1, "items": {"type": "dns-ns-record"}, "uniqueItems": true, "array": [{"required": ["ns-name"], "properties": {"ns-name": {"description": "Specify Domain Name", "format": "string", "minLength": 1, "optional": false, "maxLength": 127, "type": "string"}, "ttl": {"optional": true, "type": "number", "description": "Specify TTL", "format": "number"}}}], "type": "array", "$ref": "/axapi/v3/gslb/zone/{name}/service/{service-port}+{service-name}/dns-ns-record/{ns-name}"}, "health-check-gateway": {"description": "'enable': Enable Gateway Status Check; 'disable': Disable Gateway Status Check; ", "format": "enum", "default": "enable", "type": "string", "enum": ["enable", "disable"], "optional": true}, "disable": {"default": 0, "optional": true, "type": "number", "description": "Disable", "format": "flag"}, "dns-srv-record-list": {"minItems": 1, "items": {"type": "dns-srv-record"}, "uniqueItems": true, "array": [{"required": ["srv-name", "port"], "properties": {"priority": {"description": "Specify Priority", "format": "number", "type": "number", "maximum": 65535, "minimum": 0, "optional": true}, "srv-name": {"description": "Specify Domain Name", "format": "string", "minLength": 1, "optional": false, "maxLength": 127, "type": "string"}, "port": {"description": "Specify Port (Port Number)", "format": "number", "type": "number", "maximum": 65534, "minimum": 0, "optional": false}, "weight": {"description": "Specify Weight, default is 10", "format": "number", "default": 10, "optional": true, "maximum": 100, "minimum": 1, "type": "number"}, "ttl": {"optional": true, "type": "number", "description": "Specify TTL", "format": "number"}}}], "type": "array", "$ref": "/axapi/v3/gslb/zone/{name}/service/{service-port}+{service-name}/dns-srv-record/{srv-name}+{port}"}, "service-name": {"description": "Specify the service name for the zone, * for wildcard", "format": "string-rlx", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}, "action": {"optional": true, "enum": ["drop", "forward", "ignore", "reject"], "type": "string", "description": "'drop': Drop query; 'forward': Forward packet; 'ignore': Send empty response; 'reject': Send refuse response; ", "format": "enum"}, "dns-ptr-record-list": {"minItems": 1, "items": {"type": "dns-ptr-record"}, "uniqueItems": true, "array": [{"required": ["ptr-name"], "properties": {"ptr-name": {"description": "Specify Domain Name", "format": "string", "minLength": 1, "optional": false, "maxLength": 127, "type": "string"}, "ttl": {"optional": true, "type": "number", "description": "Specify TTL", "format": "number"}}}], "type": "array", "$ref": "/axapi/v3/gslb/zone/{name}/service/{service-port}+{service-name}/dns-ptr-record/{ptr-name}"}, "geo-location-list": {"minItems": 1, "items": {"type": "geo-location"}, "uniqueItems": true, "array": [{"required": ["geo-name"], "properties": {"forward-type": {"optional": true, "enum": ["both", "query", "response"], "type": "string", "description": "'both': Forward both query and response; 'query': Forward query from this geo-location; 'response': Forward response to this geo-location; ", "format": "enum"}, "alias": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"alias": {"minLength": 1, "maxLength": 127, "type": "string", "description": "Send CNAME response for this geo-location (Specify a CNAME record)", "format": "string"}, "optional": true}}]}, "action-type": {"optional": true, "enum": ["allow", "drop", "forward", "ignore", "reject"], "type": "string", "description": "'allow': Allow query from this geo-location; 'drop': Drop query from this geo-location; 'forward': Forward packet for this geo-location; 'ignore': Send empty response to this geo-location; 'reject': Send refuse response to this geo-location; ", "format": "enum"}, "policy": {"description": "Policy for this geo-location (Specify the policy name)", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "not": "action", "type": "string"}, "action": {"description": "Action for this geo-location", "format": "flag", "default": 0, "optional": true, "not": "policy", "type": "number"}, "geo-name": {"description": "Specify the geo-location", "format": "string", "minLength": 1, "optional": false, "maxLength": 127, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/gslb/zone/{name}/service/{service-port}+{service-name}/geo-location/{geo-name}"}}}], "type": "array", "$ref": "/axapi/v3/gslb/zone/{name}/service/{service-port}+{service-name}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/gslb/zone/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "zone"
        self.a10_url="/axapi/v3/gslb/zone/{name}"
        self.DeviceProxy = ""
        self.name = ""
        self.dns_ns_record_list = []
        self.dns_mx_record_list = []
        self.disable = ""
        self.template = {}
        self.ttl = ""
        self.policy = ""
        self.use_server_ttl = ""
        self.dns_soa_record = {}
        self.service_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


