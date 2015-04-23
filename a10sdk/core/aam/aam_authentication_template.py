from a10sdk.common.A10BaseClass import A10BaseClass


class CookieDomain(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param cookie_dmn: {"minLength": 1, "maxLength": 63, "type": "string", "description": "Specify domain scope for the authentication (ex: .a10networks.com)", "format": "string-rlx"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "cookie-domain"
        self.DeviceProxy = ""
        self.cookie_dmn = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class CookieDomainGroup(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param cookie_dmngrp: {"description": "Specify group id to join in the cookie-domain", "minimum": 0, "type": "number", "maximum": 31, "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "cookie-domain-group"
        self.DeviceProxy = ""
        self.cookie_dmngrp = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Template(A10BaseClass):
    
    """Class Description::
    Authentication template.

    Class template supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param logout_idle_timeout: {"description": "Specify idle logout time (Specify idle timeout in seconds, default is 300)", "format": "number", "default": 300, "optional": true, "maximum": 86400, "minimum": 1, "type": "number"}
    :param cookie_domain: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"cookie-dmn": {"minLength": 1, "maxLength": 63, "type": "string", "description": "Specify domain scope for the authentication (ex: .a10networks.com)", "format": "string-rlx"}, "optional": true}}]}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param name: {"description": "Authentication template name", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param relay: {"description": "Specify authentication relay (Specify authentication relay template name)", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/aam/authentication/relay/http-basic/instance"}
    :param logon: {"description": "Specify authentication logon (Specify authentication logon template name)", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/aam/authentication/logon/form-based"}
    :param saml_sp: {"description": "Specify SAML service provider", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param logout_url: {"description": "Specify logout url (Specify logout url string)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 127, "type": "string"}
    :param service_group: {"description": "Bind an authentication service group to this template (Specify authentication service group name)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 127, "not": "server", "type": "string", "$ref": "/axapi/v3/aam/authentication/service-group"}
    :param server: {"description": "Specify authentication server (Specify authentication server template name)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "not": "service-group", "type": "string", "$ref": "/axapi/v3/aam/authentication/server/ldap/instance"}
    :param cookie_domain_group: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"cookie-dmngrp": {"description": "Specify group id to join in the cookie-domain", "minimum": 0, "type": "number", "maximum": 31, "format": "number"}, "optional": true}}]}
    :param forward_logout_disable: {"default": 0, "optional": true, "type": "number", "description": "Disable forward logout request to backend application server. The config-field logut-url must be configured first", "format": "flag"}
    :param log: {"description": "'use-partition-level-config': Use configuration of authentication-log enable command; 'enable': Enable authentication logs for this template; 'disable': Disable authentication logs for this template; ", "format": "enum", "default": "use-partition-level-config", "type": "string", "enum": ["use-partition-level-config", "enable", "disable"], "optional": true}
    :param account: {"description": "Specify AD domain account", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/aam/authentication/account/kerberos-spn"}
    :param saml_idp: {"description": "Specify SAML identity provider", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param type: {"optional": true, "enum": ["saml", "standard"], "type": "string", "description": "'saml': SAML authentication template; 'standard': Standard authentication template; ", "format": "enum"}
    :param cookie_max_age: {"description": "Configure Max-Age for authentication session cookie (Configure Max-Age in seconds. Default is 604800 (1 week).)", "format": "number", "default": 604800, "optional": true, "maximum": 2592000, "minimum": 1, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/aam/authentication/template/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "template"
        self.a10_url="/axapi/v3/aam/authentication/template/{name}"
        self.DeviceProxy = ""
        self.logout_idle_timeout = ""
        self.cookie_domain = []
        self.uuid = ""
        self.name = ""
        self.relay = ""
        self.logon = ""
        self.saml_sp = ""
        self.logout_url = ""
        self.service_group = ""
        self.server = ""
        self.cookie_domain_group = []
        self.forward_logout_disable = ""
        self.log = ""
        self.account = ""
        self.saml_idp = ""
        self.A10WW_type = ""
        self.cookie_max_age = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


