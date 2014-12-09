from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param data_session_created: {"description": "Data Session Created", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "8"}
    :param transport_alloc_failure: {"description": "Transport Alloc Failure", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "8"}
    :param data_session_freed: {"description": "Data Session Freed", "format": "counter", "type": "number", "oid": "5", "optional": true, "size": "8"}
    :param transport_freed: {"description": "Transport Freed", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "8"}
    :param transport_inserted: {"description": "Transport Created", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.data_session_created = ""
        self.transport_alloc_failure = ""
        self.data_session_freed = ""
        self.transport_freed = ""
        self.transport_inserted = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Rtsp(A10BaseClass):
    
    """Class Description::
    Statistics for the object rtsp.

    Class rtsp supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/stateful-firewall/alg/rtsp/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "rtsp"
        self.a10_url="/axapi/v3/cgnv6/stateful-firewall/alg/rtsp/stats"
        self.DeviceProxy = ""
        self.stats = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


