from a10sdk.common.A10BaseClass import A10BaseClass


class EntryList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param active: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param name: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param modified: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "entry-list"
        self.DeviceProxy = ""
        self.active = ""
        self.name = ""
        self.modified = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param entry_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"active": {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}, "optional": true, "name": {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}, "modified": {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.entry_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class BindingTableFilesStatus(A10BaseClass):
    
    """Class Description::
    Operational Status for the object binding-table-files-status.

    Class binding-table-files-status supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/lw-4o6/binding-table-files-status/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "binding-table-files-status"
        self.a10_url="/axapi/v3/cgnv6/lw-4o6/binding-table-files-status/oper"
        self.DeviceProxy = ""
        self.oper = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


