from a10sdk.common.A10BaseClass import A10BaseClass


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param state: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.state = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Zone(A10BaseClass):
    
    """Class Description::
    Operational Status for the object zone.

    Class zone supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param service_list: {"minItems": 1, "items": {"type": "service"}, "uniqueItems": true, "array": [{"required": ["service-port", "service-name"], "properties": {"oper": {"type": "object", "properties": {"total-sessions": {"type": "number", "format": "number"}, "cache-list": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"cache-ttl": {"type": "number", "format": "number"}, "additional-records": {"type": "number", "format": "number"}, "question-records": {"type": "number", "format": "number"}, "cache-dns-flag": {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}, "answer-records": {"type": "number", "format": "number"}, "alias": {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}, "cache-length": {"type": "number", "format": "number"}, "optional": true, "authority-records": {"type": "number", "format": "number"}}}]}, "state": {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}, "session-list": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"aging": {"type": "number", "format": "number"}, "hits": {"type": "number", "format": "number"}, "update": {"type": "number", "format": "number"}, "client": {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}, "last-second-hits": {"type": "number", "format": "number"}, "mode": {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}, "ttl": {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}, "optional": true, "best": {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}}}]}, "matched": {"type": "number", "format": "number"}}}, "dns-a-record": {"type": "object", "properties": {"oper": {"type": "object", "properties": {}}}}, "dns-ns-record-list": {"minItems": 1, "items": {"type": "dns-ns-record"}, "uniqueItems": true, "array": [{"required": ["ns-name"], "properties": {"oper": {"type": "object", "properties": {"last-server": {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}}}, "ns-name": {"description": "Specify Domain Name", "format": "string", "minLength": 1, "oid": "1001", "optional": false, "maxLength": 127, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/gslb/zone/{name}/dns-mx-record/{mx-name}/dns-ns-record/{ns-name}/service/{service-port}+{service-name}/dns-mx-record/{mx-name}/dns-ns-record/{ns-name}"}, "service-port": {"description": "Port number of the service", "format": "number", "optional": false, "oid": "1001", "maximum": 65534, "minimum": 0, "type": "number"}, "dns-mx-record-list": {"minItems": 1, "items": {"type": "dns-mx-record"}, "uniqueItems": true, "array": [{"required": ["mx-name"], "properties": {"oper": {"type": "object", "properties": {"last-server": {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}}}, "mx-name": {"description": "Specify Domain Name", "format": "string", "minLength": 1, "oid": "1001", "optional": false, "maxLength": 127, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/gslb/zone/{name}/dns-mx-record/{mx-name}/dns-ns-record/{ns-name}/service/{service-port}+{service-name}/dns-mx-record/{mx-name}"}, "service-name": {"description": "Specify the service name for the zone, * for wildcard", "format": "string-rlx", "minLength": 1, "oid": "1002", "optional": false, "maxLength": 63, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/gslb/zone/{name}/dns-mx-record/{mx-name}/dns-ns-record/{ns-name}/service/{service-port}+{service-name}"}
    :param dns_mx_record_list: {"minItems": 1, "items": {"type": "dns-mx-record"}, "uniqueItems": true, "array": [{"required": ["mx-name"], "properties": {"oper": {"type": "object", "properties": {"last-server": {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}}}, "mx-name": {"description": "Specify Domain Name", "format": "string", "minLength": 1, "oid": "1001", "optional": false, "maxLength": 127, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/gslb/zone/{name}/dns-mx-record/{mx-name}"}
    :param name: {"description": "Specify the name for the DNS zone", "format": "string-rlx", "minLength": 1, "oid": "1001", "optional": false, "maxLength": 127, "type": "string"}
    :param dns_ns_record_list: {"minItems": 1, "items": {"type": "dns-ns-record"}, "uniqueItems": true, "array": [{"required": ["ns-name"], "properties": {"oper": {"type": "object", "properties": {"last-server": {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}}}, "ns-name": {"description": "Specify Domain Name", "format": "string", "minLength": 1, "oid": "1001", "optional": false, "maxLength": 127, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/gslb/zone/{name}/dns-mx-record/{mx-name}/dns-ns-record/{ns-name}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/gslb/zone/{name}/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "zone"
        self.a10_url="/axapi/v3/gslb/zone/{name}/oper"
        self.DeviceProxy = ""
        self.oper = {}
        self.service_list = []
        self.dns_mx_record_list = []
        self.name = ""
        self.dns_ns_record_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


