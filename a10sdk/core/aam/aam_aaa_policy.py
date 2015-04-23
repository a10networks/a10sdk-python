from a10sdk.common.A10BaseClass import A10BaseClass


class SamplingEnable(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param counters1: {"enum": ["all", "Req", "Req-Reject", "Req-Auth", "Req-Allow", "Req-Skip", "Error"], "type": "string", "description": "'all': all; 'Req': Request; 'Req-Reject': Request Rejected; 'Req-Auth': Request Matching Authentication Template; 'Req-Allow': Request Allowed; 'Req-Skip': Request Skipped; 'Error': Error; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "sampling-enable"
        self.DeviceProxy = ""
        self.counters1 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class AaaPolicy(A10BaseClass):
    
    """Class Description::
    Configure AAA policy.

    Class aaa-policy supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param aaa_rule_list: {"minItems": 1, "items": {"type": "aaa-rule"}, "uniqueItems": true, "array": [{"required": ["index"], "properties": {"index": {"description": "Specify AAA rule index", "format": "number", "type": "number", "maximum": 256, "minimum": 1, "optional": false}, "match-encoded-uri": {"default": 0, "optional": true, "type": "number", "description": "Enable URL decoding for URI matching", "format": "flag"}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}, "authorize-policy": {"description": "Specify authorization policy to bind to the AAA rule", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/aam/authorization/policy"}, "uri": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "match-type": {"enum": ["contains", "ends-with", "equals", "starts-with"], "type": "string", "description": "'contains': Match URI if request URI contains specified URI; 'ends-with': Match URI if request URI ends with specified URI; 'equals': Match URI if request URI equals specified URI; 'starts-with': Match URI if request URI starts with specified URI; ", "format": "enum"}, "uri-str": {"minLength": 1, "maxLength": 128, "type": "string", "description": "Specify URI string", "format": "string-rlx"}}}]}, "action": {"optional": true, "enum": ["allow", "deny"], "type": "string", "description": "'allow': Allow traffic that matches this rule; 'deny': Deny traffic that matches this rule; ", "format": "enum"}, "sampling-enable": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "total_count", "hit_count"], "type": "string", "description": "'all': all; 'total_count': total_count; 'hit_count': hit_count; ", "format": "enum"}}}]}, "domain-name": {"description": "Specify domain name to bind to the AAA rule (ex: a10networks.com, www.a10networks.com)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 127, "type": "string"}, "authentication-template": {"description": "Specify authentication template name to bind to the AAA rule", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/aam/authentication/template"}, "access-list": {"type": "object", "properties": {"acl-name": {"not": "acl-id", "enum": ["ip-name", "ipv6-name"], "type": "string", "description": "'ip-name': Apply an IP named access list; 'ipv6-name': Apply an IPv6 named access list; ", "format": "enum"}, "acl-id": {"description": "ACL id", "format": "number", "maximum": 199, "minimum": 1, "not": "acl-name", "type": "number", "$ref": "/axapi/v3/access-list/standard"}, "name": {"minLength": 1, "maxLength": 16, "type": "string", "description": "Specify Named Access List", "format": "string"}}}}}], "type": "array", "$ref": "/axapi/v3/aam/aaa-policy/{name}/aaa-rule/{index}"}
    :param sampling_enable: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "Req", "Req-Reject", "Req-Auth", "Req-Allow", "Req-Skip", "Error"], "type": "string", "description": "'all': all; 'Req': Request; 'Req-Reject': Request Rejected; 'Req-Auth': Request Matching Authentication Template; 'Req-Allow': Request Allowed; 'Req-Skip': Request Skipped; 'Error': Error; ", "format": "enum"}}}]}
    :param name: {"description": "Specify AAA policy name", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/aam/aaa-policy/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "aaa-policy"
        self.a10_url="/axapi/v3/aam/aaa-policy/{name}"
        self.DeviceProxy = ""
        self.aaa_rule_list = []
        self.sampling_enable = []
        self.name = ""
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


