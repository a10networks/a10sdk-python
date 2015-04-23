from a10sdk.common.A10BaseClass import A10BaseClass


class CpuUsage(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param Max_Query_Msg_Per_Packet: {"type": "number", "format": "number"}
    :param cpu_id: {"type": "number", "format": "number"}
    :param Max_Sync_Msg_Per_Packet: {"type": "number", "format": "number"}
    :param Min_Query_Msg_Per_Packet: {"type": "number", "format": "number"}
    :param Min_Sync_Msg_Per_Packet: {"type": "number", "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "cpu-usage"
        self.DeviceProxy = ""
        self.Max_Query_Msg_Per_Packet = ""
        self.cpu_id = ""
        self.Max_Sync_Msg_Per_Packet = ""
        self.Min_Query_Msg_Per_Packet = ""
        self.Min_Sync_Msg_Per_Packet = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param cpu_usage: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"Max-Query-Msg-Per-Packet": {"type": "number", "format": "number"}, "cpu-id": {"type": "number", "format": "number"}, "Max-Sync-Msg-Per-Packet": {"type": "number", "format": "number"}, "Min-Query-Msg-Per-Packet": {"type": "number", "format": "number"}, "Min-Sync-Msg-Per-Packet": {"type": "number", "format": "number"}, "optional": true}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.cpu_usage = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class StateCpu(A10BaseClass):
    
    """Class Description::
    Operational Status for the object state-cpu.

    Class state-cpu supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/vrrp-a/state-cpu/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "state-cpu"
        self.a10_url="/axapi/v3/vrrp-a/state-cpu/oper"
        self.DeviceProxy = ""
        self.oper = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


