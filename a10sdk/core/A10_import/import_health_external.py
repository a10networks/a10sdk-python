from a10sdk.common.A10BaseClass import A10BaseClass


class HealthExternal(A10BaseClass):
    
    """    :param remote_file: {"optional": true, "type": "string", "format": "url"}
    :param use_mgmt_port: {"default": 0, "optional": true, "type": "number", "description": "Use management port as source port", "format": "flag"}
    :param description: {"description": "Describe the Program Function briefly", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param externalfilename: {"description": "Specify the Program Name", "format": "string", "minLength": 1, "optional": true, "maxLength": 31, "type": "string"}
    :param overwrite: {"default": 0, "optional": true, "type": "number", "description": "Overwrite existing file", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Address the External Script Program.

    Class health-external supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/import/health-external`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "health-external"
        self.a10_url="/axapi/v3/import/health-external"
        self.DeviceProxy = ""
        self.remote_file = ""
        self.use_mgmt_port = ""
        self.description = ""
        self.externalfilename = ""
        self.overwrite = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


