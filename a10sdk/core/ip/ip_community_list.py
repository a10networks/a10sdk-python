from a10sdk.common.A10BaseClass import A10BaseClass


class CommunityList(A10BaseClass):
    
    """Class Description::
    Configure Community-list.

    Class community-list supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param expanded_num_list: {"minItems": 1, "items": {"type": "expanded-num"}, "uniqueItems": true, "array": [{"required": ["ext-list-num"], "properties": {"ext-list-num": {"description": "Community list number (expanded)", "format": "number", "type": "number", "maximum": 199, "minimum": 100, "optional": false}, "rules-list": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "ext-list-value": {"type": "string", "description": "An ordered list as a regular-expression", "format": "string-rlx"}, "ext-list-action": {"enum": ["deny", "permit"], "type": "string", "description": "'deny': Specify community to reject; 'permit': Specify community to accept; ", "format": "enum"}}}]}}}], "type": "array", "$ref": "/axapi/v3/ip/community-list/expanded-num/{ext-list-num}"}
    :param expanded_list: {"minItems": 1, "items": {"type": "expanded"}, "uniqueItems": true, "array": [{"required": ["expanded"], "properties": {"expanded": {"description": "Add an expanded community-list entry (Community list name)", "format": "string", "minLength": 1, "optional": false, "maxLength": 128, "type": "string"}, "rules-list": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"expanded-value": {"type": "string", "description": "An ordered list as a regular-expression", "format": "string-rlx"}, "optional": true, "expanded-action": {"enum": ["deny", "permit"], "type": "string", "description": "'deny': Specify community to reject; 'permit': Specify community to accept; ", "format": "enum"}}}]}}}], "type": "array", "$ref": "/axapi/v3/ip/community-list/expanded/{expanded}"}
    :param standard_num_list: {"minItems": 1, "items": {"type": "standard-num"}, "uniqueItems": true, "array": [{"required": ["std-list-num"], "properties": {"rules-list": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "std-list-action": {"enum": ["deny", "permit"], "type": "string", "description": "'deny': Specify community to reject; 'permit': Specify community to accept; ", "format": "enum"}, "std-list-comm-value": {"type": "string", "description": "community value in the format 1-4294967295|AA:NN|internet|local-AS|no-advertise|no-export", "format": "string-rlx"}}}]}, "std-list-num": {"description": "Community list number (standard)", "format": "number", "type": "number", "maximum": 99, "minimum": 1, "optional": false}}}], "type": "array", "$ref": "/axapi/v3/ip/community-list/standard-num/{std-list-num}"}
    :param standard_list: {"minItems": 1, "items": {"type": "standard"}, "uniqueItems": true, "array": [{"required": ["standard"], "properties": {"rules-list": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"standard-action": {"enum": ["deny", "permit"], "type": "string", "description": "'deny': Specify community to reject; 'permit': Specify community to accept; ", "format": "enum"}, "optional": true, "standard-comm-value": {"type": "string", "description": "community value in the format 1-4294967295|AA:NN|internet|local-AS|no-advertise|no-export", "format": "string-rlx"}}}]}, "standard": {"description": "Add a standard community-list entry (Community list name)", "format": "string", "minLength": 1, "optional": false, "maxLength": 128, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/ip/community-list/standard/{standard}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/ip/community-list`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "community-list"
        self.a10_url="/axapi/v3/ip/community-list"
        self.DeviceProxy = ""
        self.expanded_num_list = []
        self.expanded_list = []
        self.standard_num_list = []
        self.standard_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


