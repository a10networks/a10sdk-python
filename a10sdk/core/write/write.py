from a10sdk.common.A10BaseClass import A10BaseClass


class Force(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param all_partitions: {"type": "number", "description": "All partition configurations", "format": "flag"}
    :param name: {"description": "Local Configuration Profile Name", "format": "string", "minLength": "1", "optional": false, "maxLength": "31", "type": "string"}
    :param primary: {"type": "number", "description": "Write to default Primary Configuration", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "force"
        self.DeviceProxy = ""
        self.all_partitions = ""
        self.name = ""
        self.primary = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Memory(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param all_partitions: {"type": "number", "description": "All partition configurations", "format": "flag"}
    :param name: {"description": "Local Configuration Profile Name", "format": "string", "minLength": "1", "optional": false, "maxLength": "31", "type": "string"}
    :param primary: {"type": "number", "description": "Write to default Primary Configuration", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "memory"
        self.DeviceProxy = ""
        self.all_partitions = ""
        self.name = ""
        self.primary = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Write(A10BaseClass):
    
    """Class Description::
    Write Configuration.

    Class write supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/write`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "write"
        self.a10_url="/axapi/v3/write"
        self.DeviceProxy = ""
        self.terminal = {}
        self.force = {}
        self.memory = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


