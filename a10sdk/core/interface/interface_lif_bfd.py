from a10sdk.common.A10BaseClass import A10BaseClass


class Authentication(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param encrypted: {"type": "encrypted", "description": "Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED password string)", "format": "encrypted"}
    :param password: {"minLength": 1, "maxLength": 16, "type": "string", "description": "Key String", "format": "password"}
    :param method: {"enum": ["md5", "meticulous-md5", "meticulous-sha1", "sha1", "simple"], "type": "string", "description": "'md5': Keyed MD5; 'meticulous-md5': Meticulous Keyed MD5; 'meticulous-sha1': Meticulous Keyed SHA1; 'sha1': Keyed SHA1; 'simple': Simple Password; ", "format": "enum"}
    :param key_id: {"description": "Key ID", "minimum": 0, "type": "number", "maximum": 255, "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "authentication"
        self.DeviceProxy = ""
        self.encrypted = ""
        self.password = ""
        self.method = ""
        self.key_id = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class IntervalCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param interval: {"description": "Transmit interval between BFD packets (Milliseconds)", "minimum": 48, "type": "number", "maximum": 1000, "format": "number"}
    :param min_rx: {"description": "Minimum receive interval capability (Milliseconds)", "minimum": 48, "type": "number", "maximum": 1000, "format": "number"}
    :param multiplier: {"description": "Multiplier value used to compute holddown (value used to multiply the interval)", "minimum": 3, "type": "number", "maximum": 50, "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "interval-cfg"
        self.DeviceProxy = ""
        self.interval = ""
        self.min_rx = ""
        self.multiplier = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Bfd(A10BaseClass):
    
    """Class Description::
    Configure BFD (Bidirectional Forwarding Detection).

    Class bfd supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param demand: {"default": 0, "optional": true, "type": "number", "description": "Demand mode", "format": "flag"}
    :param echo: {"default": 0, "optional": true, "type": "number", "description": "Enable BFD Echo", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/interface/lif/{ifnum}/bfd`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "bfd"
        self.a10_url="/axapi/v3/interface/lif/{ifnum}/bfd"
        self.DeviceProxy = ""
        self.authentication = {}
        self.demand = ""
        self.interval_cfg = {}
        self.echo = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


