from a10sdk.common.A10BaseClass import A10BaseClass


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param hd_sec: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param cf_default: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param hd_pri: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param cf_pri: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param cf_sec: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param hd_default: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.hd_sec = ""
        self.cf_default = ""
        self.hd_pri = ""
        self.cf_pri = ""
        self.cf_sec = ""
        self.hd_default = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Bootimage(A10BaseClass):
    
    """Class Description::
    Operational Status for the object bootimage.

    Class bootimage supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/bootimage/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "bootimage"
        self.a10_url="/axapi/v3/bootimage/oper"
        self.DeviceProxy = ""
        self.oper = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


