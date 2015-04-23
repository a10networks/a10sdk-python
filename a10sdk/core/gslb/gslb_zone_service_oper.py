from a10sdk.common.A10BaseClass import A10BaseClass


class CacheList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param cache_ttl: {"type": "number", "format": "number"}
    :param additional_records: {"type": "number", "format": "number"}
    :param question_records: {"type": "number", "format": "number"}
    :param cache_dns_flag: {"type": "string", "format": "string"}
    :param answer_records: {"type": "number", "format": "number"}
    :param alias: {"type": "string", "format": "string"}
    :param cache_length: {"type": "number", "format": "number"}
    :param authority_records: {"type": "number", "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "cache-list"
        self.DeviceProxy = ""
        self.cache_ttl = ""
        self.additional_records = ""
        self.question_records = ""
        self.cache_dns_flag = ""
        self.answer_records = ""
        self.alias = ""
        self.cache_length = ""
        self.authority_records = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class SessionList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param aging: {"type": "number", "format": "number"}
    :param hits: {"type": "number", "format": "number"}
    :param update: {"type": "number", "format": "number"}
    :param client: {"type": "string", "format": "string"}
    :param last_second_hits: {"type": "number", "format": "number"}
    :param mode: {"type": "string", "format": "string"}
    :param ttl: {"type": "string", "format": "string"}
    :param best: {"type": "string", "format": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "session-list"
        self.DeviceProxy = ""
        self.aging = ""
        self.hits = ""
        self.update = ""
        self.client = ""
        self.last_second_hits = ""
        self.mode = ""
        self.ttl = ""
        self.best = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param total_sessions: {"type": "number", "format": "number"}
    :param cache_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"cache-ttl": {"type": "number", "format": "number"}, "additional-records": {"type": "number", "format": "number"}, "question-records": {"type": "number", "format": "number"}, "cache-dns-flag": {"type": "string", "format": "string"}, "answer-records": {"type": "number", "format": "number"}, "alias": {"type": "string", "format": "string"}, "cache-length": {"type": "number", "format": "number"}, "optional": true, "authority-records": {"type": "number", "format": "number"}}}]}
    :param state: {"type": "string", "format": "string"}
    :param session_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"aging": {"type": "number", "format": "number"}, "hits": {"type": "number", "format": "number"}, "update": {"type": "number", "format": "number"}, "client": {"type": "string", "format": "string"}, "last-second-hits": {"type": "number", "format": "number"}, "mode": {"type": "string", "format": "string"}, "ttl": {"type": "string", "format": "string"}, "optional": true, "best": {"type": "string", "format": "string"}}}]}
    :param matched: {"type": "number", "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.total_sessions = ""
        self.cache_list = []
        self.state = ""
        self.session_list = []
        self.matched = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Service(A10BaseClass):
    
    """Class Description::
    Operational Status for the object service.

    Class service supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param service_port: {"description": "Port number of the service", "format": "number", "optional": false, "oid": "1001", "maximum": 65534, "minimum": 0, "type": "number"}
    :param dns_mx_record_list: {"minItems": 1, "items": {"type": "dns-mx-record"}, "uniqueItems": true, "array": [{"required": ["mx-name"], "properties": {"oper": {"type": "object", "properties": {"last-server": {"type": "string", "format": "string"}}}, "mx-name": {"description": "Specify Domain Name", "format": "string", "minLength": 1, "oid": "1001", "optional": false, "maxLength": 127, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/gslb/zone/{name}/service/{service-port}+{service-name}/dns-mx-record/{mx-name}"}
    :param dns_ns_record_list: {"minItems": 1, "items": {"type": "dns-ns-record"}, "uniqueItems": true, "array": [{"required": ["ns-name"], "properties": {"oper": {"type": "object", "properties": {"last-server": {"type": "string", "format": "string"}}}, "ns-name": {"description": "Specify Domain Name", "format": "string", "minLength": 1, "oid": "1001", "optional": false, "maxLength": 127, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/gslb/zone/{name}/service/{service-port}+{service-name}/dns-mx-record/{mx-name}/dns-ns-record/{ns-name}"}
    :param service_name: {"description": "Specify the service name for the zone, * for wildcard", "format": "string-rlx", "minLength": 1, "oid": "1002", "optional": false, "maxLength": 63, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/gslb/zone/{name}/service/{service_port}+{service_name}/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "service"
        self.a10_url="/axapi/v3/gslb/zone/{name}/service/{service_port}+{service_name}/oper"
        self.DeviceProxy = ""
        self.oper = {}
        self.service_port = ""
        self.dns_mx_record_list = []
        self.dns_ns_record_list = []
        self.service_name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


