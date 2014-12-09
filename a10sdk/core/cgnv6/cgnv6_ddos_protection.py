from a10sdk.common.A10BaseClass import A10BaseClass


class PacketsPerSecond(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ip: {"description": "Configure packets-per-second threshold per IP(default 3000)", "format": "number", "default": 3000, "maximum": 30000000, "minimum": 0, "type": "number"}
    :param udp: {"description": "Configure packets-per-second threshold per UDP port (default: 3000)", "format": "number", "default": 3000, "maximum": 30000000, "minimum": 0, "type": "number"}
    :param other: {"description": "Configure packets-per-second threshold for other L4 protocols(default 10000)", "format": "number", "default": 10000, "maximum": 30000000, "minimum": 0, "type": "number"}
    :param tcp: {"description": "Configure packets-per-second threshold per TCP port (default: 3000)", "format": "number", "default": 3000, "maximum": 30000000, "minimum": 0, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "packets-per-second"
        self.DeviceProxy = ""
        self.ip = ""
        self.udp = ""
        self.other = ""
        self.tcp = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Logging(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param logging_toggle: {"default": "enable", "enum": ["enable", "disable"], "type": "string", "description": "'enable': Enable CGNV6 NAT pool DDoS protection logging (default); 'disable': Disable CGNV6 NAT pool DDoS protection logging; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "logging"
        self.DeviceProxy = ""
        self.logging_toggle = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class DdosProtection(A10BaseClass):
    
    """Class Description::
    Configure CGNV6 DDoS Protection.

    Class ddos-protection supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param toggle: {"description": "'enable': Enable CGNV6 NAT pool DDoS protection (default); 'disable': Disable CGNV6 NAT pool DDoS protection; ", "format": "enum", "default": "enable", "type": "string", "enum": ["enable", "disable"], "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/ddos-protection`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "ddos-protection"
        self.a10_url="/axapi/v3/cgnv6/ddos-protection"
        self.DeviceProxy = ""
        self.packets_per_second = {}
        self.toggle = ""
        self.logging = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


