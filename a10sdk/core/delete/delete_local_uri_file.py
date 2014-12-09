from a10sdk.common.A10BaseClass import A10BaseClass


class LocalUriFile(A10BaseClass):
    
    """    :param file_name: {"description": "Local File Name", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Local URI files for http response.

    Class local-uri-file supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/delete/local-uri-file`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "local-uri-file"
        self.a10_url="/axapi/v3/delete/local-uri-file"
        self.DeviceProxy = ""
        self.file_name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


