from a10sdk.common.A10BaseClass import A10BaseClass


class SplitHorizonCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param state: {"default": "poisoned", "enum": ["poisoned", "disable", "enable"], "type": "string", "description": "'poisoned': Perform split horizon with poisoned reverse; 'disable': Disable split horizon; 'enable': Perform split horizon without poisoned reverse; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "split-horizon-cfg"
        self.DeviceProxy = ""
        self.state = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Rip(A10BaseClass):
    
    """Class Description::
    RIP.

    Class rip supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/interface/ve/{ifnum}/ipv6/rip`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "rip"
        self.a10_url="/axapi/v3/interface/ve/{ifnum}/ipv6/rip"
        self.DeviceProxy = ""
        self.split_horizon_cfg = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


