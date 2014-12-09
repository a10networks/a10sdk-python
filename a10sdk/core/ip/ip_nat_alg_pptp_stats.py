from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param truncated_gre_packet: {"optional": true, "size": "8", "type": "number", "oid": "10", "format": "counter"}
    :param smp_session_creation_failure: {"optional": true, "size": "8", "type": "number", "oid": "3", "format": "counter"}
    :param mismatched_pns_call_id: {"optional": true, "size": "8", "type": "number", "oid": "6", "format": "counter"}
    :param mismatched_pac_call_id: {"optional": true, "size": "8", "type": "number", "oid": "7", "format": "counter"}
    :param current_gre_sessions: {"optional": true, "size": "8", "type": "number", "oid": "2", "format": "counter"}
    :param no_matching_gre_session: {"optional": true, "size": "8", "type": "number", "oid": "12", "format": "counter"}
    :param truncated_pac_message: {"optional": true, "size": "8", "type": "number", "oid": "5", "format": "counter"}
    :param truncated_pns_message: {"optional": true, "size": "8", "type": "number", "oid": "4", "format": "counter"}
    :param unknown_gre_version: {"optional": true, "size": "8", "type": "number", "oid": "11", "format": "counter"}
    :param current_smp_sessions: {"optional": true, "size": "8", "type": "number", "oid": "1", "format": "counter"}
    :param retransmitted_pns_message: {"optional": true, "size": "8", "type": "number", "oid": "8", "format": "counter"}
    :param retransmitted_pac_message: {"optional": true, "size": "8", "type": "number", "oid": "9", "format": "counter"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.truncated_gre_packet = ""
        self.smp_session_creation_failure = ""
        self.mismatched_pns_call_id = ""
        self.mismatched_pac_call_id = ""
        self.current_gre_sessions = ""
        self.no_matching_gre_session = ""
        self.truncated_pac_message = ""
        self.truncated_pns_message = ""
        self.unknown_gre_version = ""
        self.current_smp_sessions = ""
        self.retransmitted_pns_message = ""
        self.retransmitted_pac_message = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Pptp(A10BaseClass):
    
    """Class Description::
    Statistics for the object pptp.

    Class pptp supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/ip/nat/alg/pptp/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "pptp"
        self.a10_url="/axapi/v3/ip/nat/alg/pptp/stats"
        self.DeviceProxy = ""
        self.stats = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


