from a10sdk.common.A10BaseClass import A10BaseClass


class PortCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param username: {"minLength": 1, "maxLength": 128, "type": "string", "description": "Specify the username", "format": "string"}
    :param monitor: {"default": 0, "type": "number", "description": "Specify monitor TACACS+ server", "format": "flag"}
    :param encrypted: {"minLength": 1, "maxLength": 255, "type": "encrypted", "description": "Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED secret string)", "format": "encrypted"}
    :param timeout: {"description": "Specify the maximum time allowed for setting up a connection with the TACACS+ server. (default timeout is 12 seconds) (Maximum time allowed for setting up a connection with the TACACS+ server, in seconds (default 12))", "format": "number", "default": 12, "maximum": 12, "minimum": 1, "type": "number"}
    :param password_value: {"minLength": 1, "maxLength": 31, "type": "string", "description": "The user password", "format": "password"}
    :param password: {"default": 0, "type": "number", "description": "Specify the user password", "format": "flag"}
    :param port: {"description": "Specify the port number used by TACACS+ server.( default port is 49) (Port number (default 49))", "format": "number", "default": 49, "maximum": 65535, "minimum": 1, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "port-cfg"
        self.DeviceProxy = ""
        self.username = ""
        self.monitor = ""
        self.encrypted = ""
        self.timeout = ""
        self.password_value = ""
        self.password = ""
        self.port = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Secret(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param encrypted: {"minLength": 1, "maxLength": 255, "type": "encrypted", "description": "Do NOT use this option manually. (This is an A10 reserved keyword.) help-val The ENCRYPTED secret string", "format": "encrypted"}
    :param secret_value: {"minLength": 1, "maxLength": 127, "type": "string", "description": "The TACACS+ server's secret", "format": "password"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "secret"
        self.DeviceProxy = ""
        self.port_cfg = {}
        self.encrypted = ""
        self.secret_value = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Ipv6(A10BaseClass):
    
    """Class Description::
    Specify the hostname of TACACS+ server.

    Class ipv6 supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param ipv6_addr: {"optional": false, "type": "string", "description": "IPV6 address of TACACS+ server", "format": "ipv6-address"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/tacacs-server/host/ipv6/{ipv6_addr}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "ipv6_addr"]

        self.b_key = "ipv6"
        self.a10_url="/axapi/v3/tacacs-server/host/ipv6/{ipv6_addr}"
        self.DeviceProxy = ""
        self.secret = {}
        self.ipv6_addr = ""
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


