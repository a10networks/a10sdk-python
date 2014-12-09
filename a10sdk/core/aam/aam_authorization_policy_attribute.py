from a10sdk.common.A10BaseClass import A10BaseClass


class Attribute(A10BaseClass):
    
    """Class Description::
    Authorization-policy attribute configuration.

    Class attribute supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param attribute_name: {"description": "Specify attribute name", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "not": "A10-AX-AUTH-URI", "type": "string"}
    :param integer_type: {"default": 0, "not": "string-type", "type": "number", "optional": true, "format": "flag"}
    :param custom_attr_type: {"default": 0, "optional": true, "type": "number", "description": "Specify attribute type", "format": "flag"}
    :param attr_type: {"default": 0, "optional": true, "type": "number", "description": "Specify attribute type", "format": "flag"}
    :param attr_str: {"optional": true, "enum": ["match", "sub-string"], "type": "string", "description": "'match': Operation type is match; 'sub-string': Operation type is sub-string; ", "format": "enum"}
    :param a10_dynamic_defined: {"default": 0, "optional": true, "type": "number", "description": "The value of this attribute will depend on AX configuration instead of user configuration", "format": "flag"}
    :param attr_str_val: {"description": "Set attribute value", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 31, "type": "string"}
    :param string_type: {"default": 0, "not": "integer-type", "type": "number", "optional": true, "format": "flag"}
    :param attr_num: {"description": "Set attribute ID for authorization policy", "format": "number", "type": "number", "maximum": 32, "minimum": 1, "optional": false}
    :param A10_AX_AUTH_URI: {"description": "Custom-defined attribute", "format": "flag", "default": 0, "optional": true, "not": "attribute-name", "type": "number"}
    :param attr_int: {"optional": true, "enum": ["equal", "not-equal", "less-than", "more-than", "less-than-equal-to", "more-than-equal-to"], "type": "string", "description": "'equal': Operation type is equal; 'not-equal': Operation type is not equal; 'less-than': Operation type is less-than; 'more-than': Operation type is more-than; 'less-than-equal-to': Operation type is less-than-equal-to; 'more-than-equal-to': Operation type is more-thatn-equal-to; ", "format": "enum"}
    :param custom_attr_str: {"optional": true, "enum": ["match", "sub-string"], "type": "string", "description": "'match': Operation type is match; 'sub-string': Operation type is sub-string; ", "format": "enum"}
    :param attr_int_val: {"optional": true, "type": "number", "description": "Set attribute value", "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/aam/authorization/policy/{name}/attribute/{attr_num}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "attr_num"]

        self.b_key = "attribute"
        self.a10_url="/axapi/v3/aam/authorization/policy/{name}/attribute/{attr_num}"
        self.DeviceProxy = ""
        self.attribute_name = ""
        self.integer_type = ""
        self.custom_attr_type = ""
        self.attr_type = ""
        self.attr_str = ""
        self.a10_dynamic_defined = ""
        self.attr_str_val = ""
        self.string_type = ""
        self.attr_num = ""
        self.A10_AX_AUTH_URI = ""
        self.attr_int = ""
        self.custom_attr_str = ""
        self.attr_int_val = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


