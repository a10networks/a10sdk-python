from a10sdk.common.A10BaseClass import A10BaseClass


class Fragmentation(A10BaseClass):
    
    """Class Description::
    DS-Lite fragmentation parameters.

    Class fragmentation supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/ds-lite/fragmentation`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "fragmentation"
        self.a10_url="/axapi/v3/cgnv6/ds-lite/fragmentation"
        self.DeviceProxy = ""
        self.inbound = {}
        self.outbound = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


