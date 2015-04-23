from a10sdk.common.A10BaseClass import A10BaseClass


class SamplingEnable(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param counters1: {"enum": ["all", "sessions_alloc", "sessions_freed", "out_of_sessions", "too_many_sessions", "called", "permitted", "threshold_exceed", "lockout_drop", "log_msg_sent"], "type": "string", "description": "'all': all; 'sessions_alloc': Sessions allocated; 'sessions_freed': Sessions freed; 'out_of_sessions': Out of sessions; 'too_many_sessions': Too many sessions consumed; 'called': Threshold check count; 'permitted': Honor threshold  count; 'threshold_exceed': Threshold exceeded count; 'lockout_drop': Lockout drops; 'log_msg_sent': Log messages sent; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "sampling-enable"
        self.DeviceProxy = ""
        self.counters1 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class CrlSrcip(A10BaseClass):
    
    """    :param sampling_enable: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "sessions_alloc", "sessions_freed", "out_of_sessions", "too_many_sessions", "called", "permitted", "threshold_exceed", "lockout_drop", "log_msg_sent"], "type": "string", "description": "'all': all; 'sessions_alloc': Sessions allocated; 'sessions_freed': Sessions freed; 'out_of_sessions': Out of sessions; 'too_many_sessions': Too many sessions consumed; 'called': Threshold check count; 'permitted': Honor threshold  count; 'threshold_exceed': Threshold exceeded count; 'lockout_drop': Lockout drops; 'log_msg_sent': Log messages sent; ", "format": "enum"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Show connection rate limit statistics.

    Class crl-srcip supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/crl-srcip`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "crl-srcip"
        self.a10_url="/axapi/v3/slb/crl-srcip"
        self.DeviceProxy = ""
        self.sampling_enable = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


