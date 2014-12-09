from a10sdk.common.A10BaseClass import A10BaseClass


class Pop3(A10BaseClass):
    
    """Class Description::
    POP3 type.

    Class pop3 supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param pop3_password_string: {"description": "Specify the user password, '' means empty passworddd", "format": "password", "minLength": 1, "optional": true, "maxLength": 31, "type": "string"}
    :param pop3_password: {"default": 0, "optional": true, "type": "number", "description": "Specify the user password", "format": "flag"}
    :param pop3_username: {"description": "Specify the username", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 31, "type": "string"}
    :param pop3_port: {"description": "Specify the POP3 port, default is 110 (Port Number (default 110))", "format": "number", "default": 110, "optional": true, "maximum": 65534, "minimum": 1, "type": "number"}
    :param pop3: {"default": 0, "optional": true, "type": "number", "description": "POP3 type", "format": "flag"}
    :param pop3_encrypted: {"optional": true, "type": "encrypted", "description": "Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED password string)", "format": "encrypted"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/health/monitor/{name}/method/pop3`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "pop3"
        self.a10_url="/axapi/v3/health/monitor/{name}/method/pop3"
        self.DeviceProxy = ""
        self.pop3_password_string = ""
        self.pop3_password = ""
        self.pop3_username = ""
        self.pop3_port = ""
        self.pop3 = ""
        self.pop3_encrypted = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


