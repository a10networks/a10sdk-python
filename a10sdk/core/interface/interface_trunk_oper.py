from a10sdk.common.A10BaseClass import A10BaseClass


class TrunkMember(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param members: {"minimum": 1, "type": "number", "maximum": 12, "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "trunk-member"
        self.DeviceProxy = ""
        self.members = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ipv4_netmask: {"type": "string", "description": "IP subnet mask", "format": "ipv4-netmask"}
    :param Hardware: {"enum": ["TrunkGroup"], "type": "string", "format": "enum"}
    :param state: {"enum": ["UP", "DOWN", "DISABLED"], "type": "string", "format": "enum"}
    :param Address: {"minLength": 11, "maxLength": 17, "type": "string", "format": "mac-address"}
    :param trunk_member: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "members": {"minimum": 1, "type": "number", "maximum": 12, "format": "number"}}}]}
    :param line_protocol: {"enum": ["UP", "DOWN"], "type": "string", "format": "enum"}
    :param ipv4_address: {"type": "string", "description": "IP address", "format": "ipv4-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.ipv4_netmask = ""
        self.Hardware = ""
        self.state = ""
        self.Address = ""
        self.trunk_member = []
        self.line_protocol = ""
        self.ipv4_address = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Trunk(A10BaseClass):
    
    """Class Description::
    Operational Status for the object trunk.

    Class trunk supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param ifnum: {"optional": false, "oid": "1001", "type": "number", "description": "Trunk interface number", "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/interface/trunk/{ifnum}/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "trunk"
        self.a10_url="/axapi/v3/interface/trunk/{ifnum}/oper"
        self.DeviceProxy = ""
        self.oper = {}
        self.ifnum = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


