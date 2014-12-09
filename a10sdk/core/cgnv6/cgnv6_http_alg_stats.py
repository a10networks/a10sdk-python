from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param radius_response_dropped: {"description": "Query Response Dropped", "format": "counter", "type": "number", "oid": "11", "optional": true, "size": "8"}
    :param radius_requst_sent: {"description": "Query Request Sent", "format": "counter", "type": "number", "oid": "8", "optional": true, "size": "8"}
    :param radius_requst_dropped: {"description": "Query Request Dropped", "format": "counter", "type": "number", "oid": "9", "optional": true, "size": "8"}
    :param request_insert_client_ip_performed: {"description": "HTTP Client IP Insertion Performed", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "8"}
    :param radius_query_succeed: {"description": "MSISDN Query Succeed", "format": "counter", "type": "number", "oid": "6", "optional": true, "size": "8"}
    :param request_insert_msisdn_unavailable: {"description": "Inserted MSISDN is 0000 (MSISDN Unavailable)", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "8"}
    :param request_processed: {"description": "HTTP Request Processed", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}
    :param request_insert_msisdn_performed: {"description": "HTTP MSISDN Insertion Performed", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "8"}
    :param radius_query_failed: {"description": "MSISDN Query Failed", "format": "counter", "type": "number", "oid": "7", "optional": true, "size": "8"}
    :param queued_session_too_many: {"description": "Queued Session Exceed Drop", "format": "counter", "type": "number", "oid": "5", "optional": true, "size": "8"}
    :param radius_response_received: {"description": "Query Response Received", "format": "counter", "type": "number", "oid": "10", "optional": true, "size": "8"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.radius_response_dropped = ""
        self.radius_requst_sent = ""
        self.radius_requst_dropped = ""
        self.request_insert_client_ip_performed = ""
        self.radius_query_succeed = ""
        self.request_insert_msisdn_unavailable = ""
        self.request_processed = ""
        self.request_insert_msisdn_performed = ""
        self.radius_query_failed = ""
        self.queued_session_too_many = ""
        self.radius_response_received = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class HttpAlg(A10BaseClass):
    
    """Class Description::
    Statistics for the object http-alg.

    Class http-alg supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/http-alg/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "http-alg"
        self.a10_url="/axapi/v3/cgnv6/http-alg/stats"
        self.DeviceProxy = ""
        self.stats = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


