from a10sdk.common.A10BaseClass import A10BaseClass


class HealthPostfile(A10BaseClass):
    
    """    :param remote_file: {"optional": true, "type": "string", "description": "Profile name for remote url", "format": "url"}
    :param postfilename: {"description": "Specify the File Name", "format": "string", "minLength": 1, "optional": true, "maxLength": 31, "type": "string"}
    :param use_mgmt_port: {"default": 0, "optional": true, "type": "number", "description": "Use management port as source port", "format": "flag"}
    :param overwrite: {"default": 0, "optional": true, "type": "number", "description": "Overwrite existing file", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Address the HTTP Post data file.

    Class health-postfile supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/import/health-postfile`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "health-postfile"
        self.a10_url="/axapi/v3/import/health-postfile"
        self.DeviceProxy = ""
        self.remote_file = ""
        self.postfilename = ""
        self.use_mgmt_port = ""
        self.overwrite = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


