from a10sdk.common.A10BaseClass import A10BaseClass


class IcmpTimeout(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param icmp_timeout_val: {"description": "Timeout in seconds (Interval of 60 seconds)", "minimum": 2, "type": "number", "maximum": 15000, "format": "number"}
    :param icmp_timeout: {"default": "fast", "enum": ["age", "fast"], "type": "string", "description": "'age': Expiration time; 'fast': Use Fast aging; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "icmp-timeout"
        self.DeviceProxy = ""
        self.icmp_timeout_val = ""
        self.icmp_timeout = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Translation(A10BaseClass):
    
    """Class Description::
    Change or Disable NAT translation values.

    Class translation supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param tcp_timeout: {"description": "TCP protocol extended translations (Timeout in seconds (Interval of 60 seconds), default is 300 seconds (5 minutes))", "format": "number", "default": 300, "optional": true, "maximum": 15000, "minimum": 2, "type": "number"}
    :param service_timeout_list: {"minItems": 1, "items": {"type": "service-timeout"}, "uniqueItems": true, "array": [{"required": ["service-type", "port"], "properties": {"timeout-val": {"description": "Timeout in seconds (Interval of 60 seconds)", "format": "number", "type": "number", "maximum": 15000, "minimum": 2, "optional": true}, "service-type": {"optional": false, "enum": ["tcp", "udp"], "type": "string", "description": "'tcp': TCP Protocol; 'udp': UDP Protocol; ", "format": "enum"}, "timeout-type": {"optional": true, "enum": ["age", "fast"], "type": "string", "description": "'age': Expiration time; 'fast': Use Fast aging; ", "format": "enum"}, "port": {"description": "Port Number", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": false}}}], "type": "array", "$ref": "/axapi/v3/ip/nat/translation/service-timeout/{service-type}+{port}"}
    :param udp_timeout: {"description": "UDP protocol extended translations (Timeout in seconds (Interval of 60 seconds), default is 300 seconds (5 minutes))", "format": "number", "default": 300, "optional": true, "maximum": 15000, "minimum": 2, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/ip/nat/translation`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "translation"
        self.a10_url="/axapi/v3/ip/nat/translation"
        self.DeviceProxy = ""
        self.tcp_timeout = ""
        self.service_timeout_list = []
        self.udp_timeout = ""
        self.icmp_timeout = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


