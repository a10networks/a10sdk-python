from a10sdk.common.A10BaseClass import A10BaseClass


class DeleteCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param store_name_del: {"minLength": 1, "maxLength": 31, "type": "string", "description": "profile name for deleting", "format": "string"}
    :param delete: {"default": 0, "type": "number", "description": "Delete store", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "delete-cfg"
        self.DeviceProxy = ""
        self.store_name_del = ""
        self.delete = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class CreatCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param create: {"default": 0, "type": "number", "description": "Create store", "format": "flag"}
    :param remote_file: {"type": "string", "description": "profile name for remote url", "format": "url"}
    :param store_name: {"minLength": 1, "maxLength": 31, "type": "string", "description": "profile name to store remote url", "format": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "creat-cfg"
        self.DeviceProxy = ""
        self.create = ""
        self.remote_file = ""
        self.store_name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Store(A10BaseClass):
    
    """    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Save backup store information.

    Class store supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/backup/store`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "store"
        self.a10_url="/axapi/v3/backup/store"
        self.DeviceProxy = ""
        self.delete_cfg = {}
        self.creat_cfg = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


