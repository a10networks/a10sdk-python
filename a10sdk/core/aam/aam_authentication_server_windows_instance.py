from a10sdk.common.A10BaseClass import A10BaseClass


class Host(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param hostipv6: {"not": "hostip", "type": "string", "description": "Specify the Windows server's IPV6 address", "format": "ipv6-address"}
    :param hostip: {"description": "Specify the Windows server's hostname(Length 1-31) or IP address", "format": "host", "minLength": 1, "maxLength": 31, "not": "hostipv6", "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "host"
        self.DeviceProxy = ""
        self.hostipv6 = ""
        self.hostip = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class AuthProtocol(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ntlm_health_check: {"description": "Check NTLM port's health status", "format": "string", "minLength": 1, "maxLength": 31, "not": "ntlm-health-check-disable", "type": "string", "$ref": "/axapi/v3/health/monitor"}
    :param kport_hm_disable: {"default": 0, "not": "kport-hm", "type": "number", "description": "Disable configured Kerberos port health check configuration", "format": "flag"}
    :param kerberos_disable: {"default": 0, "type": "number", "description": "Disable Kerberos authentication protocol", "format": "flag"}
    :param ntlm_health_check_disable: {"default": 0, "not": "ntlm-health-check", "type": "number", "description": "Disable configured NTLM port health check configuration", "format": "flag"}
    :param kerberos_port: {"description": "Specify the Kerbros port, default is 88", "format": "number", "default": 88, "maximum": 65534, "minimum": 1, "type": "number"}
    :param ntlm_version: {"description": "Specify NTLM version, default is 2", "format": "number", "default": 2, "maximum": 2, "minimum": 1, "type": "number"}
    :param ntlm_disable: {"default": 0, "type": "number", "description": "Disable NTLM authentication protocol", "format": "flag"}
    :param kport_hm: {"description": "Check Kerberos port's health status", "format": "string", "minLength": 1, "maxLength": 31, "not": "kport-hm-disable", "type": "string", "$ref": "/axapi/v3/health/monitor"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "auth-protocol"
        self.DeviceProxy = ""
        self.ntlm_health_check = ""
        self.kport_hm_disable = ""
        self.kerberos_disable = ""
        self.ntlm_health_check_disable = ""
        self.kerberos_port = ""
        self.ntlm_version = ""
        self.ntlm_disable = ""
        self.kport_hm = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Instance(A10BaseClass):
    
    """Class Description::
    "Windows Server, using Kerberos or NTLM for authentication".

    Class instance supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param health_check_string: {"description": "Health monitor name", "format": "string", "minLength": 1, "optional": true, "maxLength": 31, "type": "string", "$ref": "/axapi/v3/health/monitor"}
    :param realm: {"description": "Specify realm of Windows server", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param name: {"description": "Specify Windows authentication server name", "format": "string-rlx", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param health_check_disable: {"description": "Disable configured health check configuration", "format": "flag", "default": 0, "optional": true, "not": "health-check", "type": "number"}
    :param timeout: {"description": "Specify connection timeout to server, default is 10 seconds", "format": "number", "default": 10, "optional": true, "maximum": 255, "minimum": 1, "type": "number"}
    :param support_apacheds_kdc: {"default": 0, "optional": true, "type": "number", "description": "Enable weak cipher (DES CRC/MD5/MD4) and merge AS-REQ in single packet", "format": "flag"}
    :param health_check: {"description": "Check server's health status", "format": "flag", "default": 0, "optional": true, "not": "health-check-disable", "type": "number"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/aam/authentication/server/windows/instance/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "instance"
        self.a10_url="/axapi/v3/aam/authentication/server/windows/instance/{name}"
        self.DeviceProxy = ""
        self.health_check_string = ""
        self.realm = ""
        self.name = ""
        self.health_check_disable = ""
        self.host = {}
        self.auth_protocol = {}
        self.timeout = ""
        self.support_apacheds_kdc = ""
        self.health_check = ""
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


