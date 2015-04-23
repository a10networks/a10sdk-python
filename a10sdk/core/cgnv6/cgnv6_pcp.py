from a10sdk.common.A10BaseClass import A10BaseClass


class SamplingEnable(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param counters1: {"enum": ["all", "packets-rcv", "lsn-map-process-success", "dslite-map-process-success", "nat64-map-process-success", "lsn-peer-process-success", "dslite-peer-process-success", "nat64-peer-process-success", "lsn-announce-process-success", "dslite-announce-process-success", "nat64-announce-process-success", "pkt-not-request-drop", "pkt-too-short-drop", "noroute-drop", "unsupported-version", "not-authorized", "malform-request", "unsupp-opcode", "unsupp-option", "malform-option", "no-resources", "unsupp-protocol", "user-quota-exceeded", "cannot-provide-suggest", "address-mismatch", "excessive-remote-peers", "pkt-not-from-nat-inside", "l4-process-error", "internal-error-drop", "unsol_ance_sent_succ", "unsol_ance_sent_fail", "ha_sync_epoch_sent", "ha_sync_epoch_rcv", "fullcone-ext-alloc", "fullcone-ext-free", "fullcone-ext-alloc-failure", "fullcone-ext-notfound", "fullcone-ext-reuse", "client-nonce-mismatch", "map-filter-set", "map-filter-deny"], "type": "string", "description": "'all': all; 'packets-rcv': Packets Received; 'lsn-map-process-success': PCP MAP Request Processing Success (NAT44); 'dslite-map-process-success': PCP MAP Request Processing Success (DS-Lite); 'nat64-map-process-success': PCP MAP Request Processing Success (NAT64); 'lsn-peer-process-success': PCP PEER Request Processing Success (NAT44); 'dslite-peer-process-success': PCP PEER Request Processing Success (DS-Lite); 'nat64-peer-process-success': PCP PEER Request Processing Success (NAT64); 'lsn-announce-process-success': PCP ANNOUNCE Request Processing Success (NAT44); 'dslite-announce-process-success': PCP ANNOUNCE Request Processing Success (DS-Lite); 'nat64-announce-process-success': PCP ANNOUNCE Request Processing Success (NAT64); 'pkt-not-request-drop': Packet Not a PCP Request; 'pkt-too-short-drop': Packet Too Short; 'noroute-drop': Response No Route; 'unsupported-version': Unsupported PCP version; 'not-authorized': PCP Request Not Authorized; 'malform-request': PCP Request Malformed; 'unsupp-opcode': Unsupported PCP Opcode; 'unsupp-option': Unsupported PCP Option; 'malform-option': PCP Option Malformed; 'no-resources': No System or NAT Resources; 'unsupp-protocol': Unsupported Mapping Protocol; 'user-quota-exceeded': User Quota Exceeded; 'cannot-provide-suggest': Cannot Provide Suggested Port When PREFER_FAILURE; 'address-mismatch': PCP Client Address Mismatch; 'excessive-remote-peers': Excessive Remote Peers; 'pkt-not-from-nat-inside': Packet Dropped For Not Coming From NAT Inside; 'l4-process-error': L3/L4 Process Error; 'internal-error-drop': Internal Error; 'unsol_ance_sent_succ': Unsolicited Announce Sent; 'unsol_ance_sent_fail': Unsolicited Announce Send Failure; 'ha_sync_epoch_sent': HA Sync PCP Epoch Sent; 'ha_sync_epoch_rcv': HA Sync PCP Epoch Recv; 'fullcone-ext-alloc': PCP Fullcone Extension Alloc; 'fullcone-ext-free': PCP Fullcone Extension Free; 'fullcone-ext-alloc-failure': PCP Fullcone Extension Alloc Failure; 'fullcone-ext-notfound': PCP Fullcone Extension Not Found; 'fullcone-ext-reuse': PCP Fullcone Extension Reuse; 'client-nonce-mismatch': PCP Client Nonce Mismatch; 'map-filter-set': PCP MAP Filter Set; 'map-filter-deny': PCP MAP Filter Deny Inbound; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "sampling-enable"
        self.DeviceProxy = ""
        self.counters1 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Pcp(A10BaseClass):
    
    """    :param sampling_enable: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "packets-rcv", "lsn-map-process-success", "dslite-map-process-success", "nat64-map-process-success", "lsn-peer-process-success", "dslite-peer-process-success", "nat64-peer-process-success", "lsn-announce-process-success", "dslite-announce-process-success", "nat64-announce-process-success", "pkt-not-request-drop", "pkt-too-short-drop", "noroute-drop", "unsupported-version", "not-authorized", "malform-request", "unsupp-opcode", "unsupp-option", "malform-option", "no-resources", "unsupp-protocol", "user-quota-exceeded", "cannot-provide-suggest", "address-mismatch", "excessive-remote-peers", "pkt-not-from-nat-inside", "l4-process-error", "internal-error-drop", "unsol_ance_sent_succ", "unsol_ance_sent_fail", "ha_sync_epoch_sent", "ha_sync_epoch_rcv", "fullcone-ext-alloc", "fullcone-ext-free", "fullcone-ext-alloc-failure", "fullcone-ext-notfound", "fullcone-ext-reuse", "client-nonce-mismatch", "map-filter-set", "map-filter-deny"], "type": "string", "description": "'all': all; 'packets-rcv': Packets Received; 'lsn-map-process-success': PCP MAP Request Processing Success (NAT44); 'dslite-map-process-success': PCP MAP Request Processing Success (DS-Lite); 'nat64-map-process-success': PCP MAP Request Processing Success (NAT64); 'lsn-peer-process-success': PCP PEER Request Processing Success (NAT44); 'dslite-peer-process-success': PCP PEER Request Processing Success (DS-Lite); 'nat64-peer-process-success': PCP PEER Request Processing Success (NAT64); 'lsn-announce-process-success': PCP ANNOUNCE Request Processing Success (NAT44); 'dslite-announce-process-success': PCP ANNOUNCE Request Processing Success (DS-Lite); 'nat64-announce-process-success': PCP ANNOUNCE Request Processing Success (NAT64); 'pkt-not-request-drop': Packet Not a PCP Request; 'pkt-too-short-drop': Packet Too Short; 'noroute-drop': Response No Route; 'unsupported-version': Unsupported PCP version; 'not-authorized': PCP Request Not Authorized; 'malform-request': PCP Request Malformed; 'unsupp-opcode': Unsupported PCP Opcode; 'unsupp-option': Unsupported PCP Option; 'malform-option': PCP Option Malformed; 'no-resources': No System or NAT Resources; 'unsupp-protocol': Unsupported Mapping Protocol; 'user-quota-exceeded': User Quota Exceeded; 'cannot-provide-suggest': Cannot Provide Suggested Port When PREFER_FAILURE; 'address-mismatch': PCP Client Address Mismatch; 'excessive-remote-peers': Excessive Remote Peers; 'pkt-not-from-nat-inside': Packet Dropped For Not Coming From NAT Inside; 'l4-process-error': L3/L4 Process Error; 'internal-error-drop': Internal Error; 'unsol_ance_sent_succ': Unsolicited Announce Sent; 'unsol_ance_sent_fail': Unsolicited Announce Send Failure; 'ha_sync_epoch_sent': HA Sync PCP Epoch Sent; 'ha_sync_epoch_rcv': HA Sync PCP Epoch Recv; 'fullcone-ext-alloc': PCP Fullcone Extension Alloc; 'fullcone-ext-free': PCP Fullcone Extension Free; 'fullcone-ext-alloc-failure': PCP Fullcone Extension Alloc Failure; 'fullcone-ext-notfound': PCP Fullcone Extension Not Found; 'fullcone-ext-reuse': PCP Fullcone Extension Reuse; 'client-nonce-mismatch': PCP Client Nonce Mismatch; 'map-filter-set': PCP MAP Filter Set; 'map-filter-deny': PCP MAP Filter Deny Inbound; ", "format": "enum"}}}]}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param default_template: {"description": "Bind the default template for PCP (Bind a PCP template)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Set Port Control Protocol parameters.

    Class pcp supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/pcp`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "pcp"
        self.a10_url="/axapi/v3/cgnv6/pcp"
        self.DeviceProxy = ""
        self.sampling_enable = []
        self.uuid = ""
        self.default_template = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


