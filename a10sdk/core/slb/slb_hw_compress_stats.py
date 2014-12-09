from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param max_outstanding_request_count: {"description": "Max queued request count", "format": "counter", "type": "number", "oid": "7", "optional": true, "size": "2"}
    :param failure_count: {"description": "Total failure count", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "2"}
    :param response_count: {"description": "Total response count", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "2"}
    :param ring_full_count: {"description": "Compression queue full", "format": "counter", "type": "number", "oid": "6", "optional": true, "size": "2"}
    :param submit_count: {"description": "Total submit count", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "2"}
    :param request_count: {"description": "Total request count", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "2"}
    :param max_outstanding_submit_count: {"description": "Max queued submit count", "format": "counter", "type": "number", "oid": "8", "optional": true, "size": "2"}
    :param failure_code: {"description": "Last failure code", "format": "counter", "type": "number", "oid": "5", "optional": true, "size": "2"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.max_outstanding_request_count = ""
        self.failure_count = ""
        self.response_count = ""
        self.ring_full_count = ""
        self.submit_count = ""
        self.request_count = ""
        self.max_outstanding_submit_count = ""
        self.failure_code = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class HwCompress(A10BaseClass):
    
    """Class Description::
    Statistics for the object hw-compress.

    Class hw-compress supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/hw-compress/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "hw-compress"
        self.a10_url="/axapi/v3/slb/hw-compress/stats"
        self.DeviceProxy = ""
        self.stats = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


