from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param stream_creation_failure: {"description": "Stream Creation Failures", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "8"}
    :param streams_created: {"description": "Streams Created", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}
    :param no_session_mem: {"description": "Data Session Creation Failures", "format": "counter", "type": "number", "oid": "10", "optional": true, "size": "8"}
    :param ports_allocated: {"description": "Stream Client Ports Allocated", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "8"}
    :param port_allocation_failure: {"description": "Stream Client Port Allocation Failures", "format": "counter", "type": "number", "oid": "6", "optional": true, "size": "8"}
    :param streams_freed: {"description": "Streams Freed", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "8"}
    :param unknown_client_port_from_server: {"description": "Server Replies With Unknown Client Ports", "format": "counter", "type": "number", "oid": "7", "optional": true, "size": "8"}
    :param ports_freed: {"description": "Stream Client Ports Freed", "format": "counter", "type": "number", "oid": "5", "optional": true, "size": "8"}
    :param data_session_freed: {"description": "Data Session Freed", "format": "counter", "type": "number", "oid": "9", "optional": true, "size": "8"}
    :param data_session_created: {"description": "Data Session Created", "format": "counter", "type": "number", "oid": "8", "optional": true, "size": "8"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.stream_creation_failure = ""
        self.streams_created = ""
        self.no_session_mem = ""
        self.ports_allocated = ""
        self.port_allocation_failure = ""
        self.streams_freed = ""
        self.unknown_client_port_from_server = ""
        self.ports_freed = ""
        self.data_session_freed = ""
        self.data_session_created = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Rtsp(A10BaseClass):
    
    """Class Description::
    Statistics for the object rtsp.

    Class rtsp supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/lsn/alg/rtsp/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "rtsp"
        self.a10_url="/axapi/v3/cgnv6/lsn/alg/rtsp/stats"
        self.DeviceProxy = ""
        self.stats = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


