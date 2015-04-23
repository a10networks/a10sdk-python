from a10sdk.common.A10BaseClass import A10BaseClass


class ExecBannerCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param exec_banner: {"type": "string", "description": "Banner text", "format": "string-rlx"}
    :param exec: {"default": 0, "type": "number", "description": "Set EXEC process creation banner", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "exec-banner-cfg"
        self.DeviceProxy = ""
        self.exec_banner = ""
        self.A10WW_exec = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class LoginBannerCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param login: {"default": 0, "partition-visibility": "shared", "type": "number", "description": "Set login banner", "format": "flag"}
    :param login_banner: {"partition-visibility": "shared", "type": "string", "description": "Banner text", "format": "string-rlx"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "login-banner-cfg"
        self.DeviceProxy = ""
        self.login = ""
        self.login_banner = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Banner(A10BaseClass):
    
    """Class Description::
    Define a login banner.

    Class banner supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/banner`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "banner"
        self.a10_url="/axapi/v3/banner"
        self.DeviceProxy = ""
        self.exec_banner_cfg = {}
        self.uuid = ""
        self.login_banner_cfg = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


