from a10sdk.common.A10BaseClass import A10BaseClass


class CpuUsage(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param cpu_id: {"type": "number", "format": "number"}
    :param 30_sec: {"type": "number", "format": "number"}
    :param 60_sec: {"type": "number", "format": "number"}
    :param 10_sec: {"type": "number", "format": "number"}
    :param 5_sec: {"type": "number", "format": "number"}
    :param 1_sec: {"type": "number", "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "cpu-usage"
        self.DeviceProxy = ""
        self.cpu_id = ""
        self.A10WW_30_sec = ""
        self.A10WW_60_sec = ""
        self.A10WW_10_sec = ""
        self.A10WW_5_sec = ""
        self.A10WW_1_sec = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param cpu_usage: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"cpu-id": {"type": "number", "format": "number"}, "30-sec": {"type": "number", "format": "number"}, "optional": true, "60-sec": {"type": "number", "format": "number"}, "10-sec": {"type": "number", "format": "number"}, "5-sec": {"type": "number", "format": "number"}, "1-sec": {"type": "number", "format": "number"}}}]}
    :param number_of_cpu: {"type": "number", "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.cpu_usage = []
        self.number_of_cpu = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class DataCpu(A10BaseClass):
    
    """Class Description::
    Operational Status for the object data-cpu.

    Class data-cpu supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/system-cpu/data-cpu/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "data-cpu"
        self.a10_url="/axapi/v3/system-cpu/data-cpu/oper"
        self.DeviceProxy = ""
        self.oper = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


