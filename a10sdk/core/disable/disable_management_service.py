from a10sdk.common.A10BaseClass import A10BaseClass


class Service(A10BaseClass):
    
    """Class Description::
    Disable management services.

    Class service supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/disable-management/service`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "service"
        self.a10_url="/axapi/v3/disable-management/service"
        self.DeviceProxy = ""
        self.http = {}
        self.ping = {}
        self.ssh = {}
        self.https = {}
        self.snmp = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


