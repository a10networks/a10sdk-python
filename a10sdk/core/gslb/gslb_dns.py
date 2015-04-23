from a10sdk.common.A10BaseClass import A10BaseClass


class SamplingEnable(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param counters1: {"enum": ["all", "total-query", "total-response", "bad-packet-query", "bad-packet-response", "bad-header-query", "bad-header-response", "bad-format-query", "bad-format-response", "bad-service-query", "bad-service-response", "bad-class-query", "bad-class-response", "bad-type-query", "bad-type-response", "no_answer"], "type": "string", "description": "'all': all; 'total-query': Total number of DNS queries received; 'total-response': Total number of DNS replies sent to clients; 'bad-packet-query': Number of queries with incorrect data length; 'bad-packet-response': Number of replies with incorrect data length; 'bad-header-query': Number of queries with incorrect header; 'bad-header-response': Number of replies with incorrect header; 'bad-format-query': Number of queries with incorrect format; 'bad-format-response': Number of replies with incorrect format; 'bad-service-query': Number of queries with unknown service; 'bad-service-response': Number of replies with unknown service; 'bad-class-query': Number of queries with incorrect class; 'bad-class-response': Number of replies with incorrect class; 'bad-type-query': Number of queries with incorrect type; 'bad-type-response': Number of replies with incorrect type; 'no_answer': Number of replies with unknown server IP; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "sampling-enable"
        self.DeviceProxy = ""
        self.counters1 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Dns(A10BaseClass):
    
    """    :param action: {"description": "'none': No action (default); 'drop': Drop query; 'reject': Send refuse response; 'ignore': Send empty response; ", "format": "enum", "default": "none", "type": "string", "enum": ["none", "drop", "reject", "ignore"], "optional": true}
    :param sampling_enable: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "total-query", "total-response", "bad-packet-query", "bad-packet-response", "bad-header-query", "bad-header-response", "bad-format-query", "bad-format-response", "bad-service-query", "bad-service-response", "bad-class-query", "bad-class-response", "bad-type-query", "bad-type-response", "no_answer"], "type": "string", "description": "'all': all; 'total-query': Total number of DNS queries received; 'total-response': Total number of DNS replies sent to clients; 'bad-packet-query': Number of queries with incorrect data length; 'bad-packet-response': Number of replies with incorrect data length; 'bad-header-query': Number of queries with incorrect header; 'bad-header-response': Number of replies with incorrect header; 'bad-format-query': Number of queries with incorrect format; 'bad-format-response': Number of replies with incorrect format; 'bad-service-query': Number of queries with unknown service; 'bad-service-response': Number of replies with unknown service; 'bad-class-query': Number of queries with incorrect class; 'bad-class-response': Number of replies with incorrect class; 'bad-type-query': Number of queries with incorrect type; 'bad-type-response': Number of replies with incorrect type; 'no_answer': Number of replies with unknown server IP; ", "format": "enum"}}}]}
    :param logging: {"description": "'none': No logging (default); 'query': DNS Query; 'response': DNS Response; 'both': Both DNS Query and Response; ", "format": "enum", "default": "none", "type": "string", "enum": ["none", "query", "response", "both"], "optional": true}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    DNS Global Options.

    Class dns supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/gslb/dns`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "dns"
        self.a10_url="/axapi/v3/gslb/dns"
        self.DeviceProxy = ""
        self.action = ""
        self.sampling_enable = []
        self.logging = ""
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


