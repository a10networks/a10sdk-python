from a10sdk.common.A10BaseClass import A10BaseClass


class Rip(A10BaseClass):
    
    """Class Description::
    RIP Routing for IPv6.

    Class rip supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/interface/trunk/{ifnum}/ipv6/router/rip`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "rip"
        self.a10_url="/axapi/v3/interface/trunk/{ifnum}/ipv6/router/rip"
        self.DeviceProxy = ""
        
        for keys, value in kwargs.items():
            setattr(self,keys, value)


