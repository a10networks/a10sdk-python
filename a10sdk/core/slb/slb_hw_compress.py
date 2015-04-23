from a10sdk.common.A10BaseClass import A10BaseClass


class SamplingEnable(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param counters1: {"enum": ["all", "request_count", "submit_count", "response_count", "failure_count", "failure_code", "ring_full_count", "max_outstanding_request_count", "max_outstanding_submit_count"], "type": "string", "description": "'all': all; 'request_count': Total request count; 'submit_count': Total submit count; 'response_count': Total response count; 'failure_count': Total failure count; 'failure_code': Last failure code; 'ring_full_count': Compression queue full; 'max_outstanding_request_count': Max queued request count; 'max_outstanding_submit_count': Max queued submit count; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "sampling-enable"
        self.DeviceProxy = ""
        self.counters1 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class HwCompress(A10BaseClass):
    
    """    :param sampling_enable: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "request_count", "submit_count", "response_count", "failure_count", "failure_code", "ring_full_count", "max_outstanding_request_count", "max_outstanding_submit_count"], "type": "string", "description": "'all': all; 'request_count': Total request count; 'submit_count': Total submit count; 'response_count': Total response count; 'failure_count': Total failure count; 'failure_code': Last failure code; 'ring_full_count': Compression queue full; 'max_outstanding_request_count': Max queued request count; 'max_outstanding_submit_count': Max queued submit count; ", "format": "enum"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Show HW compression Statistics.

    Class hw-compress supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/hw-compress`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "hw-compress"
        self.a10_url="/axapi/v3/slb/hw-compress"
        self.DeviceProxy = ""
        self.sampling_enable = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


