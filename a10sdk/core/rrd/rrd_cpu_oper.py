from a10sdk.common.A10BaseClass import A10BaseClass


class CpuUsage(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param cpu_usage: {"type": "string", "format": "string"}
    :param cpu_id: {"type": "number", "format": "number"}
    :param time: {"type": "number", "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "cpu-usage"
        self.DeviceProxy = ""
        self.cpu_usage = ""
        self.cpu_id = ""
        self.time = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param cpu_usage: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"cpu-usage": {"type": "string", "format": "string"}, "optional": true, "cpu-id": {"type": "number", "format": "number"}, "time": {"type": "number", "format": "number"}}}]}
    :param end_time: {"type": "number", "format": "number"}
    :param start_time: {"type": "number", "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.cpu_usage = []
        self.end_time = ""
        self.start_time = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Cpu(A10BaseClass):
    
    """Class Description::
    Operational Status for the object cpu.

    Class cpu supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/rrd/cpu/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "cpu"
        self.a10_url="/axapi/v3/rrd/cpu/oper"
        self.DeviceProxy = ""
        self.oper = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


