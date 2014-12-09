from a10sdk.common.A10BaseClass import A10BaseClass


class TrunkMemberStatus(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param oper_status: {"enum": ["Blocked", "Up", "Dn"], "type": "string", "format": "enum"}
    :param cfg_status: {"enum": ["Enb", "Dis"], "type": "string", "format": "enum"}
    :param members: {"type": "number", "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "trunk-member-status"
        self.DeviceProxy = ""
        self.oper_status = ""
        self.cfg_status = ""
        self.members = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Trunk(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param trunk_type: {"enum": ["Dynamic-LACP", "Static"], "type": "string", "format": "enum"}
    :param member_count: {"type": "number", "format": "number"}
    :param trunk_member_status: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"oper_status": {"enum": ["Blocked", "Up", "Dn"], "type": "string", "format": "enum"}, "optional": true, "cfg_status": {"enum": ["Enb", "Dis"], "type": "string", "format": "enum"}, "members": {"type": "number", "format": "number"}}}]}
    :param timer: {"type": "number", "format": "number"}
    :param trunk_status: {"enum": ["Up", "Down"], "type": "string", "format": "enum"}
    :param admin_key: {"type": "number", "format": "number"}
    :param timer_running: {"enum": ["Yes", "No"], "type": "string", "format": "enum"}
    :param ports_threshold: {"type": "number", "format": "number"}
    :param trunk_id: {"minimum": 1, "type": "number", "maximum": 16, "format": "number"}
    :param working_lead: {"type": "number", "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "trunk"
        self.DeviceProxy = ""
        self.trunk_type = ""
        self.member_count = ""
        self.trunk_member_status = []
        self.timer = ""
        self.trunk_status = ""
        self.admin_key = ""
        self.timer_running = ""
        self.ports_threshold = ""
        self.trunk_id = ""
        self.working_lead = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param trunk: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"trunk_type": {"enum": ["Dynamic-LACP", "Static"], "type": "string", "format": "enum"}, "member_count": {"type": "number", "format": "number"}, "trunk-member-status": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"oper_status": {"enum": ["Blocked", "Up", "Dn"], "type": "string", "format": "enum"}, "optional": true, "cfg_status": {"enum": ["Enb", "Dis"], "type": "string", "format": "enum"}, "members": {"type": "number", "format": "number"}}}]}, "timer": {"type": "number", "format": "number"}, "trunk_status": {"enum": ["Up", "Down"], "type": "string", "format": "enum"}, "admin_key": {"type": "number", "format": "number"}, "timer_running": {"enum": ["Yes", "No"], "type": "string", "format": "enum"}, "ports_threshold": {"type": "number", "format": "number"}, "trunk_id": {"minimum": 1, "type": "number", "maximum": 16, "format": "number"}, "optional": true, "working_lead": {"type": "number", "format": "number"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.trunk = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Trunk(A10BaseClass):
    
    """Class Description::
    Operational Status for the object trunk.

    Class trunk supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/trunk/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "trunk"
        self.a10_url="/axapi/v3/trunk/oper"
        self.DeviceProxy = ""
        self.oper = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


