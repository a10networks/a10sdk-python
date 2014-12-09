from a10sdk.common.A10BaseClass import A10BaseClass


class RulesList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ext_list_value: {"type": "string", "description": "An ordered list as a regular-expression", "format": "string-rlx"}
    :param ext_list_action: {"enum": ["deny", "permit"], "type": "string", "description": "'deny': Specify community to reject; 'permit': Specify community to accept; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "rules-list"
        self.DeviceProxy = ""
        self.ext_list_value = ""
        self.ext_list_action = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class ExpandedNum(A10BaseClass):
    
    """Class Description::
    Configure Expanded number Community-list.

    Class expanded-num supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param ext_list_num: {"description": "Extended Community list number (expanded)", "format": "number", "type": "number", "maximum": 199, "minimum": 100, "optional": false}
    :param rules_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "ext-list-value": {"type": "string", "description": "An ordered list as a regular-expression", "format": "string-rlx"}, "ext-list-action": {"enum": ["deny", "permit"], "type": "string", "description": "'deny': Specify community to reject; 'permit': Specify community to accept; ", "format": "enum"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/ip/extcommunity-list/expanded-num/{ext_list_num}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "ext_list_num"]

        self.b_key = "expanded-num"
        self.a10_url="/axapi/v3/ip/extcommunity-list/expanded-num/{ext_list_num}"
        self.DeviceProxy = ""
        self.ext_list_num = ""
        self.rules_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


