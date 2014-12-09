from a10sdk.common.A10BaseClass import A10BaseClass


class Authorization(A10BaseClass):
    
    """Class Description::
    Configure authorization related settings.

    Class authorization supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param policy_list: {"minItems": 1, "items": {"type": "policy"}, "uniqueItems": true, "array": [{"required": ["name"], "properties": {"attribute-list": {"minItems": 1, "items": {"type": "attribute"}, "uniqueItems": true, "array": [{"required": ["attr-num"], "properties": {"attribute-name": {"description": "Specify attribute name", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "not": "A10-AX-AUTH-URI", "type": "string"}, "integer-type": {"default": 0, "not": "string-type", "type": "number", "optional": true, "format": "flag"}, "custom-attr-type": {"default": 0, "optional": true, "type": "number", "description": "Specify attribute type", "format": "flag"}, "attr-type": {"default": 0, "optional": true, "type": "number", "description": "Specify attribute type", "format": "flag"}, "attr-str": {"optional": true, "enum": ["match", "sub-string"], "type": "string", "description": "'match': Operation type is match; 'sub-string': Operation type is sub-string; ", "format": "enum"}, "a10-dynamic-defined": {"default": 0, "optional": true, "type": "number", "description": "The value of this attribute will depend on AX configuration instead of user configuration", "format": "flag"}, "attr-str-val": {"description": "Set attribute value", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 31, "type": "string"}, "string-type": {"default": 0, "not": "integer-type", "type": "number", "optional": true, "format": "flag"}, "attr-num": {"description": "Set attribute ID for authorization policy", "format": "number", "type": "number", "maximum": 32, "minimum": 1, "optional": false}, "A10-AX-AUTH-URI": {"description": "Custom-defined attribute", "format": "flag", "default": 0, "optional": true, "not": "attribute-name", "type": "number"}, "attr-int": {"optional": true, "enum": ["equal", "not-equal", "less-than", "more-than", "less-than-equal-to", "more-than-equal-to"], "type": "string", "description": "'equal': Operation type is equal; 'not-equal': Operation type is not equal; 'less-than': Operation type is less-than; 'more-than': Operation type is more-than; 'less-than-equal-to': Operation type is less-than-equal-to; 'more-than-equal-to': Operation type is more-thatn-equal-to; ", "format": "enum"}, "custom-attr-str": {"optional": true, "enum": ["match", "sub-string"], "type": "string", "description": "'match': Operation type is match; 'sub-string': Operation type is sub-string; ", "format": "enum"}, "attr-int-val": {"optional": true, "type": "number", "description": "Set attribute value", "format": "number"}}}], "type": "array", "$ref": "/axapi/v3/aam/authorization/policy/{name}/attribute/{attr-num}"}, "name": {"description": "Specify authorization policy name", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}, "attribute-rule": {"optional": true, "type": "string", "description": "Define attribute rule for authorization policy", "format": "string-rlx"}}}], "type": "array", "$ref": "/axapi/v3/aam/authorization/policy/{name}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/aam/authorization`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "authorization"
        self.a10_url="/axapi/v3/aam/authorization"
        self.DeviceProxy = ""
        self.policy_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


