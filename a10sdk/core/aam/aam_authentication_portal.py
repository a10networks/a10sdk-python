from a10sdk.common.A10BaseClass import A10BaseClass


class LogoCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param logo: {"minLength": 1, "maxLength": 63, "type": "string", "description": "Specify logo image filename", "format": "string-rlx"}
    :param height: {"description": "Specify logo image height", "minimum": 50, "type": "number", "maximum": 400, "format": "number"}
    :param width: {"description": "Specify logo image width", "minimum": 50, "type": "number", "maximum": 400, "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "logo-cfg"
        self.DeviceProxy = ""
        self.logo = ""
        self.height = ""
        self.width = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Portal(A10BaseClass):
    
    """Class Description::
    Authentication portal configuration.

    Class portal supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param name: {"optional": false, "enum": ["default-portal"], "type": "string", "description": "'default-portal': Default portal configuration; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/aam/authentication/portal/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "portal"
        self.a10_url="/axapi/v3/aam/authentication/portal/{name}"
        self.DeviceProxy = ""
        self.logon_fail = {}
        self.logon = {}
        self.logo_cfg = {}
        self.name = ""
        self.change_password = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


