from a10sdk.common.A10BaseClass import A10BaseClass


class SamplingEnable(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param counters1: {"enum": ["all", "request-processed", "request-insert-msisdn-performed", "request-insert-client-ip-performed", "request-insert-msisdn-unavailable", "queued-session-too-many", "radius-query-succeed", "radius-query-failed", "radius-requst-sent", "radius-requst-dropped", "radius-response-received", "radius-response-dropped", "out-of-memory-dropped", "queue-len-exceed-dropped", "out-of-order-dropped", "buff-resent", "buff-spilt-failed", "header-insertion-failed", "header-removal-failed", "no-queue"], "type": "string", "description": "'all': all; 'request-processed': HTTP Request Processed; 'request-insert-msisdn-performed': HTTP MSISDN Insertion Performed; 'request-insert-client-ip-performed': HTTP Client IP Insertion Performed; 'request-insert-msisdn-unavailable': Inserted MSISDN is 0000 (MSISDN Unavailable); 'queued-session-too-many': Queued Session Exceed Drop; 'radius-query-succeed': MSISDN Query Succeed; 'radius-query-failed': MSISDN Query Failed; 'radius-requst-sent': Query Request Sent; 'radius-requst-dropped': Query Request Dropped; 'radius-response-received': Query Response Received; 'radius-response-dropped': Query Response Dropped; 'out-of-memory-dropped': Out-of-Memory Dropped; 'queue-len-exceed-dropped': Queue Length Exceed Dropped; 'out-of-order-dropped': Packet Out-of-Order Dropped; 'buff-resent': Packet Resent from Queue; 'buff-spilt-failed': Buff Split Failed; 'header-insertion-failed': Buff Insertion Failed; 'header-removal-failed': Buff Removal Failed; 'no-queue': No Queue; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "sampling-enable"
        self.DeviceProxy = ""
        self.counters1 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class HttpAlg(A10BaseClass):
    
    """    :param sampling_enable: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "request-processed", "request-insert-msisdn-performed", "request-insert-client-ip-performed", "request-insert-msisdn-unavailable", "queued-session-too-many", "radius-query-succeed", "radius-query-failed", "radius-requst-sent", "radius-requst-dropped", "radius-response-received", "radius-response-dropped", "out-of-memory-dropped", "queue-len-exceed-dropped", "out-of-order-dropped", "buff-resent", "buff-spilt-failed", "header-insertion-failed", "header-removal-failed", "no-queue"], "type": "string", "description": "'all': all; 'request-processed': HTTP Request Processed; 'request-insert-msisdn-performed': HTTP MSISDN Insertion Performed; 'request-insert-client-ip-performed': HTTP Client IP Insertion Performed; 'request-insert-msisdn-unavailable': Inserted MSISDN is 0000 (MSISDN Unavailable); 'queued-session-too-many': Queued Session Exceed Drop; 'radius-query-succeed': MSISDN Query Succeed; 'radius-query-failed': MSISDN Query Failed; 'radius-requst-sent': Query Request Sent; 'radius-requst-dropped': Query Request Dropped; 'radius-response-received': Query Response Received; 'radius-response-dropped': Query Response Dropped; 'out-of-memory-dropped': Out-of-Memory Dropped; 'queue-len-exceed-dropped': Queue Length Exceed Dropped; 'out-of-order-dropped': Packet Out-of-Order Dropped; 'buff-resent': Packet Resent from Queue; 'buff-spilt-failed': Buff Split Failed; 'header-insertion-failed': Buff Insertion Failed; 'header-removal-failed': Buff Removal Failed; 'no-queue': No Queue; ", "format": "enum"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    HTTP-ALG Statistics.

    Class http-alg supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/http-alg`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "http-alg"
        self.a10_url="/axapi/v3/cgnv6/http-alg"
        self.DeviceProxy = ""
        self.sampling_enable = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


