from a10sdk.common.A10BaseClass import A10BaseClass


class SamplingEnable(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param counters1: {"enum": ["all", "method-register", "method-invite", "method-ack", "method-cancel", "method-bye", "method-options", "method-prack", "method-subscribe", "method-notify", "method-publish", "method-info", "method-refer", "method-message", "method-update", "method-unknown", "parse-error", "req-uri-op-failrue", "via-hdr-op-failrue", "contact-hdr-op-failrue", "from-hdr-op-failrue", "to-hdr-op-failrue", "route-hdr-op-failrue", "record-route-hdr-op-failrue", "content-length-hdr-op-failrue", "third-party-registration", "conn-ext-creation-failure", "alloc-contact-port-failure", "outside-contact-port-mismatch", "inside-contact-port-mismatch", "third-party-sdp", "sdp-process-candidate-failure", "sdp-op-failure", "sdp-alloc-port-map-success", "sdp-alloc-port-map-failure", "modify-failure", "rewrite-failure", "tcp-out-of-order-drop"], "type": "string", "description": "'all': all; 'method-register': SIP Method REGISTER; 'method-invite': SIP Method INVITE; 'method-ack': SIP Method ACK; 'method-cancel': SIP Method CANCEL; 'method-bye': SIP Method BYE; 'method-options': SIP Method OPTIONS; 'method-prack': SIP Method PRACK; 'method-subscribe': SIP Method SUBSCRIBE; 'method-notify': SIP Method NOTIFY; 'method-publish': SIP Method PUBLISH; 'method-info': SIP Method INFO; 'method-refer': SIP Method REFER; 'method-message': SIP Method MESSAGE; 'method-update': SIP Method UPDATE; 'method-unknown': SIP Method UNKNOWN; 'parse-error': SIP Message Parse Error; 'req-uri-op-failrue': SIP Operate Request Uri Failure; 'via-hdr-op-failrue': SIP Operate Via Header Failure; 'contact-hdr-op-failrue': SIP Operate Contact Header Failure; 'from-hdr-op-failrue': SIP Operate From Header Failure; 'to-hdr-op-failrue': SIP Operate To Header Failure; 'route-hdr-op-failrue': SIP Operate Route Header Failure; 'record-route-hdr-op-failrue': SIP Operate Record-Route Header Failure; 'content-length-hdr-op-failrue': SIP Operate Content-Length Failure; 'third-party-registration': SIP Third-Party Registration; 'conn-ext-creation-failure': SIP Create Connection Extension Failure; 'alloc-contact-port-failure': SIP Alloc Contact Port Failure; 'outside-contact-port-mismatch': SIP Outside Contact Port Mismatch NAT Port; 'inside-contact-port-mismatch': SIP Inside Contact Port Mismatch; 'third-party-sdp': SIP Third-Party SDP; 'sdp-process-candidate-failure': SIP Operate SDP Media Candidate Attribute Failure; 'sdp-op-failure': SIP Operate SDP Failure; 'sdp-alloc-port-map-success': SIP Alloc SDP Port Map Success; 'sdp-alloc-port-map-failure': SIP Alloc SDP Port Map Failure; 'modify-failure': SIP Message Modify Failure; 'rewrite-failure': SIP Message Rewrite Failure; 'tcp-out-of-order-drop': TCP Out-of-Order Drop; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "sampling-enable"
        self.DeviceProxy = ""
        self.counters1 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Sip(A10BaseClass):
    
    """    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param sampling_enable: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "method-register", "method-invite", "method-ack", "method-cancel", "method-bye", "method-options", "method-prack", "method-subscribe", "method-notify", "method-publish", "method-info", "method-refer", "method-message", "method-update", "method-unknown", "parse-error", "req-uri-op-failrue", "via-hdr-op-failrue", "contact-hdr-op-failrue", "from-hdr-op-failrue", "to-hdr-op-failrue", "route-hdr-op-failrue", "record-route-hdr-op-failrue", "content-length-hdr-op-failrue", "third-party-registration", "conn-ext-creation-failure", "alloc-contact-port-failure", "outside-contact-port-mismatch", "inside-contact-port-mismatch", "third-party-sdp", "sdp-process-candidate-failure", "sdp-op-failure", "sdp-alloc-port-map-success", "sdp-alloc-port-map-failure", "modify-failure", "rewrite-failure", "tcp-out-of-order-drop"], "type": "string", "description": "'all': all; 'method-register': SIP Method REGISTER; 'method-invite': SIP Method INVITE; 'method-ack': SIP Method ACK; 'method-cancel': SIP Method CANCEL; 'method-bye': SIP Method BYE; 'method-options': SIP Method OPTIONS; 'method-prack': SIP Method PRACK; 'method-subscribe': SIP Method SUBSCRIBE; 'method-notify': SIP Method NOTIFY; 'method-publish': SIP Method PUBLISH; 'method-info': SIP Method INFO; 'method-refer': SIP Method REFER; 'method-message': SIP Method MESSAGE; 'method-update': SIP Method UPDATE; 'method-unknown': SIP Method UNKNOWN; 'parse-error': SIP Message Parse Error; 'req-uri-op-failrue': SIP Operate Request Uri Failure; 'via-hdr-op-failrue': SIP Operate Via Header Failure; 'contact-hdr-op-failrue': SIP Operate Contact Header Failure; 'from-hdr-op-failrue': SIP Operate From Header Failure; 'to-hdr-op-failrue': SIP Operate To Header Failure; 'route-hdr-op-failrue': SIP Operate Route Header Failure; 'record-route-hdr-op-failrue': SIP Operate Record-Route Header Failure; 'content-length-hdr-op-failrue': SIP Operate Content-Length Failure; 'third-party-registration': SIP Third-Party Registration; 'conn-ext-creation-failure': SIP Create Connection Extension Failure; 'alloc-contact-port-failure': SIP Alloc Contact Port Failure; 'outside-contact-port-mismatch': SIP Outside Contact Port Mismatch NAT Port; 'inside-contact-port-mismatch': SIP Inside Contact Port Mismatch; 'third-party-sdp': SIP Third-Party SDP; 'sdp-process-candidate-failure': SIP Operate SDP Media Candidate Attribute Failure; 'sdp-op-failure': SIP Operate SDP Failure; 'sdp-alloc-port-map-success': SIP Alloc SDP Port Map Success; 'sdp-alloc-port-map-failure': SIP Alloc SDP Port Map Failure; 'modify-failure': SIP Message Modify Failure; 'rewrite-failure': SIP Message Rewrite Failure; 'tcp-out-of-order-drop': TCP Out-of-Order Drop; ", "format": "enum"}}}]}
    :param sip_value: {"optional": true, "enum": ["enable"], "type": "string", "description": "'enable': Enable SIP ALG for LSN; ", "format": "enum"}
    :param rtp_stun_timeout: {"description": "RTP/RTCP STUN timeout in minutes (Default is 5 minutes)", "format": "number", "default": 5, "optional": true, "maximum": 10, "minimum": 2, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Change LSN SIP ALG Settings.

    Class sip supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/lsn/alg/sip`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "sip"
        self.a10_url="/axapi/v3/cgnv6/lsn/alg/sip"
        self.DeviceProxy = ""
        self.uuid = ""
        self.sampling_enable = []
        self.sip_value = ""
        self.rtp_stun_timeout = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


