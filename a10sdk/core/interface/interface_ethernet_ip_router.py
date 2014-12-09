from a10sdk.common.A10BaseClass import A10BaseClass


class Router(A10BaseClass):
    
    """Class Description::
    Router.

    Class router supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/interface/ethernet/{ifnum}/ip/router`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "router"
        self.a10_url="/axapi/v3/interface/ethernet/{ifnum}/ip/router"
        self.DeviceProxy = ""
        self.isis = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


