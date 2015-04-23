from a10sdk.common.A10BaseClass import A10BaseClass


class SamplingEnable(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param counters1: {"enum": ["all", "calls-established", "mismatched-pns-call-id", "gre-sessions-created", "gre-sessions-freed", "no-gre-session-match", "smp-sessions-created", "smp-sessions-freed", "smp-session-creation-failure", "extension-creation-failure", "ha-sent", "ha-rcv", "ha-no-mem", "ha-conflict", "ha-overwrite", "ha-call-sent", "ha-call-rcv", "ha-smp-conflict", "ha-smp-in-del-q", "smp-app-type-mismatch", "quota-inc", "quota-dec", "quota-inc-not-found", "quota-dec-not-found"], "type": "string", "description": "'all': all; 'calls-established': Calls Established; 'mismatched-pns-call-id': Mismatched PNS Call ID; 'gre-sessions-created': GRE Sessions Created; 'gre-sessions-freed': GRE Sessions Freed; 'no-gre-session-match': No Matching GRE Session; 'smp-sessions-created': SMP Sessions Created; 'smp-sessions-freed': SMP Sessions Freed; 'smp-session-creation-failure': SMP Session Creation Failures; 'extension-creation-failure': Extension Creation Failures; 'ha-sent': HA Info Sent; 'ha-rcv': HA Info Received; 'ha-no-mem': HA Memory Allocation Failure; 'ha-conflict': HA Call ID Conflicts; 'ha-overwrite': HA Call ID Overwrites; 'ha-call-sent': HA Call Sent; 'ha-call-rcv': HA Call Received; 'ha-smp-conflict': HA SMP Conflicts; 'ha-smp-in-del-q': HA SMP Deleted; 'smp-app-type-mismatch': SMP ALG App Type Mismatch; 'quota-inc': Quota Incremented; 'quota-dec': Quota Decremented; 'quota-inc-not-found': Quota Not Found on Increment; 'quota-dec-not-found': Quota Not Found on Decrement; ", "format": "enum"}
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
    
    """    :param pptp_value: {"optional": true, "enum": ["enable"], "type": "string", "description": "'enable': Enable PPTP ALG for LSN; ", "format": "enum"}
    :param sampling_enable: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "calls-established", "mismatched-pns-call-id", "gre-sessions-created", "gre-sessions-freed", "no-gre-session-match", "smp-sessions-created", "smp-sessions-freed", "smp-session-creation-failure", "extension-creation-failure", "ha-sent", "ha-rcv", "ha-no-mem", "ha-conflict", "ha-overwrite", "ha-call-sent", "ha-call-rcv", "ha-smp-conflict", "ha-smp-in-del-q", "smp-app-type-mismatch", "quota-inc", "quota-dec", "quota-inc-not-found", "quota-dec-not-found"], "type": "string", "description": "'all': all; 'calls-established': Calls Established; 'mismatched-pns-call-id': Mismatched PNS Call ID; 'gre-sessions-created': GRE Sessions Created; 'gre-sessions-freed': GRE Sessions Freed; 'no-gre-session-match': No Matching GRE Session; 'smp-sessions-created': SMP Sessions Created; 'smp-sessions-freed': SMP Sessions Freed; 'smp-session-creation-failure': SMP Session Creation Failures; 'extension-creation-failure': Extension Creation Failures; 'ha-sent': HA Info Sent; 'ha-rcv': HA Info Received; 'ha-no-mem': HA Memory Allocation Failure; 'ha-conflict': HA Call ID Conflicts; 'ha-overwrite': HA Call ID Overwrites; 'ha-call-sent': HA Call Sent; 'ha-call-rcv': HA Call Received; 'ha-smp-conflict': HA SMP Conflicts; 'ha-smp-in-del-q': HA SMP Deleted; 'smp-app-type-mismatch': SMP ALG App Type Mismatch; 'quota-inc': Quota Incremented; 'quota-dec': Quota Decremented; 'quota-inc-not-found': Quota Not Found on Increment; 'quota-dec-not-found': Quota Not Found on Decrement; ", "format": "enum"}}}]}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Change LSN PPTP ALG Settings.

    Class pptp supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/lsn/alg/pptp`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "pptp"
        self.a10_url="/axapi/v3/cgnv6/lsn/alg/pptp"
        self.DeviceProxy = ""
        self.pptp_value = ""
        self.sampling_enable = []
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


