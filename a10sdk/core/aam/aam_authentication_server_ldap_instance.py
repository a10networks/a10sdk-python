from a10sdk.common.A10BaseClass import A10BaseClass


class Host(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param hostipv6: {"not": "hostip", "type": "string", "description": "Server's IPV6 address", "format": "ipv6-address"}
    :param hostip: {"description": "Server's hostname(Length 1-31) or IP address", "format": "host", "minLength": 1, "maxLength": 31, "not": "hostipv6", "type": "string"}
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


class DeriveBindDn(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param username_attr: {"minLength": 1, "maxLength": 31, "type": "string", "description": "Specify attribute name of username", "format": "string-rlx"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "derive-bind-dn"
        self.DeviceProxy = ""
        self.username_attr = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Instance(A10BaseClass):
    
    """Class Description::
    LDAP Authentication Server.

    Class instance supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param health_check_string: {"description": "Health monitor name", "format": "string", "minLength": 1, "optional": true, "maxLength": 31, "type": "string", "$ref": "/axapi/v3/health/monitor"}
    :param port_hm: {"description": "Check port's health status", "format": "string", "minLength": 1, "optional": true, "maxLength": 31, "not": "port-hm-disable", "type": "string", "$ref": "/axapi/v3/health/monitor"}
    :param name: {"description": "Specify LDAP authentication server name", "format": "string-rlx", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param port_hm_disable: {"description": "Disable configured port health check configuration", "format": "flag", "default": 0, "optional": true, "not": "port-hm", "type": "number"}
    :param admin_dn: {"description": "The LDAP server's admin DN", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 127, "type": "string"}
    :param encrypted: {"optional": true, "type": "encrypted", "description": "Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED secret string)", "format": "encrypted"}
    :param default_domain: {"description": "Specify default domain for LDAP", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param health_check_disable: {"description": "Disable configured health check configuration", "format": "flag", "default": 0, "optional": true, "not": "health-check", "type": "number"}
    :param admin_secret: {"default": 0, "optional": true, "type": "number", "description": "Specify the LDAP server's admin secret password", "format": "flag"}
    :param health_check: {"description": "Check server's health status", "format": "flag", "default": 0, "optional": true, "not": "health-check-disable", "type": "number"}
    :param bind_with_dn: {"default": 0, "optional": true, "type": "number", "description": "Enforce using DN for LDAP binding(All user input name will be used to create DN)", "format": "flag"}
    :param base: {"description": "Specify the LDAP server's search base", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 127, "type": "string"}
    :param dn_attribute: {"description": "Specify Distinguished Name attribute, default is CN", "format": "string-rlx", "default": "cn", "minLength": 1, "optional": true, "maxLength": 31, "type": "string"}
    :param timeout: {"description": "Specify timout for LDAP, default is 10 seconds (The timeout, default is 10 seconds)", "format": "number", "default": 10, "optional": true, "maximum": 255, "minimum": 1, "type": "number"}
    :param pwdmaxage: {"description": "Specify the LDAP server's default password expiration time (in seconds) (The LDAP server's default password expiration time (in seconds), default is 0 (no expiration))", "format": "number", "default": 0, "optional": true, "maximum": 4294967295, "minimum": 0, "type": "number"}
    :param port: {"description": "Specify the LDAP server's authentication port, default is 389", "format": "number", "default": 389, "optional": true, "maximum": 65534, "minimum": 1, "type": "number"}
    :param secret_string: {"description": "secret password", "format": "password", "minLength": 1, "optional": true, "maxLength": 128, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/aam/authentication/server/ldap/instance/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "instance"
        self.a10_url="/axapi/v3/aam/authentication/server/ldap/instance/{name}"
        self.DeviceProxy = ""
        self.uuid = ""
        self.health_check_string = ""
        self.port_hm = ""
        self.name = ""
        self.port_hm_disable = ""
        self.admin_dn = ""
        self.encrypted = ""
        self.default_domain = ""
        self.health_check_disable = ""
        self.admin_secret = ""
        self.health_check = ""
        self.bind_with_dn = ""
        self.host = {}
        self.base = ""
        self.dn_attribute = ""
        self.timeout = ""
        self.pwdmaxage = ""
        self.derive_bind_dn = {}
        self.port = ""
        self.secret_string = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


