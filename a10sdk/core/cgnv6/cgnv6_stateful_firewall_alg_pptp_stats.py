from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param call_req_pns_call_id_mismatch: {"description": "Call ID Mismatch on Call Request", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "8"}
    :param gre_session_created: {"description": "GRE Session Created", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "8"}
    :param gre_session_freed: {"description": "GRE Session Freed", "format": "counter", "type": "number", "oid": "5", "optional": true, "size": "8"}
    :param call_reply_pns_call_id_mismatch: {"description": "Call ID Mismatch on Call Reply", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "8"}
    :param calls_established: {"description": "Calls Established", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.call_req_pns_call_id_mismatch = ""
        self.gre_session_created = ""
        self.gre_session_freed = ""
        self.call_reply_pns_call_id_mismatch = ""
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
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/stateful-firewall/alg/pptp/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "pptp"
        self.a10_url="/axapi/v3/cgnv6/stateful-firewall/alg/pptp/stats"
        self.DeviceProxy = ""
        self.stats = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


