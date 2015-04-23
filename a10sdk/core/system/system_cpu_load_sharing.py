from a10sdk.common.A10BaseClass import A10BaseClass


class PacketsPerSecond(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param min: {"description": "Minimum packets-per-second threshold (per CPU) before redistribution will take effect (Minimum packets-per-second threshold (per CPU) before redistribution will take effect (default: 100000))", "format": "number", "default": 100000, "maximum": 30000000, "minimum": 0, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "packets-per-second"
        self.DeviceProxy = ""
        self.A10WW_min = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class CpuUsage(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param high: {"description": "CPU usage threshold (percentage) that will trigger the redistribution (default: 75)", "format": "number", "default": 75, "maximum": 100, "minimum": 0, "type": "number"}
    :param low: {"description": "CPU usage threshold (percentage) that will restore the normal packet distribution (default: 60)", "format": "number", "default": 60, "maximum": 100, "minimum": 0, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "cpu-usage"
        self.DeviceProxy = ""
        self.high = ""
        self.low = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class CpuLoadSharing(A10BaseClass):
    
    """    :param disable: {"default": 0, "optional": true, "type": "number", "description": "Disable CPU load sharing in overload situations", "format": "flag"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Redistribute packets uniformly to all CPUs during overload situations.

    Class cpu-load-sharing supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/system/cpu-load-sharing`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "cpu-load-sharing"
        self.a10_url="/axapi/v3/system/cpu-load-sharing"
        self.DeviceProxy = ""
        self.packets_per_second = {}
        self.cpu_usage = {}
        self.disable = ""
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


