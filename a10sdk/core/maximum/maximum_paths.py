from a10sdk.common.A10BaseClass import A10BaseClass


class MaximumPaths(A10BaseClass):
    
    """Class Description::
    Set maximum number of route multipaths installed into FIB.

    Class maximum-paths supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param path: {"description": "supported multipath numbers", "format": "number", "default": 4, "optional": true, "maximum": 64, "minimum": 1, "type": "number"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
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
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


