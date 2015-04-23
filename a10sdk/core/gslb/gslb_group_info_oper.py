from a10sdk.common.A10BaseClass import A10BaseClass


class MemberList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param status: {"type": "string", "format": "string"}
    :param passive: {"type": "number", "format": "number"}
    :param connect_success: {"type": "number", "format": "number"}
    :param member_name: {"type": "string", "format": "string"}
    :param address: {"type": "string", "format": "ipv4-address"}
    :param sync_sequence_number: {"type": "number", "format": "number"}
    :param connect_fail: {"type": "number", "format": "number"}
    :param priority: {"type": "number", "format": "number"}
    :param group_name: {"type": "string", "format": "string"}
    :param open_out: {"type": "number", "format": "number"}
    :param learn: {"type": "number", "format": "number"}
    :param is_master: {"type": "number", "format": "number"}
    :param open_success: {"type": "number", "format": "number"}
    :param open_in: {"type": "number", "format": "number"}
    :param sys_id: {"type": "number", "format": "number"}
    :param update_in: {"type": "number", "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "member-list"
        self.DeviceProxy = ""
        self.status = ""
        self.passive = ""
        self.connect_success = ""
        self.member_name = ""
        self.address = ""
        self.sync_sequence_number = ""
        self.connect_fail = ""
        self.priority = ""
        self.group_name = ""
        self.open_out = ""
        self.learn = ""
        self.is_master = ""
        self.open_success = ""
        self.open_in = ""
        self.sys_id = ""
        self.update_in = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param member_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"status": {"type": "string", "format": "string"}, "passive": {"type": "number", "format": "number"}, "connect-success": {"type": "number", "format": "number"}, "member-name": {"type": "string", "format": "string"}, "address": {"type": "string", "format": "ipv4-address"}, "sync-sequence-number": {"type": "number", "format": "number"}, "connect-fail": {"type": "number", "format": "number"}, "priority": {"type": "number", "format": "number"}, "group-name": {"type": "string", "format": "string"}, "open-out": {"type": "number", "format": "number"}, "learn": {"type": "number", "format": "number"}, "is_master": {"type": "number", "format": "number"}, "open-success": {"type": "number", "format": "number"}, "open-in": {"type": "number", "format": "number"}, "optional": true, "sys-id": {"type": "number", "format": "number"}, "update-in": {"type": "number", "format": "number"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.member_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class GroupInfo(A10BaseClass):
    
    """Class Description::
    Operational Status for the object group-info.

    Class group-info supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/gslb/group-info/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "group-info"
        self.a10_url="/axapi/v3/gslb/group-info/oper"
        self.DeviceProxy = ""
        self.oper = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


