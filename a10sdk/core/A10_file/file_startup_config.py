from a10sdk.common.A10BaseClass import A10BaseClass


class StartupConfig(A10BaseClass):
    
    """    :param action: {"optional": true, "enum": ["create", "import", "export", "copy", "rename", "check", "replace", "delete"], "type": "string", "description": "'create': create; 'import': import; 'export': export; 'copy': copy; 'rename': rename; 'check': check; 'replace': replace; 'delete': delete; ", "format": "enum"}
    :param dst_file: {"description": "destination file name for copy and rename action", "format": "string", "minLength": 1, "optional": true, "maxLength": 32, "type": "string"}
    :param file_handle: {"description": "full path of the uploaded file", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 255, "type": "string"}
    :param file: {"description": "startup-config local file name", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param size: {"description": "startup-config file size in byte", "format": "number", "type": "number", "maximum": 2147483647, "minimum": 0, "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Contents of Startup Configuration.

    Class startup-config supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/file/startup-config`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "startup-config"
        self.a10_url="/axapi/v3/file/startup-config"
        self.DeviceProxy = ""
        self.action = ""
        self.dst_file = ""
        self.file_handle = ""
        self.A10WW_file = ""
        self.size = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


