from a10sdk.common.A10BaseClass import A10BaseClass


class SamplingEnable(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param counters1: {"enum": ["all", "data-sessions-current-epoch", "fullcone-created-current-epoch", "user-quote-created-current-epoch", "data-sessions-previous-epoch-first", "fullcone-created-previous-epoch-first", "user-quote-created-previous-epoch-first", "data-sessions-previous-epoch-last", "fullcone-created-previous-epoch-last", "user-quote-created-previous-epoch-last"], "type": "string", "description": "'all': all; 'data-sessions-current-epoch': data-sessions-current-epoch; 'fullcone-created-current-epoch': fullcone-created-current-epoch; 'user-quote-created-current-epoch': user-quote-created-current-epoch; 'data-sessions-previous-epoch-first': data-sessions-previous-epoch-first; 'fullcone-created-previous-epoch-first': fullcone-created-previous-epoch-first; 'user-quote-created-previous-epoch-first': user-quote-created-previous-epoch-first; 'data-sessions-previous-epoch-last': data-sessions-previous-epoch-last; 'fullcone-created-previous-epoch-last': fullcone-created-previous-epoch-last; 'user-quote-created-previous-epoch-last': user-quote-created-previous-epoch-last; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "sampling-enable"
        self.DeviceProxy = ""
        self.counters1 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Performance(A10BaseClass):
    
    """    :param sampling_enable: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "data-sessions-current-epoch", "fullcone-created-current-epoch", "user-quote-created-current-epoch", "data-sessions-previous-epoch-first", "fullcone-created-previous-epoch-first", "user-quote-created-previous-epoch-first", "data-sessions-previous-epoch-last", "fullcone-created-previous-epoch-last", "user-quote-created-previous-epoch-last"], "type": "string", "description": "'all': all; 'data-sessions-current-epoch': data-sessions-current-epoch; 'fullcone-created-current-epoch': fullcone-created-current-epoch; 'user-quote-created-current-epoch': user-quote-created-current-epoch; 'data-sessions-previous-epoch-first': data-sessions-previous-epoch-first; 'fullcone-created-previous-epoch-first': fullcone-created-previous-epoch-first; 'user-quote-created-previous-epoch-first': user-quote-created-previous-epoch-first; 'data-sessions-previous-epoch-last': data-sessions-previous-epoch-last; 'fullcone-created-previous-epoch-last': fullcone-created-previous-epoch-last; 'user-quote-created-previous-epoch-last': user-quote-created-previous-epoch-last; ", "format": "enum"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Large-Scale NAT performance statistics.

    Class performance supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/lsn/performance`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "performance"
        self.a10_url="/axapi/v3/cgnv6/lsn/performance"
        self.DeviceProxy = ""
        self.sampling_enable = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


