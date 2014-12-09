from a10sdk.common.A10BaseClass import A10BaseClass


class SessionList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param Session_id: {"type": "number", "format": "number"}
    :param TTL_in_seconds: {"type": "number", "format": "number"}
    :param Domain: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param Client_IP: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param Domain_Group: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param VIP: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param User: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param VPort: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param Type: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param Created_Time: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "session-list"
        self.DeviceProxy = ""
        self.Session_id = ""
        self.TTL_in_seconds = ""
        self.Domain = ""
        self.Client_IP = ""
        self.Domain_Group = ""
        self.VIP = ""
        self.User = ""
        self.VPort = ""
        self.Type = ""
        self.Created_Time = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param session_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"Session-id": {"type": "number", "format": "number"}, "TTL-in-seconds": {"type": "number", "format": "number"}, "Domain": {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}, "Client-IP": {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}, "optional": true, "Domain-Group": {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}, "VIP": {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}, "User": {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}, "VPort": {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}, "Type": {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}, "Created-Time": {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.session_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Session(A10BaseClass):
    
    """Class Description::
    Operational Status for the object session.

    Class session supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/aam/authentication/session/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "session"
        self.a10_url="/axapi/v3/aam/authentication/session/oper"
        self.DeviceProxy = ""
        self.oper = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


