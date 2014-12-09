from a10sdk.common.A10BaseClass import A10BaseClass


class AddressFamily(A10BaseClass):
    
    """Class Description::
    Enter Address Family command mode.

    Class address-family supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/router/isis/{tag}/address-family`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "address-family"
        self.a10_url="/axapi/v3/router/isis/{tag}/address-family"
        self.DeviceProxy = ""
        self.ipv6 = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


