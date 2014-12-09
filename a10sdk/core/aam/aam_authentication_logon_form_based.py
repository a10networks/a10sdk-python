from a10sdk.common.A10BaseClass import A10BaseClass


class Portal(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param new_pin_page: {"minLength": 1, "maxLength": 63, "type": "string", "description": "Specify new PIN page name for RSA-RADIUS", "format": "string-rlx"}
    :param portal_name: {"description": "Specify portal name", "format": "string", "minLength": 1, "maxLength": 63, "not": "default-portal", "type": "string"}
    :param default_portal: {"default": 0, "not": "portal-name", "type": "number", "description": "Use default portal", "format": "flag"}
    :param next_token_page: {"minLength": 1, "maxLength": 63, "type": "string", "description": "Specify next token page name for RSA-RADIUS", "format": "string-rlx"}
    :param failpage: {"minLength": 1, "maxLength": 63, "type": "string", "description": "Specify logon fail page name (portal fail page name)", "format": "string-rlx"}
    :param changepasswordpage: {"minLength": 1, "maxLength": 63, "type": "string", "description": "Specify change password page name", "format": "string-rlx"}
    :param logon: {"minLength": 1, "maxLength": 63, "type": "string", "description": "Specify logon page name", "format": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "portal"
        self.DeviceProxy = ""
        self.new_pin_page = ""
        self.portal_name = ""
        self.default_portal = ""
        self.next_token_page = ""
        self.failpage = ""
        self.changepasswordpage = ""
        self.logon = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class LogonPageCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param action_url: {"minLength": 1, "maxLength": 127, "type": "string", "description": "Specify form submission action url", "format": "string-rlx"}
    :param username_variable: {"minLength": 1, "maxLength": 63, "type": "string", "description": "Specify username variable name in form submission", "format": "string-rlx"}
    :param password_variable: {"minLength": 1, "maxLength": 63, "type": "string", "description": "Specify password variable name in form submission", "format": "string-rlx"}
    :param login_failure_message: {"minLength": 1, "maxLength": 127, "type": "string", "description": "Specify login failure message shown in logon page (Specify error string, default is \"Invalid username or password. Please try again.\")", "format": "string-rlx"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "logon-page-cfg"
        self.DeviceProxy = ""
        self.action_url = ""
        self.username_variable = ""
        self.password_variable = ""
        self.login_failure_message = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class CpPageCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param cp_cfm_pwd_enum: {"enum": ["changepassword-password-confirm-variable"], "type": "string", "description": "'changepassword-password-confirm-variable': Specify password confirm variable name in form submission; ", "format": "enum"}
    :param cp_cfm_pwd_var: {"minLength": 1, "maxLength": 63, "type": "string", "description": "Specify password confirm variable name", "format": "string-rlx"}
    :param cp_new_pwd_var: {"minLength": 1, "maxLength": 63, "type": "string", "description": "Specify new password variable name", "format": "string-rlx"}
    :param changepassword_url: {"minLength": 1, "maxLength": 127, "type": "string", "description": "Specify changepassword form submission action url (changepassword action url)", "format": "string-rlx"}
    :param cp_new_pwd_enum: {"enum": ["changepassword-new-password-variable"], "type": "string", "description": "'changepassword-new-password-variable': Specify new password variable name in form submission; ", "format": "enum"}
    :param cp_old_pwd_enum: {"enum": ["changepassword-old-password-variable"], "type": "string", "description": "'changepassword-old-password-variable': Specify old password variable name in form submission; ", "format": "enum"}
    :param cp_user_var: {"minLength": 1, "maxLength": 63, "type": "string", "description": "Specify username variable name", "format": "string-rlx"}
    :param cp_old_pwd_var: {"minLength": 1, "maxLength": 63, "type": "string", "description": "Specify old password variable name", "format": "string-rlx"}
    :param cp_user_enum: {"enum": ["changepassword-username-variable"], "type": "string", "description": "'changepassword-username-variable': Specify username variable name in form submission; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "cp-page-cfg"
        self.DeviceProxy = ""
        self.cp_cfm_pwd_enum = ""
        self.cp_cfm_pwd_var = ""
        self.cp_new_pwd_var = ""
        self.changepassword_url = ""
        self.cp_new_pwd_enum = ""
        self.cp_old_pwd_enum = ""
        self.cp_user_var = ""
        self.cp_old_pwd_var = ""
        self.cp_user_enum = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class FormBased(A10BaseClass):
    
    """Class Description::
    Form-based Authentication Logon.

    Class form-based supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param retry: {"description": "Specify max. number of failure retry (Specify retry count (1 ~ 32), default is 3)", "format": "number", "default": 3, "optional": true, "maximum": 32, "minimum": 1, "type": "number"}
    :param name: {"description": "Specify form-based authentication logon name", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param next_token_variable: {"description": "Specify next-token variable name in form submission", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param new_pin_variable: {"description": "Specify new-pin variable name in form submission", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/aam/authentication/logon/form-based/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "form-based"
        self.a10_url="/axapi/v3/aam/authentication/logon/form-based/{name}"
        self.DeviceProxy = ""
        self.retry = ""
        self.name = ""
        self.next_token_variable = ""
        self.new_pin_variable = ""
        self.portal = {}
        self.logon_page_cfg = {}
        self.cp_page_cfg = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


