from a10sdk.common.A10BaseClass import A10BaseClass


class DnsARecord(A10BaseClass):
    
    """Class Description::
    Specify DNS Address Record.

    Class dns-a-record supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param dns_a_record_ipv6_list: {"minItems": 1, "items": {"type": "dns-a-record-ipv6"}, "uniqueItems": true, "array": [{"required": ["dns-a-record-ipv6"], "properties": {"as-replace": {"default": 0, "optional": true, "type": "number", "description": "Return this Service-IP when enable ip-replace", "format": "flag"}, "dns-a-record-ipv6": {"optional": false, "type": "string", "description": "IPV6 address", "format": "ipv6-address"}, "as-backup": {"default": 0, "optional": true, "type": "number", "description": "As backup when fail", "format": "flag"}, "weight": {"description": "Specify weight for Service-IP (Weight value)", "format": "number", "type": "number", "maximum": 100, "minimum": 1, "optional": true}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}, "sampling-enable": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "hits"], "type": "string", "description": "'all': all; 'hits': Number of times the record has been used; ", "format": "enum"}}}]}, "disable": {"default": 0, "optional": true, "type": "number", "description": "Disable this Service-IP", "format": "flag"}, "static": {"default": 0, "optional": true, "type": "number", "description": "Return this Service-IP in DNS server mode", "format": "flag"}, "ttl": {"description": "Specify TTL for Service-IP", "format": "number", "default": 0, "optional": true, "maximum": 2147483647, "minimum": 0, "type": "number"}, "admin-ip": {"description": "Specify admin priority of Service-IP (Specify the priority)", "format": "number", "type": "number", "maximum": 255, "minimum": 1, "optional": true}, "no-resp": {"default": 0, "optional": true, "type": "number", "description": "Don't use this Service-IP as DNS response", "format": "flag"}}}], "type": "array", "$ref": "/axapi/v3/gslb/zone/{name}/service/{service-port}+{service-name}/dns-a-record/dns-a-record-ipv6/{dns-a-record-ipv6}"}
    :param dns_a_record_ipv4_list: {"minItems": 1, "items": {"type": "dns-a-record-ipv4"}, "uniqueItems": true, "array": [{"required": ["dns-a-record-ip"], "properties": {"as-replace": {"default": 0, "optional": true, "type": "number", "description": "Return this Service-IP when enable ip-replace", "format": "flag"}, "dns-a-record-ip": {"optional": false, "type": "string", "description": "Specify IP address", "format": "ipv4-address"}, "as-backup": {"default": 0, "optional": true, "type": "number", "description": "As backup when fail", "format": "flag"}, "weight": {"description": "Specify weight for Service-IP (Weight value)", "format": "number", "type": "number", "maximum": 100, "minimum": 1, "optional": true}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}, "sampling-enable": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "hits"], "type": "string", "description": "'all': all; 'hits': Number of times the record has been used; ", "format": "enum"}}}]}, "disable": {"default": 0, "optional": true, "type": "number", "description": "Disable this Service-IP", "format": "flag"}, "static": {"default": 0, "optional": true, "type": "number", "description": "Return this Service-IP in DNS server mode", "format": "flag"}, "ttl": {"description": "Specify TTL for Service-IP", "format": "number", "default": 0, "optional": true, "maximum": 2147483647, "minimum": 0, "type": "number"}, "admin-ip": {"description": "Specify admin priority of Service-IP (Specify the priority)", "format": "number", "type": "number", "maximum": 255, "minimum": 1, "optional": true}, "no-resp": {"default": 0, "optional": true, "type": "number", "description": "Don't use this Service-IP as DNS response", "format": "flag"}}}], "type": "array", "$ref": "/axapi/v3/gslb/zone/{name}/service/{service-port}+{service-name}/dns-a-record/dns-a-record-ipv4/{dns-a-record-ip}"}
    :param dns_a_record_srv_list: {"minItems": 1, "items": {"type": "dns-a-record-srv"}, "uniqueItems": true, "array": [{"required": ["svrname"], "properties": {"as-replace": {"default": 0, "optional": true, "type": "number", "description": "Return this Service-IP when enable ip-replace", "format": "flag"}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}, "as-backup": {"default": 0, "optional": true, "type": "number", "description": "As backup when fail", "format": "flag"}, "weight": {"description": "Specify weight for Service-IP (Weight value)", "format": "number", "type": "number", "maximum": 100, "minimum": 1, "optional": true}, "svrname": {"description": "Specify name", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/gslb/service-ip"}, "sampling-enable": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "hits"], "type": "string", "description": "'all': all; 'hits': Number of times the record has been used; ", "format": "enum"}}}]}, "disable": {"default": 0, "optional": true, "type": "number", "description": "Disable this Service-IP", "format": "flag"}, "static": {"default": 0, "optional": true, "type": "number", "description": "Return this Service-IP in DNS server mode", "format": "flag"}, "ttl": {"description": "Specify TTL for Service-IP", "format": "number", "default": 0, "optional": true, "maximum": 2147483647, "minimum": 0, "type": "number"}, "admin-ip": {"description": "Specify admin priority of Service-IP (Specify the priority)", "format": "number", "type": "number", "maximum": 255, "minimum": 1, "optional": true}, "no-resp": {"default": 0, "optional": true, "type": "number", "description": "Don't use this Service-IP as DNS response", "format": "flag"}}}], "type": "array", "$ref": "/axapi/v3/gslb/zone/{name}/service/{service-port}+{service-name}/dns-a-record/dns-a-record-srv/{svrname}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/gslb/zone/{name}/service/{service_port}+{service_name}/dns-a-record`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "dns-a-record"
        self.a10_url="/axapi/v3/gslb/zone/{name}/service/{service_port}+{service_name}/dns-a-record"
        self.DeviceProxy = ""
        self.dns_a_record_ipv6_list = []
        self.dns_a_record_ipv4_list = []
        self.dns_a_record_srv_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


