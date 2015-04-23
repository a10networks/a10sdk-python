from a10sdk.common.A10BaseClass import A10BaseClass


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


class Role(A10BaseClass):
    
    """Class Description::
    Role configuration for RBA support.

    Class role supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param name: {"description": "Name for the RBA role", "format": "string", "minLength": 1, "optional": false, "maxLength": 32, "type": "string"}
    :param rule_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"operation": {"enum": ["no-access", "read", "write"], "type": "string", "description": "'no-access': no-access; 'read': read; 'write': write; ", "format": "enum"}, "object": {"minLength": 1, "maxLength": 128, "type": "string", "description": "Lineage of object class for permitted operation", "format": "string"}, "optional": true}}]}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/rba/role/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "role"
        self.a10_url="/axapi/v3/rba/role/{name}"
        self.DeviceProxy = ""
        self.name = ""
        self.rule_list = []
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


