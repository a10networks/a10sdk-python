from a10sdk.common.A10BaseClass import A10BaseClass


class Routing(A10BaseClass):
    
    """Class Description::
    Enable routing traps.

    Class routing supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/snmp-server/enable/traps/routing`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "routing"
        self.a10_url="/axapi/v3/snmp-server/enable/traps/routing"
        self.DeviceProxy = ""
        self.bgp = {}
        self.ospf = {}
        self.isis = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


