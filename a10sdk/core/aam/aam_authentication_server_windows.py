from a10sdk.common.A10BaseClass import A10BaseClass


class Windows(A10BaseClass):
    
    """Class Description::
    "Windows Server, using Kerberos or NTLM for authentication".

    Class windows supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param instance_list: {"minItems": 1, "items": {"type": "instance"}, "uniqueItems": true, "array": [{"required": ["name"], "properties": {"health-check-string": {"description": "Health monitor name", "format": "string", "minLength": 1, "optional": true, "maxLength": 31, "type": "string", "$ref": "/axapi/v3/health/monitor"}, "realm": {"description": "Specify realm of Windows server", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}, "name": {"description": "Specify Windows authentication server name", "format": "string-rlx", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}, "health-check-disable": {"description": "Disable configured health check configuration", "format": "flag", "default": 0, "optional": true, "not": "health-check", "type": "number"}, "host": {"type": "object", "properties": {"hostipv6": {"not": "hostip", "type": "string", "description": "Specify the Windows server's IPV6 address", "format": "ipv6-address"}, "hostip": {"description": "Specify the Windows server's hostname(Length 1-31) or IP address", "format": "host", "minLength": 1, "maxLength": 31, "not": "hostipv6", "type": "string"}}}, "auth-protocol": {"type": "object", "properties": {"ntlm-health-check": {"description": "Check NTLM port's health status", "format": "string", "minLength": 1, "maxLength": 31, "not": "ntlm-health-check-disable", "type": "string", "$ref": "/axapi/v3/health/monitor"}, "kport-hm-disable": {"default": 0, "not": "kport-hm", "type": "number", "description": "Disable configured Kerberos port health check configuration", "format": "flag"}, "kerberos-disable": {"default": 0, "type": "number", "description": "Disable Kerberos authentication protocol", "format": "flag"}, "ntlm-health-check-disable": {"default": 0, "not": "ntlm-health-check", "type": "number", "description": "Disable configured NTLM port health check configuration", "format": "flag"}, "kerberos-port": {"description": "Specify the Kerbros port, default is 88", "format": "number", "default": 88, "maximum": 65535, "minimum": 1, "type": "number"}, "ntlm-version": {"description": "Specify NTLM version, default is 2", "format": "number", "default": 2, "maximum": 2, "minimum": 1, "type": "number"}, "ntlm-disable": {"default": 0, "type": "number", "description": "Disable NTLM authentication protocol", "format": "flag"}, "kport-hm": {"description": "Check Kerberos port's health status", "format": "string", "minLength": 1, "maxLength": 31, "not": "kport-hm-disable", "type": "string", "$ref": "/axapi/v3/health/monitor"}}}, "timeout": {"description": "Specify connection timeout to server, default is 10 seconds", "format": "number", "default": 10, "optional": true, "maximum": 255, "minimum": 1, "type": "number"}, "health-check": {"description": "Check server's health status", "format": "flag", "default": 0, "optional": true, "not": "health-check-disable", "type": "number"}}}], "type": "array", "$ref": "/axapi/v3/aam/authentication/server/windows/instance/{name}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/aam/authentication/server/windows`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "windows"
        self.a10_url="/axapi/v3/aam/authentication/server/windows"
        self.DeviceProxy = ""
        self.instance_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


