from a10sdk.common.A10BaseClass import A10BaseClass


class DeviceContext(A10BaseClass):
    
    """Class Description::
    The target device the following router commands to configure for.

    Class device-context supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param dev_id: {"description": "Device ID", "format": "number", "type": "number", "maximum": 8, "minimum": 1, "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/router/device-context`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "device-context"
        self.a10_url="/axapi/v3/router/device-context"
        self.DeviceProxy = ""
        self.dev_id = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


