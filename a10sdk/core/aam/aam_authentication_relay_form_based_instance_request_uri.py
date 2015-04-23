from a10sdk.common.A10BaseClass import A10BaseClass


class CookieValue(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param cookie_value: {"minLength": 1, "maxLength": 127, "type": "string", "description": "Specify cookie in POST packet", "format": "string-rlx"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "cookie-value"
        self.DeviceProxy = ""
        self.cookie_value = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Cookie(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "cookie"
        self.DeviceProxy = ""
        self.cookie_value = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class RequestUri(A10BaseClass):
    
    """Class Description::
    URI of authentication web page.

    Class request-uri supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param other_variables: {"description": "Specify other variables (n1=v1&n2=v2) in form relay", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 127, "type": "string"}
    :param action_uri: {"description": "Specify the action-URI", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 127, "type": "string"}
    :param uri: {"description": "Specify request URI", "format": "string-rlx", "minLength": 1, "optional": false, "maxLength": 127, "type": "string"}
    :param user_variable: {"description": "Specify username variable name", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param domain_variable: {"description": "Specify domain variable name", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param password_variable: {"description": "Specify password variable name", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param match_type: {"optional": false, "enum": ["equals", "contains", "starts-with", "ends-with"], "type": "string", "description": "'equals': URI exactly matches the string; 'contains': URI string contains another sub string; 'starts-with': URI string starts with sub string; 'ends-with': URI string ends with sub string; ", "format": "enum"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/aam/authentication/relay/form-based/instance/{name}/request-uri/{match_type}+{uri}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "match_type","uri"]

        self.b_key = "request-uri"
        self.a10_url="/axapi/v3/aam/authentication/relay/form-based/instance/{name}/request-uri/{match_type}+{uri}"
        self.DeviceProxy = ""
        self.other_variables = ""
        self.action_uri = ""
        self.uri = ""
        self.cookie = {}
        self.user_variable = ""
        self.domain_variable = ""
        self.password_variable = ""
        self.match_type = ""
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


