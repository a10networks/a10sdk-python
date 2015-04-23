from a10sdk.common.A10BaseClass import A10BaseClass


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param class_list_ipv6_addr_max: {"type": "number", "format": "number"}
    :param class_list_ipv6_addr_default: {"type": "number", "format": "number"}
    :param l4_session_count_max: {"type": "number", "format": "number"}
    :param class_list_ipv6_addr_min: {"type": "number", "format": "number"}
    :param l4_session_count_default: {"type": "number", "format": "number"}
    :param l4_session_count_min: {"type": "number", "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.class_list_ipv6_addr_max = ""
        self.class_list_ipv6_addr_default = ""
        self.l4_session_count_max = ""
        self.class_list_ipv6_addr_min = ""
        self.l4_session_count_default = ""
        self.l4_session_count_min = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class ResourceUsage(A10BaseClass):
    
    """Class Description::
    Operational Status for the object resource-usage.

    Class resource-usage supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/system/resource-usage/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "resource-usage"
        self.a10_url="/axapi/v3/system/resource-usage/oper"
        self.DeviceProxy = ""
        self.oper = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


