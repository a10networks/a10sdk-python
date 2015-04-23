from a10sdk.common.A10BaseClass import A10BaseClass


class SystemJumboGlobal(A10BaseClass):
    
    """Class Description::
    To enable/disable jumbo.

    Class system-jumbo-global supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param enable_jumbo: {"default": 0, "optional": true, "type": "number", "description": "Enable jumbo frame", "format": "flag"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/system-jumbo-global`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "system-jumbo-global"
        self.a10_url="/axapi/v3/system-jumbo-global"
        self.DeviceProxy = ""
        self.enable_jumbo = ""
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


