from a10sdk.common.A10BaseClass import A10BaseClass


class SamplingEnable(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param counters1: {"enum": ["all", "current_open", "current_active", "nbind", "nunbind", "nestab", "ntermi", "ntermi_err", "delay_unbind", "long_resp", "miss_resp", "unbound_data_rcv", "pause_conn", "pause_conn_fail", "resume_conn", "not_remove_from_rport"], "type": "string", "description": "'all': all; 'current_open': Open persist; 'current_active': Active persist; 'nbind': Total bind; 'nunbind': Total unbind; 'nestab': Total established; 'ntermi': Total terminated; 'ntermi_err': Total terminated by err; 'delay_unbind': Delayed unbind; 'long_resp': Long resp; 'miss_resp': Missed resp; 'unbound_data_rcv': Unbound data rcvd; 'pause_conn': Pause request; 'pause_conn_fail': Pause request fail; 'resume_conn': Resume request; 'not_remove_from_rport': Not remove from list; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "sampling-enable"
        self.DeviceProxy = ""
        self.counters1 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class ConnectionReuse(A10BaseClass):
    
    """    :param sampling_enable: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "current_open", "current_active", "nbind", "nunbind", "nestab", "ntermi", "ntermi_err", "delay_unbind", "long_resp", "miss_resp", "unbound_data_rcv", "pause_conn", "pause_conn_fail", "resume_conn", "not_remove_from_rport"], "type": "string", "description": "'all': all; 'current_open': Open persist; 'current_active': Active persist; 'nbind': Total bind; 'nunbind': Total unbind; 'nestab': Total established; 'ntermi': Total terminated; 'ntermi_err': Total terminated by err; 'delay_unbind': Delayed unbind; 'long_resp': Long resp; 'miss_resp': Missed resp; 'unbound_data_rcv': Unbound data rcvd; 'pause_conn': Pause request; 'pause_conn_fail': Pause request fail; 'resume_conn': Resume request; 'not_remove_from_rport': Not remove from list; ", "format": "enum"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Show Connection Reuse Statistics.

    Class connection-reuse supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/connection-reuse`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "connection-reuse"
        self.a10_url="/axapi/v3/slb/connection-reuse"
        self.DeviceProxy = ""
        self.sampling_enable = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


