from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param unsol_ance_sent_fail: {"description": "Unsolicited Announce Send Failure", "format": "counter", "type": "number", "oid": "30", "optional": true, "size": "8"}
    :param malform_request: {"description": "PCP Request Malformed", "format": "counter", "type": "number", "oid": "16", "optional": true, "size": "8"}
    :param unsupp_option: {"description": "Unsupported PCP Option", "format": "counter", "type": "number", "oid": "18", "optional": true, "size": "8"}
    :param unsupported_version: {"description": "Unsupported PCP version", "format": "counter", "type": "number", "oid": "14", "optional": true, "size": "8"}
    :param no_resources: {"description": "No System or NAT Resources", "format": "counter", "type": "number", "oid": "20", "optional": true, "size": "8"}
    :param unsupp_opcode: {"description": "Unsupported PCP Opcode", "format": "counter", "type": "number", "oid": "17", "optional": true, "size": "8"}
    :param dslite_announce_process_success: {"description": "PCP ANNOUNCE Request Processing Success (DS-Lite)", "format": "counter", "type": "number", "oid": "9", "optional": true, "size": "8"}
    :param l4_process_error: {"description": "L3/L4 Process Error", "format": "counter", "type": "number", "oid": "27", "optional": true, "size": "8"}
    :param not_authorized: {"description": "PCP Request Not Authorized", "format": "counter", "type": "number", "oid": "15", "optional": true, "size": "8"}
    :param ha_sync_epoch_sent: {"description": "HA Sync PCP Epoch Sent", "format": "counter", "type": "number", "oid": "31", "optional": true, "size": "8"}
    :param nat64_announce_process_success: {"description": "PCP ANNOUNCE Request Processing Success (NAT64)", "format": "counter", "type": "number", "oid": "10", "optional": true, "size": "8"}
    :param pkt_not_from_nat_inside: {"description": "Packet Dropped For Not Coming From NAT Inside", "format": "counter", "type": "number", "oid": "26", "optional": true, "size": "8"}
    :param user_quota_exceeded: {"description": "User Quota Exceeded", "format": "counter", "type": "number", "oid": "22", "optional": true, "size": "8"}
    :param dslite_map_process_success: {"description": "PCP MAP Request Processing Success (DS-Lite)", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "8"}
    :param packets_rcv: {"description": "Packets Received", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}
    :param lsn_announce_process_success: {"description": "PCP ANNOUNCE Request Processing Success (NAT44)", "format": "counter", "type": "number", "oid": "8", "optional": true, "size": "8"}
    :param cannot_provide_suggest: {"description": "Cannot Provide Suggested Port When PREFER_FAILURE", "format": "counter", "type": "number", "oid": "23", "optional": true, "size": "8"}
    :param nat64_map_process_success: {"description": "PCP MAP Request Processing Success (NAT64)", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "8"}
    :param internal_error_drop: {"description": "Internal Error", "format": "counter", "type": "number", "oid": "28", "optional": true, "size": "8"}
    :param dslite_peer_process_success: {"description": "PCP PEER Request Processing Success (DS-Lite)", "format": "counter", "type": "number", "oid": "6", "optional": true, "size": "8"}
    :param malform_option: {"description": "PCP Option Malformed", "format": "counter", "type": "number", "oid": "19", "optional": true, "size": "8"}
    :param excessive_remote_peers: {"description": "Excessive Remote Peers", "format": "counter", "type": "number", "oid": "25", "optional": true, "size": "8"}
    :param lsn_map_process_success: {"description": "PCP MAP Request Processing Success (NAT44)", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "8"}
    :param unsupp_protocol: {"description": "Unsupported Mapping Protocol", "format": "counter", "type": "number", "oid": "21", "optional": true, "size": "8"}
    :param ha_sync_epoch_rcv: {"description": "HA Sync PCP Epoch Recv", "format": "counter", "type": "number", "oid": "32", "optional": true, "size": "8"}
    :param unsol_ance_sent_succ: {"description": "Unsolicited Announce Sent", "format": "counter", "type": "number", "oid": "29", "optional": true, "size": "8"}
    :param pkt_not_request_drop: {"description": "Packet Not a PCP Request", "format": "counter", "type": "number", "oid": "11", "optional": true, "size": "8"}
    :param address_mismatch: {"description": "PCP Client Address Mismatch", "format": "counter", "type": "number", "oid": "24", "optional": true, "size": "8"}
    :param noroute_drop: {"description": "Response No Route", "format": "counter", "type": "number", "oid": "13", "optional": true, "size": "8"}
    :param lsn_peer_process_success: {"description": "PCP PEER Request Processing Success (NAT44)", "format": "counter", "type": "number", "oid": "5", "optional": true, "size": "8"}
    :param nat64_peer_process_success: {"description": "PCP PEER Request Processing Success (NAT64)", "format": "counter", "type": "number", "oid": "7", "optional": true, "size": "8"}
    :param pkt_too_short_drop: {"description": "Packet Too Short", "format": "counter", "type": "number", "oid": "12", "optional": true, "size": "8"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.unsol_ance_sent_fail = ""
        self.malform_request = ""
        self.unsupp_option = ""
        self.unsupported_version = ""
        self.no_resources = ""
        self.unsupp_opcode = ""
        self.dslite_announce_process_success = ""
        self.l4_process_error = ""
        self.not_authorized = ""
        self.ha_sync_epoch_sent = ""
        self.nat64_announce_process_success = ""
        self.pkt_not_from_nat_inside = ""
        self.user_quota_exceeded = ""
        self.dslite_map_process_success = ""
        self.packets_rcv = ""
        self.lsn_announce_process_success = ""
        self.cannot_provide_suggest = ""
        self.nat64_map_process_success = ""
        self.internal_error_drop = ""
        self.dslite_peer_process_success = ""
        self.malform_option = ""
        self.excessive_remote_peers = ""
        self.lsn_map_process_success = ""
        self.unsupp_protocol = ""
        self.ha_sync_epoch_rcv = ""
        self.unsol_ance_sent_succ = ""
        self.pkt_not_request_drop = ""
        self.address_mismatch = ""
        self.noroute_drop = ""
        self.lsn_peer_process_success = ""
        self.nat64_peer_process_success = ""
        self.pkt_too_short_drop = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Pcp(A10BaseClass):
    
    """Class Description::
    Statistics for the object pcp.

    Class pcp supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/pcp/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "pcp"
        self.a10_url="/axapi/v3/cgnv6/pcp/stats"
        self.DeviceProxy = ""
        self.stats = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


