from a10sdk.common.A10BaseClass import A10BaseClass


class PortResp(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param port_contains: {"minLength": 1, "maxLength": 127, "type": "string", "description": "Mark server up if response string contains another string (Specify the string)", "format": "string-rlx"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "port-resp"
        self.DeviceProxy = ""
        self.port_contains = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Tcp(A10BaseClass):
    
    """Class Description::
    TCP type.

    Class tcp supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param port_send: {"description": "Send a string to server (Specify the string)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 127, "not": "port-halfopen", "type": "string"}
    :param method_tcp: {"default": 0, "optional": true, "type": "number", "description": "TCP type", "format": "flag"}
    :param port_halfopen: {"description": "Set TCP SYN check", "format": "flag", "default": 0, "optional": true, "not": "port-send", "type": "number"}
    :param tcp_port: {"description": "Specify TCP port (Specify port number)", "format": "number", "type": "number", "maximum": 65534, "minimum": 1, "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/health/monitor/{name}/method/tcp`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "tcp"
        self.a10_url="/axapi/v3/health/monitor/{name}/method/tcp"
        self.DeviceProxy = ""
        self.port_send = ""
        self.method_tcp = ""
        self.port_halfopen = ""
        self.port_resp = {}
        self.tcp_port = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


