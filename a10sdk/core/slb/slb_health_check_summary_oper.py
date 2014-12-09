from a10sdk.common.A10BaseClass import A10BaseClass


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param server_port_up: {"type": "number", "format": "number"}
    :param server_port_down: {"type": "number", "format": "number"}
    :param server_up: {"type": "number", "format": "number"}
    :param server_down: {"type": "number", "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.server_port_up = ""
        self.server_port_down = ""
        self.server_up = ""
        self.server_down = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class HealthCheckSummary(A10BaseClass):
    
    """Class Description::
    Operational Status for the object health-check-summary.

    Class health-check-summary supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/health-check-summary/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "health-check-summary"
        self.a10_url="/axapi/v3/slb/health-check-summary/oper"
        self.DeviceProxy = ""
        self.oper = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


