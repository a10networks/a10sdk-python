from a10sdk.common.A10BaseClass import A10BaseClass


class FixedNat(A10BaseClass):
    
    """    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Configure Fixed NAT.

    Class fixed-nat supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/fixed-nat`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "fixed-nat"
        self.a10_url="/axapi/v3/cgnv6/fixed-nat"
        self.DeviceProxy = ""
        self.alg = {}
        self.inside = {}
        self.A10WW_global = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


