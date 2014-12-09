from a10sdk.common.A10BaseClass import A10BaseClass


class Logon(A10BaseClass):
    
    """Class Description::
    Authentication logon configuration.

    Class logon supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param form_based_list: {"minItems": 1, "items": {"type": "form-based"}, "uniqueItems": true, "array": [{"required": ["name"], "properties": {"retry": {"description": "Specify max. number of failure retry (Specify retry count (1 ~ 32), default is 3)", "format": "number", "default": 3, "optional": true, "maximum": 32, "minimum": 1, "type": "number"}, "name": {"description": "Specify form-based authentication logon name", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}, "next-token-variable": {"description": "Specify next-token variable name in form submission", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}, "new-pin-variable": {"description": "Specify new-pin variable name in form submission", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}, "portal": {"type": "object", "properties": {"new-pin-page": {"minLength": 1, "maxLength": 63, "type": "string", "description": "Specify new PIN page name for RSA-RADIUS", "format": "string-rlx"}, "portal-name": {"description": "Specify portal name", "format": "string", "minLength": 1, "maxLength": 63, "not": "default-portal", "type": "string"}, "default-portal": {"default": 0, "not": "portal-name", "type": "number", "description": "Use default portal", "format": "flag"}, "next-token-page": {"minLength": 1, "maxLength": 63, "type": "string", "description": "Specify next token page name for RSA-RADIUS", "format": "string-rlx"}, "failpage": {"minLength": 1, "maxLength": 63, "type": "string", "description": "Specify logon fail page name (portal fail page name)", "format": "string-rlx"}, "changepasswordpage": {"minLength": 1, "maxLength": 63, "type": "string", "description": "Specify change password page name", "format": "string-rlx"}, "logon": {"minLength": 1, "maxLength": 63, "type": "string", "description": "Specify logon page name", "format": "string"}}}, "logon-page-cfg": {"type": "object", "properties": {"action-url": {"minLength": 1, "maxLength": 127, "type": "string", "description": "Specify form submission action url", "format": "string-rlx"}, "username-variable": {"minLength": 1, "maxLength": 63, "type": "string", "description": "Specify username variable name in form submission", "format": "string-rlx"}, "password-variable": {"minLength": 1, "maxLength": 63, "type": "string", "description": "Specify password variable name in form submission", "format": "string-rlx"}, "login-failure-message": {"minLength": 1, "maxLength": 127, "type": "string", "description": "Specify login failure message shown in logon page (Specify error string, default is \"Invalid username or password. Please try again.\")", "format": "string-rlx"}}}, "cp-page-cfg": {"type": "object", "properties": {"cp-cfm-pwd-enum": {"enum": ["changepassword-password-confirm-variable"], "type": "string", "description": "'changepassword-password-confirm-variable': Specify password confirm variable name in form submission; ", "format": "enum"}, "cp-cfm-pwd-var": {"minLength": 1, "maxLength": 63, "type": "string", "description": "Specify password confirm variable name", "format": "string-rlx"}, "cp-new-pwd-var": {"minLength": 1, "maxLength": 63, "type": "string", "description": "Specify new password variable name", "format": "string-rlx"}, "changepassword-url": {"minLength": 1, "maxLength": 127, "type": "string", "description": "Specify changepassword form submission action url (changepassword action url)", "format": "string-rlx"}, "cp-new-pwd-enum": {"enum": ["changepassword-new-password-variable"], "type": "string", "description": "'changepassword-new-password-variable': Specify new password variable name in form submission; ", "format": "enum"}, "cp-old-pwd-enum": {"enum": ["changepassword-old-password-variable"], "type": "string", "description": "'changepassword-old-password-variable': Specify old password variable name in form submission; ", "format": "enum"}, "cp-user-var": {"minLength": 1, "maxLength": 63, "type": "string", "description": "Specify username variable name", "format": "string-rlx"}, "cp-old-pwd-var": {"minLength": 1, "maxLength": 63, "type": "string", "description": "Specify old password variable name", "format": "string-rlx"}, "cp-user-enum": {"enum": ["changepassword-username-variable"], "type": "string", "description": "'changepassword-username-variable': Specify username variable name in form submission; ", "format": "enum"}}}}}], "type": "array", "$ref": "/axapi/v3/aam/authentication/logon/form-based/{name}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/aam/authentication/logon`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "logon"
        self.a10_url="/axapi/v3/aam/authentication/logon"
        self.DeviceProxy = ""
        self.form_based_list = []
        self.http_authenticate = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


