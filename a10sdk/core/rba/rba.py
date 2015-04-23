from a10sdk.common.A10BaseClass import A10BaseClass


class Rba(A10BaseClass):
    
    """Class Description::
    Role Based Access configuration.

    Class rba supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param action: {"description": "'enable': Enable RBA; 'disable': Disable RBA; ", "format": "enum", "default": "disable", "type": "string", "enum": ["enable", "disable"], "optional": true}
    :param group_list: {"minItems": 1, "items": {"type": "group"}, "uniqueItems": true, "array": [{"required": ["name"], "properties": {"partition-list": {"minItems": 1, "items": {"type": "partition"}, "uniqueItems": true, "array": [{"required": ["partition-name"], "properties": {"partition-name": {"description": "partition name", "format": "string", "minLength": 1, "optional": false, "maxLength": 14, "type": "string"}, "role-list": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "role": {"description": "Role in a given partition", "format": "string", "minLength": 1, "maxLength": 32, "type": "string", "$ref": "/axapi/v3/rba/role"}}}]}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}, "rule-list": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"operation": {"enum": ["no-access", "read", "write"], "type": "string", "description": "'no-access': no-access; 'read': read; 'write': write; ", "format": "enum"}, "object": {"minLength": 1, "maxLength": 128, "type": "string", "description": "Lineage of object class for permitted operation", "format": "string"}, "optional": true}}]}}}], "type": "array", "$ref": "/axapi/v3/rba/group/{name}/partition/{partition-name}"}, "user-list": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "user": {"minLength": 1, "maxLength": 32, "type": "string", "description": "Users in the group", "format": "string"}}}]}, "name": {"description": "Name of a RBA group", "format": "string", "minLength": 1, "optional": false, "maxLength": 32, "type": "string"}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/rba/group/{name}"}
    :param user_list: {"minItems": 1, "items": {"type": "user"}, "uniqueItems": true, "array": [{"required": ["name"], "properties": {"partition-list": {"minItems": 1, "items": {"type": "partition"}, "uniqueItems": true, "array": [{"required": ["partition-name"], "properties": {"partition-name": {"description": "partition name", "format": "string", "minLength": 1, "optional": false, "maxLength": 14, "type": "string", "$ref": "/axapi/v3/partition"}, "role-list": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "role": {"description": "Role in a given partition", "format": "string", "minLength": 1, "maxLength": 32, "type": "string", "$ref": "/axapi/v3/rba/role"}}}]}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}, "rule-list": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"operation": {"enum": ["no-access", "read", "write"], "type": "string", "description": "'no-access': no-access; 'read': read; 'write': write; ", "format": "enum"}, "object": {"minLength": 1, "maxLength": 128, "type": "string", "description": "Lineage of object class for permitted operation", "format": "string"}, "optional": true}}]}}}], "type": "array", "$ref": "/axapi/v3/rba/user/{name}/partition/{partition-name}"}, "name": {"description": "Name of a user account", "format": "string", "minLength": 1, "optional": false, "maxLength": 32, "type": "string"}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/rba/user/{name}"}
    :param role_list: {"minItems": 1, "items": {"type": "role"}, "uniqueItems": true, "array": [{"required": ["name"], "properties": {"name": {"description": "Name for the RBA role", "format": "string", "minLength": 1, "optional": false, "maxLength": 32, "type": "string"}, "rule-list": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"operation": {"enum": ["no-access", "read", "write"], "type": "string", "description": "'no-access': no-access; 'read': read; 'write': write; ", "format": "enum"}, "object": {"minLength": 1, "maxLength": 128, "type": "string", "description": "Lineage of object class for permitted operation", "format": "string"}, "optional": true}}]}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/rba/role/{name}"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/rba`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "rba"
        self.a10_url="/axapi/v3/rba"
        self.DeviceProxy = ""
        self.action = ""
        self.group_list = []
        self.user_list = []
        self.role_list = []
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


