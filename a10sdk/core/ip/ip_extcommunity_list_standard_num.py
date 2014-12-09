from a10sdk.common.A10BaseClass import A10BaseClass


class RulesList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param std_list_action: {"enum": ["deny", "permit"], "type": "string", "description": "'deny': Specify community to reject; 'permit': Specify community to accept; ", "format": "enum"}
    :param std_list_value: {"type": "string", "description": "rt Route Target extended community in aa:nn or IPaddr:nn format OR soo Site-of-Origin extended community in aa:nn or IPaddr:nn ", "format": "string-rlx"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "rules-list"
        self.DeviceProxy = ""
        self.std_list_action = ""
        self.std_list_value = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class StandardNum(A10BaseClass):
    
    """Class Description::
    Configure Standard number Community-list.

    Class standard-num supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param rules_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "std-list-action": {"enum": ["deny", "permit"], "type": "string", "description": "'deny': Specify community to reject; 'permit': Specify community to accept; ", "format": "enum"}, "std-list-value": {"type": "string", "description": "rt Route Target extended community in aa:nn or IPaddr:nn format OR soo Site-of-Origin extended community in aa:nn or IPaddr:nn ", "format": "string-rlx"}}}]}
    :param std_list_num: {"description": "Extended Community list number (standard)", "format": "number", "type": "number", "maximum": 99, "minimum": 1, "optional": false}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/ip/extcommunity-list/standard-num/{std_list_num}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "std_list_num"]

        self.b_key = "standard-num"
        self.a10_url="/axapi/v3/ip/extcommunity-list/standard-num/{std_list_num}"
        self.DeviceProxy = ""
        self.rules_list = []
        self.std_list_num = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


