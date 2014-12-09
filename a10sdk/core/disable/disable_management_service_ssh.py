from a10sdk.common.A10BaseClass import A10BaseClass


class Ssh(A10BaseClass):
    
    """Class Description::
    SSH service.

    Class ssh supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param management: {"default": 0, "optional": true, "type": "number", "description": "Management port", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/disable-management/service/ssh`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "ssh"
        self.a10_url="/axapi/v3/disable-management/service/ssh"
        self.DeviceProxy = ""
        self.management = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


