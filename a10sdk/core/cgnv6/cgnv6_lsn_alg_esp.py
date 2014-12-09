from a10sdk.common.A10BaseClass import A10BaseClass


class Esp(A10BaseClass):
    
    """Class Description::
    Change LSN ESP ALG Settings.

    Class esp supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param esp_value: {"optional": true, "enum": ["enable"], "type": "string", "description": "'enable': Enable ESP ALG for LSN; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/lsn/alg/esp`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "esp"
        self.a10_url="/axapi/v3/cgnv6/lsn/alg/esp"
        self.DeviceProxy = ""
        self.esp_value = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


