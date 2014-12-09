from a10sdk.common.A10BaseClass import A10BaseClass


class Pmtu(A10BaseClass):
    
    """Class Description::
    Configure Path MTU option.

    Class pmtu supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param action: {"description": "\"disable\": Disable IPv6 PMTU processing; \"enable\": Enable IPv6 PMTU processing; ", "format": "enum", "default": "disable", "type": "string", "enum": ["disable", "enable"], "optional": true}
    :param timeout: {"description": "Path MTU timeout to restore the original value (Path MTU timeout of the aggregated route (Default: 300 secs)).", "format": "number", "type": "number", "maximum": 900, "minimum": 120, "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/ipv6/pmtu`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "pmtu"
        self.a10_url="/axapi/v3/ipv6/pmtu"
        self.DeviceProxy = ""
        self.action = ""
        self.timeout = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


