from a10sdk.common.A10BaseClass import A10BaseClass


class SamplingEnable(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param counters1: {"enum": ["all", "calls-established", "call-req-pns-call-id-mismatch", "call-reply-pns-call-id-mismatch", "gre-session-created", "gre-session-freed", "call-req-retransmit", "call-req-new", "call-req-ext-alloc-failure", "call-reply-call-id-unknown", "call-reply-retransmit", "call-reply-ext-ext-alloc-failure", "smp-app-type-mismatch", "smp-client-call-id-mismatch", "smp-sessions-created", "smp-sessions-freed", "smp-alloc-failure", "gre-conn-creation-failure", "gre-conn-ext-creation-failure", "gre-no-fwd-route", "gre-no-rev-route", "gre-no-control-conn", "gre-conn-already-exists", "gre-free-no-ext", "gre-free-no-smp", "gre-free-smp-app-type-mismatch", "control-freed", "control-free-no-ext", "control-free-no-smp", "control-free-smp-app-type-mismatch"], "type": "string", "description": "'all': all; 'calls-established': Calls Established; 'call-req-pns-call-id-mismatch': Call ID Mismatch on Call Request; 'call-reply-pns-call-id-mismatch': Call ID Mismatch on Call Reply; 'gre-session-created': GRE Session Created; 'gre-session-freed': GRE Session Freed; 'call-req-retransmit': Call Request Retransmit; 'call-req-new': Call Request New; 'call-req-ext-alloc-failure': Call Request Ext Alloc Failure; 'call-reply-call-id-unknown': Call Reply Unknown Client Call ID; 'call-reply-retransmit': Call Reply Retransmit; 'call-reply-ext-ext-alloc-failure': Call Request Ext Alloc Failure; 'smp-app-type-mismatch': SMP App Type Mismatch; 'smp-client-call-id-mismatch': SMP Client Call ID Mismatch; 'smp-sessions-created': SMP Session Created; 'smp-sessions-freed': SMP Session Freed; 'smp-alloc-failure': SMP Session Alloc Failure; 'gre-conn-creation-failure': GRE Conn Alloc Failure; 'gre-conn-ext-creation-failure': GRE Conn Ext Alloc Failure; 'gre-no-fwd-route': GRE No Fwd Route; 'gre-no-rev-route': GRE No Rev Route; 'gre-no-control-conn': GRE No Control Conn; 'gre-conn-already-exists': GRE Conn Already Exists; 'gre-free-no-ext': GRE Free No Ext; 'gre-free-no-smp': GRE Free No SMP; 'gre-free-smp-app-type-mismatch': GRE Free SMP App Type Mismatch; 'control-freed': Control Session Freed; 'control-free-no-ext': Control Free No Ext; 'control-free-no-smp': Control Free No SMP; 'control-free-smp-app-type-mismatch': Control Free SMP App Type Mismatch; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "sampling-enable"
        self.DeviceProxy = ""
        self.counters1 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Pptp(A10BaseClass):
    
    """    :param pptp_value: {"optional": true, "enum": ["disable"], "type": "string", "description": "'disable': Disable ALG; ", "format": "enum"}
    :param sampling_enable: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "calls-established", "call-req-pns-call-id-mismatch", "call-reply-pns-call-id-mismatch", "gre-session-created", "gre-session-freed", "call-req-retransmit", "call-req-new", "call-req-ext-alloc-failure", "call-reply-call-id-unknown", "call-reply-retransmit", "call-reply-ext-ext-alloc-failure", "smp-app-type-mismatch", "smp-client-call-id-mismatch", "smp-sessions-created", "smp-sessions-freed", "smp-alloc-failure", "gre-conn-creation-failure", "gre-conn-ext-creation-failure", "gre-no-fwd-route", "gre-no-rev-route", "gre-no-control-conn", "gre-conn-already-exists", "gre-free-no-ext", "gre-free-no-smp", "gre-free-smp-app-type-mismatch", "control-freed", "control-free-no-ext", "control-free-no-smp", "control-free-smp-app-type-mismatch"], "type": "string", "description": "'all': all; 'calls-established': Calls Established; 'call-req-pns-call-id-mismatch': Call ID Mismatch on Call Request; 'call-reply-pns-call-id-mismatch': Call ID Mismatch on Call Reply; 'gre-session-created': GRE Session Created; 'gre-session-freed': GRE Session Freed; 'call-req-retransmit': Call Request Retransmit; 'call-req-new': Call Request New; 'call-req-ext-alloc-failure': Call Request Ext Alloc Failure; 'call-reply-call-id-unknown': Call Reply Unknown Client Call ID; 'call-reply-retransmit': Call Reply Retransmit; 'call-reply-ext-ext-alloc-failure': Call Request Ext Alloc Failure; 'smp-app-type-mismatch': SMP App Type Mismatch; 'smp-client-call-id-mismatch': SMP Client Call ID Mismatch; 'smp-sessions-created': SMP Session Created; 'smp-sessions-freed': SMP Session Freed; 'smp-alloc-failure': SMP Session Alloc Failure; 'gre-conn-creation-failure': GRE Conn Alloc Failure; 'gre-conn-ext-creation-failure': GRE Conn Ext Alloc Failure; 'gre-no-fwd-route': GRE No Fwd Route; 'gre-no-rev-route': GRE No Rev Route; 'gre-no-control-conn': GRE No Control Conn; 'gre-conn-already-exists': GRE Conn Already Exists; 'gre-free-no-ext': GRE Free No Ext; 'gre-free-no-smp': GRE Free No SMP; 'gre-free-smp-app-type-mismatch': GRE Free SMP App Type Mismatch; 'control-freed': Control Session Freed; 'control-free-no-ext': Control Free No Ext; 'control-free-no-smp': Control Free No SMP; 'control-free-smp-app-type-mismatch': Control Free SMP App Type Mismatch; ", "format": "enum"}}}]}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Configure PPTP ALG for NAT stateful firewall (default: enabled).

    Class pptp supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/stateful-firewall/alg/pptp`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "pptp"
        self.a10_url="/axapi/v3/cgnv6/stateful-firewall/alg/pptp"
        self.DeviceProxy = ""
        self.pptp_value = ""
        self.sampling_enable = []
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


