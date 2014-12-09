from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param threshold_exceed: {"description": "Threshold exceeded count", "format": "counter", "type": "number", "oid": "7", "optional": true, "size": "2"}
    :param lockout_drop: {"description": "Lockout drops", "format": "counter", "type": "number", "oid": "8", "optional": true, "size": "2"}
    :param too_many_sessions: {"description": "Too many sessions consumed", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "2"}
    :param sessions_freed: {"description": "Sessions freed", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "2"}
    :param permitted: {"description": "Honor threshold  count", "format": "counter", "type": "number", "oid": "6", "optional": true, "size": "2"}
    :param log_msg_sent: {"description": "Log messages sent", "format": "counter", "type": "number", "oid": "9", "optional": true, "size": "2"}
    :param sessions_alloc: {"description": "Sessions allocated", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "2"}
    :param out_of_sessions: {"description": "Out of sessions", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "2"}
    :param called: {"description": "Threshold check count", "format": "counter", "type": "number", "oid": "5", "optional": true, "size": "2"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.threshold_exceed = ""
        self.lockout_drop = ""
        self.too_many_sessions = ""
        self.sessions_freed = ""
        self.permitted = ""
        self.log_msg_sent = ""
        self.sessions_alloc = ""
        self.out_of_sessions = ""
        self.called = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class CrlSrcip(A10BaseClass):
    
    """Class Description::
    Statistics for the object crl-srcip.

    Class crl-srcip supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/crl-srcip/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "crl-srcip"
        self.a10_url="/axapi/v3/slb/crl-srcip/stats"
        self.DeviceProxy = ""
        self.stats = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


