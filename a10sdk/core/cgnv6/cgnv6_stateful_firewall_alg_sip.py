from a10sdk.common.A10BaseClass import A10BaseClass


class SamplingEnable(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param counters1: {"enum": ["all", "stat-request", "stat-response", "method-register", "method-invite", "method-ack", "method-cancel", "method-bye", "method-port-config", "method-prack", "method-subscribe", "method-notify", "method-publish", "method-info", "method-refer", "method-message", "method-update", "method-unknown", "parse-error", "keep-alive", "contact-error", "sdp-error", "rtp-port-no-op", "rtp-rtcp-port-success", "rtp-port-failure", "rtcp-port-failure", "contact-port-no-op", "contact-port-success", "contact-port-failure", "contact-new", "contact-alloc-failure", "contact-eim", "contact-eim-set", "rtp-new", "rtp-alloc-failure", "rtp-eim"], "type": "string", "description": "'all': all; 'stat-request': Request Received; 'stat-response': Response Received; 'method-register': Method REGISTER; 'method-invite': Method INVITE; 'method-ack': Method ACK; 'method-cancel': Method CANCEL; 'method-bye': Method BYE; 'method-port-config': Method OPTIONS; 'method-prack': Method PRACK; 'method-subscribe': Method SUBSCRIBE; 'method-notify': Method NOTIFY; 'method-publish': Method PUBLISH; 'method-info': Method INFO; 'method-refer': Method REFER; 'method-message': Method MESSAGE; 'method-update': Method UPDATE; 'method-unknown': Method Unknown; 'parse-error': Message Parse Error; 'keep-alive': Keep Alive; 'contact-error': Contact Process Error; 'sdp-error': SDP Process Error; 'rtp-port-no-op': RTP Port No Op; 'rtp-rtcp-port-success': RTP RTCP Port Success; 'rtp-port-failure': RTP Port Failure; 'rtcp-port-failure': RTCP Port Failure; 'contact-port-no-op': Contact Port No Op; 'contact-port-success': Contact Port Success; 'contact-port-failure': Contact Port Failure; 'contact-new': Contact Alloc; 'contact-alloc-failure': Contact Alloc Failure; 'contact-eim': Contact EIM; 'contact-eim-set': Contact EIM Set; 'rtp-new': RTP Alloc; 'rtp-alloc-failure': RTP Alloc Failure; 'rtp-eim': RTP EIM; ", "format": "enum"}
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
    
    """    :param sampling_enable: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "stat-request", "stat-response", "method-register", "method-invite", "method-ack", "method-cancel", "method-bye", "method-port-config", "method-prack", "method-subscribe", "method-notify", "method-publish", "method-info", "method-refer", "method-message", "method-update", "method-unknown", "parse-error", "keep-alive", "contact-error", "sdp-error", "rtp-port-no-op", "rtp-rtcp-port-success", "rtp-port-failure", "rtcp-port-failure", "contact-port-no-op", "contact-port-success", "contact-port-failure", "contact-new", "contact-alloc-failure", "contact-eim", "contact-eim-set", "rtp-new", "rtp-alloc-failure", "rtp-eim"], "type": "string", "description": "'all': all; 'stat-request': Request Received; 'stat-response': Response Received; 'method-register': Method REGISTER; 'method-invite': Method INVITE; 'method-ack': Method ACK; 'method-cancel': Method CANCEL; 'method-bye': Method BYE; 'method-port-config': Method OPTIONS; 'method-prack': Method PRACK; 'method-subscribe': Method SUBSCRIBE; 'method-notify': Method NOTIFY; 'method-publish': Method PUBLISH; 'method-info': Method INFO; 'method-refer': Method REFER; 'method-message': Method MESSAGE; 'method-update': Method UPDATE; 'method-unknown': Method Unknown; 'parse-error': Message Parse Error; 'keep-alive': Keep Alive; 'contact-error': Contact Process Error; 'sdp-error': SDP Process Error; 'rtp-port-no-op': RTP Port No Op; 'rtp-rtcp-port-success': RTP RTCP Port Success; 'rtp-port-failure': RTP Port Failure; 'rtcp-port-failure': RTCP Port Failure; 'contact-port-no-op': Contact Port No Op; 'contact-port-success': Contact Port Success; 'contact-port-failure': Contact Port Failure; 'contact-new': Contact Alloc; 'contact-alloc-failure': Contact Alloc Failure; 'contact-eim': Contact EIM; 'contact-eim-set': Contact EIM Set; 'rtp-new': RTP Alloc; 'rtp-alloc-failure': RTP Alloc Failure; 'rtp-eim': RTP EIM; ", "format": "enum"}}}]}
    :param sip_value: {"optional": true, "enum": ["disable"], "type": "string", "description": "'disable': Disable ALG; ", "format": "enum"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Configure SIP ALG for NAT stateful firewall (default: enabled).

    Class sip supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/stateful-firewall/alg/sip`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "sip"
        self.a10_url="/axapi/v3/cgnv6/stateful-firewall/alg/sip"
        self.DeviceProxy = ""
        self.sampling_enable = []
        self.sip_value = ""
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


