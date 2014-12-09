from a10sdk.common.A10BaseClass import A10BaseClass


class Ldap(A10BaseClass):
    
    """Class Description::
    LDAP type.

    Class ldap supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param ldap_port: {"description": "Specify the LDAP port (Speciry port number, default is 389, or 636 if LDAP over SSL)", "format": "number", "default": 389, "optional": true, "maximum": 65534, "minimum": 1, "type": "number"}
    :param ldap_password_string: {"description": "Configure password, '' means empty passworddd", "format": "password", "minLength": 1, "optional": true, "maxLength": 31, "type": "string"}
    :param ldap_encrypted: {"optional": true, "type": "encrypted", "description": "Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED password string)", "format": "encrypted"}
    :param BaseDN: {"description": "Specify LDAP DN distinguished name", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 127, "type": "string"}
    :param ldap_query: {"description": "LDAP query to be excuted", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 255, "type": "string"}
    :param ldap_binddn: {"description": "Specify the distinguished name for bindRequest (LDAP DN distinguished name)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 127, "type": "string"}
    :param ldap_password: {"default": 0, "optional": true, "type": "number", "description": "Specify the user password", "format": "flag"}
    :param ldap_security: {"optional": true, "enum": ["overssl", "StartTLS"], "type": "string", "description": "'overssl': Set LDAP over SSL; 'StartTLS': LDAP switch to TLS; ", "format": "enum"}
    :param ldap: {"default": 0, "optional": true, "type": "number", "description": "LDAP type", "format": "flag"}
    :param AcceptNotFound: {"default": 0, "optional": true, "type": "number", "description": "Mark server up on receiving a not-found response", "format": "flag"}
    :param ldap_run_search: {"default": 0, "optional": true, "type": "number", "description": "Specify a query to be executed", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/health/monitor/{name}/method/ldap`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "ldap"
        self.a10_url="/axapi/v3/health/monitor/{name}/method/ldap"
        self.DeviceProxy = ""
        self.ldap_port = ""
        self.ldap_password_string = ""
        self.ldap_encrypted = ""
        self.BaseDN = ""
        self.ldap_query = ""
        self.ldap_binddn = ""
        self.ldap_password = ""
        self.ldap_security = ""
        self.ldap = ""
        self.AcceptNotFound = ""
        self.ldap_run_search = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


