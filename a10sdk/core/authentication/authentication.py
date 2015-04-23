from a10sdk.common.A10BaseClass import A10BaseClass


class ModeCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param mode: {"default": 0, "type": "number", "description": "Configure authentication mode", "format": "flag"}
    :param mode_type: {"default": "\"single\"", "enum": ["multiple", "single"], "type": "string", "description": "'multiple': Multiple authentication mode. If an authentication method rejected, try next one; 'single': Single authentication mode. If an authentication method rejected, don't try next one; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "mode-cfg"
        self.DeviceProxy = ""
        self.mode = ""
        self.mode_type = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class TypeCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param authen_type: {"enum": ["ldap", "local", "radius", "tacplus"], "type": "string", "format": "enum-list"}
    :param type: {"default": 0, "type": "number", "description": "The login authentication type", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "type-cfg"
        self.DeviceProxy = ""
        self.authen_type = ""
        self.A10WW_type = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class LoginCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param local: {"default": 0, "type": "number", "description": "Configure local user to enter privilege-mode", "format": "flag"}
    :param privilege_mode: {"default": 0, "type": "number", "description": "Configure to enter privilege-mode", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "login-cfg"
        self.DeviceProxy = ""
        self.local = ""
        self.privilege_mode = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class EnableCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param enable_auth_type: {"default": "local", "enum": ["local", "tacplus"], "type": "string", "description": "The enable-password authentication type", "format": "enum-list"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "enable-cfg"
        self.DeviceProxy = ""
        self.enable_auth_type = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Authentication(A10BaseClass):
    
    """Class Description::
    Configure authentication feature.

    Class authentication supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param multiple_auth_reject: {"default": 0, "optional": true, "type": "number", "description": "Multiple same user login reject", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/authentication`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "authentication"
        self.a10_url="/axapi/v3/authentication"
        self.DeviceProxy = ""
        self.console = {}
        self.uuid = ""
        self.mode_cfg = {}
        self.type_cfg = {}
        self.multiple_auth_reject = ""
        self.login_cfg = {}
        self.enable_cfg = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


