from a10sdk.common.A10BaseClass import A10BaseClass


class ExtcommunityList(A10BaseClass):
    
    """Class Description::
    Configure Extcommunity-list.

    Class extcommunity-list supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param expanded_num_list: {"minItems": 1, "items": {"type": "expanded-num"}, "uniqueItems": true, "array": [{"required": ["ext-list-num"], "properties": {"ext-list-num": {"description": "Extended Community list number (expanded)", "format": "number", "type": "number", "maximum": 199, "minimum": 100, "optional": false}, "rules-list": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "ext-list-value": {"type": "string", "description": "An ordered list as a regular-expression", "format": "string-rlx"}, "ext-list-action": {"enum": ["deny", "permit"], "type": "string", "description": "'deny': Specify community to reject; 'permit': Specify community to accept; ", "format": "enum"}}}]}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/ip/extcommunity-list/expanded-num/{ext-list-num}"}
    :param expanded_list: {"minItems": 1, "items": {"type": "expanded"}, "uniqueItems": true, "array": [{"required": ["expanded"], "properties": {"expanded": {"description": "Add an expanded extcommunity-list entry (Extended Community list name)", "format": "string", "minLength": 1, "optional": false, "maxLength": 128, "type": "string"}, "rules-list": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"expanded-value": {"type": "string", "description": "An ordered list as a regular-expression", "format": "string-rlx"}, "optional": true, "expanded-action": {"enum": ["deny", "permit"], "type": "string", "description": "'deny': Specify community to reject; 'permit': Specify community to accept; ", "format": "enum"}}}]}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/ip/extcommunity-list/expanded/{expanded}"}
    :param standard_num_list: {"minItems": 1, "items": {"type": "standard-num"}, "uniqueItems": true, "array": [{"required": ["std-list-num"], "properties": {"rules-list": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "std-list-action": {"enum": ["deny", "permit"], "type": "string", "description": "'deny': Specify community to reject; 'permit': Specify community to accept; ", "format": "enum"}, "std-list-value": {"type": "string", "description": "rt Route Target extended community in aa:nn or IPaddr:nn format OR soo Site-of-Origin extended community in aa:nn or IPaddr:nn ", "format": "string-rlx"}}}]}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}, "std-list-num": {"description": "Extended Community list number (standard)", "format": "number", "type": "number", "maximum": 99, "minimum": 1, "optional": false}}}], "type": "array", "$ref": "/axapi/v3/ip/extcommunity-list/standard-num/{std-list-num}"}
    :param standard_list: {"minItems": 1, "items": {"type": "standard"}, "uniqueItems": true, "array": [{"required": ["standard"], "properties": {"rules-list": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"standard-action": {"enum": ["deny", "permit"], "type": "string", "description": "'deny': Specify community to reject; 'permit': Specify community to accept; ", "format": "enum"}, "optional": true, "standard-value": {"type": "string", "description": "rt Route Target extended community in aa:nn or IPaddr:nn format OR soo Site-of-Origin extended community in aa:nn or IPaddr:nn ", "format": "string-rlx"}}}]}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}, "standard": {"description": "Add a standard extcommunity-list entry (Extended Community list name)", "format": "string", "minLength": 1, "optional": false, "maxLength": 128, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/ip/extcommunity-list/standard/{standard}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/ip/extcommunity-list`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "extcommunity-list"
        self.a10_url="/axapi/v3/ip/extcommunity-list"
        self.DeviceProxy = ""
        self.expanded_num_list = []
        self.expanded_list = []
        self.standard_num_list = []
        self.standard_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


