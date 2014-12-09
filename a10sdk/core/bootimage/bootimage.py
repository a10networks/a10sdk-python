from a10sdk.common.A10BaseClass import A10BaseClass


class HdCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param sec: {"default": 0, "type": "number", "description": "Secondary image", "format": "flag"}
    :param pri: {"default": 0, "type": "number", "description": "Primary image", "format": "flag"}
    :param hd: {"default": 0, "type": "number", "description": "Hard disk", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "hd-cfg"
        self.DeviceProxy = ""
        self.sec = ""
        self.pri = ""
        self.hd = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class CfCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param cf_pri: {"default": 0, "type": "number", "description": "Primary image", "format": "flag"}
    :param cf: {"default": 0, "type": "number", "description": "Compact flash", "plat-neg-list": ["soft-ax"], "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "cf-cfg"
        self.DeviceProxy = ""
        self.cf_pri = ""
        self.cf = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Bootimage(A10BaseClass):
    
    """    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Set next Boot Image.

    Class bootimage supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/bootimage`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "bootimage"
        self.a10_url="/axapi/v3/bootimage"
        self.DeviceProxy = ""
        self.hd_cfg = {}
        self.cf_cfg = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


