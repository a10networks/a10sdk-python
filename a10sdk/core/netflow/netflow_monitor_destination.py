from a10sdk.common.A10BaseClass import A10BaseClass


class IpCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ip: {"not-list": ["service-group", "ipv6"], "type": "string", "description": "IP address of netflow collector", "format": "ipv4-address"}
    :param port4: {"description": "Port number, default is 9996", "format": "number", "default": 9996, "maximum": 65535, "minimum": 1, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ip-cfg"
        self.DeviceProxy = ""
        self.ip = ""
        self.port4 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Ipv6Cfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param port6: {"description": "Port number, default is 9996", "format": "number", "default": 9996, "maximum": 65535, "minimum": 1, "type": "number"}
    :param ipv6: {"not-list": ["service-group", "ip"], "type": "string", "description": "IPv6 address of netflow collector", "format": "ipv6-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ipv6-cfg"
        self.DeviceProxy = ""
        self.port6 = ""
        self.ipv6 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Destination(A10BaseClass):
    
    """Class Description::
    Configure destination where netflow records will be sent.

    Class destination supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param service_group: {"description": "Service-group for load balancing between multiple collector servers", "format": "string-rlx", "minLength": 1, "not-list": ["ip", "ipv6"], "optional": true, "maxLength": 63, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/netflow/monitor/{name}/destination`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "destination"
        self.a10_url="/axapi/v3/netflow/monitor/{name}/destination"
        self.DeviceProxy = ""
        self.ip_cfg = {}
        self.service_group = ""
        self.ipv6_cfg = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


