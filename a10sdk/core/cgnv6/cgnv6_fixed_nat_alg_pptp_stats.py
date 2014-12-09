from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param no_gre_session_match: {"description": "No Matching GRE Session", "format": "counter", "type": "number", "oid": "5", "optional": true, "size": "8"}
    :param gre_sessions_created: {"description": "GRE Sessions Created", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "8"}
    :param mismatched_pns_call_id: {"description": "Mismatched PNS Call ID", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "8"}
    :param gre_sessions_freed: {"description": "GRE Sessions Freed", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "8"}
    :param calls_established: {"description": "Calls Established", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.no_gre_session_match = ""
        self.gre_sessions_created = ""
        self.mismatched_pns_call_id = ""
        self.gre_sessions_freed = ""
        self.calls_established = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Pptp(A10BaseClass):
    
    """Class Description::
    Statistics for the object pptp.

    Class pptp supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/fixed-nat/alg/pptp/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "pptp"
        self.a10_url="/axapi/v3/cgnv6/fixed-nat/alg/pptp/stats"
        self.DeviceProxy = ""
        self.stats = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


