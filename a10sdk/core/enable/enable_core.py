from a10sdk.common.A10BaseClass import A10BaseClass


class EnableCore(A10BaseClass):
    
    """Class Description::
    Enable system coredump switch.

    Class enable-core supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param core_level: {"description": "'a10': Enable A10 core dump, by default; 'system': Enable system coredump; ", "format": "enum", "default": "a10", "optional": true, "enum": ["a10", "system"], "not": "full", "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/enable-core`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "enable-core"
        self.a10_url="/axapi/v3/enable-core"
        self.DeviceProxy = ""
        self.core_level = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


