from a10sdk.common.A10BaseClass import A10BaseClass


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param fixed_nat_ip_addr_count_max: {"type": "number", "format": "number"}
    :param fixed_nat_ip_addr_count_default: {"type": "number", "format": "number"}
    :param lsn_nat_addr_count_min: {"type": "number", "format": "number"}
    :param fixed_nat_inside_user_count_default: {"type": "number", "format": "number"}
    :param fixed_nat_inside_user_count_min: {"type": "number", "format": "number"}
    :param lsn_nat_addr_count_max: {"type": "number", "format": "number"}
    :param fixed_nat_inside_user_count_max: {"type": "number", "format": "number"}
    :param fixed_nat_ip_addr_count_min: {"type": "number", "format": "number"}
    :param lsn_nat_addr_count_default: {"type": "number", "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.fixed_nat_ip_addr_count_max = ""
        self.fixed_nat_ip_addr_count_default = ""
        self.lsn_nat_addr_count_min = ""
        self.fixed_nat_inside_user_count_default = ""
        self.fixed_nat_inside_user_count_min = ""
        self.lsn_nat_addr_count_max = ""
        self.fixed_nat_inside_user_count_max = ""
        self.fixed_nat_ip_addr_count_min = ""
        self.lsn_nat_addr_count_default = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class ResourceUsage(A10BaseClass):
    
    """Class Description::
    Operational Status for the object resource-usage.

    Class resource-usage supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/resource-usage/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "resource-usage"
        self.a10_url="/axapi/v3/cgnv6/resource-usage/oper"
        self.DeviceProxy = ""
        self.oper = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


