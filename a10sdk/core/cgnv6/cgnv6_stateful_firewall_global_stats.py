from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param session_creation_failure: {"description": "Session Creation Failure", "format": "counter", "type": "number", "oid": "16", "optional": true, "size": "8"}
    :param tcp_packet_process: {"description": "TCP Packet Process", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}
    :param udp_fullcone_freed: {"description": "UDP Full-cone Freed", "format": "counter", "type": "number", "oid": "23", "optional": true, "size": "8"}
    :param outbound_session_created: {"description": "Outbound Session Created", "format": "counter", "type": "number", "oid": "6", "optional": true, "size": "8"}
    :param tcp_fullcone_created: {"description": "TCP Full-cone Created", "format": "counter", "type": "number", "oid": "20", "optional": true, "size": "8"}
    :param fullcone_creation_failure: {"description": "Full-Cone Creation Failure", "format": "counter", "type": "number", "oid": "24", "optional": true, "size": "8"}
    :param packet_inbound_deny: {"description": "Inbound Packet Denied", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "8"}
    :param inbound_session_created: {"description": "Inbound Session Created", "format": "counter", "type": "number", "oid": "8", "optional": true, "size": "8"}
    :param udp_fullcone_created: {"description": "UDP Full-cone Created", "format": "counter", "type": "number", "oid": "22", "optional": true, "size": "8"}
    :param other_session_created: {"description": "Other Session Created", "format": "counter", "type": "number", "oid": "14", "optional": true, "size": "8"}
    :param udp_session_created: {"description": "UDP Session Created", "format": "counter", "type": "number", "oid": "12", "optional": true, "size": "8"}
    :param udp_packet_process: {"description": "UDP Packet Process", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "8"}
    :param no_fwd_route: {"description": "No Forward Route", "format": "counter", "type": "number", "oid": "17", "optional": true, "size": "8"}
    :param tcp_session_created: {"description": "TCP Session Created", "format": "counter", "type": "number", "oid": "10", "optional": true, "size": "8"}
    :param other_session_freed: {"description": "Other Session Freed", "format": "counter", "type": "number", "oid": "15", "optional": true, "size": "8"}
    :param eif_process: {"description": "Endpnt-Independent Filter Matched", "format": "counter", "type": "number", "oid": "25", "optional": true, "size": "8"}
    :param inbound_session_freed: {"description": "Inbound Session Freed", "format": "counter", "type": "number", "oid": "9", "optional": true, "size": "8"}
    :param udp_session_freed: {"description": "UDP Session Freed", "format": "counter", "type": "number", "oid": "13", "optional": true, "size": "8"}
    :param no_rev_route: {"description": "No Reverse Route", "format": "counter", "type": "number", "oid": "18", "optional": true, "size": "8"}
    :param packet_process_failure: {"description": "Packet Error Drop", "format": "counter", "type": "number", "oid": "5", "optional": true, "size": "8"}
    :param other_packet_process: {"description": "Other Packet Process", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "8"}
    :param tcp_fullcone_freed: {"description": "TCP Full-cone Freed", "format": "counter", "type": "number", "oid": "21", "optional": true, "size": "8"}
    :param outbound_session_freed: {"description": "Outbound Session Freed", "format": "counter", "type": "number", "oid": "7", "optional": true, "size": "8"}
    :param tcp_session_freed: {"description": "TCP Session Freed", "format": "counter", "type": "number", "oid": "11", "optional": true, "size": "8"}
    :param packet_standby_drop: {"description": "Standby Drop", "format": "counter", "type": "number", "oid": "19", "optional": true, "size": "8"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.session_creation_failure = ""
        self.tcp_packet_process = ""
        self.udp_fullcone_freed = ""
        self.outbound_session_created = ""
        self.tcp_fullcone_created = ""
        self.fullcone_creation_failure = ""
        self.packet_inbound_deny = ""
        self.inbound_session_created = ""
        self.udp_fullcone_created = ""
        self.other_session_created = ""
        self.udp_session_created = ""
        self.udp_packet_process = ""
        self.no_fwd_route = ""
        self.tcp_session_created = ""
        self.other_session_freed = ""
        self.eif_process = ""
        self.inbound_session_freed = ""
        self.udp_session_freed = ""
        self.no_rev_route = ""
        self.packet_process_failure = ""
        self.other_packet_process = ""
        self.tcp_fullcone_freed = ""
        self.outbound_session_freed = ""
        self.tcp_session_freed = ""
        self.packet_standby_drop = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Global(A10BaseClass):
    
    """Class Description::
    Statistics for the object global.

    Class global supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/stateful-firewall/global/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "global"
        self.a10_url="/axapi/v3/cgnv6/stateful-firewall/global/stats"
        self.DeviceProxy = ""
        self.stats = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


