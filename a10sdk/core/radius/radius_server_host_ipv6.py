from a10sdk.common.A10BaseClass import A10BaseClass


class PortCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param acct_port: {"description": "Specify the RADIUS server's accounting port (default 1813)", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}
    :param retransmit: {"description": "Specify the maximum times allowed for resending an request to the radius server (default 3)", "format": "number", "default": 3, "maximum": 5, "minimum": 0, "type": "number"}
    :param timeout: {"description": "Specify the maximum time allowed for waiting for a response from a radius server (default 3)", "format": "number", "default": 3, "maximum": 15, "minimum": 1, "type": "number"}
    :param auth_port: {"description": "Specify the RADIUS server's authentication port (default 1812)", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "port-cfg"
        self.DeviceProxy = ""
        self.acct_port = ""
        self.retransmit = ""
        self.timeout = ""
        self.auth_port = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Secret(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param encrypted: {"type": "encrypted", "description": " Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED secret string)", "format": "encrypted"}
    :param secret_value: {"minLength": 1, "maxLength": 128, "type": "string", "description": "The RADIUS server's secret", "format": "password"}
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
    Specify the hostname of Radius server.

    Class ipv6 supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param ipv6_addr: {"optional": false, "type": "string", "description": "IPV6 address of RADIUS server", "format": "ipv6-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/radius-server/host/ipv6/{ipv6_addr}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "ipv6_addr"]

        self.b_key = "ipv6"
        self.a10_url="/axapi/v3/radius-server/host/ipv6/{ipv6_addr}"
        self.DeviceProxy = ""
        self.secret = {}
        self.ipv6_addr = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


