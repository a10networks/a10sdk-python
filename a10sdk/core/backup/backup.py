from a10sdk.common.A10BaseClass import A10BaseClass


class Backup(A10BaseClass):
    
    """    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Backup system files.

    Class backup supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/backup`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "backup"
        self.a10_url="/axapi/v3/backup"
        self.DeviceProxy = ""
        self.system = {}
        self.store = {}
        self.log = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


