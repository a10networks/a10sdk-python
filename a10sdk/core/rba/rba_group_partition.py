from a10sdk.common.A10BaseClass import A10BaseClass


class RoleList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param role: {"description": "Role in a given partition", "format": "string", "minLength": 1, "maxLength": 128, "type": "string", "$ref": "/axapi/v3/rba/role"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "role-list"
        self.DeviceProxy = ""
        self.role = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class RuleList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param operation: {"enum": ["no-access", "read", "write"], "type": "string", "description": "'no-access': no-access; 'read': read; 'write': write; ", "format": "enum"}
    :param object: {"minLength": 1, "maxLength": 128, "type": "string", "description": "Lineage of object class for permitted operation", "format": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "rule-list"
        self.DeviceProxy = ""
        self.operation = ""
        self.A10WW_object = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Partition(A10BaseClass):
    
    """Class Description::
    RBA configuration for the access privilege of a group within one partition.

    Class partition supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param partition_name: {"description": "partition name", "format": "string", "minLength": 1, "optional": false, "maxLength": 14, "type": "string"}
    :param role_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "role": {"description": "Role in a given partition", "format": "string", "minLength": 1, "maxLength": 128, "type": "string", "$ref": "/axapi/v3/rba/role"}}}]}
    :param rule_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"operation": {"enum": ["no-access", "read", "write"], "type": "string", "description": "'no-access': no-access; 'read': read; 'write': write; ", "format": "enum"}, "object": {"minLength": 1, "maxLength": 128, "type": "string", "description": "Lineage of object class for permitted operation", "format": "string"}, "optional": true}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/rba/group/{name}/partition/{partition_name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "partition_name"]

        self.b_key = "partition"
        self.a10_url="/axapi/v3/rba/group/{name}/partition/{partition_name}"
        self.DeviceProxy = ""
        self.partition_name = ""
        self.role_list = []
        self.rule_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


