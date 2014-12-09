from a10sdk.common.A10BaseClass import A10BaseClass


class VeMacScheme(A10BaseClass):
    
    """Class Description::
    VE MAC allocation scheme.

    Class ve-mac-scheme supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param ve_mac_scheme_val: {"description": "'hash-based': Hash-based using the VE number; 'round-robin': Round Robin scheme; 'system-mac': Use system MAC address; ", "format": "enum", "default": "hash-based", "type": "string", "enum": ["hash-based", "round-robin", "system-mac"], "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/system/ve-mac-scheme`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "ve-mac-scheme"
        self.a10_url="/axapi/v3/system/ve-mac-scheme"
        self.DeviceProxy = ""
        self.ve_mac_scheme_val = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


