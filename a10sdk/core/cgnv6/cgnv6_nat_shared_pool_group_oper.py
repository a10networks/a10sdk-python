from a10sdk.common.A10BaseClass import A10BaseClass


class SharedPoolGroupList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param pool_group_name: {"type": "string", "format": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "shared-pool-group-list"
        self.DeviceProxy = ""
        self.pool_group_name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param shared_pool_group_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"pool-group-name": {"type": "string", "format": "string"}, "optional": true}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.shared_pool_group_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class SharedPoolGroup(A10BaseClass):
    
    """Class Description::
    Operational Status for the object shared-pool-group.

    Class shared-pool-group supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/nat/shared-pool-group/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "shared-pool-group"
        self.a10_url="/axapi/v3/cgnv6/nat/shared-pool-group/oper"
        self.DeviceProxy = ""
        self.oper = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


