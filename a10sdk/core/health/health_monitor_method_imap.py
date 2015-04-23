from a10sdk.common.A10BaseClass import A10BaseClass


class Imap(A10BaseClass):
    
    """Class Description::
    IMAP type.

    Class imap supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param imap_cram_md5: {"default": 0, "optional": true, "type": "number", "description": "Challenge-response authentication mechanism", "format": "flag"}
    :param imap_port: {"description": "Specify the IMAP port, default is 143 (Port Number (default 143))", "format": "number", "default": 143, "optional": true, "maximum": 65534, "minimum": 1, "type": "number"}
    :param imap_login: {"default": 0, "optional": true, "type": "number", "description": "Simple login", "format": "flag"}
    :param imap_password: {"default": 0, "optional": true, "type": "number", "description": "Specify the user password", "format": "flag"}
    :param imap_password_string: {"description": "Configure password, '' means empty passworddd", "format": "password", "minLength": 1, "optional": true, "maxLength": 31, "type": "string"}
    :param imap_username: {"description": "Specify the username", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 31, "type": "string"}
    :param imap_encrypted: {"optional": true, "type": "encrypted", "description": "Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED password string)", "format": "encrypted"}
    :param pwd_auth: {"default": 0, "optional": true, "type": "number", "description": "Specify the Authentication method", "format": "flag"}
    :param imap_plain: {"default": 0, "optional": true, "type": "number", "description": "Plain text", "format": "flag"}
    :param imap: {"default": 0, "optional": true, "type": "number", "description": "IMAP type", "format": "flag"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/health/monitor/{name}/method/imap`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "imap"
        self.a10_url="/axapi/v3/health/monitor/{name}/method/imap"
        self.DeviceProxy = ""
        self.imap_cram_md5 = ""
        self.imap_port = ""
        self.imap_login = ""
        self.imap_password = ""
        self.imap_password_string = ""
        self.imap_username = ""
        self.imap_encrypted = ""
        self.pwd_auth = ""
        self.imap_plain = ""
        self.imap = ""
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


