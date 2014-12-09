from a10sdk.common.A10BaseClass import A10BaseClass


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param state: {"enum": ["UP", "DOWN", "MAINTENANCE"], "type": "string", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.state = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Member(A10BaseClass):
    
    """Class Description::
    Operational Status for the object member.

    Class member supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param name: {"description": "Member name", "format": "comp-string", "minLength": 1, "oid": "1001", "optional": false, "maxLength": 127, "type": "string"}
    :param port: {"description": "Port number", "format": "number", "default": 65534, "optional": false, "oid": "1002", "maximum": 65534, "minimum": 0, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/service-group/{name}/member/{name}+{port}/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "member"
        self.a10_url="/axapi/v3/slb/service-group/{name}/member/{name}+{port}/oper"
        self.DeviceProxy = ""
        self.oper = {}
        self.name = ""
        self.port = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


