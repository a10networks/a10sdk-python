from a10sdk.common.A10BaseClass import A10BaseClass


class Radius(A10BaseClass):
    
    """Class Description::
    RADIUS type.

    Class radius supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param radius_username: {"description": "Specify the username", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 31, "type": "string"}
    :param radius_password_string: {"description": "Configure password, '' means empty passworddd", "format": "password", "minLength": 1, "optional": true, "maxLength": 31, "type": "string"}
    :param radius_encrypted: {"optional": true, "type": "encrypted", "description": "Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED password string)", "format": "encrypted"}
    :param radius_response_code: {"description": "Specify response code range (e.g. 2,4-7) (Format is xx,xx-xx (xx between [1, 13]))", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 31, "type": "string"}
    :param radius_expect: {"default": 0, "optional": true, "type": "number", "description": "Specify what you expect from the response message", "format": "flag"}
    :param radius: {"default": 0, "optional": true, "type": "number", "description": "RADIUS type", "format": "flag"}
    :param radius_secret: {"description": "Specify the shared secret of RADIUS server (Shared Crypto Key)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 31, "type": "string"}
    :param radius_password: {"default": 0, "optional": true, "type": "number", "description": "Specify the user password", "format": "flag"}
    :param radius_port: {"description": "Specify the RADIUS port, default is 1812 (Port number (default 1812))", "format": "number", "default": 1812, "optional": true, "maximum": 65534, "minimum": 1, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/health/monitor/{name}/method/radius`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "radius"
        self.a10_url="/axapi/v3/health/monitor/{name}/method/radius"
        self.DeviceProxy = ""
        self.radius_username = ""
        self.radius_password_string = ""
        self.radius_encrypted = ""
        self.radius_response_code = ""
        self.radius_expect = ""
        self.radius = ""
        self.radius_secret = ""
        self.radius_password = ""
        self.radius_port = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


