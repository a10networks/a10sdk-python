from a10sdk.common.A10BaseClass import A10BaseClass


class SamplingEnable(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param counters1: {"enum": ["all", "over_limit_drop", "limit_intf_drop", "limit_vserver_drop", "limit_total_drop", "lockup_time_left", "curr_rate", "v6_over_limit_drop", "v6_limit_intf_drop", "v6_limit_vserver_drop", "v6_limit_total_drop", "v6_lockup_time_left", "v6_curr_rate"], "type": "string", "description": "'all': all; 'over_limit_drop': Over limit drops; 'limit_intf_drop': Interfaces rate limit drops; 'limit_vserver_drop': Virtual Server rate limit drops; 'limit_total_drop': Total rate limit drops; 'lockup_time_left': Lockup time left; 'curr_rate': Current rate; 'v6_over_limit_drop': Over limit drops (v6); 'v6_limit_intf_drop': Interfaces rate limit drops (v6); 'v6_limit_vserver_drop': Virtual Server rate limit drops (v6); 'v6_limit_total_drop': Total rate limit drops (v6); 'v6_lockup_time_left': Lockup time left (v6); 'v6_curr_rate': Current rate (v6); ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "sampling-enable"
        self.DeviceProxy = ""
        self.counters1 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class IcmpRate(A10BaseClass):
    
    """    :param sampling_enable: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "over_limit_drop", "limit_intf_drop", "limit_vserver_drop", "limit_total_drop", "lockup_time_left", "curr_rate", "v6_over_limit_drop", "v6_limit_intf_drop", "v6_limit_vserver_drop", "v6_limit_total_drop", "v6_lockup_time_left", "v6_curr_rate"], "type": "string", "description": "'all': all; 'over_limit_drop': Over limit drops; 'limit_intf_drop': Interfaces rate limit drops; 'limit_vserver_drop': Virtual Server rate limit drops; 'limit_total_drop': Total rate limit drops; 'lockup_time_left': Lockup time left; 'curr_rate': Current rate; 'v6_over_limit_drop': Over limit drops (v6); 'v6_limit_intf_drop': Interfaces rate limit drops (v6); 'v6_limit_vserver_drop': Virtual Server rate limit drops (v6); 'v6_limit_total_drop': Total rate limit drops (v6); 'v6_lockup_time_left': Lockup time left (v6); 'v6_curr_rate': Current rate (v6); ", "format": "enum"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Icmp rate limit statistics.

    Class icmp-rate supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/system/icmp-rate`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "icmp-rate"
        self.a10_url="/axapi/v3/system/icmp-rate"
        self.DeviceProxy = ""
        self.sampling_enable = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


