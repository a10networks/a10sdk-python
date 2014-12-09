from a10sdk.common.A10BaseClass import A10BaseClass


class Disable(A10BaseClass):
    
    """Class Description::
    Disable l3v partition trap.

    Class disable supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/snmp-server/disable`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "disable"
        self.a10_url="/axapi/v3/snmp-server/disable"
        self.DeviceProxy = ""
        self.traps = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


