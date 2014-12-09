from a10sdk.common.A10BaseClass import A10BaseClass


class RulesList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param standard_action: {"enum": ["deny", "permit"], "type": "string", "description": "'deny': Specify community to reject; 'permit': Specify community to accept; ", "format": "enum"}
    :param standard_comm_value: {"type": "string", "description": "community value in the format 1-4294967295|AA:NN|internet|local-AS|no-advertise|no-export", "format": "string-rlx"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "rules-list"
        self.DeviceProxy = ""
        self.standard_action = ""
        self.standard_comm_value = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Standard(A10BaseClass):
    
    """Class Description::
    Configure Standard Community-list.

    Class standard supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param rules_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"standard-action": {"enum": ["deny", "permit"], "type": "string", "description": "'deny': Specify community to reject; 'permit': Specify community to accept; ", "format": "enum"}, "optional": true, "standard-comm-value": {"type": "string", "description": "community value in the format 1-4294967295|AA:NN|internet|local-AS|no-advertise|no-export", "format": "string-rlx"}}}]}
    :param standard: {"description": "Add a standard community-list entry (Community list name)", "format": "string", "minLength": 1, "optional": false, "maxLength": 128, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/ip/community-list/standard/{standard}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "standard"]

        self.b_key = "standard"
        self.a10_url="/axapi/v3/ip/community-list/standard/{standard}"
        self.DeviceProxy = ""
        self.rules_list = []
        self.standard = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


