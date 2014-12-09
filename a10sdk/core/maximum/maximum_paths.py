from a10sdk.common.A10BaseClass import A10BaseClass


class MaximumPaths(A10BaseClass):
    
    """Class Description::
    Set multipath numbers installed to FIB.

    Class maximum-paths supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param path: {"description": "supported multipath numbers", "format": "number", "default": 4, "optional": true, "maximum": 10, "minimum": 1, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/maximum-paths`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "maximum-paths"
        self.a10_url="/axapi/v3/maximum-paths"
        self.DeviceProxy = ""
        self.path = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


