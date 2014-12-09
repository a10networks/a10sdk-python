from a10sdk.common.A10BaseClass import A10BaseClass


class PartitionList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param status: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param partition_id: {"type": "number", "format": "number"}
    :param app_Type: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param partition_name: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param admin_Count: {"type": "number", "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "partition-list"
        self.DeviceProxy = ""
        self.status = ""
        self.partition_id = ""
        self.app_Type = ""
        self.partition_name = ""
        self.admin_Count = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param partition_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"status": {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}, "partition-id": {"type": "number", "format": "number"}, "app-Type": {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}, "partition-name": {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}, "admin-Count": {"type": "number", "format": "number"}, "optional": true}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.partition_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class PartitionAll(A10BaseClass):
    
    """Class Description::
    Operational Status for the object partition-all.

    Class partition-all supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/partition-all/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "partition-all"
        self.a10_url="/axapi/v3/partition-all/oper"
        self.DeviceProxy = ""
        self.oper = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


