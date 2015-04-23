from a10sdk.common.A10BaseClass import A10BaseClass


class SamplingEnable(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param counters1: {"enum": ["all", "pause_conn", "pause_conn_fail", "resume_conn", "event_resume_conn", "timer_resume_conn", "try_to_resume_conn", "retry_resume_conn", "error_resume_conn", "open_new_server_conn", "reuse_server_idle_conn", "inc_aflow_limit"], "type": "string", "description": "'all': all; 'pause_conn': Pause connection; 'pause_conn_fail': Pause connection fail; 'resume_conn': Resume connection; 'event_resume_conn': Resume conn by event; 'timer_resume_conn': Resume conn by timer; 'try_to_resume_conn': Resume conn by trying; 'retry_resume_conn': Resume conn by retry; 'error_resume_conn': Resume conn by error; 'open_new_server_conn': Open new server conn; 'reuse_server_idle_conn': Reuse idle server conn; 'inc_aflow_limit': Inc aFlow limit; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "sampling-enable"
        self.DeviceProxy = ""
        self.counters1 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Aflow(A10BaseClass):
    
    """    :param sampling_enable: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "pause_conn", "pause_conn_fail", "resume_conn", "event_resume_conn", "timer_resume_conn", "try_to_resume_conn", "retry_resume_conn", "error_resume_conn", "open_new_server_conn", "reuse_server_idle_conn", "inc_aflow_limit"], "type": "string", "description": "'all': all; 'pause_conn': Pause connection; 'pause_conn_fail': Pause connection fail; 'resume_conn': Resume connection; 'event_resume_conn': Resume conn by event; 'timer_resume_conn': Resume conn by timer; 'try_to_resume_conn': Resume conn by trying; 'retry_resume_conn': Resume conn by retry; 'error_resume_conn': Resume conn by error; 'open_new_server_conn': Open new server conn; 'reuse_server_idle_conn': Reuse idle server conn; 'inc_aflow_limit': Inc aFlow limit; ", "format": "enum"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Show aFlow statistics.

    Class aflow supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/aflow`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "aflow"
        self.a10_url="/axapi/v3/slb/aflow"
        self.DeviceProxy = ""
        self.sampling_enable = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


