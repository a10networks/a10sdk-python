from a10sdk.common.A10BaseClass import A10BaseClass


class SamplingEnable(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param counters1: {"enum": ["all", "hits"], "type": "string", "description": "'all': all; 'hits': Number of times the record has been used; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "sampling-enable"
        self.DeviceProxy = ""
        self.counters1 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class DnsARecordIpv6(A10BaseClass):
    
    """Class Description::
    Specify DNS Address Record.

    Class dns-a-record-ipv6 supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param as_replace: {"default": 0, "optional": true, "type": "number", "description": "Return this Service-IP when enable ip-replace", "format": "flag"}
    :param dns_a_record_ipv6: {"optional": false, "type": "string", "description": "IPV6 address", "format": "ipv6-address"}
    :param as_backup: {"default": 0, "optional": true, "type": "number", "description": "As backup when fail", "format": "flag"}
    :param weight: {"description": "Specify weight for Service-IP (Weight value)", "format": "number", "type": "number", "maximum": 100, "minimum": 1, "optional": true}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param sampling_enable: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "hits"], "type": "string", "description": "'all': all; 'hits': Number of times the record has been used; ", "format": "enum"}}}]}
    :param disable: {"default": 0, "optional": true, "type": "number", "description": "Disable this Service-IP", "format": "flag"}
    :param static: {"default": 0, "optional": true, "type": "number", "description": "Return this Service-IP in DNS server mode", "format": "flag"}
    :param ttl: {"description": "Specify TTL for Service-IP", "format": "number", "default": 0, "optional": true, "maximum": 2147483647, "minimum": 0, "type": "number"}
    :param admin_ip: {"description": "Specify admin priority of Service-IP (Specify the priority)", "format": "number", "type": "number", "maximum": 255, "minimum": 1, "optional": true}
    :param no_resp: {"default": 0, "optional": true, "type": "number", "description": "Don't use this Service-IP as DNS response", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/gslb/zone/{name}/service/{service_port}+{service_name}/dns-a-record/dns-a-record-ipv6/{dns_a_record_ipv6}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "dns_a_record_ipv6"]

        self.b_key = "dns-a-record-ipv6"
        self.a10_url="/axapi/v3/gslb/zone/{name}/service/{service_port}+{service_name}/dns-a-record/dns-a-record-ipv6/{dns_a_record_ipv6}"
        self.DeviceProxy = ""
        self.as_replace = ""
        self.dns_a_record_ipv6 = ""
        self.as_backup = ""
        self.weight = ""
        self.uuid = ""
        self.sampling_enable = []
        self.disable = ""
        self.static = ""
        self.ttl = ""
        self.admin_ip = ""
        self.no_resp = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


