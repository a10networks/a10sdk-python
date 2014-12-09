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


class Sampling(A10BaseClass):
    
    """Class Description::
    Configure sFlow sampling on specified interfaces.

    Class sampling supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param eth_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"eth-end": {"type": "number", "description": "Ethernet interface to sample", "format": "interface"}, "optional": true, "eth-start": {"type": "number", "description": "Ethernet interface to sample", "format": "interface"}}}]}
    :param ve_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"ve-end": {"$ref": "/axapi/v3/interface/ve", "type": "number", "description": "VE interface to sample", "format": "number"}, "ve-start": {"$ref": "/axapi/v3/interface/ve", "type": "number", "description": "VE interface to sample", "format": "number"}, "optional": true}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/sflow/sampling`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "sampling"
        self.a10_url="/axapi/v3/sflow/sampling"
        self.DeviceProxy = ""
        self.eth_list = []
        self.ve_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


