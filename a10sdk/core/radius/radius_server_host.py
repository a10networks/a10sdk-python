from a10sdk.common.A10BaseClass import A10BaseClass


class Host(A10BaseClass):
    
    """Class Description::
    Specify the RADIUS server's hostname or IP address.

    Class host supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param ipv4_list: {"minItems": 1, "items": {"type": "ipv4"}, "uniqueItems": true, "array": [{"required": ["ipv4-addr"], "properties": {"ipv4-addr": {"optional": false, "type": "string", "description": "IPV4 address of RADIUS server", "format": "ipv4-address"}, "secret": {"type": "object", "properties": {"port-cfg": {"type": "object", "properties": {"acct-port": {"description": "Specify the RADIUS server's accounting port (default 1813)", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}, "retransmit": {"description": "Specify the maximum times allowed for resending an request to the radius server (default 3)", "format": "number", "default": 3, "maximum": 5, "minimum": 0, "type": "number"}, "timeout": {"description": "Specify the maximum time allowed for waiting for a response from a radius server (default 3)", "format": "number", "default": 3, "maximum": 15, "minimum": 1, "type": "number"}, "auth-port": {"description": "Specify the RADIUS server's authentication port (default 1812)", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}}}, "encrypted": {"type": "encrypted", "description": " Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED secret string)", "format": "encrypted"}, "secret-value": {"minLength": 1, "maxLength": 128, "type": "string", "description": "The RADIUS server's secret", "format": "password"}}}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/radius-server/host/ipv4/{ipv4-addr}"}
    :param name_list: {"minItems": 1, "items": {"type": "name"}, "uniqueItems": true, "array": [{"required": ["hostname"], "properties": {"secret": {"type": "object", "properties": {"port-cfg": {"type": "object", "properties": {"acct-port": {"description": "Specify the RADIUS server's accounting port (default 1813)", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}, "retransmit": {"description": "Specify the maximum times allowed for resending an request to the radius server (default 3)", "format": "number", "default": 3, "maximum": 5, "minimum": 0, "type": "number"}, "timeout": {"description": "Specify the maximum time allowed for waiting for a response from a radius server (default 3)", "format": "number", "default": 3, "maximum": 15, "minimum": 1, "type": "number"}, "auth-port": {"description": "Specify the RADIUS server's authentication port (default 1812)", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}}}, "encrypted": {"type": "encrypted", "description": " Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED secret string)", "format": "encrypted"}, "secret-value": {"minLength": 1, "maxLength": 128, "type": "string", "description": "The RADIUS server's secret", "format": "password"}}}, "hostname": {"description": "Hostname of RADIUS server", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/radius-server/host/name/{hostname}"}
    :param ipv6_list: {"minItems": 1, "items": {"type": "ipv6"}, "uniqueItems": true, "array": [{"required": ["ipv6-addr"], "properties": {"secret": {"type": "object", "properties": {"port-cfg": {"type": "object", "properties": {"acct-port": {"description": "Specify the RADIUS server's accounting port (default 1813)", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}, "retransmit": {"description": "Specify the maximum times allowed for resending an request to the radius server (default 3)", "format": "number", "default": 3, "maximum": 5, "minimum": 0, "type": "number"}, "timeout": {"description": "Specify the maximum time allowed for waiting for a response from a radius server (default 3)", "format": "number", "default": 3, "maximum": 15, "minimum": 1, "type": "number"}, "auth-port": {"description": "Specify the RADIUS server's authentication port (default 1812)", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}}}, "encrypted": {"type": "encrypted", "description": " Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED secret string)", "format": "encrypted"}, "secret-value": {"minLength": 1, "maxLength": 128, "type": "string", "description": "The RADIUS server's secret", "format": "password"}}}, "ipv6-addr": {"optional": false, "type": "string", "description": "IPV6 address of RADIUS server", "format": "ipv6-address"}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/radius-server/host/ipv6/{ipv6-addr}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/radius-server/host`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "host"
        self.a10_url="/axapi/v3/radius-server/host"
        self.DeviceProxy = ""
        self.ipv4_list = []
        self.name_list = []
        self.ipv6_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


