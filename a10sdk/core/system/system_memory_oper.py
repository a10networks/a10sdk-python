from a10sdk.common.A10BaseClass import A10BaseClass


class SystemMemory(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param Max: {"type": "number", "format": "number"}
    :param Allocated: {"type": "number", "format": "number"}
    :param Object_size: {"type": "number", "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "System-memory"
        self.DeviceProxy = ""
        self.Max = ""
        self.Allocated = ""
        self.Object_size = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class N2Memory(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param Max: {"type": "number", "format": "number"}
    :param Allocated: {"type": "number", "format": "number"}
    :param Object_size: {"type": "number", "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "N2-memory"
        self.DeviceProxy = ""
        self.Max = ""
        self.Allocated = ""
        self.Object_size = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class TcpMemory(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param Max: {"type": "number", "format": "number"}
    :param Allocated: {"type": "number", "format": "number"}
    :param Object_size: {"type": "number", "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "TCP-memory"
        self.DeviceProxy = ""
        self.Max = ""
        self.Allocated = ""
        self.Object_size = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class AflexMemory(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param Max: {"type": "number", "format": "number"}
    :param Allocated: {"type": "number", "format": "number"}
    :param Object_size: {"type": "number", "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "aFleX-memory"
        self.DeviceProxy = ""
        self.Max = ""
        self.Allocated = ""
        self.Object_size = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class SslMemory(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param Max: {"type": "number", "format": "number"}
    :param Allocated: {"type": "number", "format": "number"}
    :param Object_size: {"type": "number", "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "SSL-memory"
        self.DeviceProxy = ""
        self.Max = ""
        self.Allocated = ""
        self.Object_size = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param System_memory: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"Max": {"type": "number", "format": "number"}, "Allocated": {"type": "number", "format": "number"}, "optional": true, "Object-size": {"type": "number", "format": "number"}}}]}
    :param Used: {"type": "number", "format": "number"}
    :param N2_memory: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"Max": {"type": "number", "format": "number"}, "Allocated": {"type": "number", "format": "number"}, "optional": true, "Object-size": {"type": "number", "format": "number"}}}]}
    :param TCP_memory: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"Max": {"type": "number", "format": "number"}, "Allocated": {"type": "number", "format": "number"}, "optional": true, "Object-size": {"type": "number", "format": "number"}}}]}
    :param Free: {"type": "number", "format": "number"}
    :param aFleX_memory: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"Max": {"type": "number", "format": "number"}, "Allocated": {"type": "number", "format": "number"}, "optional": true, "Object-size": {"type": "number", "format": "number"}}}]}
    :param SSL_memory: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"Max": {"type": "number", "format": "number"}, "Allocated": {"type": "number", "format": "number"}, "optional": true, "Object-size": {"type": "number", "format": "number"}}}]}
    :param Usage: {"type": "string", "format": "string"}
    :param Total: {"type": "number", "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.System_memory = []
        self.Used = ""
        self.N2_memory = []
        self.TCP_memory = []
        self.Free = ""
        self.aFleX_memory = []
        self.SSL_memory = []
        self.Usage = ""
        self.Total = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Memory(A10BaseClass):
    
    """Class Description::
    Operational Status for the object memory.

    Class memory supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/system/memory/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "memory"
        self.a10_url="/axapi/v3/system/memory/oper"
        self.DeviceProxy = ""
        self.oper = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


