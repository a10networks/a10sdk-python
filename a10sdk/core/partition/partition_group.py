from a10sdk.common.A10BaseClass import A10BaseClass


class MemberList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param member: {"description": "Partition Name", "format": "string", "minLength": 1, "maxLength": 14, "type": "string", "$ref": "/axapi/v3/partition"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "member-list"
        self.DeviceProxy = ""
        self.member = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class PartitionGroup(A10BaseClass):
    
    """Class Description::
    Modify a partition group.

    Class partition-group supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param partition_group_name: {"description": "Partition Group Name", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param member_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"member": {"description": "Partition Name", "format": "string", "minLength": 1, "maxLength": 14, "type": "string", "$ref": "/axapi/v3/partition"}, "optional": true}}]}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/partition-group/{partition_group_name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "partition_group_name"]

        self.b_key = "partition-group"
        self.a10_url="/axapi/v3/partition-group/{partition_group_name}"
        self.DeviceProxy = ""
        self.partition_group_name = ""
        self.member_list = []
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


