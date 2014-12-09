from a10sdk.common.A10BaseClass import A10BaseClass


class Aam(A10BaseClass):
    
    """Class Description::
    Configure AAM related settings.

    Class aam supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param aaa_policy_list: {"minItems": 1, "items": {"type": "aaa-policy"}, "uniqueItems": true, "array": [{"required": ["name"], "properties": {"aaa-rule-list": {"minItems": 1, "items": {"type": "aaa-rule"}, "uniqueItems": true, "array": [{"required": ["index"], "properties": {"index": {"description": "Specify AAA rule index", "format": "number", "type": "number", "maximum": 256, "minimum": 1, "optional": false}, "authorize-policy": {"description": "Specify authorization policy to bind to the AAA rule", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/aam/authorization/policy"}, "uri": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "match-type": {"enum": ["contains", "ends-with", "equals", "starts-with"], "type": "string", "description": "'contains': Match URI if request URI contains specified URI; 'ends-with': Match URI if request URI ends with specified URI; 'equals': Match URI if request URI equals specified URI; 'starts-with': Match URI if request URI starts with specified URI; ", "format": "enum"}, "uri-str": {"minLength": 1, "maxLength": 128, "type": "string", "description": "Specify URI string", "format": "string-rlx"}}}]}, "action": {"optional": true, "enum": ["allow", "deny"], "type": "string", "description": "'allow': Allow traffic that matches this rule; 'deny': Deny traffic that matches this rule; ", "format": "enum"}, "domain-name": {"description": "Specify domain name to bind to the AAA rule (ex: a10networks.com, www.a10networks.com)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 127, "type": "string"}, "authentication-template": {"description": "Specify authentication template name to bind to the AAA rule", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/aam/authentication/template"}, "access-list": {"type": "object", "properties": {"acl-name": {"not": "acl-id", "enum": ["ip-name", "ipv6-name"], "type": "string", "description": "'ip-name': Apply an IP named access list; 'ipv6-name': Apply an IPv6 named access list; ", "format": "enum"}, "acl-id": {"description": "ACL id", "format": "number", "maximum": 199, "$ref-list": ["/axapi/v3/access-list/standard", "/axapi/v3/access-list/extended"], "minimum": 1, "not": "acl-name", "type": "number"}, "name": {"minLength": 1, "maxLength": 16, "type": "string", "description": "Specify Named Access List", "format": "string"}}}}}], "type": "array", "$ref": "/axapi/v3/aam/aaa-policy/{name}/aaa-rule/{index}"}, "name": {"description": "Specify AAA policy name", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/aam/aaa-policy/{name}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/aam`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "aam"
        self.a10_url="/axapi/v3/aam"
        self.DeviceProxy = ""
        self.authentication = {}
        self.aaa_policy_list = []
        self.authorization = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


