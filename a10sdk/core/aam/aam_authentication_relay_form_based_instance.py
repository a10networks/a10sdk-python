from a10sdk.common.A10BaseClass import A10BaseClass


class Instance(A10BaseClass):
    
    """Class Description::
    Form-based Authentication Relay.

    Class instance supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param request_uri_list: {"minItems": 1, "items": {"type": "request-uri"}, "uniqueItems": true, "array": [{"required": ["match-type", "uri"], "properties": {"other-variables": {"description": "Specify other variables (n1=v1&n2=v2) in form relay", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 127, "type": "string"}, "action-uri": {"description": "Specify the action-URI", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 127, "type": "string"}, "uri": {"description": "Specify request URI", "format": "string-rlx", "minLength": 1, "optional": false, "maxLength": 127, "type": "string"}, "cookie": {"type": "object", "properties": {"cookie-value": {"type": "object", "properties": {"cookie-value": {"minLength": 1, "maxLength": 127, "type": "string", "description": "Specify cookie in POST packet", "format": "string-rlx"}}}}}, "user-variable": {"description": "Specify username variable name", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}, "domain-variable": {"description": "Specify domain variable name", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}, "password-variable": {"description": "Specify password variable name", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}, "match-type": {"optional": false, "enum": ["equals", "contains", "starts-with", "ends-with"], "type": "string", "description": "'equals': URI exactly matches the string; 'contains': URI string contains another sub string; 'starts-with': URI string starts with sub string; 'ends-with': URI string ends with sub string; ", "format": "enum"}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/aam/authentication/relay/form-based/instance/{name}/request-uri/{match-type}+{uri}"}
    :param name: {"description": "Specify form-based authentication relay name", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/aam/authentication/relay/form-based/instance/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "instance"
        self.a10_url="/axapi/v3/aam/authentication/relay/form-based/instance/{name}"
        self.DeviceProxy = ""
        self.request_uri_list = []
        self.name = ""
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


