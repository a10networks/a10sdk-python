from a10sdk.common.A10BaseClass import A10BaseClass


class Connect(A10BaseClass):
    
    """Class Description::
    Connect to license manager to activate.

    Class connect supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param connect: {"description": "Connect to license manager to activate", "partition-visibility": "shared", "default": 0, "type": "number", "format": "flag", "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/license-manager/connect`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "connect"
        self.a10_url="/axapi/v3/license-manager/connect"
        self.DeviceProxy = ""
        self.connect = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


