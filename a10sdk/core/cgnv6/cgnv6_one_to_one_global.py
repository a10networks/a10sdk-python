from a10sdk.common.A10BaseClass import A10BaseClass


class Global(A10BaseClass):
    
    """Class Description::
    Set one-to-one NAT config parameters.

    Class global supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param mapping_timeout: {"description": "Configure timeout for the one-to-one NAT mapping (Timeout in minutes (default: 10 minutes))", "format": "number", "default": 10, "optional": true, "maximum": 180, "minimum": 0, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/one-to-one/global`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "global"
        self.a10_url="/axapi/v3/cgnv6/one-to-one/global"
        self.DeviceProxy = ""
        self.mapping_timeout = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


