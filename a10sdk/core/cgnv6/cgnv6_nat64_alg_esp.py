from a10sdk.common.A10BaseClass import A10BaseClass


class Esp(A10BaseClass):
    
    """Class Description::
    NAT64 ESP ALG (default: disabled).

    Class esp supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param esp_enable: {"optional": true, "enum": ["enable"], "type": "string", "description": "'enable': Enable NAT64 ESP ALG; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/nat64/alg/esp`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "esp"
        self.a10_url="/axapi/v3/cgnv6/nat64/alg/esp"
        self.DeviceProxy = ""
        self.uuid = ""
        self.esp_enable = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


