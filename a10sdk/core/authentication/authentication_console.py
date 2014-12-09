from a10sdk.common.A10BaseClass import A10BaseClass


class TypeCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param console_type: {"enum": ["ldap", "local", "radius", "tacplus"], "type": "string", "format": "enum-list"}
    :param type: {"default": 0, "type": "number", "description": "The login authentication type", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "type-cfg"
        self.DeviceProxy = ""
        self.console_type = ""
        self.A10WW_type = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Console(A10BaseClass):
    
    """Class Description::
    Configure console authentication type.

    Class console supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/authentication/console`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "console"
        self.a10_url="/axapi/v3/authentication/console"
        self.DeviceProxy = ""
        self.type_cfg = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


