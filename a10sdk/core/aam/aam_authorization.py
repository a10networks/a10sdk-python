from a10sdk.common.A10BaseClass import A10BaseClass


class Authorization(A10BaseClass):
    
    """Class Description::
    Configure authorization related settings.

    Class authorization supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param policy_list: {"minItems": 1, "items": {"type": "policy"}, "uniqueItems": true, "array": [{"required": ["name"], "properties": {"uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}, "server": {"description": "Specify a LDAP or RADIUS server for authorization (Specify a LDAP or RADIUS server name)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "not": "service-group", "type": "string", "$ref": "/axapi/v3/aam/authentication/server/ldap/instance"}, "service-group": {"description": "Specify an authentication service group for authorization (Specify authentication service group name)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 127, "not": "server", "type": "string", "$ref": "/axapi/v3/aam/authentication/service-group"}, "attribute-list": {"minItems": 1, "items": {"type": "attribute"}, "uniqueItems": true, "array": [{"required": ["attr-num"], "properties": {"attribute-name": {"description": "Specify attribute name", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "not": "A10-AX-AUTH-URI", "type": "string"}, "ip-type": {"description": "IP address is transformed into network byte order", "format": "flag", "default": 0, "optional": true, "not-list": ["string-type", "integer-type"], "type": "number"}, "custom-attr-type": {"default": 0, "optional": true, "type": "number", "description": "Specify attribute type", "format": "flag"}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}, "string-type": {"description": "Attribute type is string", "format": "flag", "default": 0, "optional": true, "not-list": ["integer-type", "ip-type"], "type": "number"}, "custom-attr-str": {"optional": true, "enum": ["match", "sub-string"], "type": "string", "description": "'match': Operation type is match; 'sub-string': Operation type is sub-string; ", "format": "enum"}, "attr-str-val": {"description": "Set attribute value", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}, "attr-ipv4": {"optional": true, "type": "string", "description": "IPv4 address", "format": "ipv4-address"}, "attr-type": {"default": 0, "optional": true, "type": "number", "description": "Specify attribute type", "format": "flag"}, "attr-num": {"description": "Set attribute ID for authorization policy", "format": "number", "type": "number", "maximum": 32, "minimum": 1, "optional": false}, "A10-AX-AUTH-URI": {"description": "Custom-defined attribute", "format": "flag", "default": 0, "optional": true, "not": "attribute-name", "type": "number"}, "integer-type": {"description": "Attribute type is integer", "format": "flag", "default": 0, "optional": true, "not-list": ["string-type", "ip-type"], "type": "number"}, "a10-dynamic-defined": {"default": 0, "optional": true, "type": "number", "description": "The value of this attribute will depend on AX configuration instead of user configuration", "format": "flag"}, "attr-ip": {"optional": true, "enum": ["equal", "not-equal"], "type": "string", "description": "'equal': Operation type is equal; 'not-equal': Operation type is not-equal; ", "format": "enum"}, "attr-int": {"optional": true, "enum": ["equal", "not-equal", "less-than", "more-than", "less-than-equal-to", "more-than-equal-to"], "type": "string", "description": "'equal': Operation type is equal; 'not-equal': Operation type is not equal; 'less-than': Operation type is less-than; 'more-than': Operation type is more-than; 'less-than-equal-to': Operation type is less-than-equal-to; 'more-than-equal-to': Operation type is more-thatn-equal-to; ", "format": "enum"}, "attr-str": {"optional": true, "enum": ["match", "sub-string"], "type": "string", "description": "'match': Operation type is match; 'sub-string': Operation type is sub-string; ", "format": "enum"}, "attr-int-val": {"description": "Set attribute value", "format": "number", "type": "number", "maximum": 4294967295, "minimum": 0, "optional": true}}}], "type": "array", "$ref": "/axapi/v3/aam/authorization/policy/{name}/attribute/{attr-num}"}, "attribute-rule": {"optional": true, "type": "string", "description": "Define attribute rule for authorization policy", "format": "string-rlx"}, "name": {"description": "Specify authorization policy name", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/aam/authorization/policy/{name}"}
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


