from a10sdk.common.A10BaseClass import A10BaseClass


class Generate(A10BaseClass):
    
    """    :param country: {"description": "The country name", "format": "string", "minLength": 2, "optional": true, "maxLength": 2, "type": "string"}
    :param state: {"description": "The location", "format": "string", "minLength": 1, "optional": true, "maxLength": 128, "type": "string"}
    :param domain_name: {"description": "The domain name", "format": "string", "minLength": 1, "optional": true, "maxLength": 128, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Web-service secure generate operation.

    Class generate supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/web-service/secure/generate`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "generate"
        self.a10_url="/axapi/v3/web-service/secure/generate"
        self.DeviceProxy = ""
        self.country = ""
        self.state = ""
        self.domain_name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


