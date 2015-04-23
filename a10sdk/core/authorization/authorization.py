from a10sdk.common.A10BaseClass import A10BaseClass


class Method(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param none: {"default": 0, "type": "number", "description": "No command authorization", "format": "flag"}
    :param tacplus: {"default": 0, "type": "number", "description": "Using TACACS+ protocol", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "method"
        self.DeviceProxy = ""
        self.none = ""
        self.tacplus = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Authorization(A10BaseClass):
    
    """Class Description::
    Configuration for command authorization.

    Class authorization supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param debug: {"description": "Specify the debug level for authorization (Debug level for command authorization. bitwise OR of the following: 1(common), 2(packet),4(packet detail), 8(md5))", "format": "number", "type": "number", "maximum": 15, "minimum": 1, "optional": true}
    :param commands: {"description": "Commands level for authorization", "format": "number", "type": "number", "maximum": 15, "minimum": 0, "optional": true}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/authorization`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "authorization"
        self.a10_url="/axapi/v3/authorization"
        self.DeviceProxy = ""
        self.debug = ""
        self.commands = ""
        self.method = {}
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


