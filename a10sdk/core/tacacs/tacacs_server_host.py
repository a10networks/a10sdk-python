from a10sdk.common.A10BaseClass import A10BaseClass


class Host(A10BaseClass):
    
    """Class Description::
    Specify the hostname of TACACS+ server.

    Class host supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param tacacs_hostname_list: {"minItems": 1, "items": {"type": "tacacs-hostname"}, "uniqueItems": true, "array": [{"required": ["hostname"], "properties": {"secret": {"type": "object", "properties": {"port-cfg": {"type": "object", "properties": {"username": {"minLength": 1, "maxLength": 128, "type": "string", "description": "Specify the username", "format": "string"}, "monitor": {"default": 0, "type": "number", "description": "Specify monitor TACACS+ server", "format": "flag"}, "encrypted": {"minLength": 1, "maxLength": 255, "type": "encrypted", "description": "Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED secret string)", "format": "encrypted"}, "timeout": {"description": "Specify the maximum time allowed for setting up a connection with the TACACS+ server. (default timeout is 12 seconds) (Maximum time allowed for setting up a connection with the TACACS+ server, in seconds (default 12))", "format": "number", "default": 12, "maximum": 12, "minimum": 1, "type": "number"}, "password-value": {"minLength": 1, "maxLength": 31, "type": "string", "description": "The user password", "format": "password"}, "password": {"default": 0, "type": "number", "description": "Specify the user password", "format": "flag"}, "port": {"description": "Specify the port number used by TACACS+ server.( default port is 49) (Port number (default 49))", "format": "number", "default": 49, "maximum": 65535, "minimum": 1, "type": "number"}}}, "encrypted": {"minLength": 1, "maxLength": 255, "type": "encrypted", "description": "Do NOT use this option manually. (This is an A10 reserved keyword.) help-val The ENCRYPTED secret string", "format": "encrypted"}, "secret-value": {"minLength": 1, "maxLength": 127, "type": "string", "description": "The TACACS+ server's secret", "format": "password"}}}, "hostname": {"description": "Hostname of TACACS+ server", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/tacacs-server/host/tacacs-hostname/{hostname}"}
    :param ipv4_list: {"minItems": 1, "items": {"type": "ipv4"}, "uniqueItems": true, "array": [{"required": ["ipv4-addr"], "properties": {"ipv4-addr": {"optional": false, "type": "string", "description": "IPV4 address of TACACS+ server", "format": "ipv4-address"}, "secret": {"type": "object", "properties": {"port-cfg": {"type": "object", "properties": {"username": {"minLength": 1, "maxLength": 128, "type": "string", "description": "Specify the username", "format": "string"}, "monitor": {"default": 0, "type": "number", "description": "Specify monitor TACACS+ server", "format": "flag"}, "encrypted": {"minLength": 1, "maxLength": 255, "type": "encrypted", "description": "Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED secret string)", "format": "encrypted"}, "timeout": {"description": "Specify the maximum time allowed for setting up a connection with the TACACS+ server. (default timeout is 12 seconds) (Maximum time allowed for setting up a connection with the TACACS+ server, in seconds (default 12))", "format": "number", "default": 12, "maximum": 12, "minimum": 1, "type": "number"}, "password-value": {"minLength": 1, "maxLength": 31, "type": "string", "description": "The user password", "format": "password"}, "password": {"default": 0, "type": "number", "description": "Specify the user password", "format": "flag"}, "port": {"description": "Specify the port number used by TACACS+ server.( default port is 49) (Port number (default 49))", "format": "number", "default": 49, "maximum": 65535, "minimum": 1, "type": "number"}}}, "encrypted": {"minLength": 1, "maxLength": 255, "type": "encrypted", "description": "Do NOT use this option manually. (This is an A10 reserved keyword.) help-val The ENCRYPTED secret string", "format": "encrypted"}, "secret-value": {"minLength": 1, "maxLength": 127, "type": "string", "description": "The TACACS+ server's secret", "format": "password"}}}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/tacacs-server/host/ipv4/{ipv4-addr}"}
    :param ipv6_list: {"minItems": 1, "items": {"type": "ipv6"}, "uniqueItems": true, "array": [{"required": ["ipv6-addr"], "properties": {"secret": {"type": "object", "properties": {"port-cfg": {"type": "object", "properties": {"username": {"minLength": 1, "maxLength": 128, "type": "string", "description": "Specify the username", "format": "string"}, "monitor": {"default": 0, "type": "number", "description": "Specify monitor TACACS+ server", "format": "flag"}, "encrypted": {"minLength": 1, "maxLength": 255, "type": "encrypted", "description": "Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED secret string)", "format": "encrypted"}, "timeout": {"description": "Specify the maximum time allowed for setting up a connection with the TACACS+ server. (default timeout is 12 seconds) (Maximum time allowed for setting up a connection with the TACACS+ server, in seconds (default 12))", "format": "number", "default": 12, "maximum": 12, "minimum": 1, "type": "number"}, "password-value": {"minLength": 1, "maxLength": 31, "type": "string", "description": "The user password", "format": "password"}, "password": {"default": 0, "type": "number", "description": "Specify the user password", "format": "flag"}, "port": {"description": "Specify the port number used by TACACS+ server.( default port is 49) (Port number (default 49))", "format": "number", "default": 49, "maximum": 65535, "minimum": 1, "type": "number"}}}, "encrypted": {"minLength": 1, "maxLength": 255, "type": "encrypted", "description": "Do NOT use this option manually. (This is an A10 reserved keyword.) help-val The ENCRYPTED secret string", "format": "encrypted"}, "secret-value": {"minLength": 1, "maxLength": 127, "type": "string", "description": "The TACACS+ server's secret", "format": "password"}}}, "ipv6-addr": {"optional": false, "type": "string", "description": "IPV6 address of TACACS+ server", "format": "ipv6-address"}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/tacacs-server/host/ipv6/{ipv6-addr}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/tacacs-server/host`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "host"
        self.a10_url="/axapi/v3/tacacs-server/host"
        self.DeviceProxy = ""
        self.tacacs_hostname_list = []
        self.ipv4_list = []
        self.ipv6_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


