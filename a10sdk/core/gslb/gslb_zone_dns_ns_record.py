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


class DnsNsRecord(A10BaseClass):
    
    """Class Description::
    Specify DNS NS Record.

    Class dns-ns-record supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param sampling_enable: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "hits"], "type": "string", "description": "'all': all; 'hits': Number of times the record has been used; ", "format": "enum"}}}]}
    :param ns_name: {"description": "Specify Domain Name", "format": "string", "minLength": 1, "optional": false, "maxLength": 127, "type": "string"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param ttl: {"description": "Specify TTL", "format": "number", "type": "number", "maximum": 2147483647, "minimum": 0, "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/gslb/zone/{name}/dns-ns-record/{ns_name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "ns_name"]

        self.b_key = "dns-ns-record"
        self.a10_url="/axapi/v3/gslb/zone/{name}/dns-ns-record/{ns_name}"
        self.DeviceProxy = ""
        self.sampling_enable = []
        self.ns_name = ""
        self.uuid = ""
        self.ttl = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


