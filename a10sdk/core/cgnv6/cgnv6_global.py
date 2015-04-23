from a10sdk.common.A10BaseClass import A10BaseClass


class SamplingEnable(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param counters1: {"enum": ["all", "tcp-total-ports-allocated", "udp-total-ports-allocated", "icmp-total-ports-allocated"], "type": "string", "description": "'all': all; 'tcp-total-ports-allocated': Total TCP ports allocated; 'udp-total-ports-allocated': Total UDP ports allocated; 'icmp-total-ports-allocated': Total ICMP ports allocated; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "sampling-enable"
        self.DeviceProxy = ""
        self.counters1 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Global(A10BaseClass):
    
    """    :param sampling_enable: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "tcp-total-ports-allocated", "udp-total-ports-allocated", "icmp-total-ports-allocated"], "type": "string", "description": "'all': all; 'tcp-total-ports-allocated': Total TCP ports allocated; 'udp-total-ports-allocated': Total UDP ports allocated; 'icmp-total-ports-allocated': Total ICMP ports allocated; ", "format": "enum"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    CGN global paramters.

    Class global supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/global`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "global"
        self.a10_url="/axapi/v3/cgnv6/global"
        self.DeviceProxy = ""
        self.sampling_enable = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


