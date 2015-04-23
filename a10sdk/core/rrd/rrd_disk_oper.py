from a10sdk.common.A10BaseClass import A10BaseClass


class DiskUsage(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param disk_usage: {"type": "string", "format": "string"}
    :param time: {"type": "number", "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "disk-usage"
        self.DeviceProxy = ""
        self.disk_usage = ""
        self.time = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param end_time: {"type": "number", "format": "number"}
    :param start_time: {"type": "number", "format": "number"}
    :param total_disk: {"type": "string", "format": "string"}
    :param disk_usage: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"disk-usage": {"type": "string", "format": "string"}, "optional": true, "time": {"type": "number", "format": "number"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.end_time = ""
        self.start_time = ""
        self.total_disk = ""
        self.disk_usage = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Disk(A10BaseClass):
    
    """Class Description::
    Operational Status for the object disk.

    Class disk supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/rrd/disk/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "disk"
        self.a10_url="/axapi/v3/rrd/disk/oper"
        self.DeviceProxy = ""
        self.oper = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


