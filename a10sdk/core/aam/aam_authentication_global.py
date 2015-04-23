from a10sdk.common.A10BaseClass import A10BaseClass


class SamplingEnable(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param counters1: {"enum": ["all", "Requests", "Responses", "Misses", "Ocsp-Stapling-Requests-to-a10authd", "Ocsp-Stapling-Responses-from-a10authd", "Opened-socket", "Open-socket-failed", "Connect", "Connect-failed", "Created-timer", "Create-timer-failed", "Total-request", "Get-socket-option-failed", "Aflex-authz-succ", "Aflex-authz-fail"], "type": "string", "description": "'all': all; 'Requests': Total Authentication Request; 'Responses': Total Authentication Response; 'Misses': Total Authentication Request Missed; 'Ocsp-Stapling-Requests-to-a10authd': Total OCSP Stapling Request; 'Ocsp-Stapling-Responses-from-a10authd': Total OCSP Stapling Response; 'Opened-socket': Total AAM Socket Opened; 'Open-socket-failed': Total AAM Open Socket Failed; 'Connect': Total AAM Connection; 'Connect-failed': Total AAM Connect Failed; 'Created-timer': Total AAM Timer Created; 'Create-timer-failed': Total AAM Timer Creation Failed; 'Total-request': Total Request Received by A10 Auth Service; 'Get-socket-option-failed': Total AAM Get Socket Option Failed; 'Aflex-authz-succ': Total Authorization success number in aFleX; 'Aflex-authz-fail': Total Authorization failure number in aFleX; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "sampling-enable"
        self.DeviceProxy = ""
        self.counters1 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Global(A10BaseClass):
    
    """    :param sampling_enable: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "Requests", "Responses", "Misses", "Ocsp-Stapling-Requests-to-a10authd", "Ocsp-Stapling-Responses-from-a10authd", "Opened-socket", "Open-socket-failed", "Connect", "Connect-failed", "Created-timer", "Create-timer-failed", "Total-request", "Get-socket-option-failed", "Aflex-authz-succ", "Aflex-authz-fail"], "type": "string", "description": "'all': all; 'Requests': Total Authentication Request; 'Responses': Total Authentication Response; 'Misses': Total Authentication Request Missed; 'Ocsp-Stapling-Requests-to-a10authd': Total OCSP Stapling Request; 'Ocsp-Stapling-Responses-from-a10authd': Total OCSP Stapling Response; 'Opened-socket': Total AAM Socket Opened; 'Open-socket-failed': Total AAM Open Socket Failed; 'Connect': Total AAM Connection; 'Connect-failed': Total AAM Connect Failed; 'Created-timer': Total AAM Timer Created; 'Create-timer-failed': Total AAM Timer Creation Failed; 'Total-request': Total Request Received by A10 Auth Service; 'Get-socket-option-failed': Total AAM Get Socket Option Failed; 'Aflex-authz-succ': Total Authorization success number in aFleX; 'Aflex-authz-fail': Total Authorization failure number in aFleX; ", "format": "enum"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Global AAM authentication statistics.

    Class global supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/aam/authentication/global`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "global"
        self.a10_url="/axapi/v3/aam/authentication/global"
        self.DeviceProxy = ""
        self.sampling_enable = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


