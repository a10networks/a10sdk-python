from a10sdk.common.A10BaseClass import A10BaseClass


class VmasterTakeOver(A10BaseClass):
    
    """    :param vmaster_take_over: {"description": "vMaster take over priority", "format": "number", "type": "number", "maximum": 255, "minimum": 1, "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Forcefully take over mastership.

    Class vmaster-take-over supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/vcs/vmaster-take-over`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "vmaster-take-over"
        self.a10_url="/axapi/v3/vcs/vmaster-take-over"
        self.DeviceProxy = ""
        self.vmaster_take_over = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


