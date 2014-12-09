from a10sdk.common.A10BaseClass import A10BaseClass


class StartupConfig(A10BaseClass):
    
    """    :param default: {"description": "Default startup-config", "partition-visibility": "shared", "default": 0, "type": "number", "format": "flag", "optional": true}
    :param secondary: {"default": 0, "optional": true, "type": "number", "description": "Create link in secondary partition", "format": "flag"}
    :param primary: {"default": 0, "optional": true, "type": "number", "description": "Create link in primary partition", "format": "flag"}
    :param file_name: {"description": "Local Configuration Profile Name", "format": "string", "minLength": 1, "optional": true, "maxLength": 31, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Startup Configuration.

    Class startup-config supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/link/startup-config`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "startup-config"
        self.a10_url="/axapi/v3/link/startup-config"
        self.DeviceProxy = ""
        self.default = ""
        self.secondary = ""
        self.primary = ""
        self.file_name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


