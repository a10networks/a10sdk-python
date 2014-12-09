from a10sdk.common.A10BaseClass import A10BaseClass


class SessionList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param name: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param cfg_mode: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param src_ip: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param sid: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param type: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "session-list"
        self.DeviceProxy = ""
        self.name = ""
        self.cfg_mode = ""
        self.src_ip = ""
        self.sid = ""
        self.A10WW_type = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param session_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"name": {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}, "optional": true, "cfg_mode": {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}, "src_ip": {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}, "sid": {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}, "type": {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.session_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class AdminSession(A10BaseClass):
    
    """Class Description::
    Operational Status for the object admin-session.

    Class admin-session supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/admin-session/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "admin-session"
        self.a10_url="/axapi/v3/admin-session/oper"
        self.DeviceProxy = ""
        self.oper = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


