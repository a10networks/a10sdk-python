from a10sdk.common.A10BaseClass import A10BaseClass


class SessionList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param Session_id: {"type": "number", "format": "number"}
    :param TTL_in_seconds: {"type": "number", "format": "number"}
    :param Domain: {"type": "string", "format": "string"}
    :param Client_IP: {"type": "string", "format": "string"}
    :param Domain_Group: {"type": "string", "format": "string"}
    :param VIP: {"type": "string", "format": "string"}
    :param User: {"type": "string", "format": "string"}
    :param VPort: {"type": "string", "format": "string"}
    :param Type: {"type": "string", "format": "string"}
    :param Created_Time: {"type": "string", "format": "string"}
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

    :param session_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"Session-id": {"type": "number", "format": "number"}, "TTL-in-seconds": {"type": "number", "format": "number"}, "Domain": {"type": "string", "format": "string"}, "Client-IP": {"type": "string", "format": "string"}, "optional": true, "Domain-Group": {"type": "string", "format": "string"}, "VIP": {"type": "string", "format": "string"}, "User": {"type": "string", "format": "string"}, "VPort": {"type": "string", "format": "string"}, "Type": {"type": "string", "format": "string"}, "Created-Time": {"type": "string", "format": "string"}}}]}
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


