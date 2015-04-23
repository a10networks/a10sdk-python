from a10sdk.common.A10BaseClass import A10BaseClass


class UserList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param user: {"minLength": 1, "maxLength": 32, "type": "string", "description": "Users in the group", "format": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "user-list"
        self.DeviceProxy = ""
        self.user = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Group(A10BaseClass):
    
    """Class Description::
    RBA configuration for a group.

    Class group supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param partition_list: {"minItems": 1, "items": {"type": "partition"}, "uniqueItems": true, "array": [{"required": ["partition-name"], "properties": {"partition-name": {"description": "partition name", "format": "string", "minLength": 1, "optional": false, "maxLength": 14, "type": "string"}, "role-list": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "role": {"description": "Role in a given partition", "format": "string", "minLength": 1, "maxLength": 32, "type": "string", "$ref": "/axapi/v3/rba/role"}}}]}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}, "rule-list": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"operation": {"enum": ["no-access", "read", "write"], "type": "string", "description": "'no-access': no-access; 'read': read; 'write': write; ", "format": "enum"}, "object": {"minLength": 1, "maxLength": 128, "type": "string", "description": "Lineage of object class for permitted operation", "format": "string"}, "optional": true}}]}}}], "type": "array", "$ref": "/axapi/v3/rba/group/{name}/partition/{partition-name}"}
    :param user_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "user": {"minLength": 1, "maxLength": 32, "type": "string", "description": "Users in the group", "format": "string"}}}]}
    :param name: {"description": "Name of a RBA group", "format": "string", "minLength": 1, "optional": false, "maxLength": 32, "type": "string"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/rba/group/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "group"
        self.a10_url="/axapi/v3/rba/group/{name}"
        self.DeviceProxy = ""
        self.partition_list = []
        self.user_list = []
        self.name = ""
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


