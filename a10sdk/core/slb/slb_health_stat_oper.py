from a10sdk.common.A10BaseClass import A10BaseClass


class HealthCheckList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param status: {"type": "string", "format": "string"}
    :param retries: {"type": "number", "format": "number"}
    :param down_state: {"type": "number", "format": "number"}
    :param up_retries: {"type": "number", "format": "number"}
    :param down_cause: {"type": "number", "format": "number"}
    :param partition_id: {"type": "number", "format": "number"}
    :param up_cause: {"type": "number", "format": "number"}
    :param ip_address: {"type": "string", "format": "string"}
    :param total_retry: {"type": "number", "format": "number"}
    :param health_monitor: {"type": "string", "format": "string"}
    :param port: {"type": "string", "format": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "health-check-list"
        self.DeviceProxy = ""
        self.status = ""
        self.retries = ""
        self.down_state = ""
        self.up_retries = ""
        self.down_cause = ""
        self.partition_id = ""
        self.up_cause = ""
        self.ip_address = ""
        self.total_retry = ""
        self.health_monitor = ""
        self.port = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param health_check_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"status": {"type": "string", "format": "string"}, "retries": {"type": "number", "format": "number"}, "down-state": {"type": "number", "format": "number"}, "up-retries": {"type": "number", "format": "number"}, "down-cause": {"type": "number", "format": "number"}, "partition-id": {"type": "number", "format": "number"}, "up-cause": {"type": "number", "format": "number"}, "ip-address": {"type": "string", "format": "string"}, "total-retry": {"type": "number", "format": "number"}, "health-monitor": {"type": "string", "format": "string"}, "optional": true, "port": {"type": "string", "format": "string"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.health_check_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class HealthStat(A10BaseClass):
    
    """Class Description::
    Operational Status for the object health-stat.

    Class health-stat supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/health-stat/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "health-stat"
        self.a10_url="/axapi/v3/slb/health-stat/oper"
        self.DeviceProxy = ""
        self.oper = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


