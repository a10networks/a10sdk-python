from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param miss_resp: {"description": "Missed resp", "format": "counter", "type": "number", "oid": "10", "optional": true, "size": "8"}
    :param ntermi_err: {"description": "Total terminated by err", "format": "counter", "type": "number", "oid": "7", "optional": true, "size": "8"}
    :param current_open: {"description": "Open persist", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}
    :param current_active: {"description": "Active persist", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "8"}
    :param pause_conn: {"description": "Pause request", "format": "counter", "type": "number", "oid": "12", "optional": true, "size": "8"}
    :param delay_unbind: {"description": "Delayed unbind", "format": "counter", "type": "number", "oid": "8", "optional": true, "size": "8"}
    :param long_resp: {"description": "Long resp", "format": "counter", "type": "number", "oid": "9", "optional": true, "size": "8"}
    :param ntermi: {"description": "Total terminated", "format": "counter", "type": "number", "oid": "6", "optional": true, "size": "8"}
    :param pause_conn_fail: {"description": "Pause request fail", "format": "counter", "type": "number", "oid": "13", "optional": true, "size": "8"}
    :param nunbind: {"description": "Total unbind", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "8"}
    :param unbound_data_rcv: {"description": "Unbound data rcvd", "format": "counter", "type": "number", "oid": "11", "optional": true, "size": "8"}
    :param resume_conn: {"description": "Resume request", "format": "counter", "type": "number", "oid": "14", "optional": true, "size": "8"}
    :param nbind: {"description": "Total bind", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "8"}
    :param not_remove_from_rport: {"description": "Not remove from list", "format": "counter", "type": "number", "oid": "15", "optional": true, "size": "8"}
    :param nestab: {"description": "Total established", "format": "counter", "type": "number", "oid": "5", "optional": true, "size": "8"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.miss_resp = ""
        self.ntermi_err = ""
        self.current_open = ""
        self.current_active = ""
        self.pause_conn = ""
        self.delay_unbind = ""
        self.long_resp = ""
        self.ntermi = ""
        self.pause_conn_fail = ""
        self.nunbind = ""
        self.unbound_data_rcv = ""
        self.resume_conn = ""
        self.nbind = ""
        self.not_remove_from_rport = ""
        self.nestab = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class ConnectionReuse(A10BaseClass):
    
    """Class Description::
    Statistics for the object connection-reuse.

    Class connection-reuse supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/connection-reuse/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "connection-reuse"
        self.a10_url="/axapi/v3/slb/connection-reuse/stats"
        self.DeviceProxy = ""
        self.stats = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


