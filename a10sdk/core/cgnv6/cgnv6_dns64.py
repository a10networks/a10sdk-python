from a10sdk.common.A10BaseClass import A10BaseClass


class SamplingEnable(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param counters1: {"enum": ["all", "query", "query-bad-pkt", "query-chg", "query-parallel", "query-passive", "resp", "resp-bad-pkt", "resp-bad-qr", "resp-chg", "resp-err", "resp-empty", "resp-local", "adjust", "cache", "drop"], "type": "string", "description": "'all': all; 'query': Query; 'query-bad-pkt': Query Bad Packet; 'query-chg': Query Changed; 'query-parallel': Query Parallel; 'query-passive': Query Passive; 'resp': Response; 'resp-bad-pkt': Response Bad Packet; 'resp-bad-qr': Response Bad Query; 'resp-chg': Response Changed; 'resp-err': Response Error; 'resp-empty': Response Empty; 'resp-local': Response Local; 'adjust': Translated; 'cache': Cache; 'drop': Dropped; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "sampling-enable"
        self.DeviceProxy = ""
        self.counters1 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Dns64(A10BaseClass):
    
    """    :param sampling_enable: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "query", "query-bad-pkt", "query-chg", "query-parallel", "query-passive", "resp", "resp-bad-pkt", "resp-bad-qr", "resp-chg", "resp-err", "resp-empty", "resp-local", "adjust", "cache", "drop"], "type": "string", "description": "'all': all; 'query': Query; 'query-bad-pkt': Query Bad Packet; 'query-chg': Query Changed; 'query-parallel': Query Parallel; 'query-passive': Query Passive; 'resp': Response; 'resp-bad-pkt': Response Bad Packet; 'resp-bad-qr': Response Bad Query; 'resp-chg': Response Changed; 'resp-err': Response Error; 'resp-empty': Response Empty; 'resp-local': Response Local; 'adjust': Translated; 'cache': Cache; 'drop': Dropped; ", "format": "enum"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    DNS64 Statistics.

    Class dns64 supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/dns64`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "dns64"
        self.a10_url="/axapi/v3/cgnv6/dns64"
        self.DeviceProxy = ""
        self.sampling_enable = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


