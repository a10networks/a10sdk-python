from a10sdk.common.A10BaseClass import A10BaseClass


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param time: {"type": "string", "format": "string"}
    :param offset: {"type": "string", "format": "string"}
    :param date: {"type": "string", "format": "string"}
    :param timezone: {"type": "string", "format": "string"}
    :param source_type: {"type": "number", "format": "number"}
    :param day: {"type": "string", "format": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.time = ""
        self.offset = ""
        self.date = ""
        self.timezone = ""
        self.source_type = ""
        self.day = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Show(A10BaseClass):
    
    """Class Description::
    Operational Status for the object show.

    Class show supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/clock/show/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "show"
        self.a10_url="/axapi/v3/clock/show/oper"
        self.DeviceProxy = ""
        self.oper = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


