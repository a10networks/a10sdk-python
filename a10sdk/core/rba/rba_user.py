from a10sdk.common.A10BaseClass import A10BaseClass


class User(A10BaseClass):
    
    """Class Description::
    RBA configuration for a user.

    Class user supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param partition_list: {"minItems": 1, "items": {"type": "partition"}, "uniqueItems": true, "array": [{"required": ["partition-name"], "properties": {"partition-name": {"description": "partition name", "format": "string", "minLength": 1, "optional": false, "maxLength": 14, "type": "string"}, "role-list": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "role": {"description": "Role in a given partition", "format": "string", "minLength": 1, "maxLength": 128, "type": "string", "$ref": "/axapi/v3/rba/role"}}}]}, "rule-list": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"operation": {"enum": ["no-access", "read", "write"], "type": "string", "description": "'no-access': no-access; 'read': read; 'write': write; ", "format": "enum"}, "object": {"minLength": 1, "maxLength": 128, "type": "string", "description": "Lineage of object class for permitted operation", "format": "string"}, "optional": true}}]}}}], "type": "array", "$ref": "/axapi/v3/rba/user/{name}/partition/{partition-name}"}
    :param name: {"description": "Name of a user account", "format": "string", "minLength": 1, "optional": false, "maxLength": 32, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/rba/user/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "user"
        self.a10_url="/axapi/v3/rba/user/{name}"
        self.DeviceProxy = ""
        self.partition_list = []
        self.name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


