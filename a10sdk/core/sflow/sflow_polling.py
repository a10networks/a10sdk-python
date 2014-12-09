from a10sdk.common.A10BaseClass import A10BaseClass


class EthList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param eth_end: {"type": "number", "description": "Ethernet interface to sample", "format": "interface"}
    :param eth_start: {"type": "number", "description": "Ethernet interface to sample", "format": "interface"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "eth-list"
        self.DeviceProxy = ""
        self.eth_end = ""
        self.eth_start = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class VeList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ve_end: {"$ref": "/axapi/v3/interface/ve", "type": "number", "description": "VE interface to sample", "format": "number"}
    :param ve_start: {"$ref": "/axapi/v3/interface/ve", "type": "number", "description": "VE interface to sample", "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ve-list"
        self.DeviceProxy = ""
        self.ve_end = ""
        self.ve_start = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Polling(A10BaseClass):
    
    """Class Description::
    Configure sFlow counter polling on specified source.

    Class polling supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param cpu_usage: {"default": 0, "optional": true, "type": "number", "description": "Polling CPU usage", "format": "flag"}
    :param eth_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"eth-end": {"type": "number", "description": "Ethernet interface to sample", "format": "interface"}, "optional": true, "eth-start": {"type": "number", "description": "Ethernet interface to sample", "format": "interface"}}}]}
    :param http_counter: {"default": 0, "optional": true, "type": "number", "description": "Polling HTTP counters", "format": "flag"}
    :param ve_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"ve-end": {"$ref": "/axapi/v3/interface/ve", "type": "number", "description": "VE interface to sample", "format": "number"}, "ve-start": {"$ref": "/axapi/v3/interface/ve", "type": "number", "description": "VE interface to sample", "format": "number"}, "optional": true}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/sflow/polling`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "polling"
        self.a10_url="/axapi/v3/sflow/polling"
        self.DeviceProxy = ""
        self.cpu_usage = ""
        self.eth_list = []
        self.http_counter = ""
        self.ve_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


