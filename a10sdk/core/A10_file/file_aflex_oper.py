from a10sdk.common.A10BaseClass import A10BaseClass


class VportList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param vserver: {"type": "string", "format": "string"}
    :param port: {"type": "number", "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "vport-list"
        self.DeviceProxy = ""
        self.vserver = ""
        self.port = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Events(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param failures: {"type": "number", "format": "number"}
    :param aborts: {"type": "number", "format": "number"}
    :param total_executions: {"type": "number", "format": "number"}
    :param event_type: {"type": "string", "format": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "events"
        self.DeviceProxy = ""
        self.failures = ""
        self.aborts = ""
        self.total_executions = ""
        self.event_type = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class FileList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param syntax: {"type": "string", "format": "string"}
    :param vport_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"vserver": {"type": "string", "format": "string"}, "optional": true, "port": {"type": "number", "format": "number"}}}]}
    :param file: {"type": "string", "format": "string"}
    :param vport: {"type": "string", "format": "string"}
    :param events: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"failures": {"type": "number", "format": "number"}, "aborts": {"type": "number", "format": "number"}, "optional": true, "total-executions": {"type": "number", "format": "number"}, "event-type": {"type": "string", "format": "string"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "file-list"
        self.DeviceProxy = ""
        self.syntax = ""
        self.vport_list = []
        self.A10WW_file = ""
        self.vport = ""
        self.events = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param file_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"syntax": {"type": "string", "format": "string"}, "vport-list": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"vserver": {"type": "string", "format": "string"}, "optional": true, "port": {"type": "number", "format": "number"}}}]}, "file": {"type": "string", "format": "string"}, "vport": {"type": "string", "format": "string"}, "optional": true, "events": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"failures": {"type": "number", "format": "number"}, "aborts": {"type": "number", "format": "number"}, "optional": true, "total-executions": {"type": "number", "format": "number"}, "event-type": {"type": "string", "format": "string"}}}]}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.file_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Aflex(A10BaseClass):
    
    """Class Description::
    Operational Status for the object aflex.

    Class aflex supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/file/aflex/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "aflex"
        self.a10_url="/axapi/v3/file/aflex/oper"
        self.DeviceProxy = ""
        self.oper = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


