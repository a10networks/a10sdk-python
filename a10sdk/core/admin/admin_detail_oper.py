from a10sdk.common.A10BaseClass import A10BaseClass


class UserList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param status: {"type": "string", "format": "string"}
    :param priviledge: {"type": "string", "format": "string"}
    :param lock_time: {"type": "string", "format": "string"}
    :param unlock_time: {"type": "string", "format": "string"}
    :param trusted_host: {"type": "string", "format": "string"}
    :param partition: {"type": "string", "format": "string"}
    :param access_type: {"type": "string", "format": "string"}
    :param password: {"type": "string", "format": "string"}
    :param gui_role: {"type": "string", "format": "string"}
    :param lock_status: {"type": "string", "format": "string"}
    :param password_type: {"type": "string", "format": "string"}
    :param user_name: {"type": "string", "format": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "user-list"
        self.DeviceProxy = ""
        self.status = ""
        self.priviledge = ""
        self.lock_time = ""
        self.unlock_time = ""
        self.trusted_host = ""
        self.partition = ""
        self.access_type = ""
        self.password = ""
        self.gui_role = ""
        self.lock_status = ""
        self.password_type = ""
        self.user_name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param user_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"status": {"type": "string", "format": "string"}, "priviledge": {"type": "string", "format": "string"}, "lock_time": {"type": "string", "format": "string"}, "unlock_time": {"type": "string", "format": "string"}, "trusted_host": {"type": "string", "format": "string"}, "optional": true, "partition": {"type": "string", "format": "string"}, "access_type": {"type": "string", "format": "string"}, "password": {"type": "string", "format": "string"}, "gui_role": {"type": "string", "format": "string"}, "lock_status": {"type": "string", "format": "string"}, "password_type": {"type": "string", "format": "string"}, "user_name": {"type": "string", "format": "string"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.user_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class AdminDetail(A10BaseClass):
    
    """Class Description::
    Operational Status for the object admin-detail.

    Class admin-detail supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/admin-detail/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "admin-detail"
        self.a10_url="/axapi/v3/admin-detail/oper"
        self.DeviceProxy = ""
        self.oper = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


