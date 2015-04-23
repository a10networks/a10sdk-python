from a10sdk.common.A10BaseClass import A10BaseClass


class FileList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param file_name: {"type": "string", "format": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "file-list"
        self.DeviceProxy = ""
        self.file_name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param file_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"file_name": {"type": "string", "format": "string"}, "optional": true}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.file_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class License(A10BaseClass):
    
    """Class Description::
    Operational Status for the object license.

    Class license supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/file/license/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "license"
        self.a10_url="/axapi/v3/file/license/oper"
        self.DeviceProxy = ""
        self.oper = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


