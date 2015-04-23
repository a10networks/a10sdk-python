from a10sdk.common.A10BaseClass import A10BaseClass


class SamplingEnable(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param counters1: {"enum": ["all", "Kerberos-request-send", "Kerberos-response-get", "Kerberos-timeout-error", "Kerberos-other-error", "NTLM-Authentication-success", "NTLM-Authentication-failure", "NTLM-proto-negotiation-success", "NTLM-proto-negotiation-failure", "NTLM-session-setup-success", "NTLM-session-setup-failed"], "type": "string", "description": "'all': all; 'Kerberos-request-send': Total Kerberos Request; 'Kerberos-response-get': Total Kerberos Response; 'Kerberos-timeout-error': Total Kerberos Timeout; 'Kerberos-other-error': Total Kerberos Other Error; 'NTLM-Authentication-success': Total NTLM Authentication Success; 'NTLM-Authentication-failure': Total NTLM Authentication Failure; 'NTLM-proto-negotiation-success': Total NTLM Protocol Negotiation Success; 'NTLM-proto-negotiation-failure': Total NTLM Protocol Negotiation Failure; 'NTLM-session-setup-success': Total NTLM Session Setup Success; 'NTLM-session-setup-failed': Total NTLM Session Setup Failure; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "sampling-enable"
        self.DeviceProxy = ""
        self.counters1 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Windows(A10BaseClass):
    
    """    :param sampling_enable: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "Kerberos-request-send", "Kerberos-response-get", "Kerberos-timeout-error", "Kerberos-other-error", "NTLM-Authentication-success", "NTLM-Authentication-failure", "NTLM-proto-negotiation-success", "NTLM-proto-negotiation-failure", "NTLM-session-setup-success", "NTLM-session-setup-failed"], "type": "string", "description": "'all': all; 'Kerberos-request-send': Total Kerberos Request; 'Kerberos-response-get': Total Kerberos Response; 'Kerberos-timeout-error': Total Kerberos Timeout; 'Kerberos-other-error': Total Kerberos Other Error; 'NTLM-Authentication-success': Total NTLM Authentication Success; 'NTLM-Authentication-failure': Total NTLM Authentication Failure; 'NTLM-proto-negotiation-success': Total NTLM Protocol Negotiation Success; 'NTLM-proto-negotiation-failure': Total NTLM Protocol Negotiation Failure; 'NTLM-session-setup-success': Total NTLM Session Setup Success; 'NTLM-session-setup-failed': Total NTLM Session Setup Failure; ", "format": "enum"}}}]}
    :param instance_list: {"minItems": 1, "items": {"type": "instance"}, "uniqueItems": true, "array": [{"required": ["name"], "properties": {"health-check-string": {"description": "Health monitor name", "format": "string", "minLength": 1, "optional": true, "maxLength": 31, "type": "string", "$ref": "/axapi/v3/health/monitor"}, "realm": {"description": "Specify realm of Windows server", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}, "name": {"description": "Specify Windows authentication server name", "format": "string-rlx", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}, "health-check-disable": {"description": "Disable configured health check configuration", "format": "flag", "default": 0, "optional": true, "not": "health-check", "type": "number"}, "host": {"type": "object", "properties": {"hostipv6": {"not": "hostip", "type": "string", "description": "Specify the Windows server's IPV6 address", "format": "ipv6-address"}, "hostip": {"description": "Specify the Windows server's hostname(Length 1-31) or IP address", "format": "host", "minLength": 1, "maxLength": 31, "not": "hostipv6", "type": "string"}}}, "auth-protocol": {"type": "object", "properties": {"ntlm-health-check": {"description": "Check NTLM port's health status", "format": "string", "minLength": 1, "maxLength": 31, "not": "ntlm-health-check-disable", "type": "string", "$ref": "/axapi/v3/health/monitor"}, "kport-hm-disable": {"default": 0, "not": "kport-hm", "type": "number", "description": "Disable configured Kerberos port health check configuration", "format": "flag"}, "kerberos-disable": {"default": 0, "type": "number", "description": "Disable Kerberos authentication protocol", "format": "flag"}, "ntlm-health-check-disable": {"default": 0, "not": "ntlm-health-check", "type": "number", "description": "Disable configured NTLM port health check configuration", "format": "flag"}, "kerberos-port": {"description": "Specify the Kerbros port, default is 88", "format": "number", "default": 88, "maximum": 65534, "minimum": 1, "type": "number"}, "ntlm-version": {"description": "Specify NTLM version, default is 2", "format": "number", "default": 2, "maximum": 2, "minimum": 1, "type": "number"}, "ntlm-disable": {"default": 0, "type": "number", "description": "Disable NTLM authentication protocol", "format": "flag"}, "kport-hm": {"description": "Check Kerberos port's health status", "format": "string", "minLength": 1, "maxLength": 31, "not": "kport-hm-disable", "type": "string", "$ref": "/axapi/v3/health/monitor"}}}, "timeout": {"description": "Specify connection timeout to server, default is 10 seconds", "format": "number", "default": 10, "optional": true, "maximum": 255, "minimum": 1, "type": "number"}, "support-apacheds-kdc": {"default": 0, "optional": true, "type": "number", "description": "Enable weak cipher (DES CRC/MD5/MD4) and merge AS-REQ in single packet", "format": "flag"}, "health-check": {"description": "Check server's health status", "format": "flag", "default": 0, "optional": true, "not": "health-check-disable", "type": "number"}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/aam/authentication/server/windows/instance/{name}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    "Windows Server, using Kerberos or NTLM for authentication".

    Class windows supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/aam/authentication/server/windows`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "windows"
        self.a10_url="/axapi/v3/aam/authentication/server/windows"
        self.DeviceProxy = ""
        self.sampling_enable = []
        self.instance_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


