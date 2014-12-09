from a10sdk.common.A10BaseClass import A10BaseClass


class Uri(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param match_type: {"enum": ["contains", "ends-with", "equals", "starts-with"], "type": "string", "description": "'contains': Match URI if request URI contains specified URI; 'ends-with': Match URI if request URI ends with specified URI; 'equals': Match URI if request URI equals specified URI; 'starts-with': Match URI if request URI starts with specified URI; ", "format": "enum"}
    :param uri_str: {"minLength": 1, "maxLength": 128, "type": "string", "description": "Specify URI string", "format": "string-rlx"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "uri"
        self.DeviceProxy = ""
        self.match_type = ""
        self.uri_str = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class AccessList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param acl_name: {"not": "acl-id", "enum": ["ip-name", "ipv6-name"], "type": "string", "description": "'ip-name': Apply an IP named access list; 'ipv6-name': Apply an IPv6 named access list; ", "format": "enum"}
    :param acl_id: {"description": "ACL id", "format": "number", "maximum": 199, "minimum": 1, "not": "acl-name", "type": "number", "$ref": "/axapi/v3/access-list/standard"}
    :param name: {"minLength": 1, "maxLength": 16, "type": "string", "description": "Specify Named Access List", "format": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "access-list"
        self.DeviceProxy = ""
        self.acl_name = ""
        self.acl_id = ""
        self.name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class AaaRule(A10BaseClass):
    
    """Class Description::
    Rules of AAA policy.

    Class aaa-rule supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param index: {"description": "Specify AAA rule index", "format": "number", "type": "number", "maximum": 256, "minimum": 1, "optional": false}
    :param authorize_policy: {"description": "Specify authorization policy to bind to the AAA rule", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/aam/authorization/policy"}
    :param uri: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "match-type": {"enum": ["contains", "ends-with", "equals", "starts-with"], "type": "string", "description": "'contains': Match URI if request URI contains specified URI; 'ends-with': Match URI if request URI ends with specified URI; 'equals': Match URI if request URI equals specified URI; 'starts-with': Match URI if request URI starts with specified URI; ", "format": "enum"}, "uri-str": {"minLength": 1, "maxLength": 128, "type": "string", "description": "Specify URI string", "format": "string-rlx"}}}]}
    :param action: {"optional": true, "enum": ["allow", "deny"], "type": "string", "description": "'allow': Allow traffic that matches this rule; 'deny': Deny traffic that matches this rule; ", "format": "enum"}
    :param domain_name: {"description": "Specify domain name to bind to the AAA rule (ex: a10networks.com, www.a10networks.com)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 127, "type": "string"}
    :param authentication_template: {"description": "Specify authentication template name to bind to the AAA rule", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/aam/authentication/template"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/aam/aaa-policy/{name}/aaa-rule/{index}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "index"]

        self.b_key = "aaa-rule"
        self.a10_url="/axapi/v3/aam/aaa-policy/{name}/aaa-rule/{index}"
        self.DeviceProxy = ""
        self.index = ""
        self.authorize_policy = ""
        self.uri = []
        self.action = ""
        self.domain_name = ""
        self.authentication_template = ""
        self.access_list = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


