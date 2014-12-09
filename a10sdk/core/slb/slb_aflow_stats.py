from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param open_new_server_conn: {"description": "Open new server conn", "format": "counter", "type": "number", "oid": "9", "optional": true, "size": "8"}
    :param reuse_server_idle_conn: {"description": "Reuse idle server conn", "format": "counter", "type": "number", "oid": "10", "optional": true, "size": "8"}
    :param inc_aflow_limit: {"description": "Inc aFlow limit", "format": "counter", "type": "number", "oid": "11", "optional": true, "size": "8"}
    :param pause_conn_fail: {"description": "Pause connection fail", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "8"}
    :param pause_conn: {"description": "Pause connection", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}
    :param event_resume_conn: {"description": "Resume conn by event", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "8"}
    :param try_to_resume_conn: {"description": "Resume conn by trying", "format": "counter", "type": "number", "oid": "6", "optional": true, "size": "8"}
    :param resume_conn: {"description": "Resume connection", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "8"}
    :param retry_resume_conn: {"description": "Resume conn by retry", "format": "counter", "type": "number", "oid": "7", "optional": true, "size": "8"}
    :param error_resume_conn: {"description": "Resume conn by error", "format": "counter", "type": "number", "oid": "8", "optional": true, "size": "8"}
    :param timer_resume_conn: {"description": "Resume conn by timer", "format": "counter", "type": "number", "oid": "5", "optional": true, "size": "8"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.open_new_server_conn = ""
        self.reuse_server_idle_conn = ""
        self.inc_aflow_limit = ""
        self.pause_conn_fail = ""
        self.pause_conn = ""
        self.event_resume_conn = ""
        self.try_to_resume_conn = ""
        self.resume_conn = ""
        self.retry_resume_conn = ""
        self.error_resume_conn = ""
        self.timer_resume_conn = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Aflow(A10BaseClass):
    
    """Class Description::
    Statistics for the object aflow.

    Class aflow supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/aflow/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "aflow"
        self.a10_url="/axapi/v3/slb/aflow/stats"
        self.DeviceProxy = ""
        self.stats = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


