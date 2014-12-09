from a10sdk.common.A10BaseClass import A10BaseClass


class ResourceUsage(A10BaseClass):
    
    """Class Description::
    Configure CGNV6 Resource Usage.

    Class resource-usage supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param lsn_nat_addr_count: {"platform-specific-range": 1, "platform-specific-default": 1, "description": "Total configurable CGNV6 NAT Pool addresses", "format": "number", "optional": true, "type": "number"}
    :param fixed_nat_ip_addr_count: {"platform-specific-range": 1, "platform-specific-default": 1, "description": "Total configurable CGNV6 Fixed NAT addresses", "format": "number", "optional": true, "type": "number"}
    :param fixed_nat_inside_user_count: {"platform-specific-range": 1, "platform-specific-default": 1, "description": "Total configurable CGNV6 Fixed NAT inside users", "format": "number", "optional": true, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/resource-usage`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "resource-usage"
        self.a10_url="/axapi/v3/cgnv6/resource-usage"
        self.DeviceProxy = ""
        self.lsn_nat_addr_count = ""
        self.fixed_nat_ip_addr_count = ""
        self.fixed_nat_inside_user_count = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


