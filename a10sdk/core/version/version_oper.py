from a10sdk.common.A10BaseClass import A10BaseClass


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param firmware_version: {"type": "string", "format": "string"}
    :param hw_code: {"type": "string", "format": "string"}
    :param hd_sec: {"type": "string", "format": "string"}
    :param hd_pri: {"type": "string", "format": "string"}
    :param copyright: {"type": "string", "format": "string"}
    :param sw_version: {"type": "string", "format": "string"}
    :param boot_from: {"type": "string", "format": "string"}
    :param plat_features: {"type": "string", "format": "string"}
    :param hw_platform: {"type": "string", "format": "string"}
    :param serial_number: {"type": "string", "format": "string"}
    :param up_time: {"type": "string", "format": "string"}
    :param current_time: {"type": "string", "format": "string"}
    :param aflex_version: {"type": "string", "format": "string"}
    :param last_config_saved_time: {"type": "string", "format": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.firmware_version = ""
        self.hw_code = ""
        self.hd_sec = ""
        self.hd_pri = ""
        self.A10WW_copyright = ""
        self.sw_version = ""
        self.boot_from = ""
        self.plat_features = ""
        self.hw_platform = ""
        self.serial_number = ""
        self.up_time = ""
        self.current_time = ""
        self.aflex_version = ""
        self.last_config_saved_time = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Version(A10BaseClass):
    
    """Class Description::
    Operational Status for the object version.

    Class version supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/version/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "version"
        self.a10_url="/axapi/v3/version/oper"
        self.DeviceProxy = ""
        self.oper = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


