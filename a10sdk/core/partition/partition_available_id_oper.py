from a10sdk.common.A10BaseClass import A10BaseClass


class RangeList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param start: {"type": "string", "format": "string"}
    :param end: {"type": "string", "format": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "range-list"
        self.DeviceProxy = ""
        self.start = ""
        self.end = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param range_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"start": {"type": "string", "format": "string"}, "end": {"type": "string", "format": "string"}, "optional": true}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.range_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class PartitionAvailableId(A10BaseClass):
    
    """Class Description::
    Operational Status for the object partition-available-id.

    Class partition-available-id supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/partition-available-id/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "partition-available-id"
        self.a10_url="/axapi/v3/partition-available-id/oper"
        self.DeviceProxy = ""
        self.oper = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


