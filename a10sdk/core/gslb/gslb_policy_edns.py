from a10sdk.common.A10BaseClass import A10BaseClass


class Edns(A10BaseClass):
    
    """Class Description::
    Use EDNS extension.

    Class edns supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param client_subnet_geographic: {"default": 0, "optional": true, "type": "number", "description": "Use client subnet for geo-location", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/gslb/policy/{name}/edns`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "edns"
        self.a10_url="/axapi/v3/gslb/policy/{name}/edns"
        self.DeviceProxy = ""
        self.uuid = ""
        self.client_subnet_geographic = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


