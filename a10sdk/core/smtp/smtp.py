from a10sdk.common.A10BaseClass import A10BaseClass


class Password(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param encrypted: {"type": "encrypted", "description": " Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED password string)", "format": "encrypted"}
    :param smtp_password: {"minLength": 1, "maxLength": 31, "type": "string", "description": "Configure SMTP login password", "format": "password"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "password"
        self.DeviceProxy = ""
        self.encrypted = ""
        self.smtp_password = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class UsernameCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param username: {"minLength": 1, "maxLength": 31, "type": "string", "description": "Configure SMTP login username", "format": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "username-cfg"
        self.DeviceProxy = ""
        self.username = ""
        self.password = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Smtp(A10BaseClass):
    
    """Class Description::
    Configure SMTP Server.

    Class smtp supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param mailfrom: {"description": "Configure email source address", "format": "email-addr", "minLength": 1, "optional": true, "maxLength": 31, "type": "string"}
    :param smtp_server: {"description": "Configure SMTP Server (length:1-31)", "format": "host", "minLength": 1, "optional": true, "maxLength": 31, "not": "smtp-server-v6", "type": "string"}
    :param needauthentication: {"default": 0, "optional": true, "type": "number", "description": "Configure SMTP server need authtication", "format": "flag"}
    :param port: {"description": "Configure SMTP Port (Configure SMTP port, default is 25)", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": true}
    :param smtp_server_v6: {"not": "smtp-server", "optional": true, "type": "string", "description": "Configure SMTP Server IPV6 address", "format": "ipv6-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/smtp`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "smtp"
        self.a10_url="/axapi/v3/smtp"
        self.DeviceProxy = ""
        self.mailfrom = ""
        self.smtp_server = ""
        self.username_cfg = {}
        self.needauthentication = ""
        self.port = ""
        self.smtp_server_v6 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


