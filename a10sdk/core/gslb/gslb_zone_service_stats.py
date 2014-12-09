from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param received_query: {"description": "Number of DNS queries received for the service", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}
    :param sent_response: {"description": "Number of DNS replies sent to clients for the service", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "8"}
    :param sticky_mode_response: {"description": "Number of DNS replies sent to clients by the ACOS device to keep the clients on the same site. (This statistic applies only if ", "format": "counter", "type": "number", "oid": "6", "optional": true, "size": "8"}
    :param server_mode_response: {"description": "Number of DNS replies sent to clients by the ACOS device as a DNS server for the service. (This statistic applies only if the D", "format": "counter", "type": "number", "oid": "5", "optional": true, "size": "8"}
    :param cache_mode_response: {"description": "Number of cached DNS replies sent to clients by the ACOS device for the service. (This statistic applies only if the DNS cache ", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "8"}
    :param backup_mode_response: {"description": "help Number of DNS replies sent to clients by the ACOS device in backup mode", "format": "counter", "type": "number", "oid": "7", "optional": true, "size": "8"}
    :param proxy_mode_response: {"description": "Number of DNS replies sent to clients by the ACOS device as a DNS proxy for the service", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "8"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.received_query = ""
        self.sent_response = ""
        self.sticky_mode_response = ""
        self.server_mode_response = ""
        self.cache_mode_response = ""
        self.backup_mode_response = ""
        self.proxy_mode_response = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Service(A10BaseClass):
    
    """Class Description::
    Statistics for the object service.

    Class service supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param dns_ns_record_list: {"minItems": 1, "items": {"type": "dns-ns-record"}, "uniqueItems": true, "array": [{"required": ["ns-name"], "properties": {"stats": {"type": "object", "properties": {"hits": {"description": "Number of times the record has been used", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}}}, "ns-name": {"description": "Specify Domain Name", "format": "string", "minLength": 1, "oid": "1001", "optional": false, "maxLength": 127, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/gslb/zone/{name}/service/{service-port}+{service-name}/dns-a-record/dns-cname-record/{alias-name}/dns-mx-record/{mx-name}/dns-ns-record/{ns-name}"}
    :param dns_cname_record_list: {"minItems": 1, "items": {"type": "dns-cname-record"}, "uniqueItems": true, "array": [{"required": ["alias-name"], "properties": {}}], "type": "array", "$ref": "/axapi/v3/gslb/zone/{name}/service/{service-port}+{service-name}/dns-a-record/dns-cname-record/{alias-name}"}
    :param dns_txt_record_list: {"minItems": 1, "items": {"type": "dns-txt-record"}, "uniqueItems": true, "array": [{"required": ["record-name"], "properties": {"record-name": {"description": "Specify the Object Name for TXT Data", "format": "string", "minLength": 1, "oid": "1001", "optional": false, "maxLength": 63, "type": "string"}, "stats": {"type": "object", "properties": {"hits": {"description": "Number of times the record has been used", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}}}}}], "type": "array", "$ref": "/axapi/v3/gslb/zone/{name}/service/{service-port}+{service-name}/dns-a-record/dns-cname-record/{alias-name}/dns-mx-record/{mx-name}/dns-ns-record/{ns-name}/dns-ptr-record/{ptr-name}/dns-srv-record/{srv-name}+{port}/dns-txt-record/{record-name}"}
    :param service_port: {"description": "Port number of the service", "format": "number", "optional": false, "oid": "1001", "maximum": 65534, "minimum": 0, "type": "number"}
    :param dns_mx_record_list: {"minItems": 1, "items": {"type": "dns-mx-record"}, "uniqueItems": true, "array": [{"required": ["mx-name"], "properties": {"stats": {"type": "object", "properties": {"hits": {"description": "Number of times the record has been used", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}}}, "mx-name": {"description": "Specify Domain Name", "format": "string", "minLength": 1, "oid": "1001", "optional": false, "maxLength": 127, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/gslb/zone/{name}/service/{service-port}+{service-name}/dns-a-record/dns-cname-record/{alias-name}/dns-mx-record/{mx-name}"}
    :param dns_record_list: {"minItems": 1, "items": {"type": "dns-record"}, "uniqueItems": true, "array": [{"required": ["type"], "properties": {}}], "type": "array", "$ref": "/axapi/v3/gslb/zone/{name}/service/{service-port}+{service-name}/dns-a-record/dns-cname-record/{alias-name}/dns-mx-record/{mx-name}/dns-ns-record/{ns-name}/dns-ptr-record/{ptr-name}/dns-srv-record/{srv-name}+{port}/dns-txt-record/{record-name}/dns-record/{type}"}
    :param geo_location_list: {"minItems": 1, "items": {"type": "geo-location"}, "uniqueItems": true, "array": [{"required": ["geo-name"], "properties": {}}], "type": "array", "$ref": "/axapi/v3/gslb/zone/{name}/service/{service-port}+{service-name}/dns-a-record/dns-cname-record/{alias-name}/dns-mx-record/{mx-name}/dns-ns-record/{ns-name}/dns-ptr-record/{ptr-name}/dns-srv-record/{srv-name}+{port}/dns-txt-record/{record-name}/dns-record/{type}/geo-location/{geo-name}"}
    :param dns_srv_record_list: {"minItems": 1, "items": {"type": "dns-srv-record"}, "uniqueItems": true, "array": [{"required": ["srv-name", "port"], "properties": {"srv-name": {"description": "Specify Domain Name", "format": "string", "minLength": 1, "oid": "1001", "optional": false, "maxLength": 127, "type": "string"}, "stats": {"type": "object", "properties": {"hits": {"description": "Number of times the record has been used", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}}}, "port": {"description": "Specify Port (Port Number)", "format": "number", "optional": false, "oid": "1002", "maximum": 65534, "minimum": 0, "type": "number"}}}], "type": "array", "$ref": "/axapi/v3/gslb/zone/{name}/service/{service-port}+{service-name}/dns-a-record/dns-cname-record/{alias-name}/dns-mx-record/{mx-name}/dns-ns-record/{ns-name}/dns-ptr-record/{ptr-name}/dns-srv-record/{srv-name}+{port}"}
    :param service_name: {"description": "Specify the service name for the zone, * for wildcard", "format": "string-rlx", "minLength": 1, "oid": "1002", "optional": false, "maxLength": 63, "type": "string"}
    :param dns_ptr_record_list: {"minItems": 1, "items": {"type": "dns-ptr-record"}, "uniqueItems": true, "array": [{"required": ["ptr-name"], "properties": {"ptr-name": {"description": "Specify Domain Name", "format": "string", "minLength": 1, "oid": "1001", "optional": false, "maxLength": 127, "type": "string"}, "stats": {"type": "object", "properties": {"hits": {"description": "Number of times the record has been used", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}}}}}], "type": "array", "$ref": "/axapi/v3/gslb/zone/{name}/service/{service-port}+{service-name}/dns-a-record/dns-cname-record/{alias-name}/dns-mx-record/{mx-name}/dns-ns-record/{ns-name}/dns-ptr-record/{ptr-name}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/gslb/zone/{name}/service/{service_port}+{service_name}/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "service_port","service_name"]

        self.b_key = "service"
        self.a10_url="/axapi/v3/gslb/zone/{name}/service/{service_port}+{service_name}/stats"
        self.DeviceProxy = ""
        self.dns_a_record = {}
        self.stats = {}
        self.dns_ns_record_list = []
        self.dns_cname_record_list = []
        self.dns_txt_record_list = []
        self.service_port = ""
        self.dns_mx_record_list = []
        self.dns_record_list = []
        self.geo_location_list = []
        self.dns_srv_record_list = []
        self.service_name = ""
        self.dns_ptr_record_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


