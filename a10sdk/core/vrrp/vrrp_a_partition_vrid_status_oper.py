from a10sdk.common.A10BaseClass import A10BaseClass


class AllPartitionList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param active_priority: {"type": "number", "format": "number"}
    :param vrid: {"type": "number", "format": "number"}
    :param local_device_ID: {"type": "number", "format": "number"}
    :param partition_name: {"type": "string", "format": "string"}
    :param active_device_id: {"type": "number", "format": "number"}
    :param active_weight: {"type": "number", "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "all-partition-list"
        self.DeviceProxy = ""
        self.active_priority = ""
        self.vrid = ""
        self.local_device_ID = ""
        self.partition_name = ""
        self.active_device_id = ""
        self.active_weight = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param all_partition_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"active_priority": {"type": "number", "format": "number"}, "vrid": {"type": "number", "format": "number"}, "local_device_ID": {"type": "number", "format": "number"}, "partition-name": {"type": "string", "format": "string"}, "active_device_id": {"type": "number", "format": "number"}, "active_weight": {"type": "number", "format": "number"}, "optional": true}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.all_partition_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class PartitionVridStatus(A10BaseClass):
    
    """Class Description::
    Operational Status for the object partition-vrid-status.

    Class partition-vrid-status supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/vrrp-a/partition-vrid-status/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "partition-vrid-status"
        self.a10_url="/axapi/v3/vrrp-a/partition-vrid-status/oper"
        self.DeviceProxy = ""
        self.oper = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


