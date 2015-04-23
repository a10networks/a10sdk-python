from a10sdk.common.A10BaseClass import A10BaseClass


class ApplicationType(A10BaseClass):
    
    """Class Description::
    Configure application to be used in partition (ADC/CGNV6).

    Class application-type supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param type: {"optional": true, "enum": ["adc", "cgnv6"], "type": "string", "description": "'adc': Application type ADC; 'cgnv6': Application type CGNv6; ", "format": "enum"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/application-type`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "application-type"
        self.a10_url="/axapi/v3/application-type"
        self.DeviceProxy = ""
        self.A10WW_type = ""
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


