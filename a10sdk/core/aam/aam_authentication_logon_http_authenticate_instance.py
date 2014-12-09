from a10sdk.common.A10BaseClass import A10BaseClass


class Ntlm(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ntlm_enable: {"default": 0, "type": "number", "description": "Enable NTLM logon", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ntlm"
        self.DeviceProxy = ""
        self.ntlm_enable = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Negotiate(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param negotiate_enable: {"default": 0, "type": "number", "description": "Enable SPENGO logon", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "negotiate"
        self.DeviceProxy = ""
        self.negotiate_enable = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Basic(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param new_pin_page: {"minLength": 1, "maxLength": 63, "type": "string", "description": "Specify new PIN page name for RSA-RADIUS", "format": "string-rlx"}
    :param basic_enable: {"default": 0, "type": "number", "description": "Enable Basic logon", "format": "flag"}
    :param next_token_variable: {"minLength": 1, "maxLength": 63, "type": "string", "description": "Specify next-token variable name", "format": "string-rlx"}
    :param next_token_page: {"minLength": 1, "maxLength": 63, "type": "string", "description": "Specify next-token page name for RSA-RADIUS", "format": "string-rlx"}
    :param basic_realm: {"minLength": 1, "maxLength": 128, "type": "string", "description": "Specify realm for basic logon", "format": "string-rlx"}
    :param new_pin_variable: {"minLength": 1, "maxLength": 63, "type": "string", "description": "Specify new PIN variable name", "format": "string-rlx"}
    :param challenge_response_form: {"minLength": 1, "maxLength": 63, "type": "string", "description": "Specify challenge-response form for RSA-RADIUS authentication", "format": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "basic"
        self.DeviceProxy = ""
        self.new_pin_page = ""
        self.basic_enable = ""
        self.next_token_variable = ""
        self.next_token_page = ""
        self.basic_realm = ""
        self.new_pin_variable = ""
        self.challenge_response_form = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class AuthMethod(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "auth-method"
        self.DeviceProxy = ""
        self.ntlm = {}
        self.negotiate = {}
        self.basic = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Instance(A10BaseClass):
    
    """Class Description::
    HTTP-authenticate Logon.

    Class instance supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param retry: {"description": "Specify max. number of failure retry (1 ~ 32), default is 3", "format": "number", "default": 3, "optional": true, "maximum": 32, "minimum": 1, "type": "number"}
    :param name: {"description": "Specify HTTP-Authenticate logon name", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/aam/authentication/logon/http-authenticate/instance/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "instance"
        self.a10_url="/axapi/v3/aam/authentication/logon/http-authenticate/instance/{name}"
        self.DeviceProxy = ""
        self.retry = ""
        self.name = ""
        self.auth_method = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


