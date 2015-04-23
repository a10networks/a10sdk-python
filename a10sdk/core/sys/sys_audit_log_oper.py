from a10sdk.common.A10BaseClass import A10BaseClass


class SystemAuditLog(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param log_audit_data: {"type": "string", "format": "string"}
    :param log_audit_search: {"type": "string", "format": "string"}
    :param partitions: {"type": "string", "format": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "system-audit-log"
        self.DeviceProxy = ""
        self.log_audit_data = ""
        self.log_audit_search = ""
        self.partitions = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param system_audit_log: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"log-audit-data": {"type": "string", "format": "string"}, "optional": true, "log-audit-search": {"type": "string", "format": "string"}, "partitions": {"type": "string", "format": "string"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.system_audit_log = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class SysAuditLog(A10BaseClass):
    
    """Class Description::
    Operational Status for the object sys-audit-log.

    Class sys-audit-log supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/sys-audit-log/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "sys-audit-log"
        self.a10_url="/axapi/v3/sys-audit-log/oper"
        self.DeviceProxy = ""
        self.oper = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


