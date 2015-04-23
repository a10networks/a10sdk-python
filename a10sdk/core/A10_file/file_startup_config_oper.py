from a10sdk.common.A10BaseClass import A10BaseClass


class FileList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param update_time: {"type": "string", "format": "string"}
    :param Profile_Name: {"type": "string", "format": "string"}
    :param Size: {"type": "number", "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "file-list"
        self.DeviceProxy = ""
        self.update_time = ""
        self.Profile_Name = ""
        self.Size = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param current_startup_config: {"type": "string", "format": "string"}
    :param sec_startup_config: {"type": "string", "format": "string"}
    :param pri_startup_config: {"type": "string", "format": "string"}
    :param file_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "update-time": {"type": "string", "format": "string"}, "Profile-Name": {"type": "string", "format": "string"}, "Size": {"type": "number", "format": "number"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.current_startup_config = ""
        self.sec_startup_config = ""
        self.pri_startup_config = ""
        self.file_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class StartupConfig(A10BaseClass):
    
    """Class Description::
    Operational Status for the object startup-config.

    Class startup-config supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/file/startup-config/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "startup-config"
        self.a10_url="/axapi/v3/file/startup-config/oper"
        self.DeviceProxy = ""
        self.oper = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


