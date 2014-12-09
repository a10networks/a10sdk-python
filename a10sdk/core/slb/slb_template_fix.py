from a10sdk.common.A10BaseClass import A10BaseClass


class TagSwitching(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param service_group: {"description": "Create a Service Group comprising Servers (Service Group Name)", "format": "string-rlx", "minLength": 1, "maxLength": 127, "type": "string", "$ref": "/axapi/v3/slb/service-group"}
    :param equals: {"minLength": 1, "maxLength": 63, "type": "string", "description": "Equals (Tag String)", "format": "string"}
    :param switching_type: {"enum": ["sender-comp-id", "target-comp-id"], "type": "string", "description": "'sender-comp-id': Select service group based on SenderCompID; 'target-comp-id': Select service group based on TargetCompID; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "tag-switching"
        self.DeviceProxy = ""
        self.service_group = ""
        self.equals = ""
        self.switching_type = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Fix(A10BaseClass):
    
    """Class Description::
    FIX template.

    Class fix supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param name: {"description": "FIX Template Name", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param tag_switching: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"service-group": {"description": "Create a Service Group comprising Servers (Service Group Name)", "format": "string-rlx", "minLength": 1, "maxLength": 127, "type": "string", "$ref": "/axapi/v3/slb/service-group"}, "optional": true, "equals": {"minLength": 1, "maxLength": 63, "type": "string", "description": "Equals (Tag String)", "format": "string"}, "switching-type": {"enum": ["sender-comp-id", "target-comp-id"], "type": "string", "description": "'sender-comp-id': Select service group based on SenderCompID; 'target-comp-id': Select service group based on TargetCompID; ", "format": "enum"}}}]}
    :param insert_client_ip: {"default": 0, "optional": true, "type": "number", "description": "Insert client ip to tag 11447", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/template/fix/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "fix"
        self.a10_url="/axapi/v3/slb/template/fix/{name}"
        self.DeviceProxy = ""
        self.name = ""
        self.tag_switching = []
        self.insert_client_ip = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


