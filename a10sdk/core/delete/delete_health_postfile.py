from a10sdk.common.A10BaseClass import A10BaseClass


class HealthPostfile(A10BaseClass):
    
    """    :param file_name: {"description": "Specify the File Name", "format": "string", "minLength": 1, "optional": true, "maxLength": 31, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Address the HTTP Post data file.

    Class health-postfile supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/delete/health-postfile`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "health-postfile"
        self.a10_url="/axapi/v3/delete/health-postfile"
        self.DeviceProxy = ""
        self.file_name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


