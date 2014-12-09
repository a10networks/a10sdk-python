from a10sdk.common.A10BaseClass import A10BaseClass


class Reset(A10BaseClass):
    
    """    :param auto_switch: {"default": 0, "optional": true, "type": "number", "description": "Reset auto stateless state", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Reset.

    Class reset supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/service-group/{name}/reset`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "reset"
        self.a10_url="/axapi/v3/slb/service-group/{name}/reset"
        self.DeviceProxy = ""
        self.auto_switch = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


