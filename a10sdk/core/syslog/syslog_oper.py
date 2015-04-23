from a10sdk.common.A10BaseClass import A10BaseClass


class SystemLog(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param log_data_search: {"type": "string", "format": "string"}
    :param log_data: {"type": "string", "format": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "system-log"
        self.DeviceProxy = ""
        self.log_data_search = ""
        self.log_data = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param system_log: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"log-data-search": {"type": "string", "format": "string"}, "optional": true, "log-data": {"type": "string", "format": "string"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.system_log = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Syslog(A10BaseClass):
    
    """Class Description::
    Operational Status for the object syslog.

    Class syslog supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/syslog/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "syslog"
        self.a10_url="/axapi/v3/syslog/oper"
        self.DeviceProxy = ""
        self.oper = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


