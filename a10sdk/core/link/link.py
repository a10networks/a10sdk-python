from a10sdk.common.A10BaseClass import A10BaseClass


class Link(A10BaseClass):
    
    """    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Link to Configuration Profile.

    Class link supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/link`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "link"
        self.a10_url="/axapi/v3/link"
        self.DeviceProxy = ""
        self.startup_config = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


