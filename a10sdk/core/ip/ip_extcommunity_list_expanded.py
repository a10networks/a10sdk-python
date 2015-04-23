from a10sdk.common.A10BaseClass import A10BaseClass


class RulesList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param expanded_value: {"type": "string", "description": "An ordered list as a regular-expression", "format": "string-rlx"}
    :param expanded_action: {"enum": ["deny", "permit"], "type": "string", "description": "'deny': Specify community to reject; 'permit': Specify community to accept; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "rules-list"
        self.DeviceProxy = ""
        self.expanded_value = ""
        self.expanded_action = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Expanded(A10BaseClass):
    
    """Class Description::
    Configure Extended Community-list.

    Class expanded supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param expanded: {"description": "Add an expanded extcommunity-list entry (Extended Community list name)", "format": "string", "minLength": 1, "optional": false, "maxLength": 128, "type": "string"}
    :param rules_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"expanded-value": {"type": "string", "description": "An ordered list as a regular-expression", "format": "string-rlx"}, "optional": true, "expanded-action": {"enum": ["deny", "permit"], "type": "string", "description": "'deny': Specify community to reject; 'permit': Specify community to accept; ", "format": "enum"}}}]}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/ip/extcommunity-list/expanded/{expanded}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "expanded"]

        self.b_key = "expanded"
        self.a10_url="/axapi/v3/ip/extcommunity-list/expanded/{expanded}"
        self.DeviceProxy = ""
        self.expanded = ""
        self.rules_list = []
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


