from a10sdk.common.A10BaseClass import A10BaseClass


class IfList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param IF_Status: {"enum": ["pristine", "owned"], "type": "string", "format": "enum"}
    :param IF_Num: {"type": "number", "format": "number"}
    :param IF_Type: {"enum": ["trunk"], "type": "string", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "if-list"
        self.DeviceProxy = ""
        self.IF_Status = ""
        self.IF_Num = ""
        self.IF_Type = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param if_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"IF-Status": {"enum": ["pristine", "owned"], "type": "string", "format": "enum"}, "IF-Num": {"type": "number", "format": "number"}, "IF-Type": {"enum": ["trunk"], "type": "string", "format": "enum"}, "optional": true}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.if_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class TrunkAvailableList(A10BaseClass):
    
    """Class Description::
    Operational Status for the object trunk-available-list.

    Class trunk-available-list supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/network/trunk-available-list/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "trunk-available-list"
        self.a10_url="/axapi/v3/network/trunk-available-list/oper"
        self.DeviceProxy = ""
        self.oper = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


