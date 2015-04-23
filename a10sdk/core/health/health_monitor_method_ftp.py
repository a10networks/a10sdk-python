from a10sdk.common.A10BaseClass import A10BaseClass


class Ftp(A10BaseClass):
    
    """Class Description::
    FTP type.

    Class ftp supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param ftp: {"default": 0, "optional": true, "type": "number", "description": "FTP type", "format": "flag"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param ftp_password_string: {"description": "Specify the user password, '' means empty passworddd", "format": "password", "minLength": 1, "optional": true, "maxLength": 31, "type": "string"}
    :param ftp_password: {"default": 0, "optional": true, "type": "number", "description": "Specify the user password", "format": "flag"}
    :param ftp_port: {"description": "Specify FTP port (Specify port number, default is 21)", "format": "number", "default": 21, "optional": true, "maximum": 65534, "minimum": 1, "type": "number"}
    :param ftp_encrypted: {"optional": true, "type": "encrypted", "description": "Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED password string)", "format": "encrypted"}
    :param ftp_username: {"description": "Specify the username", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 31, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/health/monitor/{name}/method/ftp`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "ftp"
        self.a10_url="/axapi/v3/health/monitor/{name}/method/ftp"
        self.DeviceProxy = ""
        self.ftp = ""
        self.uuid = ""
        self.ftp_password_string = ""
        self.ftp_password = ""
        self.ftp_port = ""
        self.ftp_encrypted = ""
        self.ftp_username = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


