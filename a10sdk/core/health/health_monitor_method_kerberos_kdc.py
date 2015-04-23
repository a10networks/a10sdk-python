from a10sdk.common.A10BaseClass import A10BaseClass


class KerberosCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param tcp_only: {"default": 0, "type": "number", "description": "Specify the kerberos tcp only", "format": "flag"}
    :param kpasswd_pricipal_name: {"minLength": 1, "maxLength": 127, "type": "string", "description": "Specify the pricipal name", "format": "string-rlx"}
    :param kinit_password: {"minLength": 1, "maxLength": 31, "type": "string", "description": "Password", "format": "password"}
    :param kpasswd_password: {"minLength": 1, "maxLength": 31, "type": "string", "description": "Password", "format": "password"}
    :param kpasswd: {"default": 0, "not-list": ["kinit", "kadmin"], "type": "number", "description": "Kerberos change passwd", "format": "flag"}
    :param kinit_pricipal_name: {"minLength": 1, "maxLength": 127, "type": "string", "description": "Specify the pricipal name", "format": "string-rlx"}
    :param kpasswd_kdc: {"minLength": 1, "maxLength": 63, "type": "string", "description": "Specify the kdc server, host|ip [:port]", "format": "string-rlx"}
    :param kpasswd_server: {"minLength": 1, "maxLength": 63, "type": "string", "description": "Specify the Kerberos password server, host|ip [:port]", "format": "string-rlx"}
    :param kadmin_encrypted: {"type": "encrypted", "description": "Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED password string)", "format": "encrypted"}
    :param kinit: {"default": 0, "not-list": ["kadmin", "kpasswd"], "type": "number", "description": "Kerberos KDC", "format": "flag"}
    :param kadmin_pricipal_name: {"minLength": 1, "maxLength": 127, "type": "string", "description": "Specify the pricipal name", "format": "string-rlx"}
    :param kadmin_realm: {"minLength": 1, "maxLength": 63, "type": "string", "description": "Specify the realm", "format": "string-rlx"}
    :param kinit_kdc: {"minLength": 1, "maxLength": 63, "type": "string", "description": "Specify the kdc server, host|ip [:port]", "format": "string-rlx"}
    :param kinit_encrypted: {"type": "encrypted", "description": "Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED password string)", "format": "encrypted"}
    :param kadmin: {"default": 0, "not-list": ["kinit", "kpasswd"], "type": "number", "description": "Kerberos admin", "format": "flag"}
    :param kadmin_kdc: {"minLength": 1, "maxLength": 63, "type": "string", "description": "Specify the kdc server, host|ip [:port]", "format": "string-rlx"}
    :param kadmin_server: {"minLength": 1, "maxLength": 63, "type": "string", "description": "Specify the admin server, host|ip [:port]", "format": "string-rlx"}
    :param kpasswd_encrypted: {"type": "encrypted", "description": "Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED password string)", "format": "encrypted"}
    :param kadmin_password: {"minLength": 1, "maxLength": 31, "type": "string", "description": "Password", "format": "password"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "kerberos-cfg"
        self.DeviceProxy = ""
        self.tcp_only = ""
        self.kpasswd_pricipal_name = ""
        self.kinit_password = ""
        self.kpasswd_password = ""
        self.kpasswd = ""
        self.kinit_pricipal_name = ""
        self.kpasswd_kdc = ""
        self.kpasswd_server = ""
        self.kadmin_encrypted = ""
        self.kinit = ""
        self.kadmin_pricipal_name = ""
        self.kadmin_realm = ""
        self.kinit_kdc = ""
        self.kinit_encrypted = ""
        self.kadmin = ""
        self.kadmin_kdc = ""
        self.kadmin_server = ""
        self.kpasswd_encrypted = ""
        self.kadmin_password = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class KerberosKdc(A10BaseClass):
    
    """Class Description::
    Kerberos KDC type.

    Class kerberos-kdc supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/health/monitor/{name}/method/kerberos-kdc`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "kerberos-kdc"
        self.a10_url="/axapi/v3/health/monitor/{name}/method/kerberos-kdc"
        self.DeviceProxy = ""
        self.kerberos_cfg = {}
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


